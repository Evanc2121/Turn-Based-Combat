import TBC

def main():
    hero = TBC.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2

    monster = TBC.Character("Monster", 20, 30, 5, 0)

    hero.printStats()
    monster.printStats()

    TBC.fight(hero, monster)

if __name__ == "__main__":

    main()