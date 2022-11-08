# import operator
# import datetime
# from random import choice
# class MyError(Exception):
#     def __init__(self, text):
#         self.text = text
#
#
# class Shef_povar():
#      """opisanie doma"""
#      def __init__(self,name,kalorya,s1,s2,s3):
#          '''svoistva doma'''
#          self.name = name
#          self.kalorya = kalorya
#          self.s1 = s1
#          self.s2 = s2
#          self.s3 = s3
#
#      def show(self):
#         print(' Имя салата: {} '
#               ' kalorya: {}'
#             ' s1: {}'
#             ' s2: {}'
#             ' s3:{} '.format(self.name, self.kalorya, self.s1, self.s2, self.s3))
#
#      def sort_choice(Data, choice):
#          result = sorted(Data, key=operator.attrgetter(choice))  # Сортировка по атрибуту name
#          for i in result:
#              i.show()
#
# salad1=Shef_povar('svezjy',800,'potato','tomato','tuz')
# salad2=Shef_povar('ochuchuk',600,'tomato','burysh','tuz')
# salad3=Shef_povar('alivya',400,'potato','shuzhyk','egg')
# e = [salad1,salad2,salad3]
#
#
#
# def sort_choice(Data, choice):
#     result = sorted(Data, key=operator.attrgetter(choice))  # Сортировка по атрибуту name
#     for i in result:
#         i.show()
# sal1 = []
# sal2 = []
# sal3 = []
# enter = int(input('Enter random kol: '))
# ovosh_kalorya = [[200,'ogurec'],[150,'tomato'],[50,'tuz'],[250,'egg'],[40,'burysh'],[400,'shuzhyk']]
# for i in range(enter):
#     sal1.append(choice(ovosh_kalorya))
# for i in range(enter):
#     sal2.append(choice(ovosh_kalorya))
# for i in range(enter):
#     sal3.append(choice(ovosh_kalorya))
# print(*sal1)
# print(*sal2)
# print(*sal3)
# while True:
#     print('\n1.Списоk salad')
#     print('2.Спиcok kaloryi ')
#     print('3.ovosh ')
#     print('4.vhod')
#     n=int(input())
#
#     if n < 0:
#         raise MyError("Syz terys san engyndyn on engyz")
#     if n == 1:
#         result = sorted(e, key=operator.attrgetter('name'))  # Сортировка по атрибуту name
#         for i in result:
#             i.show()
#
#     elif n == 2:
#         aralyq1 = int(input('kalorya aralyk 1:'))
#         aralyq2 = int(input('kalorya aralyk 2:'))
#         for i in e:
#
#             if i.kalorya > aralyq1 and i.kalorya < aralyq2:
#                 i.show()
#
#
#     elif n == 3:
#         ovosh = input('name ovosha:')
#
#         for i in e:
#
#             if i.s3 == ovosh:
#                 i.show()
#
#             elif n == 4:
#                 break

