""" Este es un programa que evalúa el promedio de las temperaturas
dadas en grados celcius y los convierte en grados farneheit."""

run = True

def ave(lst):
	num = 0
	for i in lst:
		num += i
	global numA 
	numA = round(num / len(lst), 2)
	return numA

def far():
	far_ = round((numA * (9/5)) + 32, 2)
	return far_ 

while run == True:
	InputV = int(input("¿Cuántos valores deseas regisitrar?: "))
	if InputV == 0:
		run = False
		break
	list = input("mínimos (min) o máximos (max): ")

	if list == "max":
		max_T = []
		for i in range(InputV):
			x = int(input())
			max_T.append(x)
		print("La temperatura promedio es de %.2f°C." % ave(max_T))
		print("Convertida a Farenheit: %.2f°F" % far())
	elif list == "min":
		min_T = []
		for i in range(InputV):
			x = int(input())
			min_T.append(x)
		print("La temperatura promedio es de %.2f°C." % ave(min_T))
		print("Convertida a Farenheit: %.2f°F" % far())
	else:
		continue

exit()