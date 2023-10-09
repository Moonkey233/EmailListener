const https = require('https');
const fs = require('fs');
const url = require('url');
const mysql = require('mysql2');

const dbConfig = {
	host: 'www.Moonkey.top',
	user: 'root',
	port: 3306,
	password: '1206',
	database: 'email'
};

const options = {
	key: fs.readFileSync('server.key'),
	cert: fs.readFileSync('server.crt')
};

var connection = mysql.createConnection(dbConfig);

connection.query(`
  CREATE TABLE IF NOT EXISTS counter (
    id VARCHAR(16) PRIMARY KEY,
    counter INT NOT NULL DEFAULT 0,
    timestamp TIMESTAMP DEFAULT NOW(),
	info VARCHAR(128) DEFAULT "NULL"
  )
`, (err) => {
	if (err) {
		console.error(err);
	}
});

const server = https.createServer(options, (req, res) => {
	const parsedUrl = url.parse(req.url, true);
	const id = parsedUrl.query.id;

	if (id) {
		connection = mysql.createConnection(dbConfig);
		connection.query('SELECT counter FROM counter WHERE id = ?', [id], (err, results) => {
			if (err) {
				console.error(err);
			} else {
				let counter = 0;
				if (results.length > 0) {
					counter = results[0].counter;
				}
				counter++;
				connection.query('INSERT INTO counter (id, counter) VALUES (?, ?) ON DUPLICATE KEY UPDATE counter = ?, timeStamp = NOW()', [id, counter, counter], (err) => {
					if (err) {
						console.error(err);
						res.writeHead(500, { 'Content-Type': 'text/plain' });
						res.end('Internal Server Error');
					} else {
						console.log(`${Date().toLocaleLowerCase()}: counter for ID ${id} updated to ${counter}`);
					}
				});
			}
		});
	}

	res.writeHead(200, { 'Content-Type': 'image/png' });
	res.end(Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEX///+nxBvIAAAAAXRSTlMAQObYZgAAAA9JREFUeNpjYBgFo2AUjIJGgAAACAAIAe5kUoAAAAASUVORK5CYII=', 'base64'));
});

server.listen(28081, () => {
	console.log('Server running at https://localhost:28081');
});