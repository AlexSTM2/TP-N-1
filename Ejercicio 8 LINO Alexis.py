#Ejercicio 8
def neg_pos(numA, numB, negative):
    if negative == True:
        if numA < 0 and numB < 0:
            print("True")
        else:
            print("False")
    elif numA < 0 or numB < 0:
        if numA > 0 or numB > 0:
            print("True")
        else:
            print("False")
    else:
        print("False")

neg_pos(-1,-1,False)        