import mysql.connector
import collections

class my_database:
    def __init__(self):
        self.mydb=mysql.connector.connect(
                host="myfashiondb.cld48setsmjg.us-east-2.rds.amazonaws.com",
                user="admin",
                password="uofthacks",
                database="myfashiondb"
            )

        #set up cursor and clear  old table
        self.mycursor=self.mydb.cursor()

        #set up table
        # self.mycursor.execute("CREATE TABLE CLOTHING (Brand VARCHAR(50), Info VARCHAR(255))")
        
        #must print if you fetch show tables
        self.mycursor.execute("SHOW TABLES")
        for tb in self.mycursor:
            print('table number',tb)

        self.insertDB('0','BLUE','ADIDAS','WINTER','MALE','www.youtube.com') 

        #get Name as a list from db
        #compare the Name list using the method you wrote
            #if it matches, get the season and exported
            #if they are exported or wrong season, subtract one from the envScore

        
        self.mydb.commit()

    def getListNamesDB(self):
        sqlFormula="SELECT NAME FROM CLOTHING"
        self.mycursor.execute(sqlFormula)
        result=self.mycursor.fetchall()
        #print(result)
        return result

    def insertDB(self,brand,info):
        #print('insert')
        #insert into Food
        sqlFormula="INSERT INTO CLOTHING (Brand, Info) VALUES (%s,%s)"
        fashionItem=(brand,info)
        self.mycursor.execute(sqlFormula,fashionItem)
        #self.showTableDB()

    def showTableDB(self):
        self.mycursor.execute('SELECT * FROM CLOTHING')
        print('show',self.mycursor.fetchall())

    def getInfoFromBrand(self,brand):
        self.mycursor.execute(("SELECT Info FROM CLOTHING WHERE Brand=%s"),(brand,))
        result=self.mycursor.fetchall()
        return result

        
    def clearDB(self):
        try:
            self.mycursor.execute("DROP TABLE testdb.CLOTHING")
        except:
            print('Table Cleared Already')