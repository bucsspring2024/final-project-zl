from src.controller.controller import SnakeGameController

def main():
    controller = SnakeGameController()
    controller.run()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()