from actors import Creatures, Wizard
import applib as al
import time


def main():
    al.print_header(40, "Fighting & Wizardry")
    # TODO: Multiple Room ?
    monsters = [Creatures("Toad", att=3, par=2),
                Creatures("Toad", att=3, par=2),
                Creatures("Toad", level=3, att=3, par=2),
                Creatures("Skeleton"),
                Creatures("Skeleton", level=2)]
    hero = Wizard("Gandalf")

    while(True):
        al.print_endinfo("You're {:s} | life {:d} | level {:d}"
                         .format(hero.name, hero.life, hero.level))
        cmd = al.input_("Do you want to [a]ttack, [r]un away, "
                        "[l]ook around or e[x]it ? ").lower().strip()

        if cmd == 'a' and hero.isAlive():
            try:
                selectedCreatureId = int(al.input_("What's the number of the "
                                                   + "creature you want to "
                                                   + "attack ? "))
            except ValueError:
                al.print_warning("Wrong input.")
                continue
            if not (0 < selectedCreatureId < len(monsters)):
                al.print_warning("This creature doesn't exist.")
                continue

            hero.attack(monsters[selectedCreatureId])

            if not monsters[selectedCreatureId].isAlive():
                del monsters[selectedCreatureId]

            for monster in monsters:
                if hero.isAlive():
                    time.sleep(1)
                    monster.attack(hero)
                else:
                    break
            if not hero.isAlive():
                al.print_result("You have been defeated")

        elif cmd == 'r':
            print("run")
        elif cmd == 'l':
            if len(monsters) == 0:
                al.print_result("Everything's empty.")
            for i in range(len(monsters)):
                al.print_result("{:d}. {:s}".format(i, str(monsters[i])))
        elif cmd == 'x':
            print("bye")
            break
        else:
            al.print_warning("Wrong input. Please use the following command:")


if __name__ == "__main__":
    main()
