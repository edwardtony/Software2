class Alumno:
    instancia = None

    @classmethod
    def get_instance(cls):
        if cls.instancia == None:
            cls.instancia = Alumno()
        return cls.instancia


def main():
    alu1 = Alumno.get_instance()
    alu2 = Alumno.get_instance()
    alu1.codigo = '20154545'

    #.........

    Alumno.get_instance().codigo

    print(alu2.codigo)

if __name__ == '__main__':
    main()
