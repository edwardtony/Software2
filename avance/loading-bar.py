import pygame, time ,random


pygame.init()

black = [0, 0, 0]
green = [0, 255, 0]

smallfont = pygame.font.SysFont("comicsansms", 25)

display_width = 1050
display_height = 500

size=[display_width, display_height]
screen = pygame.display.set_mode(size)

clock=pygame.time.Clock()

progress = 0

def text_onbjects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def loading(progress):
    if progress < 100:
        text = smallfont.render("Loading: " + str(int(progress)) +"%", True, green)
    else:
        text = smallfont.render("Loading: " + str(100) + "%", True, green)

    screen.blit(text, [453, 273])

def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    screen.blit(textSurf, textRect)


while (progress/2) < 100:
    time_count = 0.01
    increase = random.randint(1,1)
    progress += increase
    screen.fill(black)
    pygame.draw.rect(screen, green, [423, 223, 204, 49])
    pygame.draw.rect(screen, black, [424, 224, 202, 47])

    
    if(progress/2 > 100):
       pygame.draw.rect(screen, green, [425, 225, 200, 45])
    else:
       pygame.draw.rect(screen, green, [425, 225, progress, 45])
    loading(progress/2)
    pygame.display.flip()

    time.sleep(time_count)
    
        









                    
