from random import randint
from math import floor
from actors import Toad, Skeleton, Dragon


class Room:
    MAX_DIFF = 3

    MONST_BY_DIFF = [[Toad, Skeleton],
                     [Toad, Skeleton],
                     [Skeleton, Dragon],
                     [Skeleton, Dragon]]

    DESC_BY_DIFF = ["remind you of kindergarten",
                    "seems to be a good source of training",
                    "is probably gonna be your last",
                    "is what your worst nightmare looks like"]

    def __init__(self, prec=None, difficulty=0):
        self.prec = prec
        self.next = None
        self.difficulty = difficulty
        self.monsters = []
        maxNb = 8//((difficulty + 1) * 1.5)
        self.monstersNb = randint(1, max(2, maxNb))
        roomType = Room.MONST_BY_DIFF[difficulty]
        for i in range(self.monstersNb):
            monsterType = randint(0, len(roomType) - 1)
            monsterClass = roomType[monsterType]
            monsterLevel = randint(1, floor((difficulty + 1) * 1.5))
            name = monsterClass.nameGenerator()
            monster = monsterClass(name, level=monsterLevel)
            self.monsters.append(monster)

    def __repr__(self):
        r = "This room{:s}"
        if self.monstersNb > 0:
            r = r.format(" " + Room.DESC_BY_DIFF[self.difficulty] + ". ")
            r += "There's {:d} monster".format(self.monstersNb)
            if self.monstersNb > 1:
                r += "s"
            r += " in there.\n"

            r += self.printAllMonsters()
        else:
            r = r.format("'s empty.")
        return r

    def printAllMonsters(self):
        r = ""
        if self.monstersNb > 0:
            for i in range(self.monstersNb):
                monster = self.monsters[i]
                r += "{:d}. {:s}\n".format(i, str(monster))
        return r

    def isEmpty(self):
        return self.monstersNb == 0

    def removeMonster(self, id):
        self.monstersNb -= 1
        del self.monsters[id]

    def setNext(self, room):
        self.next = room
