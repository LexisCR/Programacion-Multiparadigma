from datetime import date
Fecha = date.today()

print("Menu \n1.- Imprimir YYYY/MM/DD\n2.- Imprimir MM/DD/YYYY")
numero = int(input("Escoge una opcion: "))

if numero == 1:
    print(f"{Fecha.year}/{Fecha.month}/{Fecha.day}")

else:
    print(f"{Fecha.month}/{Fecha.day}/{Fecha.year}")