# Exercici 1  Escriu un programa que demani l'edat per teclat i ens mostri un missatge que digui "Ets major d'edat" si el valor és igual o major a 18, o bé, "Ets menor d'edat" sí el valor és inferior a 18.
edat = int(input("Introdueix la teva edat: "))

if edat >= 18:
    print("Ets major d'edat")
else:
    print("Ets menor d'edat")
# Exercici 2 Escriu un programa que llegeixi tres nombres diferents i ens digui quin és el major
a = float(input("Introdueix el primer nombre: "))
b = float(input("Introdueix el segon nombre: "))
c = float(input("Introdueix el tercer nombre: "))

if a > b and a > c:
    major = a
elif b > a and b > c:
    major = b
else:
    major = c

print("El nombre major és:", major)

# Exercici 3 Escriu un programa que llegeixi un nombre i digui si és positiu o negatiu (el zero és positiu).
nombre = float(input("Introdueix un nombre: "))

if nombre >= 0:
    print("El nombre és positiu")
else:
    print("El nombre és negatiu")
