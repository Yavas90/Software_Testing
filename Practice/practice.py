class HiPerson:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Привет! Меня зовут', self.name)


p = HiPerson('YaVas')
p.say_hi()


class InfoPerson:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_info(self, n):
        for i in range(n):
            print(f"Name:{self.name}, surname:{self.surname}")


p1 = InfoPerson("Borov", "Borovskiy")
p1.print_info(3)
