#Ejercicio 10
def lost_char(txt, n):
    if n == 0:
        new_txt =  txt[1:]
        print(new_txt)
    elif n == len(txt):
        new_txt = txt[0:n-1]
        print(new_txt)
    else:
        new_txt = txt[0:n] + txt[n+1:]
        print(new_txt)

txt = str(input("Write a text string: "))
n = int(input("Write the index of the character to change in the string: "))
lost_char(txt,n)