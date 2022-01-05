# -*- coding: utf-8 -*-

import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((750,563))
    clock = pygame.time.Clock()
    
    img_bg = pygame.image.load("bg.png")
    img_it = pygame.image.load("item.png")
    img_it_on = pygame.image.load("item_target.png")

    pic_st = 0
    
    while True:

        """ event """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pic_st == 1:
                    pic_st = 2

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        """ get cursor pos """
        x, y = pygame.mouse.get_pos()
        if pic_st != 2:
            if 494 <= x <= 532 and 144 <= y <= 185:
                pic_st = 1
            else:
                pic_st = 0
        
        """ 背景・ブロック描画 """
        screen.blit(img_bg, [0, 0])
        if pic_st == 0:
            screen.blit(img_it, [494, 144])
        elif pic_st == 1:
            screen.blit(img_it_on, [494, 144])
        pygame.display.update()
        
        clock.tick(30)
        
        
if __name__ == '__main__':
    main()
