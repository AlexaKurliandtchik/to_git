class Alive:
    def __init__(self, count):
        self.count = count

    def info(self):
        print("count:", self.count)


class Plants(Alive):
    def __init__(self, koef_repr, count):
        super().__init__(count)
        self.koef_repr = koef_repr

    def grown(self):
        self.count *= self.koef_repr

    def info(self):
        print("count plants: ", self.count)

    def rabbits_food(self, count_rabbits):
        self.count -= count_rabbits * 10

    def add_plants(self, count_plants):
        self.count += count_plants


class Rabbits(Alive):
    def __init__(self, koef_repr, koef_death, count):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def reproduction(self):
        self.count *= self.koef_repr

    def death(self):
        self.count -= int(self.count * self.koef_death)

    def info(self):
        print("count rabbits: ", self.count)

    def take_away(self, count_rabbits):
        self.count -= count_rabbits

    def fox_food(self, count_foxes):
        self.count -= count_foxes * 2

    def add_rabbits(self, count_rabbits):
        self.count += count_rabbits


class Foxes(Alive):
    def __init__(self, koef_repr, koef_death, count):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def reproduction(self):
        self.count *= self.koef_repr

    def death(self):
        self.count -= int(self.count * self.koef_death)

    def info(self):
        print("count foxes: ", self.count)

    def take_away(self, count_foxes):
        self.count -= count_foxes


def factor(f):

    if f == 1:
        plants.koef_repr -= 5
    if f == 2:
        rabbits.koef_death += 0.5
        foxes.koef_death += 0.5


plants = Plants(10, 1000)
rabbits = Rabbits(7, 0.2, 10)
foxes = Foxes(3, 0.1, 1)
year = 1
print("Begin:")
plants.info()
rabbits.info()
foxes.info()
while year <= 10:
    factor(int(input("Выберите сценарий на год: 1 - засуха, 2 - болезнь, 3 - обычный год:  ")))
    if plants.count // 10 <= rabbits.count:
        print("Warning! Plants is very low")
        # plants.info()
        # rabbits.info()
        # foxes.info()
        choise1 = int(input("Enter 1 - add plants, 2 - take away rabbits  "))
        if choise1 == 1:
            count = int(input("Enter count plants: "))
            plants.add_plants(count)
        elif choise1 == 2:
            count = int(input("Enter count rabbits: "))
            rabbits.take_away(count)

    if rabbits.count // 2 <= foxes.count:
        print("Warning! Rabbits is very low")
        choise2 = int(input("Enter 1 - add rabbits, 2 - take away foxes  "))
        if choise2 == 1:
            count1 = int(input("Enter count rabbits: "))
            rabbits.add_rabbits(count1)
        elif choise2 == 2:
            count1 = int(input("Enter count foxes: "))
            foxes.take_away(count1)

    if plants.count <= 0 or rabbits.count <= 0:
        print(f"Fatality on year: {year}, all our alive is death")
        break

    plants.grown()
    plants.rabbits_food(rabbits.count)
    rabbits.reproduction()
    rabbits.death()
    rabbits.fox_food(foxes.count)
    foxes.reproduction()
    foxes.death()

    print("Year: ", year)
    plants.info()
    rabbits.info()
    foxes.info()
    year += 1


