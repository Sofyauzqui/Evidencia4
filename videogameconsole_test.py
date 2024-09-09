import unittest
from videogameconsole import *

class TestVideoGameConsole(unittest.TestCase):
    def testSwitchStatus(self):
        print("--- Test switch status ---")
        ps5 = VideoGameConsole("PS5")
        print("- Turn on:")
        ps5.switchStatus()
        self.assertEqual(ps5.on, True)
        print("- Turn off:")
        ps5.switchStatus()
        self.assertEqual(ps5.on, False)
    
    def testInsertGame(self):
        print("--- Test Insert Game ---")
        superNintendo = VideoGameConsole("Super Nintendo")
        marioCartidge = "Super Mario World"
        print(f"- Insert cartidge '{marioCartidge}'")
        superNintendo.insertGame(marioCartidge)
        self.assertEqual(superNintendo.game, marioCartidge)
        zeldaCartidge = "Zelda Link to the Past"
        print(f"- Trying insert cartidge '{zeldaCartidge}' where cartidge '{marioCartidge}' is inserted")
        superNintendo.insertGame(zeldaCartidge)
        self.assertEqual(superNintendo.game, marioCartidge)

    def testEjectGame(self):
        print("--- Test Eject Game ---")
        sega = VideoGameConsole("Sega")
        print("- Ejecting empty game:")
        sega.ejectGame()
        self.assertEqual(sega.game,"")
        sonicCartidge = "Sonic"
        sega.insertGame(sonicCartidge)
        print(f"- Ejecting game '{sonicCartidge}'")
        sega.ejectGame()
        self.assertEqual(sega.game,"")

if __name__ == '__main__':
    unittest.main()