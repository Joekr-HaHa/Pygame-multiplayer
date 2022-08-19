import pygame
from gmaenetwork import Network
from player import Player
pygame.init()
w=500
h=500
surf=pygame.display.set_mode((w,h))
pygame.display.set_caption("Client")

clientNo=0

'''def read_pos(string):
    string=str(string)
    string=string.split(",")
    x,y=string[0],string[1]
    return x,y
def read_pos(str):
    str=str.split(",")
    return int(str[0]),int(str[1])
def make_pos(tuple):
    return str(tuple[0])+","+str(tuple[1])'''

def redrawWindow(player,surf,player2):
    surf.fill((0,0,0))
    player.draw_rect(surf)
    player2.draw_rect(surf)
    pygame.display.update()

def main():
    run=True
    n=Network()
    player=n.get_player()
    clock=pygame.time.Clock()
    while run:
        clock.tick(60)

        player2=n.send(player)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                run=False
        player.move()
        redrawWindow(player,surf,player2)
main()