# from random import choice
# import operator
# import random
# from secrets import choice
# # from random import randint as choice
#
# class Shop_flower():
#     def __init__(self, gul_tury, bagasy, kol):
#         self.gul_tury = gul_tury
#         self.bagasy = bagasy
#         self.kol = kol
#     def show(self):
#         print('Гул туры: {}'
#               ' Цена: {}'
#               ' Количество: {}'.format(self.gul_tury, self.bagasy, self.kol))
#
#
# def sort_choice(Data, choice):
#     result = sorted(Data, key=operator.attrgetter(choice))
#     for i in result:
#         i.show()
#
#
# class Gulder(Shop_flower):
#
#     def __init__(self, gul_tury, bagasy, kol):
#         super().__init__(gul_tury, bagasy, kol)
#
#
# flower1 = Gulder('Roza', 200, 50)
# flower2 = Gulder('Ramashka', 500, 30)
# flower3 = Gulder('Lalagul', 300, 20)
#
# e = [flower1, flower2, flower3]
#
# while True:
#
#     print('1. Гүлдер туралы барлық ақпарат:')
#     print('2. Букет куру рандом жане клиент калауы бойынша:')
#     print('3. Неше гул калды және редактирование:')
#     print('4. exit')
#
#     n = int(input())
#
#     str = [4, 5, 6, 7, 8,9,10,11,12]
#     sq = [500, 300, 200]
#
#     s1 = random.choice(str)
#     s2 = random.choice(str)
#     s3 = random.choice(str)
#     if n <= 0 or n >= 5:
#         print('Siz engizgen malimet zhok!')
#     if n == 1:
#         for i in range(len(e)):
#             e[i].show()
#         print()
#     if n == 2:
#         print('1.Klienet akshasy boyinsha!')
#         print('2.Dayin buketter!')
#         print('3.назад')
#         nn = int(input())
#         if nn == 1:
#             ran = int(input('How much money: '))
#             s1 = random.choice(str)
#             s2 = random.choice(str)
#             s3 = random.choice(str)
#             print(f'Роза гүлінен  {s1} түп алынды')
#             print(f'Ромашка гүлінен  {s2} түп алынды')
#             print(f'Лала гүлінен  {s3} түп алынды')
#             s_flower1 = s1*200
#             s_flower2 = s2*500
#             s_flower3 = s3*300
#
#             ss = [s_flower1, s_flower2, s_flower3]
#             sim = 0
#             while True:
#                 sim += choice(sq)
#                 if sim > ran:
#                     print(f'{sim - ran} tenge sdacha')
#                     break
#
#                 elif sim == ran:
#                     print('Siz bergen summamen buket kuryldy!, sdacha jok!')
#                     break
#                 else:
#                     continue
#                     break
#         elif nn == 2:
#             print(' 1.Наличка', '\n',
#                   '2.kaspi QR', '\n',
#                   '3.Перевод')
#             tolem = int(input('Tolem turyn tandaniz:'))
#             print('Tolem tury tandaldy!')
#             print()
#             print('1.buket: 5000','\n'
#                   '2.buket: 6000','\n'
#                   '3.buket: 4000')
#             nnn = int(input('Buket turyn tandanyz: '))
#             if nnn == 1 or nnn == 2 or nnn== 3:
#                 print('Tolem satty otty! Keremet tandau, kelip turynyz!')
#             elif nnn == 4:
#                 continue
#             else:
#                 print('Siz engizgen malimet zhok!')
#         elif nn == 3:
#             continue
#         else:
#             print('Siz engizgen malimet zhok!')
#
#     if n == 3:
#         sss = [e[0].kol-s1, e[1].kol-s2, e[2].kol-s3]
#         print(f'Қалған барлық гүлдер саны : {sum(sss)}')
#         print(f'Роза гүлінен  {e[0].kol-s1} түп қалды')
#         print(f'Ромашка гүлінен  {e[1].kol-s2} түп қалды')
#         print(f'Лала гүлінен  {e[2].kol-s3} түп қалды')
#     print()
#
#
#     if n == 4:
#         break

# f = open("C:\\Users\\Asus\\Desktop\\myfile.txt","+w")
# f.write("Kozymnin karasy")
# f.close()
import operator
import random
import turtle


