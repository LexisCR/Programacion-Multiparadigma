def funcion(**kwargs):
    for key, value in kwargs.items():
        print("{" + key + "}" + ": " + "{" + value + "}")
d = dict(a = "Hola", b = "Mundo", c = "Buenos", d = "Dias")
funcion(**d)