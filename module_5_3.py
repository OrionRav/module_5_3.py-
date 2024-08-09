# Домашняя работа по уроку "Перегрузка операторов."

# Цель: применить знания о перегрузке арифметических операторов и операторов сравнения.

# Задача "Нужно больше этажей":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".

# Необходимо дополнить класс House следующими специальными методами:
# 1. __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# 2. Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать
# результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# 3. __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# 4. __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).

# Остальные методы арифметических операторов, где self - x, other - y:

# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед
# выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.

# Пример результата выполнения программы:
# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)

# print(h1)
# print(h2)

# print(h1 == h2) # __eq__

# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)

# h1 += 10 # __iadd__
# print(h1)

# h2 = 10 + h2 # __radd__
# print(h2)

# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__

# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# False
# Название: ЖК Эльбрус, кол-во этажей: 20
# True
# Название: ЖК Эльбрус, кол-во этажей: 30
# Название: ЖК Акация, кол-во этажей: 30
# False
# True
# False
# True
# False

# Примечания:
# 1. Методы __iadd__ и __radd__ не обязательно описывать заново, достаточно вернуть значение вызова __add__.
# 2. Более подробно о работе всех перечисленных методов можно прочитать здесь и здесь.

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(0, new_floor + 1):          # а по заданию надо поставить вместо 0 (или убрать) => 1
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
                continue
            if 0 == new_floor:
                print(f'Это подвал или парковка на нижнем этаже: {new_floor}')
                continue
            else:
                print(f'Такого этажа не существует: {new_floor}')
                break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

# дополнено методами:
    def __eq__(self, other):                                                            # 1
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __add__(self, value):                                                           # 3
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):                                                          # 3
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):                                                          # 2
        return self.__iadd__(value)   # или заменим условием (все три строчки следующие) или __add__
        # if isinstance(value, int):
        #     self.number_of_floors += value
        # return self

    def __gt__(self, other):                                                            # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):                                                            # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):                                                            # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):                                                            # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):                                                            # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)      # __eq__

h1 = h1 + 10         # __add__
print(h1)
print(h1 == h2)

h1 += 10             # __iadd__
print(h1)

h2 = 10 + h2         # __radd__
print(h2)

print(h1 > h2)       # __gt__
print(h1 >= h2)      # __ge__
print(h1 < h2)       # __lt__
print(h1 <= h2)      # __le__
print(h1 != h2)      # __ne__