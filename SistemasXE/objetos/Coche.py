class Coche:
    ruedas = 4
    matricula = ""
    propietario = "Manuel"
    itv = True

    def __init__(self,matricula,propietario,itv):
        self.matricula=matricula
        self.propietario=propietario
        self.itv = itv

    def __str__(self):
        return f"Coche: Matricula {self.matricula}"


coche2 = Coche("123aSD","PEPE",False)
print(coche2.__str__())
