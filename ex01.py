""" Programa que calcula el valor que tiene que recueprar una acción
para que regresar a su valor original """

# Valor original de la acción
oVal = float(input("¿Cuál era el valor de la acción?:\n"))
# Valor del porcentaje de pérdida
pPor = float(input("¿Qué porcentaje perdió de valor?:\n"))
# Valor de la pérdida
pVal = oVal * (pPor/100)
# Valor después de restarle la pérdida
nVal = oVal - pVal
# Porcentaje necesario para recuperar el valor original.
nPor = (pVal * 100) / nVal
print('''
	La acción solía costar $ %.2f USD. Después de una 
	pérdida del %.2f%%, el valor de la acción quedó en: $ %.2f USD.
	Lo que significa que para que recupere su valor original
	requiere un incremento del %.2f%%.
	''' % (oVal, pPor, nVal, nPor))
