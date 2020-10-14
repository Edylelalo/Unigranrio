cadastro = 0
inferior = 0
entre = 0
superior = 0

x = range(1,11)
for cadastro in x:
 altura = float(input('digite a altura: '))
 if altura < 1.60:
  inferior += 1
 elif 1.80 >= altura >= 1.60:
  entre += 1
 elif altura > 1.80:
  superior += 1

print ('Foram cadastradas', cadastro,'pessoas')
print ('Foram cadastradas', inferior,'com menos de 1.60')
print ('Foram cadastradas', entre,'entre 1.60 e 1.80')
print ('E foram cadastradas', superior,'com mais de 1.80')