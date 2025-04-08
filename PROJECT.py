
class Base:
    def __init__(self, n, h = 100, m = 0):
        self.name = n
        self.health = h
        self.mana = m
    def status(self):
        print(f'Имя: {self.name}')
        print(f'Здоровье: {self.health}')
        print(f'Мана: {self.mana}')
    def drink_heal_potion(self, potion_amount):
        self.health += potion_amount
    def drink_mana_potion(self, potion_amount):
        self.mana += potion_amount
    def __repr__(self):
        return self.name[0]
    def walking(self):
        return f'{self.name} go '

class MainCh(Base):
    def __init__(self, n, h, m, str, agi, inte, exp, lvl):
        super().__init__(n, h, m)
        self.strength = str
        self.agility = agi
        self.intellect = inte
        self.experience = exp
        self.level = lvl
    def scream(self):
        print(f'Я {self.name}, выбери мне специальность')
    def attack(self, target):
        if isinstance(target, Skeleton):
            while target.health > 0:
                cmd2 = input('1 --> атаковать, 2 --> убежать: ')
                if cmd2 == '1':
                    print(f'{self.name} нанес {target.name} {self.strength} единиц урона')
                    target.health -= self.strength
                elif cmd2 == '2':
                    print(f'{self.name} убежал')
                else:
                    pass
                target.review()
        if isinstance(target, Bes):
            while target.health > 0:
                cmd2 = input('1 --> атаковать, 2 --> убежать: ')
                if cmd2 == '1':
                    print(f'{self.name} нанес {target.name} {self.strength} единиц урона')
                    target.health -= self.strength
                elif cmd2 == '2':
                    print(f'{self.name} убежал')
                else:
                    pass
                target.review()
        if isinstance(target, Boss):
            while target.health > 0:
                cmd2 = input('1 --> атаковать, 2 --> убежать: ')
                if cmd2 == '1':
                    print(f'{self.name} нанес {target.name} {self.strength} единиц урона')
                    target.health -= self.strength
                elif cmd2 == '2':
                    print(f'{self.name} убежал')
                else:
                    pass
                target.review()

    def status(self):
        print(f'Имя: {self.name}')
        print(f'Здоровье: {self.health}')
        print(f'Мана: {self.mana}')
        print(f'Опыт: {self.experience}')
        print(f'Уровень: {self.level}')




class Warrior(MainCh):
    def __init__(self, n, h = 100, m = 10, str = 50, agi = 50, inte = 90, exp = 0, lvl = 1, wea = 'меч'):
        super().__init__(n, h, m, str, agi, inte, exp, lvl)
        self.weapon = wea
    def scream(self):
        print(f'Я {self.name}, я воин с {self.weapon}')
    def attack(self, target):
        if isinstance(target, Skeleton):
            while target.health > 0:
                cmd2 = input('1 --> атаковать, 2 --> убежать: ')
                if cmd2 == '1':
                    print(f'{self.name} нанес {target.name} {self.strength} единиц урона')
                    target.health -= self.strength
                elif cmd2 == '2':
                    print(f'{self.name} убежал')
                else:
                    pass
                target.review()
        if isinstance(target, Bes):
            while target.health > 0:
                cmd2 = input('1 --> атаковать, 2 --> убежать: ')
                if cmd2 == '1':
                    print(f'{self.name} нанес {target.name} {self.strength} единиц урона')
                    target.health -= self.strength
                elif cmd2 == '2':
                    print(f'{self.name} убежал')
                else:
                    pass
                target.review()
        if isinstance(target, Boss):
            while target.health > 0:
                cmd2 = input('1 --> атаковать, 2 --> убежать: ')
                if cmd2 == '1':
                    print(f'{self.name} нанес {target.name} {self.strength} единиц урона')
                    target.health -= self.strength
                elif cmd2 == '2':
                    print(f'{self.name} убежал')
                else:
                    pass
                target.review()
        self.experience += 10
        if self.experience == 100:
            print(f'Вы достигли нового уровня! Улучшены все показатели героя! Опыт сброшен.')
            self.level += 1
            self.strength += 3
            self.agility += 2
            self.intellect += 1
            self.experience = 0
