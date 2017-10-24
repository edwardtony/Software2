# Clase base de Observadores
class Alumno:
    def on_fijas_dadas(self):
        pass

class Ricardo(Alumno):
    def on_fijas_dadas(self):
        print("Apunta en su cuaderno")

class Diego(Alumno):
    def on_fijas_dadas(self):
        print("Apunta en notepad")

class Anthony(Alumno):
    def on_fijas_dadas(self):
        print("Se lo memoriza")

# Observado y el evento a notificar es
# dar las fijas del EP
class Profesor:
    def __init__(self):
        self.observadores = []
    def add_observador(self, observador):
        self.observadores.append(observador)
    def dar_fijas(self):
        for obs in self.observadores:
            obs.on_fijas_dadas()

def main():
    anthony = Anthony()
    ricardo = Ricardo()
    diego = Diego()

    profesor = Profesor()

    # Configuramos los observadores
    profesor.add_observador(anthony)
    profesor.add_observador(ricardo)
    profesor.add_observador(diego)

    profesor.dar_fijas()
    

if __name__ == '__main__':
    main()



