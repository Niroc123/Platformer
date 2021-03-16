class Cat():
    def __init__(self):
        self.colour = ""
        self.name = ""
        self.weight = 0

    def meow(self):
        print("MEOW")


my_cat = Cat()

my_cat.colour = "tabby"
my_cat.name = "Git"
my_cat.weight = 15

#my_cat.meow()


class Monster():
    def __int__(self):
        self.monster_name = ""
        self.monster_health = 0

    def decrease_health(self):

        self.monster_health -= 1

        if self.monster_health <= 0:
            print("The ",chad.monster_name," is dead praise the hero")


chad = Monster()

chad.monster_name = "Chad Zoomer"
chad.monster_health = 1

chad.decrease_health()
