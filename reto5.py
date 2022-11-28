##ejercicio 5 Una compañía de software contable, paga a su personal de ventas un salario de 3500000 mensuales, mas una comisión de 1500000 por cada licencia de software vendida menos el (5% del salario total + comisiones de deducciones) por impuestos. Codifica un programa que calcule e imprima el salario mensual de un vendedor dado recibiendo el numero de ventas realizadas


salario= int (3500000)
comision= int (1500000)
numventas= int (input ("ingrese la cantidad de ventas: "))
calsaltotal= int (salario + (comision * numventas)) 
total= (calsaltotal - ((calsaltotal * float(5))/100))


print  ("el salario total es",total,"pesos")