'''Programa que calcula la cantidad de 
kg de azucar necesarios para preparar
postre para cierta cantidad de personas'''

# Definir la cantidad de personas que consumirán el postre
ppl = int(input("Cuántas personas van a consumir el postre:\n"))
# Se consumen 3 tazas para un postre para 10 personas
cups = (ppl / 10) * 3
# Cada kilogramo de azúcar equivale a 4.5 tazas
kg = round(cups / 4.5,0)

print("""
	Un postre para %r personas requiere un 
	total del %.2f tazas de azúcar. Esto equivale
	a %.2f kg de azúcar.
	""" % (ppl, cups, kg))