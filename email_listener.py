import os
import uuid
import time
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from datetime import datetime, timedelta
from urllib.parse import urlparse

# 数据库连接信息
db_config = {
    'host': 'Moonkey.top',
    'port': 3306,
    'user': 'root',
    'password': '1206',
    'database': 'email',
    'cursorclass': pymysql.cursors.DictCursor
}
# 邮件发送信息
mail_config = {
    'smtp_server': 'SMTP.Moonkey.top',
    'smtp_port': 465,
    'sender': 'Moonkey_Support@Moonkey.top',
    'password': 'Mok_em@Moo.1315#'
}

def generate_uuid() -> str:
    """
    生成16位uuid
    """
    return str(uuid.uuid4()).replace('-','')[:10].lower() + hex(int(time.time()/256))[2:].lower()

def generate_http_url(host='Moonkey.top', port='28080') -> str:
    """
    生成http链接
    """
    uuid_str = generate_uuid()
    return f'http://{host}:{port}?id={uuid_str}'

def generate_https_url(host='Moonkey.top', port='28081') -> str:
    """
    生成https链接
    """
    uuid_str = generate_uuid()
    return f'https://{host}:{port}?id={uuid_str}'

def generate_html(url=generate_https_url()) -> str:
    """
    生成html代码
    """
    img_html = f'<img src="{url}"/>'
    return img_html

def send_email(receiver, text, html=None, title=None, sender=None, password=None):
    """
    发送邮件
    """
    if not sender:
        sender = mail_config['sender']
    if not password:
        password = mail_config['password']
    if not title:
        title = '邮件标题'
    msg = MIMEMultipart('related')
    msg['Subject'] = Header(title, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    # 添加HTML内容
    if html:
        msg.attach(MIMEText(f'{text}\n<img src="{html}"/>', 'html', 'utf-8'))

    # 发送邮件
    print(msg.as_string())
    server = smtplib.SMTP_SSL(mail_config['smtp_server'], mail_config['smtp_port'])
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()

def query_counter(id=None):
    """
    查询counter值
    """
    with pymysql.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            if id:
                cursor.execute('SELECT counter, timeStamp, info FROM counter WHERE id=%s', (id,))
                result = cursor.fetchone()
                if result:
                    counter = result['counter']
                    timeStamp = result['timeStamp']
                    print(f'{id}的counter值: {counter}, 最后一次打开时间: {timeStamp}, info: {result["info"]}')
                else:
                    print(f'{id}不存在')
            else:
                cursor.execute('SELECT id, counter, timeStamp, info FROM counter')
                results = cursor.fetchall()
                print("--- id --- counter --- timeStamp --- info ---")
                for row in results:
                    print(f'{row["id"]}: {row["counter"]}, {row["timeStamp"]}, {row["info"]}')

def delete_counter(id=None):
    """
    删除counter项
    """
    with pymysql.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            if id:
                cursor.execute('DELETE FROM counter WHERE id=%s', (id,))
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f'{id}已删除')
                else:
                    print(f'{id}不存在')
            else:
                now = datetime.now()
                week_ago = now - timedelta(days=7)
                cursor.execute('DELETE FROM counter WHERE timestamp<=%s', (week_ago,))
                conn.commit()
                print(f'已删除{cursor.rowcount}条记录')

def connect(id, info):
    conn = pymysql.connect(**db_config)
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM counter WHERE id = %s'
        cursor.execute(sql, (id,))
        if cursor.rowcount == 0:
            sql = 'INSERT INTO counter (id, info) VALUES (%s, %s)'
            cursor.execute(sql, (id, info))
        else:
            sql = 'UPDATE counter SET info = %s WHERE id = %s'
            cursor.execute(sql, (info, id))

        if cursor.rowcount > 0:
            conn.commit()
            print('Connected')
        else:
            print(f'error')

