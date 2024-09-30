"""
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
 (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
 ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

"""

entrada = int(input("Digite o número desejado: ")) #Entrada do número desejadop pelo usuário
fibo = [0, 1] #lista que armazena a sequencia de fibonacci

while fibo.count(entrada) == 0: #loop que se executa com a condição se a entrada está na lista
    proximo = fibo[-1] + fibo[-2] #cacula o próximo item da sequencia, pegando o ultimo numero + o penultimo número
    fibo.append(proximo)  #adicionando o próximo numero a lista
    if proximo == entrada or proximo > entrada: #condição de parada que caso a variavel de entrada seja igual ao número gerado na interação ou o numero gerado é maior que a variavel de entrada 
        break #para o loop caso seja verdadeiro uma das condições 

print(fibo)

if fibo.count(entrada) == 0: #condição que se executa caso a contagem da entrada for 0
    print(f"O número {entrada} não está na sequencia.") 
else:
    print(f"O número {entrada} está na sequencia.") 
