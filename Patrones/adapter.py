import sys

class FormatoFactory:
    def obtener_adapter(self, tipo):
        if tipo == 'xml':
            return XMLAdapter()
        elif tipo == 'json':
            return JSONAdapter()

class XML:
    def pintar_xml(self, persona):
        xml = '<persona nombre="%s" edad="%s" />'
        xml = xml % (persona.nombre, persona.edad)
        print(xml)

class JSON:
    def pintar_json(self, persona):
        json = '{ "nombre":"%s", "edad":%s }'
        json = json % (persona.nombre, persona.edad)
        print(json)

class FormatoAdapter:
    def pintar(self, persona):
        pass

class XMLAdapter(FormatoAdapter):
    def pintar(self, persona):
        XML().pintar_xml(persona)

class JSONAdapter(FormatoAdapter):
    def pintar(self, persona):
        JSON().pintar_json(persona)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def main():
    nombre = sys.argv[1]
    edad = sys.argv[2]
    tipo = sys.argv[3]
    
    persona = Persona(nombre, edad)
    factory = FormatoFactory()
    adapter = factory.obtener_adapter(tipo)
    adapter.pintar(persona)
    


if __name__ == '__main__':
    main()
