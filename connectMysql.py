import pymysql  

# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect("localhost", "root", "", "pytest")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * from status_code")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print(data)

# 关闭数据库连接
db.close()  
