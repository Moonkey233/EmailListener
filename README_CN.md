# EmailListener Tool

## 简介

[ENG](./README.md) | 中文

这个命令行工具旨在监视电子邮件活动并检查特定电子邮件是否已被打开或查看。它提供了多种功能，包括生成唯一标识符（UUID）、创建HTTP和HTTPS链接、发送电子邮件、查询数据库中的计数器值以及删除计数器条目等。此工具可用于跟踪已发送给收件人的电子邮件的打开状态。

## 功能特点

- **生成UUID**：生成一个16位字符的UUID，可用作标识符。
- **生成HTTP和HTTPS链接**：创建包含唯一标识符的HTTP和HTTPS连接。
- **生成HTML代码**：生成包含带链接的图像标签的HTML代码。
- **发送电子邮件**：发送带有文本和可选HTML内容的电子邮件。
- **查询计数器值**：从数据库中检索特定ID或所有ID的计数器值。
- **删除计数器条目**：从数据库中删除特定ID或根据时间限制删除计数器条目。
- **连接功能**：将数据库中特定ID的“info”字段设置为输入的值。

## 环境要求

- Python 3.x
- 所需的Python库：`pymysql`、`smtplib`、`email`、`datetime`、`uuid`、`time`、`os`、`argparse`

## 安装

1. 克隆存储库或下载源代码。
2. 使用 `pip install pymysql` 安装所需的Python库。

## 使用方法

### 生成UUID

要生成一个16位字符的UUID，请使用以下命令：

```
python email_monitor.py uuid
```

### 生成HTTP和HTTPS链接

要生成HTTP或HTTPS链接，请使用以下命令：

```
# 生成默认主机和端口的HTTP链接
python email_monitor.py http

# 生成自定义主机和端口的HTTP链接
python email_monitor.py http example.com 8080

# 生成默认主机和端口的HTTPS链接
python email_monitor.py https

# 生成自定义主机和端口的HTTPS链接
python email_monitor.py https example.com 8081
```

### 生成HTML代码

要生成包含带链接的图像标签的HTML代码，请使用以下命令：

```
# 生成包含HTTPS链接的HTML代码（默认）
python email_monitor.py html

# 生成包含HTTP链接的HTML代码
python email_monitor.py html http
```

### 发送电子邮件

要发送电子邮件，请使用以下命令：

```
# 发送带有文本内容的电子邮件
python email_monitor.py email recipient@example.com "电子邮件文本内容"

# 发送带有文本和HTML内容的电子邮件（可选标题、发件人和发件人密码）
python email_monitor.py email recipient@example.com "电子邮件文本内容" https "电子邮件标题" sender@example.com sender_password
```

### 查询计数器值

要查询计数器值，请使用以下命令：

```
# 查询所有计数器值
python email_monitor.py query

# 查询特定ID的计数器值
python email_monitor.py query your_id_here
```

### 删除计数器条目

要删除计数器条目，请使用以下命令：

```
# 删除所有时间超过7天的计数器条目
python email_monitor.py delete

# 删除特定ID的计数器条目
python email_monitor.py delete your_id_here
```

### 连接到ID

要设置数据库中特定ID的“info”字段，请使用以下命令：

```
python email_monitor.py connect your_id_here "您的信息消息"
```

### 帮助

要获取特定命令的帮助或列出可用命令，请使用以下命令：

```
# 显示特定命令的帮助
python email_monitor.py help 命令名称

# 列出所有可用命令
python email_monitor.py help
```

## 配置

- 在脚本中的 `db_config` 中配置数据库连接设置。
- 在脚本中的 `mail_config` 中配置电子邮件发送设置。

## 致谢

该工具是作为一个项目创建的，不适用于未经进一步开发和安全增强的生产环境。

## 联系方式

如有问题或需要支持，请联系[M@Moonkey.top](mailto:M@Moonkey.top)。

---

请随意自定义此README.md以包括与您的用例相关的任何其他信息、说明或致谢。
