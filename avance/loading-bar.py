import pygame, time ,random


pygame.init()

black = [0, 0, 0]
green = [0, 255, 0]

smallfont = pygame.font.SysFont("comicsansms", 25)

display_width = 960
display_height = 600

size=[display_width, display_height]
screen = pygame.display.set_mode(size)

clock=pygame.time.Clock()

progress = 0


def text_onbjects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def loading(progress):
    cachimbo = pygame.image.load("logo2.png").convert()
    cachimbo = pygame.transform.scale(cachimbo,(300,200))
    screen.blit(cachimbo,(350,50))
    if progress < 100:
        text = smallfont.render("Loading: " + str(int(progress)) +"%", True, green)
    else:
        text = smallfont.render("Loading: " + str(100) + "%", True, green)

    screen.blit(text, [413, 333])

def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    screen.blit(textSurf, textRect)


while (progress/2) < 100:
    time_count = 0.01
    increase = random.randint(1,1)
    progress += increase
    screen.fill(black)
    pygame.draw.rect(screen, green, [393, 283, 204, 49])
    pygame.draw.rect(screen, black, [394, 284, 202, 47])

    
    if(progress/2 > 100):
       pygame.draw.rect(screen, green, [395, 285, 200, 45])
    else:
       pygame.draw.rect(screen, green, [395, 285, progress, 45])
    loading(progress/2)
    pygame.display.flip()

    time.sleep(time_count)
    
        









                    
