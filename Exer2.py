"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
"""

palavra = input("Insira uma palavra ou frase qualquer:" ) #variavel de captura de palavra ou frase do usuario
if palavra.count("A") > 0 or palavra.count("a") > 0: #Condição que vê se há a letra a maiuscula ou minuscula na frase ou palavra
    print(f"A palavra : {palavra} tem a letra 'A' sendo maisucula - {palavra.count("A")} vezes")
    print(f"A palavra : {palavra} tem a letra 'a' sendo minuscula - {palavra.count("a")} vezes")
else:
    print(f"A palavra {palavra} não contem a letra 'a' minuscula ou maiuscula.")