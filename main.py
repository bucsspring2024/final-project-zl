import pygame
from src.controller import Controller

def main():
    pygame.init()
    
def main():
    controller = Controller()
    controller.main_loop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
