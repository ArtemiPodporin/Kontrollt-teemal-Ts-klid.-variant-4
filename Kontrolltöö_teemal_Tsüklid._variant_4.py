#1
n = int(input("Sisestage number (1-9): "))

for i in range(n):
    print("  ^---^")
    print(" ( o o )")
    print("  ! = !/)")
    print("     ")


#2
n = int(input("Sisestage number: "))
p = int(input("Sisestage võimsus: "))

for i in range(1, n+1):
    result = i**p
    if result <= n:
        print(i, "võimule", p, "=", result)


#3
import random

num_of_students = int(input("Sisestage õpilaste arv: "))

marks = []
for i in range(num_of_students):
    marks.append(random.randint(1, 10))

min_mark = min(marks)
max_mark = max(marks)

print("Miinimummärk on: ", min_mark)
print("Maksimaalne hind on: ", max_mark)


#4
keel=3
amoob=1

while keel<=24:
    amoob *= 2
    print("Pärast", keel, "tundi, tuleb", amoob, "amoob.")
    keel += 3


#5
K = int(input("Sisestage kotlettide arv: "))
M = int(input("Sisestage kotlettide arv panni kohta: "))

pan = K // M
remaining = K % M

print("Tais pannide arv: ", pan)
print("Jarelejäänud kotlettide arv: ", remaining)

