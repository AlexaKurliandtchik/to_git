class Transport():
    def __init__(self, max_weight, speed, price):
        self.max_weight = max_weight
        self.speed = speed
        self.price = price


class Car(Transport):
    def __init__(self, max_weight, speed, price):
        super().__init__(max_weight, speed, price)


class Avia(Transport):
    def __init__(self, max_weight, speed, price, min_weight, max_distance, min_distance):
        super().__init__(max_weight, speed, price)
        self.min_weight = min_weight
        self.max_distance = max_distance
        self.min_distance = min_distance


class Train(Transport):
    def __init__(self, max_weight, speed, price, min_weight, min_distance):
        super().__init__(max_weight, speed, price)
        self.min_weight = min_weight
        self.min_distance = min_distance


class Filials():
    def __init__(self, city_name):
        self.city_name = city_name


class Minsk(Filials):
    def __init__(self, city_name, to_moscow, to_paris, to_beijing):
        super().__init__(city_name)
        self.to_moscow = to_moscow
        self.to_paris = to_paris
        self.to_beijing = to_beijing


class Moscow(Filials):
    def __init__(self, city_name, to_minsk, to_paris, to_beijing):
        super().__init__(city_name)
        self.to_minsk = to_minsk
        self.to_paris = to_paris
        self.to_beijing = to_beijing


class Paris(Filials):
    def __init__(self, city_name, to_moscow, to_minsk, to_beijing):
        super().__init__(city_name)
        self.to_moscow = to_moscow
        self.to_minsk = to_minsk
        self.to_beijing = to_beijing

    # def cost_order(self):
    #     self.weigth = int(input("Введите вес груза в тоннах: "))
    #     self.city_name = input("Введите пункт доставки груза: ")
    #     if self.city_name == 'Minsk':
    #         self.distance = paris.to_minsk
    #         self.cost = self.weigth * self.distance
    #         return self.cost
    #     if self.city_name == 'Moscow':
    #         self.distance = paris.to_moscow


class Beijing(Filials):
    def __init__(self, city_name, to_moscow, to_minsk, to_paris):
        super().__init__(city_name)
        self.to_moscow = to_moscow
        self.to_minsk = to_minsk
        self.to_paris = to_paris


car = Car(22, 90, 5)
avia = Avia(110, 933, 10, 20, 14200, 500)
train = Train(220, 48, 3, 40, 100)
minsk = Minsk("Minsk", 688, 2126, 9928)
moscow = Moscow("Moscow", 688, 2813, 9190)
paris = Paris("Paris", 2813, 2126, 10610)
beijing = Beijing("Beijing", 9190, 9928, 10610)
print(paris.cost_order())
orders = []
