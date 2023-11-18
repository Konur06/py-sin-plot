import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
running = True


origin = 400

curro_pos = pygame.Vector2(10, origin)


#score setting (display position)
pygame.font.init()

font = pygame.font.Font(None, 24)

def xcord(x):
    return (x-10)/ 720 * 2 * math.pi 

def graph_sin(x):
    return (-1) * math.sin(xcord(x)) * 300 + origin





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(pygame.Color(135, 222, 177))

    display_x = font.render(f"x - coordinate: %.2f" % curro_pos.x, True, "black")
    screen.blit(display_x, (20, 10))
    display_y = font.render(f"y - coordinate: %.2f" % ((-1)* (graph_sin(curro_pos.x) - origin)), True, "black")
    screen.blit(display_y, (20, 30))

    pygame.draw.circle(screen, "red", curro_pos, 20)

    prex = 10
    xi = 10
    while(xi < curro_pos.x):
        dist = pow((xi-prex), 2) + pow((graph_sin(xi) - graph_sin(prex)), 2)
        if (dist >= 500):
            pygame.draw.circle(screen, "black", (xi, graph_sin(xi)), 2)

            prex = xi
        
        xi += 1


    keys = pygame.key.get_pressed()

    if(keys[pygame.K_LEFT]):
        if(curro_pos.x <= 10):
            pass
        else:
            curro_pos.x -= 10
            
        curro_pos.y = graph_sin(curro_pos.x)

    elif(keys[pygame.K_RIGHT]):
        if(curro_pos.x >= 1080):
            pass
        else:
            curro_pos.x += 10
        
    curro_pos.y = graph_sin(curro_pos.x)
        
    


    pygame.display.flip()

    clock.tick(60)

pygame.quit()