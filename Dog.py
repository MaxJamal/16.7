from Animal_base import Animal

class Dog(Animal):

    def __init__(self, name, gender, breed, age, doc, status, species='собака'):
        super().__init__(name, species, gender, breed, age, doc, status)

    def display_animal(self):
        print(f'Имя: {self.name}\n'
              f'Вид: {self.species}\n'
              f'Пол: {self.gender}\n'
              f'Порода: {self.breed}\n'
              f'Возраст: {self.age}\n'
              f'Регистрационный документ: {self.doc}\n'
              f'Статус: {self.status}\n')
