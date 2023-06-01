# Задача 26:  Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3^5)
# A = 2; B = 3 -> 8

def pow_rec(a, b):
    return 1 if b == 0 else a * pow(a, b-1)


a, b = int(input("A=")), int(input("B="))
print(f"{a}^{b}={pow_rec(a, b)}")
