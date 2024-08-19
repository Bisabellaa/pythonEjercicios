#Ejercicio1 1.Mostrar a cuántos segundos equivalen una cantidad de horas, días, minutos y
#segundos ingresados por consola.

#dias = int(input("Ingrese dìas: "))
#horas = int(input("Ingrese horas: "))
#minu = int(input("Ingrese minutos: "))
#seg = int(input("Ingrese segundos: "))

#calculo = int(dias*86.400 + horas*3600 + minu*60 + seg)

#print(dias, "dias, ",horas, "horas, ", minu, "minutos, ", seg, "segundos son ", calculo, "Segundos en total ")

#-------------------------------------------------------------------------------------------------------------------
#Ejercicio2 2.Realizar el procedimiento inverso al 2: Mostrar cuántos días, horas,
# minutos y segundos representa una cantidad de segundos ingresados por consola.

#segundos = int(input(" Ingrese Segundos: "))

#calc = int()

#print( segundos, "son :", "dias ,horas ,minutos ,segundos ")

#--------------------------------------------------------------------------------------------------------------------
#Ejercicio3 3. Informar superficie y perímetro de un rectángulo. Se ingresan las medidas
#de ambos lados.

#ladoMayor = int(input("Ingresa la superficie del rectangulo: "))
#ladoMenor = int(input("Ingresa el perimetro del rectangulo: "))

#superficie = ladoMayor * ladoMenor
#perimetro = ladoMayor*2 + ladoMenor*2
#print("La superficie es:",superficie, "El perimetro es: ", perimetro)

#Ejercicio4 4. Convertir una distancia en Km a metros, pulgadas, yardas y millas.

#kilometros = int(input("Ingrese una distancia en km: "))

#metros = kilometros*1000
#pulgadas = kilometros*39370.1
#yardas = kilometros*1093.61
#millas = kilometros*0.621371

#print("kilometros a metros: ",metros, "kilometros a pulgadas: ", pulgadas, "kilometros a yardas: ", yardas, "kilometros a millas: ", millas)

#-------------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio5 5. Calcule la superficie y el volúmen de una esfera, ingresando su radio.

#radio = int(input("Ingrese el radio de una esfera: "))

#calSup = 4*3.14*radio*2
#calVolum = (3/4)*3.14*(radio^3)

#print("La superficie de la esfera es: ", calSup, "y su volumen es: ", calVolum)

#-------------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio6 6. Hacer un programa que permita mostrar un ticket de devolución de envases
#para un supermercado.Se ingresa la cantidad de envases y se genera el ticket que informa la
#cantidad de envases y monto total a devolver. Por cada botella de vidrio se devuelven $1.50 y por cada botella plástica $2.00

cantEnvasesV= int(input("Ingrese cantidad de envases de vidrio: "))
cantEnvasesP = int(input("Ingrese cantidad de envases de plastico: "))

totalCant = cantEnvasesP+cantEnvasesV

botellaVidrio = cantEnvasesV*1.50
botellaPlastica = cantEnvasesP*2.00

totalPrecio = botellaVidrio+botellaPlastica
print("")
print("Ingrese botellas")
print("Vidrio: ", cantEnvasesV)
print("Plastica: ", cantEnvasesP)
print("DEVOLUCIÒN DE BOTELLAS")
print("=======================")
print("Plasticas: ", cantEnvasesP, "   " , botellaPlastica)
print("Vidrio:    ", cantEnvasesV  , "   " , botellaVidrio)
print("------------------------")
print("TOTAL:     ",   totalCant, "   " ,  totalPrecio)

#Ejercicio7 7. Mostrar el % del total de ventas de cada trimestre de un año.


