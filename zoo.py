class Zookeeper:
    Name = ''

    def do_clean(self, aviary_n):
        aviary_n.is_clean = True
        print('Aviary', aviary_n.number, 'is cleaned')

    def do_feed(self, animal_n):
        animal_n.is_hungry = False
        print('Animal', animal_n.Name, 'is fed')

    def __init__(self, name):
        self.Name = name


class Animal:
    def __init__(self, name):
        self.Name = name
        self.is_hungry = True
        self.is_happy = False


class Aviary:
    def __init__(self, num):
        self.number = num
        self._av_Animals = []
        self.is_open = False
        self.is_clean = False

    def add_anm(self, anm):
        self._av_Animals.append(anm)
        print('Av.#', self.number, ' - added animal:', anm.Name)

    def who_in(self):
        print('Aviary ', self.number, 'have:')
        for nn in self._av_Animals:
            print('   ', nn.Name)


# Main programm

av01 = Aviary(1)
av02 = Aviary(2)
av03 = Aviary(3)

kp01 = Zookeeper('John')

an01 = Animal('Tiger')
an02 = Animal('Bear')
an03 = Animal('Rabbit')

av01.add_anm(an01)
av02.add_anm(an02)
av03.add_anm(an03)

av01.who_in()
av02.who_in()
av03.who_in()

kp01.do_feed(an01)
kp01.do_clean(av01)

