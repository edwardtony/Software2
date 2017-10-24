import copy

class Alumno:
    def __clone__(self):
        return copy.deepcopy(self)

def main():
    alu1 = Alumno()
    alu1.codigo = '20143434'

    alu2 = alu1.__clone__()
    alu2.codigo = '20160000'
    print(alu1.codigo)
    print(alu2.codigo)

if __name__ == '__main__':
    main()
