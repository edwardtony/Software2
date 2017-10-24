class EstadoAlumno:
    def __init__(self, alumno):
        self.alumno = alumno
        
    def matricular(self):
        pass
    def terminar_ciclo(self):
        pass
    def expulsar(self):
        pass
    def suspender(self):
        pass
    def egresar(self):
        pass
    def terminar_suspension(self):
        pass

class EstadoNoMatriculado(EstadoAlumno):
    def matricular(self):
        self.alumno.estado = EstadoMatriculado(self.alumno)

    def expulsar(self):
        self.alumno.estado = EstadoExpulsado(self.alumno)

class EstadoMatriculado(EstadoAlumno):
    def terminar_ciclo(self):
        self.alumno.estado = EstadoNoMatriculado(self.alumno)
    def egresar(self):
        self.alumno.estado = EstadoEgresado(self.alumno)
    def expulsar(self):
        self.alumno.estado = EstadoExpulsado(self.alumno)
    def suspender(self):
        self.alumno.estado = EstadoSuspendido(self.alumno)

class EstadoExpulsado(EstadoAlumno):
    pass

class EstadoSuspendido(EstadoAlumno):
    def terminar_suspension(self):
        self.alumno.estado = EstadoNoMatriculado(self.alumno)

class EstadoEgresado(EstadoAlumno):
    pass

class Alumno:
    def __init__(self):
        self.estado = EstadoNoMatriculado(self)

def main():
    alumno = Alumno() # alumno.estado? => NoMatriculado
    alumno.estado.matricular() # alumno.estado? => Matriculado
    alumno.estado.matricular() # alumno.estado? => Matriculado
    alumno.estado.terminar_ciclo() # alumno.estado? => NoMatriculado
    alumno.estado.egresar() # alumno.estado? => NoMatriculado
    alumno.estado.expulsar() # alumno.estado? => Expulsado

if __name__ == '__main__':
    main()