class Maga(MainCh):
    def __init__(self, n, h = 100, m = 60, str = 20, agi = 4, inte = 20, exp = 0, lvl = 1, *spl):
        super().__init__(n, h, m, str, agi, inte, exp, lvl)
        self.spells = list(spl)
    def scream(self):
        print(f'Я {self.name}, я маг, и я знаю {len(self.spells)} заклинания')
    def add_spell(self, spell):
        self.spells.append(spell)
    def status(self):
        print(f'Имя: {self.name}')
        print(f'Здоровье: {self.health}')
        print(f'Мана: {self.mana}')
        print(f'Опыт: {self.experience}')
        print(f'Уровень: {self.level}')
        print(f'Список заклинаний: {self.spells}')
    def magic_attack(self, target):
        if isinstance(target, Skeleton):
            print('Какое заклинание использовать?')
            a1 = input('1 - fireball, 2 - ray of light, 3 - curse')
            if a1 == '1':
                while target.health > 0:
                    cmd2 = input('1 --> абракадабра: ')
                    a = self.intellect * 1.25
                    if cmd2 == '1':
                        print(f'{self.name} нанес {target.name} {a} единиц урона с помощью заклинания fireball')
                        target.health -= a
                    else:
                        pass
                    target.review()
            elif a1 == '2':
                while target.health > 0:
                    cmd2 = input('1 --> абракадабра: ')
                    a = self.intellect * 0.75
                    if cmd2 == '1':
                        print(f'{self.name} нанес {target.name} {a} единиц урона с помощью заклинания ray of lights')
                        target.health -= a
                    else:
                        pass
                    target.review()
            elif a1 == '3':
                while target.health > 0:
                    cmd2 = input('1 --> абракадабра: ')
                    a = self.intellect * 0.25
                    if cmd2 == '1':
                        print(f'{self.name} нанес {target.name} {a} единиц урона с помощью заклинания curse')
                        target.health -= a
                    else:
                        pass
                    target.review()

            else:
                pass
        elif isinstance(target, Bes):
            print('Какое заклинание использовать?')
            a1 = input('1 - fireball, 2 - ray of light, 3 - curse')
            if a1 == '1':
                while target.health > 0:
                    cmd2 = input('1 --> абракадабра: ')
                    a = self.intellect * 1.25
                    if cmd2 == '1':
                        print(f'{self.name} нанес {target.name} {a} единиц урона с помощью заклинания fireball')
                        target.health -= a
                    else:
                        pass
                    target.review()
            elif a1 == '2':
                while target.health > 0:
                    cmd2 = input('1 --> абракадабра: ')
                    a = self.intellect * 0.75
                    if cmd2 == '1':
                        print(
                            f'{self.name} нанес {target.name} {a} единиц урона с помощью заклинания ray of lights')
                        target.health -= a
                    else:
                        pass
                    target.review()
            elif a1 == '3':
                while target.health > 0:
                    cmd2 = input('1 --> абракадабра: ')
                    a = self.intellect * 0.25
                    if cmd2 == '1':
                        print(f'{self.name} нанес {target.name} {a} единиц урона с помощью заклинания curse')
                        target.health -= a
                    else:
                        pass
                    target.review()
            else:
                pass
        elif isinstance(target, Boss):
            print('Какое заклинание использовать?')
            a1 = input('1 - fireball, 2 - ray of light, 3 - curse')
            if a1 == '1':
                while target.health > 0:
                    cmd2 = input('1 --> абракадабра: ')
                    a = self.intellect * 1.25
                    if cmd2 == '1':
                        print(f'{self.name} нанес {target.name} {a} единиц урона с помощью заклинания fireball')
                        target.health -= a
                    else:
                        pass
                    target.review()
            elif a1 == '2':
                while target.health > 0:
                    cmd2 = input('1 --> абракадабра: ')
                    a = self.intellect * 0.75
                    if cmd2 == '1':
                        print(
                            f'{self.name} нанес {target.name} {a} единиц урона с помощью заклинания ray of lights')
                        target.health -= a
                    else:
                        pass
                    target.review()
            elif a1 == '3':
                while target.health > 0:
                    cmd2 = input('1 --> абракадабра: ')
                    a = self.intellect * 0.25
                    if cmd2 == '1':
                        print(f'{self.name} нанес {target.name} {a} единиц урона с помощью заклинания curse')
                        target.health -= a
                    else:
                        pass
                    target.review()
            else:
                pass
        else:
            pass
#Мы не успели придумать для нпс что то прикольное, поэтому нпс травника просто стоит на краю карты как декорация
class NPC(Base):
    def __init__(self, n, h, m, lvl, *itm):
        super().__init__(n, h, m)
        self.level = lvl
        self.items = list(itm)
    def scream(self):
        print(f'Я {self.name}, я обычный NPC')
    def status(self):
        print(f'Имя: {self.name}')
        print(f'Здоровье: {self.health}')
        print(f'Мана: {self.mana}')
        print(f'{self.items}')
    def __repr__(self):
        return self.name[0]

