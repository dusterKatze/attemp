#1
a=input("задайте пароль ")
b=input("повторите ввод ")
if a==b:
    print("пароль принят")
else:
    print("пароль не принят")

#2
n=input("введите номер места ")
if int(n)>54:
    print("неверный ввод номера")
else:
    if int(n)%2==0:
        print("верхняя полка")
    else:
        print("нижняя полка")
    if int(n)>36:
        print("место сбоку")
    else:
        print("место в купе")

#3
y=int(input(""))
if y%400==0 or (y%4==0 and y%100!=0):
    print("год",y,"- високосный")
else:
    print("это не високосный год")

#4
r='красный'
b='синий'
g='желтый'
v=input('введите первый цвет (красный, синий, желтый)')
vv=input('введите второй цвет (красный, синий, желтый)')
if not(v==r or v==b or v==g) or not(vv==r or vv==b or vv==g):
    print("неверный ввод")
else:
    if v==r and v!=vv:
        if vv==b:
            print('фиолетовый')
        else: #единственный оставшийся вариант это желтый
            print('оранжевый')
    elif v==g and v!=vv:
        if vv==b:
            print('зеленый')
        else: #единственный оставшийся вариант это красный
            print('оранжевый')
    elif v==b and v!=vv:
        if vv==r:
            print('фиолетовый')
        else: #единственный оставшийся вариант это желтый
            print('зеленый')
    else:
        print("ввод одного цвета дважды")