#tabla
a = int(input("Ingrese numero de tablas: "))

b = int(input("Ingrese rango: "))

cont1 = 0

for i in range(2, a+1):# numero de tablas

    print("     Tabla --> ",i)

    cont=0 #reiniciar contador

    contResta = 0

    for j in range(b):# rango de las tablas

        j=j+1

        sum = j+i

        print(j,"+",i,"=",sum)#impresion tabla

        if j%2==1:#numeros impares

            cont+=sum #sumatoria de cada tabla

            cont1+=sum #sumatoria total
    
        contResta+=sum #sumatoria de ultima tabla

    print("Valor tabla -> ",i,": ",cont) 
    
print("Valor de la ultima tabla --> ", contResta)

print("Valor de las tablas: ->",cont1)

print("RESPUESTA FINAL ES: ", cont1 - contResta)


    
            
            





