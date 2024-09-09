import _sqlite3

myConnection = _sqlite3.connect("VideoGameConsole")

myCursor = myConnection.cursor()

myCursor.execute('''
                 SELECT c.name, b.name, b.country_id, c.year 
                 FROM consoles c, brands b 
                 WHERE b.brand_id = c.brand_id
                 ''')
consolesList = myCursor.fetchall()
print("List of consoles")
for consoles in consolesList:
    print(f"Console: {consoles[0]:<6} | Brand: {consoles[1]:<8} | Country: {consoles[2]} | Year: {str(consoles[3])}") 

myCursor.execute("SELECT name FROM brands WHERE country_id='JPN'")
print("\nlist of Japanese brands")
print(myCursor.fetchall())

myCursor.execute("SELECT name FROM consoles WHERE year < 1990")
print("\nlist of consoles before 1990")
print(myCursor.fetchall())

myCursor.execute("SELECT COUNT(*) FROM consoles")
print("\nQuantity of consoles registered")
print(myCursor.fetchall())

myCursor.execute("SELECT * FROM consoles WHERE name LIKE '%NES%'")
print("\nConsoles with 'NES' in his name")
print(myCursor.fetchall())

myConnection.close()