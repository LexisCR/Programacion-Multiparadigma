def producto_total(*numeros):
    producto = 1
    for num in numeros:
        producto *= num
    return producto

resultado = producto_total(2, 3, 4, 5)
print("El producto total es:", resultado)
