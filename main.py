import os, pygame, sys, time, random
#import setup

pygame.init()

#Variable setup
size = width, height = 600,500
color_background = (255,255,200)
color_font = (0,0,0)
font_main = pygame.font.SysFont('Corbel',60) 
font_sub = pygame.font.SysFont('Corbel',35)
font_subheading = pygame.font.SysFont('Corbel', 20)

#set initial screens and level information
current_screen = "main_screen"
current_level = 0
current_score = 0

#initialize the screen
screen = pygame.display.set_mode(size)

#setting up the text
title = font_main.render('BirdWalkers' , True , color_font) 
subheading = font_subheading.render('Bird ID game for birdwatchers to travel across the world!', True, color_font)
quit = font_sub.render('Quit', True, color_font)
play = font_sub.render('Play', True, color_font)
how_to_play = font_sub.render('How to Play', True, color_font)
about = font_sub.render('About', True, color_font)
quit_button = pygame.Rect(0,0,100,50)
how_to_play_button = pygame.Rect(width/4,height/4,width/2,height/2)
about_button = pygame.Rect(0,0,100,50)

#stuff for levels
bird_na = ["Bald Eagle", "American Robin", "Canada Goose", "Mallard"]
bird_sa = ["Choco Toucan", "Hyacinth Macaw", "Crested Quetzal", ""]
bird_eu = []
bird_asia = []
bird_afr = []
bird_aus = ["Kiwi", ""]
bird_ant = []
continents_birdlist = [bird_na,bird_sa,bird_eu,bird_asia,bird_afr,bird_aus,bird_ant]
continents_list = ["North America", "South America", "Europe", "Asia", "Africa","Australia", "Antartica"]


def starting_screen():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            if 0 <= x <= 100 and 0 <= y <= 50:
                current_screen = "quit_screen"
            if 262 <= x <= 335 and 282 <= y <= 316:
                current_screen = "main_screen"
            if 218 <= x <= 392 and 335 <= y <= 369:
                current_screen = "how_to_play_screen"
            if 257 <= x <= 349 and 390 <= y <= 417:
                current_screen = "about_screen"
            print(x,y)

        #if event.type == sdfkladsfjfs
        #   current_screen = "main_screen"

   #remake screen
    screen.fill(color_background)
    pygame.draw.rect(screen, (255,0,0), quit_button)
    screen.blit(title, (width/3.5,height/4))
    screen.blit(subheading, (width/8,height/2.5))
    screen.blit(quit, (width/40,height/40))
    screen.blit(play, (width/2.2,height - height/2.3))
    screen.blit(how_to_play, (width/2.7,height - height/3))
    screen.blit(about, (width/2.3,height - height/4.5))
    pygame.display.update()

#helper for main_game
def level(current_level):
    counter = 0
    used_birds = []
    while (counter < 3):
        #generate randombird
        randomIndex = random.randint(0,3)

        #current country
        country = continents_list[current_level]

        #pull random bird, make sure not duplicate
        randomBird = continents_birdlist[current_level][randomIndex]
        while (randomBird in used_birds):
            randomBird = continents_birdlist[current_level][randomIndex]
        used_birds.append(randomBird)

        image = pygame.image.load(os.path.join("BirdImages/" + country, randomBird + ".jpg"))

        print(used_birds)
        
        screen.fill(color_background)
        screen.blit(image, (0,0))
        pygame.display.update()

        correct_flag = False

        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        sys.exit()
                    #if click on back button, break, go to main_screen

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        correct_flag = True #REMOVE THIS LATER
                        print("counter")
                        break

            if correct_flag:
                break
        

    current_level += 1

def main_game():
    while (current_level < 7):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            #if click on back button, break, go to main_screen
        if (level(current_level) == "main_screen"):
            break

    if (current_level > 7):
        current_screen = "win_screen"    
    

def win_screen():
    print("Congrats, you win!")
    print("click to continue")
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_screen = "quit_screen"

    #replace with better ending screen

def quit_screen():
    #dispay thanks for playing, made by the backend borbs
    time.sleep(1000)
    sys.exit()


if __name__ == '__main__':
    while True:
        if (current_screen == "starting_screen"):
            starting_screen()
        if (current_screen == "main_screen"):
            main_game()
        if (current_screen == "win_screen"):
            win_screen()
        if(current_screen == "quit_screen"):
            quit_screen()
    