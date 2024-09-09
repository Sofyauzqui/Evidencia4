#definimos el constructor usando la palabra reservada __init
#self es una referencia a la instancia
#podemos pasarles valores como paràmetros al constructor (como name) y asignarselos como propiedades a la instancia de la clase
#en los metodos podemos acceder a estas propiedades haciendo uso de la palabra reservada self. y el nombre de la propiedad
class VideoGameConsole: 
    def __init__(self, name):
        self.name = name
        self.on = False
        self.game = ""
    def switchStatus(self):
        if self.on:
            self.on = False
        else:
            self.on = True
    def insertGame(self, game):
        if self.game == "":
            self.game = game
        else:
            print(f"can't insert game '{game}'\ngame '{self.game}' is currently in console\n")
    def ejectGame(self):
        if self.game != "":
            print(f"game '{self.game}' ejected\n")
            self.game = ""
        else:
            print("no game device")
    def printStatus(self):
        if self.on:
            status = "on"
        else:
            status = "off"
        print(f"console name '{self.name}'\nstatus '{status}'\ngame '{self.game}'")