class Travnik(NPC):
    def __init__(self, n, h = 100, m = 0, lvl = 1, *itm, pro = 'Травник'):
        super().__init__(n, h, m, lvl, *itm)
        self.profession = pro
    def scream(self):
        print(f'Меня зовут {self.name} и я {self.profession}')
    def make_potion(self, potion_name, heal_power):
        print(f'{self.name} создал {potion_name} с силой {heal_power}')
        self.items.append(potion_name)
    def job(self, target, potion_name):
        self.items.remove(potion_name)
        print(f'{self.name} передал {potion_name} {target}')

class Smith(NPC):
    def __init__(self, n, h, m, lvl, *itm, pro = 'Кузнец'):
        super().__init__(n, h, m, lvl, *itm)
        self.profession = pro
    def scream(self):
        print(f'Меня зовут {self.name} и я {self.profession}')
    def forge_item(self, item_name, item_power):
        print(f'{self.name} создал {item_name} с силой {item_power}')
        self.items.append(item_name)
    def give_item(self, target, item_name):
        print(f'{self.name} передает {item_name} {target}')
        self.items.remove(item_name)

class Dealer(NPC):
    def __init__(self, n, h, m, lvl, *itm, pro = 'Торговец'):
        super().__init__(n, h, m, lvl, *itm)
        self.profession = pro
    def scream(self):
        print(f'Меня зовут {self.name} и я {self.profession}')
    def add_item(self, item):
        self.items.append(item)
    def sell_item(self, item_name, target, price):
        print(f'{self.name} продал {item_name} {target} за {price}')
        self.items.remove(item_name)

class StrangeWizard(NPC):
    def __init__(self, n, h, m, lvl, *itm, pro = 'Странствующий волшебник'):
        super().__init__(n, h, m, lvl, *itm)
        self.profession = pro
    def scream(self):
        print(f'Меня зовут {self.name} и я {self.profession}')
    def spell(self, target, spell_name):
        print(f'{self.name} научил {target} заклинанию {spell_name}')

class Enemy(Base):
    def __init__(self, n, h, m, lvl, *itm):
        super().__init__(n, h, m)
        self.level = lvl
        self.items = list(itm)
    def review(self):
        print(f'name: {self.name}            health: {self.health}')
    def status(self):
        print(f'Имя: {self.name}')
        print(f'Здоровье: {self.health}')
        print(f'Мана: {self.mana}')
        print(f'{self.items}')

class Bes(Enemy):
    def __init__(self, n = 'Бес', h = 100, m = 20, lvl = 5, *itm):
        super().__init__(n, h, m, lvl, *itm)
    def steal_mana(self, target, mana):
        print(f'{self.name} крадет {mana} единиц маны у {target}')
        self.mana += mana

class Skeleton(Enemy):
    def __init__(self, n = 'Скелет', h = 100, m = 30, lvl = 4, *itm):
        super().__init__(n, h, m, lvl, *itm)
    def steal_items(self, target, item):
        print(f'{self.name} выбивает {item} у {target.name}')
        self.items.append(item)

class Boss(Bes):
    def __init__(self, n = 'какой то жесткий тип', h = 300, m = 20, lvl = 13, *itm):
        super().__init__(n, h, m, lvl, *itm)
    def mownaya_ataka(self, target, damage):
        print(f'{self.name} атакует {target} нанося ему {damage} урона')
        if self.health > 120:
            self.health += 5
        else:
            pass

