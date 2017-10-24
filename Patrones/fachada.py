# Clase Fachada
class GestorReclamos:
    def __init__(self):
        # Definir jerarquia
        self.profesor = Profesor()
        self.coordinador = Coordinador()
        self.secretario = SecretarioAcademico()
        self.director = Director()

        self.profesor.set_sucesor(
            self.coordinador)
        self.coordinador.set_sucesor(
            self.secretario)
        self.secretario.set_sucesor(
            self.director)
        
    def realizar_reclamo(self,reclamo):
        self.profesor.responder(reclamo)

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
    reclamo = Reclamo(3)
    gestor = GestorReclamos()
    gestor.realizar_reclamo(reclamo)

if __name__ == '__main__':
    main()
    
