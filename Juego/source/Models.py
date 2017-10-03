import pygame

class Character:
    
    """ 
        Clase encargada de gestionar la pre-configuración del personaje, la cantidad de sprites y los sprites usados en las acciones.
    """

    # Constructor
    def __init__(self, w, h):
        self.w, self.h = w, h

    # Método que configura los sprites para la acción de Caminar
    def config_sprites_walk(self,path,cols):
        sheet = pygame.image.load(path)
        self.sprite_walk = self.generate_sprites(cols,sheet)
        self.current = self.sprite_walk[0] 

    # Método que configura los sprites para la acción de Saltar
    def config_sprites_jump(self,path,cols):
        sheet = pygame.image.load(path)
        self.sprite_jump = self.generate_sprites(cols,sheet)

    # Método con la lógica para dividir los sprites dado los datos pasados como parámetros (columnas y el sheet)
    def generate_sprites(self,cols,sheet):
        sprites = []
        for n in range(cols):
            rect = pygame.Rect(n * self.w, 0, self.w, self.h)
            image = pygame.Surface(rect.size).convert()
            image.blit(sheet, (0,0), rect)
            alpha = image.get_at((0,0))
            image.set_colorkey(alpha)
            sprites.append(image)
        return sprites

    # def walk(self):
	# 		self.is_walking = True
	# 	for index in range(len(self.sprite_walk)):
	# 		print(index)
	# 		self.current = self.sprite_walk[index]
	# 	self.current = self.sprite_walk[0]

class ConfigurationScenario:
    
    """ 
        Clase a implementar.
    """
    def __init__(self):
        pass
