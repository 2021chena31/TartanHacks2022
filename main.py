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
current_screen = ["fail_screen"]
current_level = [0]
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
bird_sa = ["Choco Toucan", "Hyacinth Macaw", "Crested Quetzal", "Harpy Eagle"]
bird_eu = ["Eurasian Blue Tit","Eurasian Collared Dove","Common Magpie","Common Nightingale"]
bird_asia = ["Red-Crowned Crane","Giant Ibis","Chinese Nuthatch","Indian Vulture"]
bird_afr = ["Common Ostrich","Lesser Flamingo","Secretary Bird", "Shoebill"]
bird_oce = ["Kiwi", "Laughing Kookaburra", "Southern Cassowary", ""]
continents_birdlist = [bird_na,bird_sa,bird_eu,bird_asia,bird_afr,bird_oce]
continents_list = ["North America", "South America", "Europe", "Asia", "Africa","Oceania"] #, "Antartica"]


def starting_screen():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            if 0 <= x <= 100 and 0 <= y <= 50:
                current_screen[0] = "quit_screen"
            if 262 <= x <= 335 and 282 <= y <= 316:
                current_screen[0] = "main_screen"
            if 218 <= x <= 392 and 335 <= y <= 369:
                current_screen[0] = "how_to_play_screen"
            if 257 <= x <= 349 and 390 <= y <= 417:
                current_screen[0] = "about_screen"
            print(x,y)

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

def answer_order(answer_order):

    return answer_order

#helper for quiz guess
def check_answer(answer, click_index):
    print("sdfdsfd")

#helper for main_game
def level(level):
    counter = 0
    incorrect_count = 0
    used_birds = []
    while (counter < 3):
        if (incorrect_count > 1):
            current_screen[0] = "fail_screen"
            break
       
        #current country
        country = continents_list[level]

        #pull random bird, make sure not duplicate
        multiple_choices = random.sample(continents_birdlist[level], 4)
        print(multiple_choices)
        randomBird = multiple_choices[0]
        while (randomBird in used_birds):
            #randomIndex = random.randint(0,3)
            #randomBird = continents_birdlist[level][randomIndex]
            multiple_choices = random.sample(continents_birdlist[level], 4)
            randomBird = multiple_choices[0]
        used_birds.append(randomBird)

        image = pygame.image.load(os.path.join("BirdImages/" + country, randomBird + ".jpg"))
        
        birda = multiple_choices[1]
        birdb = multiple_choices[2]
        birdc = multiple_choices[3]

        bird_a_text = font_sub.render(birda, True, color_font)
        bird_b_text = font_sub.render(birdb, True, color_font)
        bird_c_text = font_sub.render(birdc, True, color_font)
        bird_correct = font_sub.render(randomBird, True, color_font)

        #answer_order = []
        #answer_order = 
        screen.fill(color_background)
        screen.blit(bird_a_text, (250,250))
        screen.blit(bird_b_text, (width/2.2,height - height/2.3))
        screen.blit(bird_c_text, (width/2.7,height - height/3))
        screen.blit(bird_correct, (width/2.3,height - height/4.5))
        screen.blit(image, (150,0))
        pygame.display.update()

        correct_flag = False

        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        sys.exit()
                    #if click on back button, break, go to main_screen

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        correct_flag = True #REMOVE THIS LATER
                        counter += 1
                        print("counter")
                        break

            if correct_flag:
                break
        
    current_level[0] += 1



def main_game():
    while (current_level[0] < 7):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            #if click on back button, break, go to main_screen

        #also if it clicks on the back button
        if (level(current_level[0]) == "main_screen"):
            break
        print("level:" + str(current_level))

    if (current_level[0] > 1):
        current_screen[0] = "win_screen"    

def howToPlay():
    welcome = font_main.render("Welcome~ ", True, color_font)
    description = font_subheading.render("Travel to countries and learn about birds!", True, color_font)
    screen.fill(color_background)
    screen.blit(welcome, (width/3.5,height/4))
    screen.blit(description, (100,300)) #NEED TO CENTER THIS
    pygame.display.update()

def aboutInfo():
    aboutInfo = font_main.render("Bird Walkers", True, color_font)
    description = font_subheading.render("You are a budding bird traveling wanting to travel the world", True, color_font)
    screen.fill(color_background)
    screen.blit(aboutInfo, (width/3.5,height/4))
    screen.blit(description, (100,300)) #NEED TO CENTER THIS
    pygame.display.update()
    

def fail_screen():
    ohno = font_main.render("Oh no!", True, color_font)
    explanation = font_sub.render("You got more than 75 percent incorrect on a quiz.", True, color_font)
    play_again = font_subheading.render("Would you like to play again?", True, color_font)

    screen.fill(color_background)
    screen.blit(ohno, (width/3.5,height/4))
    screen.blit(explanation, (100,300)) #NEED TO CENTER THIS
    screen.blit(play_again, (100,400)) #NEED TO CENTER THIS
    pygame.display.update()

    
    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_screen[0] = "starting_screen"
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_screen[0] = "quit_screen"
                break
            


def win_screen():
    congrats = font_main.render("Congratulations!", True, color_font)
    win = font_sub.render("You traveled around the world!", True, color_font)
    click = font_subheading.render("Please click to continue.", True, color_font)

    screen.fill(color_background)
    screen.blit(congrats, (width/3.5,height/4))
    screen.blit(win, (100,300)) #NEED TO CENTER THIS
    screen.blit(click, (100,400)) #NEED TO CENTER THIS
    pygame.display.update()

    
    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_screen[0] = "quit_screen"
                break


def quit_screen():
    thanks = font_sub.render("Thank you for playing!", True, color_font)
    credits = font_subheading.render("Made by the Backend Borbs for TartanHacks2022", True, color_font)

    screen.fill(color_background)
    screen.blit(title, (width/3.5,height/4))
    screen.blit(thanks, (100,300)) #NEED TO CENTER THIS
    screen.blit(credits, (100,400)) #NEED TO CENTER THIS
    pygame.display.update()

    time.sleep(4)

    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

    sys.exit()


if __name__ == '__main__':
    while True:
        if (current_screen[0] == "starting_screen"):
            starting_screen()
        if (current_screen[0] == "main_screen"):
            main_game()
        if (current_screen[0] == "how_to_play_screen"):
            howToPlay()
        if (current_screen[0] == "about_screen"):
            aboutInfo()
        if (current_screen[0] == "win_screen"):
            win_screen()
        if(current_screen[0] == "quit_screen"):
            quit_screen()
        if(current_screen[0] == "fail_screen"):
            fail_screen()
    