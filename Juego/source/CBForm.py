class FormFactory():

class Form():

    def __init__(self):
        self.components = []

    def add_child(self, child):


class EditText():

    """
        Clase que genera un input en formato EditTExt
    """

    # Constructor
    def __init__(self, x=0, y=0, width=200, height=40, border=2, value='',focus=False , max=20):
        self.x = x
        self.y = y
        self.width = max * 7 if width < max * 7 else width
        self.height = height
        self.border = border
        self.value = value
        self.max = max
        self.focus = focus
        self.rect = self.draw()

    # Escribir dentro del input
    def type_char(self, char):
        if len(self.value) < self.max and self.focus:
            self.value = ''.join([self.value, char])

    # Cambiar el color de los bordes, se modifican con el atributo Focus
    def load_border_color(self):
        return Color.YELLOW   if self.focus else Color.BLACK

    # Dibujar el input en el Display
    def draw(self):
        margin = 5
        size = 40
        font = pygame.font.SysFont(None, size)
        title = font.render(self.value,True, Color.BLACK)
        screen.blit(title, (self.x + margin, self.y + margin))
        return pygame.draw.rect(screen, self.load_border_color(),(self.x,self.y,self.width,self.height),self.border)

    # Evaluar si hicieron click dentro de la input (caja)
    def collidepoint(self,mouse_position):
        if self.rect.collidepoint(mouse_position):
            self.focus = True
        else:
            self.focus = False

    # Renderiza los nuevos cambios del input
    def update(self, e):
        self.draw()
        if e.type == KEYDOWN:
            # Catch enter
            if pygame.key.name(e.key) in ['up','down','left','right']:
                return
            if e.key == 'return':
                return True
            # Move cursor
            # elif key == 'left':
            #      self._cursor_back()
            # elif key == 'right':
            #     self._cursor_forward()
            # # Edit text
            # elif key == 'backspace':
            #      self._backspace()
            elif e.key == K_BACKSPACE and self.focus == True:
                self.value = self.value[0:len(self.value)-1]
            elif e.key == K_SPACE:
                self.type_char(' ')
            elif len(e.unicode) == 1:
                self.type_char(e.unicode)
            # Signal event unused
            else:
                r = True


class RadioButtonManager():

    """
        Clase gestora del comportamiento de los radios buttons
    """

    # Constructor
    def __init__(self):
        self.buttons = []

    # Agrega botones al Radio Group
    def add_button(self,button):
        button.manager = self
        self.buttons.append(button)

    # Obtiene los botones del Radio Group
    def get_buttons(self,):
        return self.buttons

    # Elige el botón clickeado y deselecciona los otros botones
    def manage_select(self,clicked_button):
        for button in self.buttons:
            if button == clicked_button:
                button.focus = True
            else:
                button.focus = False



class Button():

    """
        Clase que genera y gestiona un botón
    """

    # Constuctor
    def __init__(self, x=0, y=0, width=200, height=40, border=2, value='', focus=False):
        self.x = x
        self.y = y
        self.width = len(value) * 19 if width < len(value) * 19 else width
        self.height = height
        self.border = border
        self.value = value
        self.focus = focus
        self.rect = self.draw()

    # Cambiar el color de los bordes, se modifican con el atributo Focus
    def load_border_color(self):
        return Color.YELLOW  if self.focus else Color.BLACK

    # Evalua si el botón fue clickeado
    def collidepoint(self,mouse_position):
        if self.rect.collidepoint(mouse_position):
            self.manager.manage_select(self)

    # Renderiza el botón en el Display
    def draw(self):
        margin = 5
        size = 40
        font = pygame.font.SysFont(None, size)
        title = font.render(self.value,True, self.load_border_color())
        screen.blit(title, (self.x + margin, self.y + margin))
        return pygame.draw.rect(screen, self.load_border_color(),(self.x,self.y,self.width,self.height),self.border)
