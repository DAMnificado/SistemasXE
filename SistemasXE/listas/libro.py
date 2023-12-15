class Libro:
    def __init__(self, titulo, paginas, autor, fanaticos):
        self.titulo = titulo
        self.paginas = paginas
        self.autor = autor
        self.fanaticos = fanaticos

    def agregar_fanatico(self, nuevo_fanatico):
        self.fanaticos.append(nuevo_fanatico)

    def extraer_nombres_fanaticos(self):
        nombres_sin_numeros = []

        for fanatico in self.fanaticos:
            nombre_sin_numeros = ''

            for letra in fanatico:
                if not letra.isdigit():
                    nombre_sin_numeros += letra

            nombres_sin_numeros.append(nombre_sin_numeros)

        return nombres_sin_numeros


libro1 = Libro("La Sombra del Viento", 500, "Carlos Ruiz Zafón", ["pedro55", "manolo2", "javier1"])
print("Fanaticos antes de agregar nuevos:", libro1.fanaticos)


libro1.agregar_fanatico("luisa3")
libro1.agregar_fanatico("ana25")


print("Fanaticos después de agregar nuevos:", libro1.fanaticos)


nombres_sin_numeros = libro1.extraer_nombres_fanaticos()
print("Nombres de fanaticos sin números:", nombres_sin_numeros)
