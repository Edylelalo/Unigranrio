Nome_aluno = (input('Digite o nome do Aluno: '))
Nota_1 = int(input('Digite a Primeira Nota: '))
Nota_2 = int(input('Digite a Segunda Nota: '))
Media = (Nota_1 + Nota_2) / 2

print ('A média é ',Media)

if Media < 7:
 print ('Reprovado')
elif Media >= 7:
 print ('Aprovado')
