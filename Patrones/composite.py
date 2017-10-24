class ComponenteCarta:
    def add_hijos(self,hijo):
        pass
    def calcular_ventas(self):
        pass

class Restomiel(ComponenteCarta):
    def __init__(self):
        self.hijos = []
    def add_hijos(self, hijo):
        self.hijos.append(hijo)
    def calcular_ventas(self):
        venta = 0
        for hijo in self.hijos:
            venta = venta+hijo.calcular_ventas()
        return venta

class ComidaMarina(ComponenteCarta):
    def __init__(self):
        self.hijos = []
    def add_hijos(self, hijo):
        self.hijos.append(hijo)
    def calcular_ventas(self):
        venta = 0
        for hijo in self.hijos:
            venta = venta + hijo.calcular_ventas()
        return venta

class ComidaCriolla(ComponenteCarta):
    def __init__(self):
        self.hijos = []
    def add_hijos(self, hijo):
        self.hijos.append(hijo)
    def calcular_ventas(self):
        venta = 0
        for hijo in self.hijos:
            venta = venta + hijo.calcular_ventas()
        return venta

class ComidaInternacional(ComponenteCarta):
    def __init__(self):
        self.hijos = []
    def add_hijos(self, hijo):
        self.hijos.append(hijo)
    def calcular_ventas(self):
        venta = 0
        for hijo in self.hijos:
            venta = venta + hijo.calcular_ventas()
        return venta

class Ceviche(ComponenteCarta):
    def calcular_ventas(self):
        return 30

class Mariscos(ComponenteCarta):
    def calcular_ventas(self):
        return 28

class Combinado(ComponenteCarta):
    def calcular_ventas(self):
        return 35

class CausaRellena(ComponenteCarta):
    def calcular_ventas(self):
        return 23

class BistecPobre(ComponenteCarta):
    def calcular_ventas(self):
        return 22

class TacuTacu(ComponenteCarta):
    def calcular_ventas(self):
        return 25

class Makis(ComponenteCarta):
    def calcular_ventas(self):
        return 28

class Fetuccini(ComponenteCarta):
    def calcular_ventas(self):
        return 26

class ArrozPollo(ComponenteCarta):
    def calcular_ventas(self):
        return 15

def main():
    # Definir la configuracion de nuestra
    # estructura
    restomiel = Restomiel()
    comida_marina = ComidaMarina()
    comida_criolla = ComidaCriolla()
    comida_internacional = ComidaInternacional()
    ceviche = Ceviche()
    mariscos = Mariscos()
    combinado = Combinado()
    causa = CausaRellena()
    bistec = BistecPobre()
    tacutacu = TacuTacu()
    makis = Makis()
    fetuccini = Fetuccini()
    arroz_pollo = ArrozPollo()

    restomiel.add_hijos(comida_marina)
    restomiel.add_hijos(comida_criolla)
    restomiel.add_hijos(comida_internacional)
    comida_marina.add_hijos(ceviche)
    comida_marina.add_hijos(mariscos)
    comida_marina.add_hijos(combinado)
    comida_criolla.add_hijos(causa)
    comida_criolla.add_hijos(bistec)
    comida_criolla.add_hijos(tacutacu)
    comida_internacional.add_hijos(makis)
    comida_internacional.add_hijos(fetuccini)
    comida_criolla.add_hijos(arroz_pollo)

    # Ejecutamos la operacion
    ventas_totales = restomiel.calcular_ventas()
    print(ventas_totales)

if __name__ == '__main__':
    main()
