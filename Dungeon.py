import random
direction_map: dict[str:str] = {"up": "down", "down": "up", "left": "right", "right": "left"}

class Item:
    def __init__(self, givenName: str, givenDesc: str):
        self.name: str = givenName
        self.description: str = givenDesc
    
    def __str__(self):
        return "There is a {}, {}. ".format(self.name, self.description)

class Loot(Item):
    def __init__(self, givenName: str, givenDesc: str, givenValue: int):
        super().__init__(givenName, givenDesc)
        self.value: int = givenValue

    def __str__(self):
        return super().__str__() + "It has a value of '{}'.".format(self.value)

class Weapon(Item):
    def __init__(self, givenName: str, givenDesc: str, givenDamge: int):
        super().__init__(givenName, givenDesc)
        self.damage: int = givenDamge

class Room:
    itemSearched: bool
    roomsObserved: bool

    def __init__(self, givenName: str, givenDesc: str, lockedRoom: bool = False, unlockItem: Item = None):  
        self.name: str = givenName
        self.description: str = givenDesc
        self.items: list[Item] = list()
        self.connectedRooms: dict[str: Room] = dict()
        self.locked: bool = lockedRoom
        self.unlockItem: Item = unlockItem
        self.itemSearched = False
        self.roomsObserved = False
    
    def __str__(self):
        return "This is '{}'. It's described as '{}'.".format(self.name, self.description)

    def addExistingItem(self, existingItem) -> None:
        self.items.append(existingItem)

    def connectRoom(self, existingRoom: "Room", direction: str, twoWay: bool = True) -> None:
        self.connectedRooms[direction] = existingRoom
        if twoWay:
            existingRoom.connectRoom(self, direction_map[direction], False)

    def removeExistingItem(self, existingItem) -> None:
        self.items.remove(existingItem)

    def displayItems(self, indexed=False):
        if len(self.items) > 0:
            for i in range(len(self.items)):
                if indexed:
                    print(str(i+1) + ") ", end="")
                print(self.items[i])
        else:
            print("There are no items in this room.")

    def setItemSearched(self, newValue) -> None:
        self.itemSearched = newValue

    def setRoomsObserved(self, newValue) -> None:
        self.roomsObserved = newValue

    def displayAdjacentRooms(self):
        for direction in self.connectedRooms.keys():
            print("To the {} is the {}.".format(direction, self.connectedRooms[direction].name))

class Enemy:
    def __init__(self, givenName:str, givenDesc:str, givenHealth:int, givenWeapon):
        self.name: str = givenName
        self.description: str = givenDesc
        self.health: int = givenHealth
    
        self.weapon: int = givenWeapon
         

    def __str__(self):
        return "Enemy: {}, Description: {}, Health: {}, Damage: {}".format(self.name, self.description, self.health, self.damage)
    
    def attack(self, target: "Player"):
        target.health -= self.weapon.damage

    def setCurrentRoom(self, newRoom: Room):
        self.currentRoom = newRoom


class Player:
    currentRoom: Room

    def __init__(self, givenName: str, givenRoom: Room, givenHealth: int = 100):
        self.name: str = givenName
        self.setCurrentRoom(givenRoom)
        self.items: list[Item] = list()
        self.health: int = givenHealth

    def __str__(self):
        return "Player: {}, current room: {}, items: {}".format(self.name, self.currentRoom.name, self.items)
    
    def setCurrentRoom(self, newRoom: Room) -> bool:
        if newRoom.locked:
            if newRoom.unlockItem in self.items:
                self.currentRoom = newRoom
                return True
        else:
            self.currentRoom = newRoom
            return True
        return False

    def collectItem(self, existingItem: Item):
        self.items.append(existingItem)
        self.currentRoom.removeExistingItem(existingItem)

