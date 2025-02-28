import os
NumMaterias = int(input("Cuantas materias desea ingresar?: "))
os.system("cls")

Materias = {}
i = 1
Suma = 0

while(i <= NumMaterias):
    while True:
        Nombre = input(f"Ingrese el nombre de la materia {i}: ")
        if (Nombre == "Administracion de redes" or Nombre == "Desarrollo android" or Nombre == "Desarrollo IOS" or Nombre == "Desarrollo aplicaciones descentralizadas"):
            os.system("cls")
            print("La materia debe ser inferior a octavo semestre!")
        else: break
    Creditos = input(f"{Nombre} cuantos creditos tiene?: ")
    Materias[Nombre] = Creditos
    Suma = Suma + int(Creditos)
    os.system("cls")
    i = i + 1

for key, value in Materias.items():
    print("{" + key + "}" + " tiene " + "{" + value + "}" + " creditos")

print(f"Creditos totales: {Suma}")