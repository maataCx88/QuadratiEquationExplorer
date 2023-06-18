from math import sqrt

def draw_pyramid(text):
    rows = 5
    width = (rows - 1) * 2 + 1
    print(text.center(width))
    for i in range(1, rows + 1):
        line = ' ' * (rows - i)
        line += '*' * (2 * i - 1)
        print(line.center(width))

draw_pyramid("Welcome To My Quadratic Explorer")
print('Please set a,b,c (ax^2+bx+c=0) : \n')
print('a: ')
a=int(input())
print('b: ')
b=int(input())
print('c: ')
c=int(input())
print("For the equation : {}x^2+{}x+{}=0 you want to : \n".format(a,b,c))
print('1 - Find how many solutions are there \n')
print('2 - Find all the possible solutions \n')
whattodo=input()
delta=(b**2)-(4*a*c)
if whattodo == '1':
    if delta > 0:
        print("There are two possible real solutions for {}x^2+{}x+{}=0".format(a,b,c))
    if delta == 0:
        print("There is one possible real solution for {}x^2+{}x+{}=0".format(a,b,c))
    if delta < 0:
        print("There is no possible real solution for {}x^2+{}x+{}=0".format(a,b,c))
else: 
    if delta > 0:
        x1=((-b)+sqrt(delta))/(2*a)
        x2=((-b)-sqrt(delta))/(2*a)
        print("{}x^2+{}x+{}=0 has two solutions which are x1={} and x2={}".format(a,b,c,x1,x2))
    if delta == 0:
         x=((-b)+sqrt(delta))/(2*a)
         print("{}x^2+{}x+{}=0 has one solution which is x={}".format(a,b,c,x))
    if delta < 0:
        print("There is no possible real solution for {}x^2+{}x+{}=0".format(a,b,c))