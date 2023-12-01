import pygame as pg
import numpy as np


def init():
    global v, m, N, screen, Wi, He
    
    Wi, He = 1400,1000
    N = 300
    
    pg.init()
    screen = pg.display.set_mode((Wi,He)) 
    
    v = np.float64(np.zeros((N*He//Wi,N,2)))
    #m = np.float64(np.ones((N*He//Wi,N))) вязкость
    		
	#Xo,Yo = 100,100
	#v[Xo-5:Xo+5,Yo] = (1600,0)	

def step_calc():
    global v
    v[0,:] = (1,0)# пост усл.
    
    nV = v * 4/9
    
    nV[:-1] += v[1:] / 9
    nV[1:] += v[:-1] / 9
    nV[:,:-1] += v[:,1:] / 9
    nV[:,1:] += v[:,:-1] / 9
    
    nV[:-1,:-1] += v[1:,1:] / 36
    nV[:-1,1:] += v[1:,:-1] / 36
    nV[1:,:-1] += v[-1:,1:] / 36
    nV[1:,1:] += v[:-1,:-1] / 36
    #FIXME должно считать по Навье-Стоксу
	
    v = nV


def draw():
	screen.fill((0,0,0))
	screen.blit(pg.transform.scale(pg.surfarray.make_surface(1+v.sum(axis = 2)),(Wi,He)), (20,100))# отрисовка по модулю скорости и позже вязкости
	pg.display.update()


def main():
	init()
	
	while True:
	    step_calc()
	    draw()


if __name__ == "__main__":
    main()