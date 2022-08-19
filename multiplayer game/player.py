import pygame
class Player():
    def __init__(self,x,y,w,h,color):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.color=color
        self.rect=(x,y,w,h)
        self.val=3

    def draw_rect(self,surf):
        pygame.draw.rect(surf,self.color,self.rect)

    def move(self):
        key=pygame.key.get_pressed()#dict of each key with 1 or 0
        if key[pygame.K_LEFT]:
            self.x-=self.val
        if key[pygame.K_RIGHT]:
            self.x+=self.val
        if key[pygame.K_DOWN]:
            self.y+=self.val
        if key[pygame.K_UP]:
            self.y-=self.val
        self.update()
    def update(self):
            
        self.rect=(self.x,self.y,self.w,self.h)

