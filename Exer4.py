"""
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____
"""



#a
num = 1

while True : #condição
    num = num + 2
    if num >= 10:
        num = num - 2
        break
print(f"Exercicio A) próximo elemento {num}")

#b
num = 2

while True:
    num = num * 2
    if num >= 129:
        num = num / 2
        break
print(f"Exercicio B) próximo elemento {num}")

#c
num = 0
impares = []
for item in range(100):
    if item % 2 != 0:
        impares.append(item)
#print(impares)
for impar in impares:
    num = num + impar
    if num > 49:
        num = num - impar
        break
print(f"Exercicio C) próximo elemento {num}")

#d
num = 0
pares = []
for item in range(12):
    if item % 2 == 0:
        pares.append(item)

#print(pares)
for par in pares:
    if par <= 10:
        num = par ** 2
    else:
        break
print(f"Exercicio D) próximo elemento {num}")

#e
fibo = [1,1]
num = 0
for item in range(8):
    num = fibo[-1] + fibo[-2]
    fibo.append(num)
print(f"Exercicio E) próximo elemento {fibo[6]}")

#f
#O resultado é 20