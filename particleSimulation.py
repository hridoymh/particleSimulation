import pygame
import random
import math
import threading

class Particle:
    def __init__(self,x,y,xv,yv,color,r) -> None:
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.color = color
        self.r = r
    def draw(self,win):
        pygame.draw.circle(win,self.color,self.cordConverter(self.x,self.y),self.r,0)

    def cordConverter(self,x,y):
        dw = pygame.display.Info().current_w
        dh = pygame.display.Info().current_h
        finalTupple = (dw//2-x,dh//2-y)
        return finalTupple
    
    def update(self, vx,vy):
        
        self.xv = vx
        self.yv = vy
        tempx = self.xv +self.x
        tempy = self.yv +self.y
        self.x += self.xv
        self.y += self.yv



class Env:
    def __init__(self,win) -> None:
        self.red = self.create(200,(255,0,0),2)
        self.blue = self.create(200,(255,255,0),2)
        self.green = self.create(200,(0,255,0),2)
        self.all = [self.red,self.blue,self.green]
        self.win = win
    def create(self,num,color,r):
        return [Particle(random.randint(-750,750),random.randint(-500,500),0,0,color,r) for i in range(num)]
    def draw(self):

        self.ruleAnR(self.red,self.red,-0.01)
        self.ruleAnR(self.blue,self.red,-0.1)
        self.ruleAnR(self.green,self.blue,-0.1)

        for i in self.all:
            for j in i:
                j.draw(self.win)
    def ruleAnR(self,list1,list2,g):
        for i in list1:
            fx = 0
            fy = 0
            for j in list2:
                dx = i.x-j.x
                dy = i.y-j.y
                distance = math.sqrt(dx*dx+dy*dy)
                if distance>0:
                    F = g/distance
                    fx = (F*dx)
                    fy = (F*dy)
            i.update(i.xv+fx,i.yv+fy)
    
        






pygame.init()

clock = pygame.time.Clock()
  
color = (0,0,0)
position = (0,0)
  
# CREATING CANVAS
disp = (1500,1000)
canvas = pygame.display.set_mode(disp)

env = Env(canvas)
  
# TITLE OF CANVAS

exit = False
  
while not exit:
    canvas.fill(color)
    
    env.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
  
    pygame.display.update()
    clock.tick(30)