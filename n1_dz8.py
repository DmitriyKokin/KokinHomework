from typing import _SpecialForm


class animals:
    """
    Под type подразумевается: млекопитающие, пресмыкающиеся и тд
    habitat - среда обитания (наземная, водная, воздушная, смешанная)
    age - возраст
    gender - пол
    wildness определяет: дикое или домашнее животное
    name - кличка
    species - разновидность (слон кот жираф и тд)
    """
    def __init__(self, typee, habitat, age, gender, wildness, species, voice):
        self.typee = typee
        self.habitat = habitat
        self.age = age
        self.gender = gender
        self.wildness = wildness
        self.species = species
        self.voice = voice
    
    def Hi(self):
        print(f'Привет! Я {self.species}.\nя отношусь к {self.typee}, мне {self.age} лет, я живу в {self.habitat} среде')

    def say(self):
        if self.typee != 'рыба':
            print(f'{self.voice}')
        else:
            print(f'Рыбы разговаривать не умеют')

"""В моем случае теряется только тип животного и добавляется параметр опасности для человека (dangerous)"""

class mammals(animals):
    def __init__(self, typee, habitat, age, gender, wildness, species, voice, dangerous):
        super().__init__(typee, habitat, age, gender, wildness, species, voice)
        self.dangerous = dangerous
        self.typee = 'МЛЕКОПИТАЮЩИЕ'
        

    def mammalsHello(self):
        try:
            a = int(self.dangerous)
            if a > 5:
                print(f'Привет, я {self.species}, у меня показатель опасности {self.dangerous}, так что будь аккуратней со мной')
            elif a > 2 and a < 6:
                 print(f'Привет, я {self.species}, у меня показатель опасности {self.dangerous}, так что предлагаю не ссориться')
            else:
                print(f'Привет, я {self.species}, у меня показатель опасности {self.dangerous}, не обижай меня')
        except Exception:
            print(f'ой вы что то не то ввели')
            exit()
            
    def say(self):
        print(f'{self.voice}')

class Human(mammals):
    def __init__(self, age,  gender, name, _PhoneNumber, wildness, species, voice, dangerous):
        super().__init__(age, gender, name, _PhoneNumber, wildness, species, voice, dangerous)
        self.name = name
        self._PhoneNumber = _PhoneNumber
        self.wildness = ''
        self.species = name
        self.voice = 'Я разговариваю как и все остальные люди!'
        self.dangerous = dangerous

    def count(self, text):
        print(f'{self.name}:  Длинна строки: {len(text)} символов')

class Cat(mammals):
    def __init__(self, age, gender, name, breed, wildness, species, voice, dangerous):
        super().__init__(name, gender, age, breed, wildness, species, voice, dangerous)
        self.species = name
        self.breed  = breed
        self.habitat = 'Наземная. Частво в гостях у человека'
        
class Dog(mammals):
    def __init__(self, age, gender, name, hunting, wildness, species, voice, dangerous):
        super().__init__(name, gender, age, hunting, wildness, species, voice, dangerous)
        self.species = name
        self.breed  = hunting
        self.habitat = 'Наземная. Частво в гостях у человека'

        


'''Знакомство с животными'''
animalone = animals('птица', 'наземно-воздушная', 4, 'male', 'yes', 'голубь', 'GUL GUL GUL')
animalone.Hi()
animalone.say()

animaltwo = animals('рыба', 'водная', 1, 'female', 'yes', 'рыба-меч', '"рыбы не разговаривают"')
animaltwo.Hi()
animaltwo.say()

"""Знакомство с млекопитающим"""
mammalone = mammals('Млекопитающее', 'наземная', 12, 'male', 'yes', 'Медведь', 'RRRRRRRRRRrR', '10')
mammalone.mammalsHello()
mammalone.say()

"""Знакомство с человеком"""
Humanone = Human(20, 'male', 'Alex', '8-800-555-35-35', '', '', '', 7)
Humanone.mammalsHello()
Humanone.say()
Humanone.count('Тестовая строка')

"""Знакомство с Котом"""
Cat1 = Cat(2, 'female', 'Барсик', 'default', 'no', 'Кот', 'meow', 2)
Cat1.say()
Cat1.mammalsHello()
Cat1.Hi()

"""Знакомство с собакой"""
Dog1 = Dog(2, 'Male', 'Шарик', 'yes', 'no', 'Собака', 'GAV', 6)
Dog1.say()
Dog1.mammalsHello()
Dog1.Hi()