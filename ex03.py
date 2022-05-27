''' Programa que calcula la cantidad de minutos que 
tarda en imprimir cierto número de páginas de acuerdo
con su velocidad de impresión'''

printR = {
	'impresora 1':15,
	'impresora 2':18,
	'impresora 3':20,
	'impresora 4':12,
	'impresora 5':15,
	'impresora 6':24,
	'impresora 7':30,
	'impresora 8':22,
	'impresora 9':20,
	'impresora 10':15}

book = int(input("Ingrese el número de libros que desea imprimir:\n"))
pages = int(input("¿Cuántas páginas tienen los libros?\n"))

pagesT = book * pages
best = (pagesT/printR['impresora 1'])/60
bPrinter = ""

for i in printR.keys():
	time = (pagesT/printR[i])/60
	if time < best:
		best = time
		bPrinter = i
	print("La impresora %s imprimirá los libros en %.2f horas" % (i, time))

print("""
La mejor opción de impresión es la %s 
con un tiempo de impresión de %.2f horas.""" % (bPrinter, best))

ttl = 0
for i in printR.values():
	ttl += i

ttlP = (pagesT / ttl) / 60

print("""
Si todas las impresiones trabajan en simultáneo 
el tiempo total de impresión de libros es de %.2f horas.""" % ttlP)


