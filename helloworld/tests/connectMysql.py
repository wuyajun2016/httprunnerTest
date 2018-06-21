import pymysql

def execSQL(sql):
    db = pymysql.connect("localhost", "root", "", "pytest")
    cursor = db.cursor()
    d = {}
    try:
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            d[id] = name
            # 打印结果
            print("id=%s,name=%s" % (id, name))
        print(d.get(2))
        return d.get(2)
    except:
        print("Error: unable to fecth data")

        # 关闭数据库连接
    db.close()
