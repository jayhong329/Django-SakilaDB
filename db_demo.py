import MySQLdb

class Category():
    def __init__():
        pass

    def create_connection():
        # Step1 建立連線
        try:
            connection = MySQLdb.connect(
                host = "localhost",
                database = "sakila",
                user = "root",
                password = "P@ssw0rd" 
            )
            return connection
        except MySQLdb.MySQLError as e:
            print(f"資料庫連線錯誤:{e}")
            return None
        
    # 讀取所有資料
    def all():
        # 放其他程式(如:爬蟲程式)
        connection = Category.create_connection()

        if not connection:
            return None

    
        # Step2 SQL語法
        sql = "SELECT * FROM category WHERE category_id=15;"

        # Step3 建立Cursor 物件執行SQL語法
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql)
                    # Step 3-1
                    results = cursor.fetchone()
                    return results
                except MySQLdb.MySQLError as e:
                    print(f"資料讀取錯:{e}")
                    return None


    # 新增資料
    def category_create(category_name):
        connection = Category.create_connection()
        if not connection:
            return None
        
        # Step2 SQL-insert into
        sql = "INSERT INTO category (name) VALUES (%s)"

        # Step3 cursor 執行 SQL
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql,(category_name,)) 
                    # tuple(id, ) +, 才能判斷是tuple型態~

                except MySQLdb.MySQLError as e:
                    print(f"資料新增錯誤:{e}")
                    return None



