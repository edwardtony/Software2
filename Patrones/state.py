
ESTADO_UNO = 1
ESTADO_DOS = 2
ESTADO_TRES = 3

class Clasesita:
    def __init__(self):
        self.estado = ESTADO_UNO
        
    def evento_a(self):
        if self.estado == ESTADO_UNO:
            self.estado = ESTADO_DOS
    
    def evento_b(self):
        if self.estado == ESTADO_UNO:
            self.estado = ESTADO_TRES

def main():
    pass

if __name__ == '__main__':
    main()
