BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "consoles" (
	"console_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	VARCHAR(35) NOT NULL,
	"brand_id"	INTEGER NOT NULL,
	"year"	INTEGER,
	FOREIGN KEY("brand_id") REFERENCES "brands"("brand_id") ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS "brands" (
	"brand_id"	INTEGER NOT NULL,
	"name"	VARCHAR(35) UNIQUE,
	"country_id"	VARCHAR(3),
	PRIMARY KEY("brand_id")
);

INSERT INTO "brands" VALUES (1,'Atari','USA');
INSERT INTO "brands" VALUES (2,'Nintendo','JPN');
INSERT INTO "brands" VALUES (3,'Sega','JPN');
INSERT INTO "brands" VALUES (4,'Sony','JPN');
INSERT INTO "brands" VALUES (5,'Microsoft','USA');

INSERT INTO "consoles" VALUES (6,'Pong',1,1975);
INSERT INTO "consoles" VALUES (7,'2600',1,1977);
INSERT INTO "consoles" VALUES (8,'5200',1,1982);
INSERT INTO "consoles" VALUES (9,'7800',1,1987);
INSERT INTO "consoles" VALUES (10,'Jaguar',1,1993);
INSERT INTO "consoles" VALUES (11,'NES',2,1983);
INSERT INTO "consoles" VALUES (12,'SNES',2,1990);
INSERT INTO "consoles" VALUES (13,'N64',2,1996);
INSERT INTO "consoles" VALUES (14,'NGC',2,2001);
INSERT INTO "consoles" VALUES (15,'WII',2,2006);
INSERT INTO "consoles" VALUES (16,'WII-U',2,2012);
INSERT INTO "consoles" VALUES (17,'Switch',2,2017);

COMMIT;

--List of consoles
SELECT c.name, b.name, b.country_id, c.year 
FROM consoles c, brands b 
WHERE b.brand_id = c.brand_id

--List of Japanese brands
SELECT name 
FROM brands 
WHERE country_id='JPN'

--List of consoles before 1990
SELECT name 
FROM consoles 
WHERE year < 1990

--Quantity of consoles registered
SELECT COUNT(*) 
FROM consoles

--Consoles with 'NES' in his name
SELECT * 
FROM consoles 
WHERE name LIKE '%NES%'