class Empleado:
    def set_sucesor(self, sucesor):
        self.sucesor = sucesor

    def responder(self, reclamo):
        pass

class Profesor(Empleado):
    def responder(self, reclamo):
        if reclamo.puntos < 2:
            print("Resuelve Profesor")
            return True
        else:
            return self.sucesor.responder(
                reclamo)

class Coordinador(Empleado):
    def responder(self, reclamo):
        if reclamo.puntos < 5:
            print("Resuelve Coordinador")
            return True
        else:
            return self.sucesor.responder(
                reclamo)

class SecretarioAcademico(Empleado):
    def responder(self, reclamo):
        if reclamo.puntos < 7:
            print("Resuelve SecretarioAcademico")
            return True
        else:
            return self.sucesor.responder(
                reclamo)

class Director(Empleado):
    def responder(self, reclamo):
        print("Resuelve Director")
        return True

class Reclamo:
    def __init__(self, puntos):
        self.puntos = puntos

def main():
    # Definir jerarquia
    profesor = Profesor()
    coordinador = Coordinador()
    secretario = SecretarioAcademico()
    director = Director()

    profesor.set_sucesor(coordinador)
    coordinador.set_sucesor(secretario)
    secretario.set_sucesor(director)

    # Atencion
    reclamo = Reclamo(3)
    profesor.responder(reclamo)

if __name__ == '__main__':
    main()