def guu():
    # Set initial position
    turtle.penup()
    turtle.left(90)
    turtle.fd(200)
    turtle.pendown()
    turtle.right(90)

    # flower base
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10, 180)
    turtle.circle(25, 110)
    turtle.left(50)
    turtle.circle(60, 45)
    turtle.circle(20, 170)
    turtle.right(24)
    turtle.fd(30)
    turtle.left(10)
    turtle.circle(30, 110)
    turtle.fd(20)
    turtle.left(40)
    turtle.circle(90, 70)
    turtle.circle(30, 150)
    turtle.right(30)
    turtle.fd(15)
    turtle.circle(80, 90)
    turtle.left(15)
    turtle.fd(45)
    turtle.right(165)
    turtle.fd(20)
    turtle.left(155)
    turtle.circle(150, 80)
    turtle.left(50)
    turtle.circle(150, 90)
    turtle.end_fill()

    # Petal 1
    turtle.left(150)
    turtle.circle(-90, 70)
    turtle.left(20)
    turtle.circle(75, 105)
    turtle.setheading(60)
    turtle.circle(80, 98)
    turtle.circle(-90, 40)

    # Petal 2
    turtle.left(180)
    turtle.circle(90, 40)
    turtle.circle(-80, 98)
    turtle.setheading(-83)

    # Leaves 1
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(25)
    turtle.left(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(-80, 90)
    turtle.right(90)
    turtle.circle(-80, 90)
    turtle.end_fill()
    turtle.right(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(85)
    turtle.left(90)
    turtle.fd(80)

    # Leaves 2
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.circle(80, 90)
    turtle.end_fill()
    turtle.left(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(60)
    turtle.right(90)
    turtle.circle(200, 60)
    turtle.done()

class Gul():
    def __init__(self, name, shtuk, price):
        self.name = name
        self.shtuk = shtuk
        self.price = price

    def show(self):
        print('Названия цветок: {}'
              ' Штук: {} штук'
              ' Цена: {} тг'.format(self.name, self.shtuk, self.price))


def sort_choice(Data, choice):
    result = sorted(Data, key=operator.attrgetter(choice))
    for i in result:
        i.show()

class Magaz(Gul):
    def __init__(self, name, shtuk, price):
        super().__init__(name, shtuk, price)


gul1 = Magaz('Roza', 50, 5000)
gul2 = Magaz('BakBak', 150, 2000)
gul3 = Magaz('Lala',100, 3500)
e = [gul1, gul2, gul3]

t = []

def su(t):
    for i in range(len(e)):
        t.append(e[i].price)
su(t)

def ajj(t):
    d = int(input("Kansha akshaga alasiz - "))
    if 0 < d < 2000:
        print("Norm Buket Zhok")
        print("Try again?")
        return ajj(t)
    elif d < 0:
        print("Minus san")
        print("Try again?")
        return ajj(t)
    else:
        r = [0]
        i = 0
        g = 0
        while g <= d:
            if e[0].shtuk == 0 or e[1].shtuk == 0 or e[2].shtuk == 0:
                print("Gul sany zhetpid")
            else:
                r.append(random.choice(t))

            i = i + 1
            if g <= d:
                g = g + r[i]
            if g > d:
                r.pop(-1)
        y = 0
        for i in range(len(r)):
            y = y + r[i]
        print(y)
        t = []
        mas = []
        su(t)
        for i in range(len(t)):
            a = 0
            for j in range(len(r)):
                if r[j] == t[i]:
                    a = a + 1
            mas.append(a)

        # a1, a2, a3 = 0, 0, 0
        # for i in range(len(r)):
        #     if r[i] == 5000:
        #         a1 = a1 + 1
        #     if r[i] == 3500:
        #         a2 = a2 + 1
        #     if r[i] == 2000:
        #         a3 = a3 + 1
        # mas = [a1, a3, a2]

        for i in range(len(e)):
            print(e[i].name, mas[i], "Dana")

        print("Alatin boldinizba?")
        print("1. Ya")
        print("2. Zhok")
        a = int(input())
        if a == 1:
            for i in range(len(e)):
                e[i].shtuk = e[i].shtuk - mas[i]
            # guu()
            print("Kalgan akshanyz - ", d - y)
        if a == 2:
            return ajj(t)


def ahh():
    print("Alatin boldinizba?")
    print("1. Ya")
    print("2. Zhok")
    a = int(input())
    if a == 1:
        for i in range(len(e)):
            e[i].shtuk = e[i].shtuk - mas[i]
        # guu()
    if a == 2:
        return ajj(t)

mas = []
def du(mas):
    for i in range(len(e)):
        a = int(input(e[i].name + " Kansh shtuk - "))
        if a <= e[i].shtuk:
            mas.append(a)
        else:
            print("ondai olshemde gul zhok zhazdynyz")
            return du(mas)

    for i in range(len(e)):
        print(e[i].name, mas[i], "Dana")

    ahh()
while True:

    print('1. Barlyk Gulder')
    print('2. Satyp Alamyn ! ')
    print('3. Admin')
    print('4. exit')

    # for i in range(len(e)-1):
    #     if e[i].shtuk == 0:
    #         e.pop(i)

    n = int(input())
    if n == 1:
        sort_choice(e, 'shtuk')

    if n == 2:
        while True:
            print('Guldi kalai aluga bolady?')
            print('1. Kolda bar aksha boinsha!')
            print('2. Bagasy boinsha!')
            print("3. Exit!")
            o = int(input())
            if o == 1:
                ajj(t)
            if o == 2:
                sort_choice(e, "shtuk")
                mas = []
                du(mas)
                # q1 = int(input(e[0].name + " Kansh shtuk - "))
                # q2 = int(input(e[1].name + " Kansh shtuk - "))
                # q3 = int(input(e[2].name + " Kansh shtuk - "))
                # mas = [q1,q2,q3]


            if o == 3:
                break
    if n == 3:
        print("Zhana gul keldy!")
        a = int(input("Kelgen gul turlerinin sany? "))
        for i in range(a):
            a1 = input("Gul aty?")
            a2 = int(input("Gul sany?"))
            a3 = int(input("Gul bagasy?"))
            r = 0
            for i in e:
                if a1.strip() == i.name:
                    i.shtuk = i.shtuk + a2
                    print("1 - Buringi baga kalsinba?")
                    print("2 - Osi baga bagaga 25 %?")
                    if i.price != a3:
                        f = int(input())
                        if f == 1:
                            continue
                        if f == 2:
                            i.price = a3 + a3 * 0.25
                    else:
                        continue
                else:
                    r = r + 1
            if r == len(e):
                w = Magaz(a1, a2, a3)
                e.append(w)

        for i in e:
            i.show()
    if n == 4:
        break


