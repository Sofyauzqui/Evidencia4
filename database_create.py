import sqlite3

myConnection = sqlite3.connect("VideoGameConsole")

myCursor = myConnection.cursor()

myCursor.execute('''
                 CREATE TABLE brands (
                 brand_id INTEGER NOT NULL PRIMARY KEY, 
                 name VARCHAR(35) UNIQUE, 
                 country_id VARCHAR(3))
                 ''')
myCursor.execute('''
                 CREATE TABLE consoles (
                 console_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 name VARCHAR(35) NOT NULL, 
                 brand_id INTEGER NOT NULL, 
                 year INTEGER, 
                 FOREIGN KEY (brand_id) REFERENCES brands (brand_id) ON DELETE CASCADE ON UPDATE NO ACTION)
                 ''')

myConnection.close()