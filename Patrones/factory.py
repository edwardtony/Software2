import sys

class RecetarioMarina:
    def obtener_recetas(self):
        print('Ceviche')
        print('Pescado Frito')

class RecetarioCriolla:
    def obtener_recetas(self):
        print('Lomo Saltado')
        print('Carapulcra')

# Clase Factory
class RecetarioFactory:
    def obtener_recetarios(self, tipo_comida):
        if tipo_comida == 'marina':
            return RecetarioMarina()
        elif tipo_comida == 'criolla':
            return RecetarioCriolla()
        else:
            return None

def main():
    factory = RecetarioFactory() # instanciamos el Factory
    recetario = factory.obtener_recetarios(sys.argv[1])
    recetario.obtener_recetas()
    

if __name__ == '__main__':
    main()









