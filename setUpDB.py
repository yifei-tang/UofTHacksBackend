import mysql.connector
import collections

class my_database:
    def __init__(self):
        self.mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="WShuaren",
                database="testdb"
            )

        #set up cursor and clear  old table
        self.mycursor=self.mydb.cursor()
        self.clearDB()

        #set up table
        self.mycursor.execute("CREATE TABLE Fashion (Brand VARCHAR(50), Info VARCHAR(255))")
        
        #must print if you fetch show tables
        self.mycursor.execute("SHOW TABLES")
        for tb in self.mycursor:
            print('table number',tb)

        self.insertDB('ADIDAS','paragraph about adidas') 
        self.insertDB('NIKE','paragraph about nike') 

        #get Name as a list from db
        #compare the Name list using the method you wrote
            #if it matches, get the season and exported
            #if they are exported or wrong season, subtract one from the envScore

        
        self.mydb.commit()

    def getListNamesDB(self):
        sqlFormula="SELECT NAME FROM Fashion"
        self.mycursor.execute(sqlFormula)
        result=self.mycursor.fetchall()
        #print(result)
        return result

    def insertDB(self,brand,info):
        #print('insert')
        #insert into Food
        sqlFormula="INSERT INTO Fashion (Brand, Info) VALUES (%s,%s)"
        fashionItem=(brand,info)
        self.mycursor.execute(sqlFormula,fashionItem)
        #self.showTableDB()

    def showTableDB(self):
        self.mycursor.execute('SELECT * FROM Fashion')
        print('show',self.mycursor.fetchall())

    def getInfoFromBrand(self,brand):
        self.mycursor.execute(("SELECT Info FROM Fashion WHERE Brand=%s"),(brand,))
        result=self.mycursor.fetchall()
        return result

        
    def clearDB(self):
        try:
            self.mycursor.execute("DROP TABLE testdb.Fashion")
        except:
            print('Table Cleared Already')