class Simulator:
    def __init__(self):
        from random import choice
        print('Добро пожаловать! Как вас звать?')
        cmd = input()
        print(f'Приятно познакомиться, {cmd}!')
        print('Выберите свою специальность')
        self.cmd1 = input('1 - Воин, 2 - Маг: ')
        if self.cmd1 == '1':
            self.mc = Warrior(f'{cmd}')
        elif self.cmd1 == '2':
            self.mc = Maga(f'{cmd}')
            self.mc.add_spell('fireball')
            self.mc.add_spell('ray of light')
            self.mc.add_spell('curse')
        self.mc.status()
        self.npc = Travnik('Мага')
        self.boss = Boss('Balls')

        a = [choice(['_','_','_','_','_','_','_','_','_','_','_','_', Bes(), Skeleton()]) for j in range(25)]
        b = [choice(['_','_','_','_','_','_','_','_','_','_','_','_', Bes(), Skeleton()]) for j in range(25)]
        c = [choice(['_','_','_','_','_','_','_','_','_','_','_','_', Bes(), Skeleton()]) for j in range(25)]
        d = [choice(['_','_','_','_','_','_','_','_','_','_','_','_', Bes(), Skeleton()]) for j in range(25)]
        e = [choice(['_','_','_','_','_','_','_','_','_','_','_','_', Bes(), Skeleton()]) for j in range(25)]

        self.map = [a, b, c, d, e]

        self.mesto0 = 4
        self.mesto1 = 2

        self.mesto2 = 0
        self.mesto3 = 0

        self.mesto4 = 2
        self.mesto5 = 24
        self.map[self.mesto4][self.mesto5] = self.boss
        self.map[self.mesto2][self.mesto3] = self.npc
        self.map[self.mesto0][self.mesto1] = self.mc


        self.start()

    def walk(self):
        cmd = input('1 - left, 2 - right, 3 - up, 4 - down:')

        if self.cmd1 == '1':
            if cmd == '1':
                print(f'{self.mc.walking()}left')
                self.map[self.mesto0][self.mesto1] = '_'
                self.map[self.mesto2][self.mesto3] = self.npc

                self.mesto0 -= 0
                self.mesto1 -= 1
                self.mc.attack(self.map[self.mesto0][self.mesto1])
                self.map[self.mesto0][self.mesto1] = self.mc

            elif cmd == '2':
                print(f'{self.mc.walking()}right')
                self.map[self.mesto0][self.mesto1] = '_'
                self.map[self.mesto2][self.mesto3] = self.npc

                self.mesto0 -= 0
                self.mesto1 += 1
                self.mc.attack(self.map[self.mesto0][self.mesto1])

                self.map[self.mesto0][self.mesto1] = self.mc
                self.map[self.mesto0][self.mesto1] = self.mc


            elif cmd == '3':
                print(f'{self.mc.walking()}up')
                self.map[self.mesto0][self.mesto1] = '_'
                self.map[self.mesto2][self.mesto3] = self.npc

                self.mesto0 -= 1
                self.mesto1 += 0
                self.mc.attack(self.map[self.mesto0][self.mesto1])
                self.map[self.mesto0][self.mesto1] = self.mc
                self.map[self.mesto0][self.mesto1] = self.mc


            elif cmd == '4':
                print(f'{self.mc.walking()}up')
                self.map[self.mesto0][self.mesto1] = '_'
                self.map[self.mesto2][self.mesto3] = self.npc

                self.mesto0 += 1
                self.mesto1 += 0
                self.mc.attack(self.map[self.mesto0][self.mesto1])
                self.map[self.mesto0][self.mesto1] = self.mc
            else:
                pass

        elif self.cmd1 == '2':
            if cmd == '1':
                print(f'{self.mc.walking()}left')
                self.map[self.mesto2][self.mesto3] = self.npc

                self.map[self.mesto0][self.mesto1] = '_'
                self.mesto0 -= 0
                self.mesto1 -= 1
                self.mc.magic_attack(self.map[self.mesto0][self.mesto1])
                self.mc.attack(self.map[self.mesto0][self.mesto1])
                self.map[self.mesto0][self.mesto1] = self.mc

            elif cmd == '2':
                print(f'{self.mc.walking()}right')
                self.map[self.mesto2][self.mesto3] = self.npc
                self.map[self.mesto0][self.mesto1] = '_'
                self.mesto0 -= 0
                self.mesto1 += 1
                self.mc.magic_attack(self.map[self.mesto0][self.mesto1])
                self.mc.attack(self.map[self.mesto0][self.mesto1])
                self.map[self.mesto0][self.mesto1] = self.mc

            elif cmd == '3':
                print(f'{self.mc.walking()}up')
                self.map[self.mesto2][self.mesto3] = self.npc
                self.map[self.mesto0][self.mesto1] = '_'
                self.mesto0 -= 1
                self.mesto1 -= 0
                self.mc.magic_attack(self.map[self.mesto0][self.mesto1])
                self.mc.attack(self.map[self.mesto0][self.mesto1])
                self.map[self.mesto0][self.mesto1] = self.mc

            elif cmd == '4':
                print(f'{self.mc.walking()}up')
                self.map[self.mesto2][self.mesto3] = self.npc
                self.map[self.mesto0][self.mesto1] = '_'
                self.mesto0 += 1
                self.mesto1 -= 0
                self.mc.magic_attack(self.map[self.mesto0][self.mesto1])
                self.mc.attack(self.map[self.mesto0][self.mesto1])
                self.map[self.mesto0][self.mesto1] = self.mc
            else:
                pass
        return self.cmd1

    def start(self):
        cmd = input('1 - walk, ..:')
        while True:
            self.interface()
            if cmd == '1':
                self.walk()
            else:
                pass

    def interface(self):
        for k in range(len(self.map)):
            print(*self.map[k])
        print(f'Name: {self.mc.name} health: {self.mc.health}')

Simulator()