import mysql.connector
import collections
import json
from article_classification import *
import random

class my_database:
    def __init__(self):
        self.mydb=mysql.connector.connect(
                host="myfashiondb.cld48setsmjg.us-east-2.rds.amazonaws.com",
                user="admin",
                password="uofthacks",
                database="myfashiondb"
            )
        print("success")
        #set up cursor and clear  old table
        self.mycursor=self.mydb.cursor()

        #set up table
        # self.mycursor.execute("CREATE TABLE CLOTHING (Brand VARCHAR(50), Info VARCHAR(255))")
        
        print("show tables")
        #must print if you fetch show tables
        self.mycursor.execute("SHOW TABLES")
        for tb in self.mycursor:
            print('table number',tb)
        #self.insertDB('0','BLUE','ADIDAS','WINTER','MALE','www.youtube.com') 

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

    def insertDB(self,id,brand,colour,gender, my_type, price, website, purchasesite):
        #print('insert')
        #insert into Food
        sqlFormula="INSERT INTO CLOTHING (id,colour,brand,gender, type, price, link, purchase) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        fashionItem=(id,colour,brand,gender, my_type, price, website,purchasesite)
        self.mycursor.execute(sqlFormula,fashionItem)
        #self.showTableDB()

    def showTableDB(self):
        self.mycursor.execute('SELECT * FROM CLOTHING')
        print('show',self.mycursor.fetchall())

    def getRowsFromDB(self,inputType,listOfColours):
        selectColour=listOfColours[random.randint(0,len(listOfColours))-1]
        self.mycursor.execute(("SELECT * FROM CLOTHING WHERE Not Type=%s and Colour=%s"),(inputType,selectColour)) #input type is not equal to the new type
        result=self.mycursor.fetchall()
        print(result)
        return result

        
    def clearDB(self):
        try:
            self.mycursor.execute("DROP TABLE testdb.CLOTHING")
        except:
            print('Table Cleared Already')

if __name__=="__main__":
    my_type, recommended_colours = article_class("https://img.favpng.com/15/4/18/t-shirt-adidas-originals-adidas-new-zealand-adidas-australia-png-favpng-u2qyRDREJzX952GtZ3xe9G8BX.jpg")
    print(my_type, recommended_colours) #select first three
    myDB=my_database()
    rows= myDB.getRowsFromDB(my_type,recommended_colours)
    print(type(rows))
    # with open('clothes_database.json') as json_file:
    #     data = json.load(json_file)
    # myDB=my_database()

    # i=0
    # for entry in data["pact"]["top"]:
    #     myDB.insertDB(i,"pact",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    #     i+=1

    # for entry in data["pact"]["bottom"]:
    #     myDB.insertDB(i,"pact",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    #     i+=1
    # for entry in data["pact"]["outerwear"]:
    #     myDB.insertDB(i,"pact",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    #     i+=1

    # # for entry in data["pact"]["shoes"]:
    # #     myDB.insertDB("pact",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])

    # for entry in data["everlane"]["top"]:
    #     myDB.insertDB(i,"everlane",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    #     i+=1

    # for entry in data["everlane"]["bottom"]:
    #     myDB.insertDB(i,"everlane",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    #     i+=1

    # for entry in data["everlane"]["outerwear"]:
    #     myDB.insertDB(i,"everlane",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    #     i+=1

    # for entry in data["everlane"]["shoes"]:
    #     myDB.insertDB(i,"everlane",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    #     i+=1

    # for entry in data["uniqlo"]["top"]:
    #     myDB.insertDB(i,"uniqlo",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    #     i+=1

    # for entry in data["uniqlo"]["bottom"]:
    #     myDB.insertDB(i,"uniqlo",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    #     i+=1

    # for entry in data["uniqlo"]["outerwear"]:
    #     myDB.insertDB(i,"uniqlo",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    #     i+=1
    # for entry in data["uniqlo"]["shoes"]:
    #     myDB.insertDB(i,"uniqlo",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    #     i+=1
    # for entry in data["boden"]["top"]:
    #     myDB.insertDB(i,"boden",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    #     i+=1
    
    # myDB.showTableDB()
    # myDB.mydb.commit()

    # for entry in data["boden"]["bottom"]:
    #     print("pact",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])
    # for entry in data["boden"]["outerwear"]:
    #     print("pact",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])

    # for entry in data["boden"]["shoes"]:
    #     print("pact",entry["colour"],entry["gender"],entry["type"],entry["price"],entry["link"],entry["product link"])