Nome_Time = (input('Digite o nome do Time: '))
Derrotas = int(input('Digite a quantidade de Derrotas: '))
Vitorias = int(input('Digite a quantidade de Vitórias: '))
Empates = int(input('Digite a quantidade de Empates: '))
Total_Partidas = Derrotas + Vitorias + Empates
Pontos_Ganhos = Vitorias * 3 + Empates
Pontos_Possiveis = Total_Partidas * 3
Pontos_Perdidos = Pontos_Possiveis - Pontos_Ganhos
Aproveitamento = (Pontos_Ganhos / Pontos_Possiveis) * 100

print ('O ', Nome_Time)
print ('Jogou ', Total_Partidas,' Partidas')
print ('Ganhou ', Pontos_Ganhos, ' Pontos')
print ('Perdeu ', Pontos_Perdidos, ' Pontos do Total de Pontos Possíveis')
print ('E teve  {0:.2f} % de Aproveitamento'.format(Aproveitamento))