def print_help(cmd=None):
    """
    输出帮助信息
    """
    if cmd:
        if cmd == 'uuid':
            print('用法: uuid')
            print('生成16位uuid')
        elif cmd == 'http':
            print('用法: http [host=\'Moonkey.top\', port=\'8080\']')
            print('生成形如http://Moonkey.top:8080?id=(在这里生成16位uuid)，其中host和port为缺省')
        elif cmd == 'https':
            print('用法: https [host=\'Moonkey.top\', port=\'8080\']')
            print('同上，http换成https，默认端口8081')
        elif cmd == 'html':
            print('用法: html \'http\'/\'https\'')
            print('生成\'<img src="上步生成的http或者https链接，默认缺省https"/>\'')
        elif cmd == 'email':
            print('用法: email receiver text [html http/https] [title] [sender] [password]')
            print('向receiver发送邮件，text为HTML类型，包含一段text文本和html命令结果（默认https），标题为title，发送者，发送者密码')
        elif cmd == 'query':
            print('用法: query [id]')
            print('查询id在数据库中的counter值，默认输出所有')
        elif cmd == 'delete':
            print('用法: delete [id]')
            print('删除id项，默认删除所有timeStamp至今超过7天的')
        elif cmd == 'connect':
            print('用法: connect id info')
            print('将id的info设置为输入值')
        elif cmd == 'help':
            print('用法: help [cmd]')
            print('列出某条命令用法，默认列出所有')
        else:
            print(f'command \'{cmd}\' not found')
    else:
        print('可用命令:')
        print('uuid')
        print('http')
        print('https')
        print('html')
        print('email')
        print('query')
        print('delete')
        print('connect')
        print('help [cmd]')

def main(cmd: str, args):
    """
    解析命令行参数
    """
    # 执行命令
    if cmd == 'uuid':
        print(generate_uuid())
    elif cmd == 'http':
        if len(args) == 1:
            print(generate_http_url())
        elif len(args) == 2:
            print(generate_http_url(args[1]))
        elif len(args) == 3:
            print(generate_http_url(args[1], args[2]))
        else:
            print('用法: http [host=\'Moonkey.top\', port=\'8080\']')
    elif cmd == 'https':
        if len(args) == 1:
            print(generate_https_url())
        elif len(args) == 2:
            print(generate_https_url(args[1]))
        elif len(args) == 3:
            print(generate_https_url(args[1], args[2]))
        else:
            print('用法: https [host=\'Moonkey.top\', port=\'8081\']')
    elif cmd == 'html':
        if len(args) == 2:
            url = args[1]
            print(generate_html(url))
        else:
            print(generate_html())
    elif cmd == 'email':
        if len(args) < 3:
            print('用法: email receiver text [html http/https] [title] [sender] [password]')
        else:
            receiver = args[1]
            text = args[2]
            html = None
            if len(args) >= 4:
                if args[3] == 'http':
                    html = generate_http_url()
                elif args[3] == 'https':
                    html = generate_https_url()
            title = args[4] if len(args) >= 5 else None
            sender = args[5] if len(args) >= 6 else None
            password = args[6] if len(args) >= 7 else None
            send_email(receiver, text, html, title, sender, password)
    elif cmd == 'query':
        if len(args) == 1:
            query_counter()
        elif len(args) == 2:
            query_counter(args[1])
        else:
            print('用法: query [id]')
    elif cmd == 'delete':
        if len(args) == 1:
            delete_counter()
        elif len(args) == 2:
            delete_counter(args[1])
        else:
            print('用法: delete [id]')
    elif cmd == 'help':
        if len(args) == 1:
            print_help()
        elif len(args) == 2:
            print_help(args[1])
        else:
            print('用法: connect id info')
    elif cmd == 'connect':
        if len(args) == 3:
            connect(args[1], args[2])
        else:
            print('用法: help [cmd]')
    else:
        print(f'command \'{cmd}\' not found')
        print_help()


if __name__ == '__main__':
    while True:
        args = input().split()
        if args:
            cmd = args[0].lower()
            if cmd == 'exit':
                break
            else:
                main(cmd, args)

exit(0)
