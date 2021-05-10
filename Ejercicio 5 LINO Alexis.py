#Ejercicio 5
def problema_loro(hablando, hora):
    if hablando == True and hora <= 7 or hora >= 20:
            print("True")
    else:
        print("False")

problema_loro(True, 7)