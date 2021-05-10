#Ejercicio 4
def diferencia21(n):
    if 21 > n:
        dif = 21 - n
    else:
        dif = (n - 21) * 2
    print ("The difference between both numbers is", abs(dif))
 
diferencia21(10)