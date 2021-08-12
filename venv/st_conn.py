import pymysql

# 1.连接本地mysql数据库
conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'yaoll100.',
    database = 'mysql',
    charset = 'utf8'
)
