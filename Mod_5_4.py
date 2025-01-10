class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        hh = []
        hh.append(args[0])
        cls.houses_history = cls.houses_history + hh
        #print(cls.houses_history)
        return object.__new__(cls)



    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= int(new_floor) <= self.number_of_floors:
            for i in range(1, int(new_floor) + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self
    def __iadd__(self, value):
        self.number_of_floors += value
        return self
    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return self

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __del__(self):
        print (f'{self.name} снесён, но он останется в истории')






h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрешки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)