#Ejercicio 9
txt = str(input("Write a text string "))
txt_low= txt.lower()
def no_str(txt):
    if txt_low[0:2] == str("no"):
        print(txt)
    else:
        print(str("No ") + txt)
no_str(txt)