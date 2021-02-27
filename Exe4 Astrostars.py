n = int(input("enter ur no: "))
b = int(input("enter true or false: "))
new=bool(b)


def function1(n):
    i = 1
    while (i <= n):
        print(i * "*")
        i = i + 1


def function2(n):
    i = n
    while (i <= n and i >= 0):
        print(i * "*")
        i = i - 1


if new == True:
    function1(n)
else:
    new == False
    function2(n)

