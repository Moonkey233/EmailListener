# EmailListener

ENG | [中文](./README_CN.md)

 A Email Monitoring Tool. Monitor the email and check if it has been opened or viewed.

## Introduction

This command-line tool is designed to monitor email activity and check if a specific email has been opened or viewed. It provides several functionalities including generating unique identifiers (UUIDs), creating HTTP and HTTPS links, sending emails, querying counter values in a database, and deleting counter entries. This tool can be useful for tracking the open status of emails sent to recipients.

## Features

- **Generate UUID**: Generate a 16-character UUID to use as an identifier.
- **Generate HTTP and HTTPS Links**: Create links with unique identifiers for HTTP and HTTPS connections.
- **Generate HTML Code**: Generate HTML code containing an image tag with a link.
- **Send Email**: Send emails with text and optional HTML content.
- **Query Counter Values**: Retrieve counter values from a database for a specific ID or all IDs.
- **Delete Counter Entries**: Remove counter entries from the database for a specific ID or based on a time limit.
- **Connect Function**: Set the "info" field for a specific ID in the database.

## Requirements

- Python 3.x
- Required Python libraries: `pymysql`, `smtplib`, `email`, `datetime`, `uuid`, `time`, `os`, `argparse`

## Installation

1. Clone the repository or download the source code.
2. Install the required Python libraries using `pip install pymysql`.

## Usage

### Generating a UUID

To generate a 16-character UUID, use the following command:

```
python email_monitor.py uuid
```

### Generating HTTP and HTTPS Links

To generate an HTTP or HTTPS link, use the following command:

```
# Generate HTTP link with default host and port
python email_monitor.py http

# Generate HTTP link with custom host and port
python email_monitor.py http example.com 8080

# Generate HTTPS link with default host and port
python email_monitor.py https

# Generate HTTPS link with custom host and port
python email_monitor.py https example.com 8081
```

### Generating HTML Code

To generate HTML code containing an image tag with a link, use the following command:

```
# Generate HTML code with an HTTPS link (default)
python email_monitor.py html

# Generate HTML code with an HTTP link
python email_monitor.py html http
```

### Sending an Email

To send an email, use the following command:

```
# Send an email with text content
python email_monitor.py email recipient@example.com "Email text content"

# Send an email with text and HTML content (with optional title, sender, and sender password)
python email_monitor.py email recipient@example.com "Email text content" https "Email Title" sender@example.com sender_password
```

### Querying Counter Values

To query counter values, use the following command:

```
# Query all counter values
python email_monitor.py query

# Query counter value for a specific ID
python email_monitor.py query your_id_here
```

### Deleting Counter Entries

To delete counter entries, use the following command:

```
# Delete all counter entries older than 7 days
python email_monitor.py delete

# Delete counter entry for a specific ID
python email_monitor.py delete your_id_here
```

### Connecting to an ID

To set the "info" field for a specific ID, use the following command:

```
python email_monitor.py connect your_id_here "Your info message here"
```

### Help

For help on a specific command or to list available commands, use the following command:

```
# Show help for a specific command
python email_monitor.py help command_name

# List all available commands
python email_monitor.py help
```

## Configuration

- Configure the database connection settings in `db_config` within the script.
- Configure the email sending settings in `mail_config` within the script.

## Acknowledgments

This tool was created as a project and is not meant for production use without further development and security enhancements.

## Contact

For questions or support, please contact [M@Moonkey.top](mailto:M@Moonkey.top).

---

Feel free to customize this README.md to include any additional information, instructions, or acknowledgments specific to your use case.
