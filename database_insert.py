import _sqlite3

myConnection = _sqlite3.connect("VideoGameConsole")

myCursor = myConnection.cursor()

brands = [
    (1,'Atari','USA'),
    (2,'Nintendo','JPN'),
    (3,'Sega','JPN'),
    (4,'Sony','JPN'),
    (5,'Microsoft','USA')
]
myCursor.executemany("INSERT INTO brands VALUES (?,?,?)", brands)
#myCursor.execute("INSERT INTO brands (brand_id, name, country_id) VALUES (1,'Atari','USA')")

consoles = [
    ('Pong',1,1975),
    ('2600',1,1977),
    ('5200',1,1982),
    ('7800',1,1987),
    ('Jaguar',1,1993),
    ('NES',2,1983),
    ('SNES',2,1990),
    ('N64',2,1996),
    ('NGC',2,2001),
    ('WII',2,2006),
    ('WII-U',2,2012),
    ('Switch',2,2017),
]
myCursor.executemany("INSERT INTO consoles VALUES (NULL,?,?,?)", consoles)
#myCursor.execute("INSERT INTO console (console_id, name, brand_id, version) VALUES (1,'Pong',1,1975)")

myConnection.commit()

myConnection.close()