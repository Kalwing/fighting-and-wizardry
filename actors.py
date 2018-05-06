import random
import applib as al


class Creatures:
    NAME_PARTICLES = ["to",
                      "ma",
                      "yv",
                      "ve",
                      "er",
                      "ric",
                      "dar",
                      "gen"]
    MAX_NAME_SIZE = 2

    @classmethod
    def nameGenerator(cls):
        r = ""
        for i in range(random.randint(1, cls.MAX_NAME_SIZE)):
            partId = random.randint(0, len(cls.NAME_PARTICLES) - 1)
            r += cls.NAME_PARTICLES[partId]
        return r.capitalize()

    def __init__(self, name, level=1, att=7, par=8):
        self.name = name
        self.level = level
        self.baseAttack = att
        self.exp = 0
        self.baseParry = par
        self.life = self.getMaxLife()

    def __repr__(self):
        level = ("{:s} a {:s} of level {:d}"
                 .format(self.name, self.__class__.__name__, self.level))
        life = " life:{:d}".format(self.life)
        return "{:<35s}|{:>10s}".format(level, life)

    def getMaxAttack(self):
        return self.baseAttack + 2 * self.level

    def getMaxParry(self):
        return self.baseParry + 2 * self.level

    def getMaxLife(self):
        return (self.baseAttack + self.baseParry) // 2 + 2 * self.level

    def getParry(self):
        return random.randint(0, self.getMaxParry())

    def getAttack(self):
        return random.randint(0, self.getMaxAttack())

    def isAlive(self):
        return self.life > 0

    def attack(self, creature):
        if creature.isAlive():
            al.print_curinfo("{:s} attack {:s} !".format(self.name,
                                                         creature.name))
            attackVal = self.getAttack()
            opponentParry = creature.getParry()
            fightValue = attackVal - opponentParry
            al.print_curinfo("{:s} made an attack of {:d} !"
                             .format(self.name, attackVal))
            al.print_curinfo("{:s} made a parry of {:d}."
                             .format(creature.name, opponentParry))
            if fightValue > 0:
                creature.loseLife(fightValue)
                al.print_result("The attack was successful.")
                al.print_endinfo("{:s} life: {:d}".format(creature.name,
                                                          creature.life))
                if not creature.isAlive():
                    self.increaseExp(creature.level)
                    al.print_result("{:s}'s dead.".format(creature.name))
            else:
                al.print_result("The attack failed.")
        else:
            al.print_warning("It's dead.")

    def loseLife(self, n: int):
        self.life = max(0, self.life - n)

    def increaseExp(self, n: int):
        self.exp += n
        newLevel = self.exp // 5 + 1
        if newLevel > self.level:
            self.life = self.getMaxLife()
            self.level = newLevel
            al.print_result("Level up ! You're now level {:d}"
                            .format(self.level))


class Wizard(Creatures):

    def getMaxLife(self):
        return (self.baseAttack + self.baseParry) // 2 + 4 * self.level

    def __init__(self, name, level=1, att=15, par=15):
        super().__init__(name, level, att, par)


class Toad(Creatures):
    NAME_PARTICLES = ["gu",
                      "bo",
                      "ga",
                      "be",
                      "a",
                      "bug",
                      "wog",
                      "blo"]
    MAX_NAME_SIZE = 3

    def __init__(self, name, level=1, att=4, par=2):
        super().__init__(name, level, att, par)


class Skeleton(Creatures):
    NAME_PARTICLES = ["kre",
                      "vox",
                      "vor",
                      "tak",
                      "an",
                      "thrax",
                      "hem",
                      "may"]
    MAX_NAME_SIZE = 2

    def __init__(self, name, level=1, att=10, par=8):
        super().__init__(name, level, att, par)


class Dragon(Creatures):
    NAME_PARTICLES = ["Faf",
                      "ner",
                      "an",
                      "cal",
                      "ag",
                      "on",
                      "drog",
                      "chry",
                      "so",
                      "phy",
                      "lax",
                      "glae",
                      "dr",
                      "er",
                      "rol",
                      "saph"
                      "i",
                      "ra",
                      "eld",
                      "rax"]
    MAX_NAME_SIZE = 4

    def __init__(self, name, level=1, att=25, par=20):
        super().__init__(name, level, att, par)
