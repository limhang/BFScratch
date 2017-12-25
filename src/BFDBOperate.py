# 既然是一个爬虫库，那么肯定要有数据库部分，这里我们采用PyMySQL作为依赖库
import pymysql

class BFDBOperate():
    def __init__(self, db, password, user, host):
        self.db = db
        self.password = password
        self.user = user
        self.host = host
        self.connect = self.connectDB();

    def connectDB(self):
        connect =  pymysql.connect(host=self.host,
                                   user=self.user,
                                   password=self.password,
                                   db=self.db,
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)
        return connect


    def insertDB(self, sql, info):
        with self.connect.cursor() as cursor:
            # Create a new record
            cursor.execute(sql, info)
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connect.commit()
            self.connect.close()

    def selectData(self, sql):
        with self.connect.cursor() as cursor:
            # Read a single record
            cursor.execute()
            result = cursor.fetchone()
            return result
