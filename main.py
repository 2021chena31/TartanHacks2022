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
current_screen = ["starting_screen"]
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
bird_oce = ["Kiwi", "Laughing Kookaburra", "Southern Cassowary", "Red Wattlebird"]
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


def correct_answer():
    screen.fill(color_background)
    correct = font_main.render('CORRECT!' , True , (0,255,0))
    screen.blit(correct, (width/4, height/3))
    pygame.display.update()

    time.sleep(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            return

    

def incorrect_answer():
    screen.fill(color_background)
    incorrect = font_main.render('INCORRECT.' , True , (255,0,0))
    screen.blit(incorrect, (width/4, height/3))
    pygame.display.update()

    time.sleep(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            return

#helper for main_game
def level(level):
    counter = 0
    incorrect_count = 0
    used_birds = []

    while (counter < 3):
        #more than 75% incorrect
        if (incorrect_count > 1):
            print("FAIL SCREEN NEEDED")
            current_screen[0] = "fail_screen"
            break
       
        #current country
        country = continents_list[level]

        #pull random bird, make sure not duplicate
        multiple_choices = random.sample(continents_birdlist[level], 4)
        randomBird = multiple_choices[0]
        while (randomBird in used_birds):
            multiple_choices = random.sample(continents_birdlist[level], 4)
            randomBird = multiple_choices[0]
        used_birds.append(randomBird)

        #get bird image
        image = pygame.image.load(os.path.join("BirdImages/" + country, randomBird + ".jpg"))
        
        birda = multiple_choices[1]
        birdb = multiple_choices[2]
        birdc = multiple_choices[3]

        bird_a_text = font_sub.render(birda, True, color_font)
        bird_b_text = font_sub.render(birdb, True, color_font)
        bird_c_text = font_sub.render(birdc, True, color_font)
        bird_correct = font_sub.render(randomBird, True, color_font)

        location_list = [250,300,350,400]
        bird_location = random.sample(location_list, 4)
        screen.fill(color_background)
        screen.blit(bird_a_text, (200,bird_location[1]))
        screen.blit(bird_b_text, (200,bird_location[2]))
        screen.blit(bird_c_text, (200,bird_location[3]))
        screen.blit(bird_correct, (200,bird_location[0]))
        screen.blit(image, (200,10))
        pygame.display.update()

        answered_flag = False

        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            x = pos[0]
                            y = pos[1]
                            if 190 <= x <= 535 and 250 <= y <= 280:
                                if (bird_location[0] == 250):
                                    correct_answer()
                                    #correct_flag = True
                                    counter += 1
                                else:
                                    print("Incorrect")
                                    incorrect_answer()
                                    incorrect_count += 1
                                answered_flag = True
                                break 

                            if 190 <= x <= 535 and 300 <= y <= 330:
                                if (bird_location[0] == 300):
                                    print("Correct")
                                    correct_answer()
                                    #correct_flag = True
                                    counter += 1
                                else:
                                    print("Incorrect")
                                    incorrect_answer()
                                    incorrect_count += 1
                                answered_flag = True
                                break 

                            if 190 <= x <= 535 and 350 <= y <= 380:
                                if (bird_location[0] == 350):
                                    print("Correct")
                                    correct_answer()
                                    #correct_flag = True
                                    counter += 1
                                else:
                                    print("Incorrect")
                                    incorrect_answer()
                                    incorrect_count += 1
                                answered_flag = True
                                break 

                            if 190 <= x <= 535 and 400 <= y <= 430:
                                if (bird_location[0] == 400):
                                    print("Correct")
                                    correct_answer()
                                    #correct_flag = True
                                    counter += 1
                                else:
                                    print("Incorrect")
                                    incorrect_answer()
                                    incorrect_count += 1
                                answered_flag = True
                                break

            if answered_flag:
                break
        
    current_level[0] += 1
    print(current_level[0])


def intermission(level):
    while True:
        continent = continents_list[level]
        image = pygame.image.load(os.path.join("Intermission/", continent + ".jpg"))
        title = font_main.render(continent, True , color_font) 
        
        screen.fill(color_background)
        screen.blit(image, (150,100))
        screen.blit(title, (150,5))

        decription_list = [ "Your journey starts in North America!",
                            "Heading south to South America!",
                            "Now, hop across the Atlantic to Europe!",
                            "Travel to the other Eurasian Continent: Asia!",
                            "Take a safari down to Africa!",
                            "Go by the \"Land Down Under\"!",
        ]
        
        description = font_subheading.render(decription_list[level], True, color_font)
        screen.blit(description, (150, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
    

def main_game():
    while (current_level[0] < 6):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

        intermission(current_level[0])
        level(current_level[0])
        print("level:" + str(current_level))
        print(current_screen[0])

        if (current_screen[0] == "fail_screen"):
            return

    if (current_level[0] > 6):
        current_screen[0] = "win_screen"    


def howToPlay():
    descriptionList = ["Travel to all around the world and learn about birds!",
                        "",
                       "Pass the bird quiz for every continent by identifying", 
                       "at least 3/4 of the birds correctly.",
                       "",
                       "Become an expert BirdVenturer by traveling to all",
                       "of the 6 available continents!"]
    welcome = font_main.render("Welcome~ ", True, color_font)
    #description = font_subheading.render("Travel to countries and learn about birds!", True, color_font)
    screen.fill(color_background)
    screen.blit(welcome, (width/3.5,height/4))
    #screen.blit(description, (100,300)) #NEED TO CENTER THIS
    for i in range(len(descriptionList)):
        description = font_subheading.render(descriptionList[i], True, color_font)
        screen.blit(description, (width/6, int(height/2) + 20*i))
    pygame.display.update()

    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_screen[0] = "starting_screen"
                break

def aboutInfo():
    descriptionList = ["You are a budding birdie wanting to travel the world",
                       "but COVID19 destroyed all your plans :(", 
                       "",
                       "Never fear! You can travel to countries through Bird Walker!",
                       "",
                       "Travel to different continents and learn about birds!",
                       "We promise you'll have a hoot! ;)"]
    aboutInfo = font_main.render("Hello Birdventurer!", True, color_font)
    screen.fill(color_background)
    for i in range(len(descriptionList)):
        description = font_subheading.render(descriptionList[i], True, color_font)
        screen.blit(description, (width/6, int(height/4) + 20*i))
    screen.blit(aboutInfo, (width/6,height/10))
    
    pygame.display.update()

    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_screen[0] = "starting_screen"
                break
    

def fail_screen():
    ohno = font_main.render("Oh no!", True, color_font)
    explanation = font_sub.render("You got more than 75% incorrect on a quiz.", True, color_font)
    play_again = font_subheading.render("Would you like to play again?", True, color_font)

    screen.fill(color_background)
    screen.blit(ohno, (width/3,height/4))
    screen.blit(explanation, (10,height/2))
    screen.blit(play_again, (width/3,height - height/4))
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
    click = font_subheading.render("Please click anywhere to continue.", True, color_font)

    screen.fill(color_background)
    screen.blit(congrats, (width/6,height/4))
    screen.blit(win, (100,250))
    screen.blit(click, (150,350)) 
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
    