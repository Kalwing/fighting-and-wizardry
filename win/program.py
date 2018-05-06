from actors import Wizard
from location import Room
import applib as al
import time
import random


def main():
    al.print_header(40, "Fighting & Wizardry")

    heroName = al.input_("What's your name valiant wizard ? ")
    hero = Wizard(heroName)

    try:
        dungeonSize = int(al.input_("How many rooms are you ready to face ? "))
    except ValueError:
        al.print_warning("Wrong input. Length set to default: 5")
        dungeonSize = 5
    if dungeonSize <= 0:
        al.print_warning("That's not much. Length set to default: 5")
        dungeonSize = 5
    rooms = createRoomChain(dungeonSize)
    actualRoom = rooms[0]

    al.print_result(str(actualRoom))

    while(True):
        al.print_endinfo("You're {}".format(hero))
        cmd = al.input_(inputStringGen(actualRoom, hero)).lower().strip()

        if ('a' in cmd and len(cmd) <= 2) and hero.isAlive():

            # Player Turn
            if cmd == 'a':  # If the user didn't specify a monster
                try:
                    selectedCreatureId = int(al.input_("What's the number of "
                                                       + "the creature you "
                                                       + "want to attack ? "))
                except ValueError:
                    al.print_warning("Wrong input.")
                    continue
            else:
                selectedCreatureId = int(cmd[-1])
            if not (0 <= selectedCreatureId < actualRoom.monstersNb):
                al.print_warning("This creature doesn't exist.")
                continue

            hero.attack(actualRoom.monsters[selectedCreatureId])
            if not actualRoom.monsters[selectedCreatureId].isAlive():
                actualRoom.removeMonster(selectedCreatureId)

            # Monsters Turn
            for monster in actualRoom.monsters:
                if hero.isAlive():
                    time.sleep(1)
                    monster.attack(hero)
                else:
                    break
            if not hero.isAlive():
                al.print_result("You have been defeated")

        elif cmd == 'g' and actualRoom.next is not None:
            al.print_curinfo("\nYou walk into the darkness..\n")
            actualRoom = actualRoom.next
            al.print_result(str(actualRoom))
        elif cmd == 'l':
            al.print_result(str(actualRoom))
        elif cmd == 'x':
            print("bye")
            break
        else:
            al.print_warning("Wrong input. Please use the following command:")


def inputStringGen(room: Room, hero: Wizard):
    r = "Do you want to "
    if hero.isAlive():
        if not room.isEmpty():
            r += "[a]ttack, "
        elif room.next is not None:
            r += "[g]o deeper in the dungeon, "
    r += "[l]ook around, "
    r += "e[x]it ? "
    return r


def createRoomChain(size: int):
    rooms = []
    last = None
    for i in range(size):
        difficulty = min(Room.MAX_DIFF, random.randint(i//Room.MAX_DIFF, i))
        room = Room(difficulty=difficulty, prec=last)
        rooms.append(room)
        last = Room
    for i in range(size):
        if i < size - 1:
            rooms[i].setNext(rooms[i+1])
    return rooms


if __name__ == "__main__":
    main()
