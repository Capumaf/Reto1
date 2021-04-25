nota1 = int (input ("Ingresar Nota1 "))
nota2 = int (input ("Ingresar Nota2 "))
nota3 = int (input ("Ingresar Nota3 "))
nota4 = int (input ("Ingresar Nota4 "))
nota5 = int (input ("Ingresar Nota5 "))

Listadenotas = [ nota1, nota2, nota3, nota4, nota5 ]
Promediodenotas = sum (Listadenotas) /5
Notamayor = max (Listadenotas)
notamenor = min (Listadenotas)

print (f'Listado de Notas {Listadenotas}')
print (f'Promedio de Notas {Promediodenotas}')
print (f'Nota Mayor {Notamayor}')
print (f'Nota Menor {notamenor}')