class Game:
    player1: Player
    rooms: list[Room]
    items: list[Item]
    adjacentRooms: dict[str: Room]

    def __init__(self):
        self.rooms = list()
        self.items = list()

        self.generateItems()
        self.generateRooms()

        uName = input("Enter your player name: ")
        self.player1 = Player(uName, self.rooms[0])

    def generateRooms(self) -> None:
        self.rooms.append(Room("Spawn Point", "The starting point of your adventure."))
        tempSpawnPoint = self.rooms[-1]

        self.rooms.append(Room("Mystic Cave", "A dark cave filled with glowing crystals and eerie sounds."))
        tempSpawnPoint.connectRoom(self.rooms[-1], "right")

        self.rooms.append(Room("Goblin Den", "A foul-smelling den inhabited by aggressive goblins."))
        self.rooms[-2].connectRoom(self.rooms[-1], "right")

        self.rooms.append(Room("Narrow Passage", "A narrow passage with barely enough room to squeeze through."))
        self.rooms[-2].connectRoom(self.rooms[-1], "right")

        self.rooms.append(Room("Treasure Room", "A room filled with glittering gold coins and precious gems.", True, self.items[0]))  # Locked room
        self.rooms[-3].connectRoom(self.rooms[-1], "down")

        self.rooms.append(Room("Library", "A room filled with ancient books and scrolls."))
        self.rooms[-2].connectRoom(self.rooms[-1], "right")

        self.rooms.append(Room("Armory", "A room filled with weapons and armor.", True, self.items[1]))  # Locked room
        self.rooms[-2].connectRoom(self.rooms[-1], "right")

        self.rooms.append(Room("Alchemy Lab", "A room filled with potions and alchemical ingredients."))
        self.rooms[-2].connectRoom(self.rooms[-1], "right")

        self.rooms.append(Room("Dining Hall", "A grand hall with a long dining table."))
        self.rooms[-2].connectRoom(self.rooms[-1], "right")

        self.rooms.append(Room("Throne Room", "A majestic room with a grand throne."))
        self.rooms[-2].connectRoom(self.rooms[-1], "right")

        self.rooms.append(Room("Secret Chamber", "A hidden chamber with mysterious artifacts.", True, self.items[2]))  # Locked room
        self.rooms[-2].connectRoom(self.rooms[-1], "right")

        self.rooms.append(Room("End Point", "The final room of your adventure."))
        self.rooms[-2].connectRoom(self.rooms[-1], "right")

    def generateItems(self) -> None:
        sword = Weapon("Sword", "A sharp sword for combat", 10)
        self.items.append(Item("Key", "Opens the Treasure Room"))
        self.items.append(Item("Armory Key", "Opens the Armory"))
        self.items.append(Item("Secret Chamber Key", "Opens the Secret Chamber"))
        self.items.append(Item("Shield", "A sturdy shield for protection"))
        self.items.append(Item("Potion", "A healing potion"))
        self.items.append(Item("Map", "A map of the dungeon"))
        self.items.append(Item("Book", "An ancient book with valuable information"))
        self.items.append(Item("Armor", "A set of protective armor"))
        self.items.append(Item("Gem", "A precious gem"))
        self.items.append(Item("Scroll", "A magical scroll"))
        self.items.append(Item("Lantern", "A lantern to light your way"))
        self.items.append(Item("Ring", "A ring with mysterious powers"))
        self.items.append(Item("Amulet", "An amulet with protective charms"))

    def generateEnemies(self) -> None:
        Goblin1 = Enemy("Goblin", "A small, green-skinned creature with sharp teeth.", 100, Weapon("Dagger", "A small, sharp dagger"))
        Goblin1.setCurrentRoom(self.rooms[2])

    def PlayGame(self):
        won: bool = False
        while not won:
            print(f"You are in '{self.player1.currentRoom.name}'")
            userChoice = input("1) Search the current Room for items\n"
                                "2) Collect item from the room\n"
                                "3) Observe adjacent rooms\n"
                                "4) Navigate into adjacent Room\n")
            
            match userChoice:
                case "1":
                    #search current room
                    self.player1.currentRoom.displayItems()
                    self.player1.currentRoom.setItemSearched(True)
                case "2":
                    #collect item
                    if self.player1.currentRoom.itemSearched:
                        self.player1.currentRoom.displayItems(True)
                        if len(self.player1.currentRoom.items) > 0:
                            itemChoice = input()
                            try:
                                itemChoice = int(itemChoice)
                                if 0 < itemChoice <= len(self.player1.currentRoom.items):
                                    self.player1.collectItem(self.player1.currentRoom.items[itemChoice-1])
                            except ValueError:
                                pass
                    else:
                        print("You must search the room first.")
                case "3":
                    #observe adjacent rooms
                    self.player1.currentRoom.displayAdjacentRooms()
                    self.player1.currentRoom.setRoomsObserved(True)
                case "4":
                    #navigate into adjacent room
                    if self.player1.currentRoom.roomsObserved:
                        if len(self.player1.currentRoom.connectedRooms.keys()) > 0:
                            directionChoice = input("Enter the direction you want to go: ")
                            if directionChoice in self.player1.currentRoom.connectedRooms.keys():
                                if self.player1.setCurrentRoom(self.player1.currentRoom.connectedRooms[directionChoice]):
                                    if self.player1.currentRoom.name == "End Point":
                                        print("Congratulations! You have reached the end of the dungeon.")
                                        won = True
                                else:
                                    print(f"The room is locked. You need {self.player1.currentRoom.unlockItem.name} to enter.")
                            else:
                                print("Invalid direction.")
                    else:
                        print("You must observe the adjacent rooms first.")

Game1: Game = Game()
Game1.PlayGame()
