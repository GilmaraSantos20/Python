
'''Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para 
organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, 
quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este 
laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas 
informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia 
utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um 
valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um 
inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo 
de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de 
cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o 
percentual deve ser apresentado com dois dígitos após o ponto. '''

coelhos = 0
ratos = 0
sapos = 0
casos = int(input("Quantos casos de teste serao digitados? "))

for c in range(1, casos + 1):
    cobaia = str(input("Tipo de cobaia: "))
    quant = int(input("Quantidade de cobaias: "))

    if cobaia == "C":
        coelhos += quant
    
    if cobaia == "R":
        ratos += quant

    if cobaia == "S":
        sapos += quant
    
print("C = ", coelhos)
print("R = ", ratos)
print("S = ", sapos)