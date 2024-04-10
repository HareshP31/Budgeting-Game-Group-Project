import pygame
import random
import sys

# Function to get difficulty
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # choose difficulty keys
            elif event.key == pygame.K_e:
                return "easy"
            elif event.key == pygame.K_m:
                return "medium"
            elif event.key == pygame.K_h:
                return "hard"     
            else:
                print("Please enter 'e', 'm', or 'h'")
    return None

# Display text function
def display_text(screen, font, text, position, color=(0, 0, 0)):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)

# Function that sets income
def chooseIncome(x):
    if x==1:
        return 1000
    if x==2:
        return 750
    if x==3:
        return 500
# Function that sets rent
def chooseRent(r):
    if r==1 or r==2:
        return 150
    if r==3:
        return 200

# Function to generate phrases
def generate_random_phrase(b):
    good_nochoice = [
        "Congratulations! You won a contest and received groceries worth:",
        "You just got a bonus! Worth:",
        "Your daughter got a full ride to her dream college and financial aid worth:",
        "It is the holiday season! You got a gift card worth:",
        "Great news! Your utility bills decreased this month due to energy-saving improvements by:",
        "Your job gave you a bonus for working overtime. Worth:",
        "Lucky day! Your insurance rewarded you for safe driving with:",
        "You received a tax refund from overpaid taxes last year. Worth:",
        "A friend paid you back after they owed you for a long time. Worth:",
        "Your favorite store is having a clearance sale, and you saved:"
    ]
    bad_nochoice = [
        "Your refrigerator stopped working and it will cost:",
        "Your car broke down and towing it will cost:",
        "Your pet fell ill recently. The cost to see the vet is:",
        "You were brushing your teeth in the bathroom when you suddenly realized, your roof is leaking! To fix it costs:",
        "You fell down the stairs and possibly twisted your ankle. A doctor visit costs:",
        "Your grandfather needs help to pay for his medical bills worth:",
    ]
    yesno = [
        "Your child is going on a school field trip to the Grand Canyon. The cost is:",
        "Your child's school is hosting a fundraising event, and the suggested donation is:",
        "Your laptop screen cracked, and replacing it will cost:",
        "Your water heater malfunctioned, and fixing it will cost:",
        "Your grandmother is ill and she needs you. The flight to see her costs:",
        "It is your best friend's birthday; the present costs:",
        "Your TV broke; a new TV costs:",
        "Your bed frame broke; a new one costs:",
        "Your friends invited you to a concert that costs:",
        "You need a haircut that will cost:",
        "Your lawn needs mowing which will cost:"
    ]
    # Sets number range based on difficulty
    if b == 1:
        random_number = random.randint(100, 200)
    elif b == 2:
        random_number = random.randint(300, 400)
    elif b == 3:
        random_number = random.randint(500, 600)
    # Store lists in one list
    lists = [good_nochoice, bad_nochoice, yesno]
    # Choose a random list
    selected_list = random.choice(lists)
    # Choose random phrase from list chosen
    if(selected_list == good_nochoice):
        y = 1
    elif(selected_list == bad_nochoice):
        y = 2
    elif(selected_list == yesno):
        y = 3
    phrase = random.choice(selected_list)
    # Return values
    return phrase, random_number, y

def reset_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                reset = 1
                return reset
            elif event.key == pygame.K_r:
                reset = 2
                return reset   
            else:
                print("Please enter 'r' or esc")
    return None

def main():
    # Initialize pygame window
    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption("Difficulty Selection")

    font = pygame.font.SysFont("comic sans", 20)

    running = True
    difficulty = None
    reset = None
    # For refreshing window to blank screen
    key_counter = 0
    # total variables
    easy_total = 1000
    medium_total = 750
    hard_total = 500

    while running:
        screen.fill((255, 255, 255))
        
        # Display instructions
        display_text(screen, font, "Press 'e' for Easy, 'm' for Medium, 'h' for Hard", (30, 100))
        display_text(screen, font, "Press space to continue (When presented with an option, press Y for Yes or N for No, then space)", (30, 120))
        # Check for events
        difficulty = handle_events()
        if difficulty:
            break

        pygame.display.flip()

    if difficulty == "easy":
        # prints header
        display_text(screen, font, "Easy selected!", (30, 150))
        display_text(screen, font, "Your income is $1,000 a week", (30, 170))
        display_text(screen, font, "Your rent is $150 a week", (30, 190))
        display_text(screen, font, "Week 1: ", (30, 210))
        # offset value
        random_offset = 230
        for i in range(28):
            while True: 
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        phrase, rand_num, y = generate_random_phrase(1)
                        break
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_r:
                        main()
            # refresh screen to blank at the end of the week
            if(key_counter%7 == 0 and key_counter != 0):
                white = (255, 255, 255)
                screen.fill(white)
                random_offset = 20
                display_text(screen, font, f"Week {(i//7)+1}: ", (30, 0))
                pygame.display.flip()
            # If it is good phrase and requires no input
            if(y == 1):
                display_text(screen, font, f"{phrase} ${rand_num} (Press Space)", (30, random_offset))
                random_offset += 25
                pygame.display.flip()
                key_counter += 1
                easy_total += rand_num
                display_text(screen, font, f"Your Total: {easy_total}", (30, random_offset), (0, 0, 255))
                random_offset += 25
                if((i+1)%7 == 0):
                    easy_total += chooseIncome(1)
                    easy_total -= chooseRent(1)
            # If it is bad phrase and requires no input
            elif(y == 2):
                display_text(screen, font, f"{phrase} ${rand_num} (Press Space)", (30, random_offset))
                random_offset += 25
                pygame.display.flip()
                key_counter += 1
                easy_total -= rand_num
                display_text(screen, font, f"Your Total: {easy_total}", (30, random_offset), (0, 0, 255))
                random_offset += 25
                if((i+1)%7 == 0):
                    easy_total += chooseIncome(1)
                    easy_total -= chooseRent(1)
            # If it is phrase that requires input
            elif(y == 3):
                display_text(screen, font, f"{phrase} ${rand_num} (Y/N?)", (30, random_offset))
                random_offset += 25
                pygame.display.flip()
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN:
                        # Y key is pressed
                        if event.key == pygame.K_y:
                            key_counter += 1
                            easy_total -= rand_num
                            display_text(screen, font, f"Your Total: {easy_total}", (30, random_offset), (0, 0, 255))
                            random_offset += 25
                            # if it is the end of the week 
                            if((i+1)%7 == 0):
                                easy_total += chooseIncome(1)
                                easy_total -= chooseRent(1)
                            break
                        # N key is pressed
                        elif event.key == pygame.K_n:
                            key_counter += 1
                            display_text(screen, font, f"Your Total: {easy_total}", (30, random_offset), (0, 0, 255))
                            random_offset += 25
                            # if it is the end of the week 
                            if((i+1)%7 == 0):
                                easy_total += chooseIncome(1)
                                easy_total -= chooseRent(1)
                            break
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()

        if easy_total > 1000:
            display_text(screen, font, "You finished with more than what you started with!", (30, random_offset), (0, 255, 0))
            random_offset += 25
        elif easy_total < 1000 and easy_total > 0:
            display_text(screen, font, "You finished with less than what you started with!", (30, random_offset), (255, 0, 0))
            random_offset += 25
        elif easy_total < 0:
            display_text(screen, font, "You finished and you are in debt :(", (30, random_offset), (255, 0, 0))
            random_offset += 25
        
        running = True
        reset = None
        display_text(screen, font, "Press r to reset the game and play again! or press esc to exit.", (30, random_offset)) 
        while running:
            reset = reset_game()
            if reset:
                break

            pygame.display.flip()

        if(reset == 2):
            main()
        elif(reset == 1):
            pygame.quit()
            sys.exit()
    
    elif difficulty == "medium":
        display_text(screen, font, "Medium selected!", (30, 150))
        display_text(screen, font, "Your income is $750 a week", (30, 170))
        display_text(screen, font, "Your rent is $150 a week", (30, 190))
        display_text(screen, font, "Week 1: ", (30, 210))
        random_offset = 230
        for i in range(28):
            while True: 
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        phrase, rand_num, y = generate_random_phrase(2)
                        break
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            if (y == 3):
              display_text(screen, font, f"{phrase} ${rand_num} (Y/N?)", (30, random_offset))
              random_offset += 25
              pygame.display.flip()
            else:
              display_text(screen, font, f"{phrase} ${rand_num} (Press Space)", (30, random_offset))
              random_offset += 25
              pygame.display.flip()

            # refresh screen to blank
            if(key_counter%7 == 0 and key_counter != 0):
                white = (255, 255, 255)
                screen.fill(white)
                random_offset = 20
                display_text(screen, font, f"Week {(i//7)+1}: ", (30, 0))
                pygame.display.flip()
            if(y == 1):
                key_counter += 1
                medium_total += rand_num
                display_text(screen, font, f"Your Total: {medium_total}", (30, random_offset), (0, 0, 255))
                random_offset += 25
                if((i+1)%7 == 0):
                    medium_total += chooseIncome(2)
                    medium_total -= chooseRent(2)
            elif(y == 2):
                key_counter += 1
                medium_total -= rand_num
                display_text(screen, font, f"Your Total: {medium_total}", (30, random_offset), (0, 0, 255))
                random_offset += 25
                if((i+1)%7 == 0):
                    medium_total += chooseIncome(2)
                    medium_total -= chooseRent(2)
            elif(y == 3):
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            key_counter += 1
                            medium_total -= rand_num
                            display_text(screen, font, f"Your Total: {medium_total}", (30, random_offset), (0, 0, 255))
                            random_offset += 25
                            if((i+1)%7 == 0):
                                medium_total += chooseIncome(2)
                                medium_total -= chooseRent(2)
                            break
                        elif event.key == pygame.K_n:
                            key_counter += 1
                            display_text(screen, font, f"Your Total: {medium_total}", (30, random_offset), (0, 0, 255))
                            random_offset += 25
                            if((i+1)%7 == 0):
                                medium_total += chooseIncome(2)
                                medium_total -= chooseRent(2)
                            break
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()

        if medium_total > 1000:
            display_text(screen, font, "You finished with more than what you started with!", (30, random_offset), (0, 255, 0))
            random_offset += 25
        elif medium_total < 1000 and medium_total > 0:
            display_text(screen, font, "You finished with less than what you started with!", (30, random_offset), (255, 0, 0))
            random_offset += 25
        elif medium_total < 0:
            display_text(screen, font, "You finished and you are in debt :(", (30, random_offset), (255, 0, 0))
            random_offset += 25
        
        running = True
        reset = None
        display_text(screen, font, "Press r to reset the game and play again! or press esc to exit.", (30, random_offset)) 
        while running:
            reset = reset_game()
            if reset:
                break

            pygame.display.flip()

        if(reset == 2):
            main()
        elif(reset == 1):
            pygame.quit()
            sys.exit()                             

    elif difficulty == "hard":
        display_text(screen, font, "Hard selected!", (30, 150))
        display_text(screen, font, "Your income is $500 a week", (30, 170))
        display_text(screen, font, "Your rent is $200 a week", (30, 190))
        display_text(screen, font, "Week 1: ", (30, 210))
        random_offset = 230
        for i in range(28):
            while True: 
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        phrase, rand_num, y = generate_random_phrase(3)
                        break
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            if (y == 3):
              display_text(screen, font, f"{phrase} ${rand_num} (Y/N?)", (30, random_offset))
              random_offset += 25
              pygame.display.flip()
            else:
              display_text(screen, font, f"{phrase} ${rand_num} (Press Space)", (30, random_offset))
              random_offset += 25
              pygame.display.flip()

            # refresh screen to blank
            if(key_counter%7 == 0 and key_counter != 0):
                white = (255, 255, 255)
                screen.fill(white)
                random_offset = 20
                display_text(screen, font, f"Week {(i//7)+1}: ", (30, 0))
                pygame.display.flip()
            if(y == 1):
                key_counter += 1
                hard_total += rand_num
                display_text(screen, font, f"Your Total: {hard_total}", (30, random_offset), (0, 0, 255))
                random_offset += 25
                if((i+1)%7 == 0):
                    hard_total += chooseIncome(3)
                    hard_total -= chooseRent(3)
            elif(y == 2):
                key_counter += 1
                hard_total -= rand_num
                display_text(screen, font, f"Your Total: {hard_total}", (30, random_offset), (0, 0, 255))
                random_offset += 25
                if((i+1)%7 == 0):
                    hard_total += chooseIncome(3)
                    hard_total -= chooseRent(3)
            elif(y == 3):
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            key_counter += 1
                            hard_total -= rand_num
                            display_text(screen, font, f"Your Total: {hard_total}", (30, random_offset), (0, 0, 255))
                            random_offset += 25
                            if((i+1)%7 == 0):
                                hard_total += chooseIncome(3)
                                hard_total -= chooseRent(3)
                            break
                        elif event.key == pygame.K_n:
                            key_counter += 1
                            display_text(screen, font, f"Your Total: {hard_total}", (30, random_offset), (0, 0, 255))
                            random_offset += 25
                            if((i+1)%7 == 0):
                                hard_total += chooseIncome(3)
                                hard_total -= chooseRent(3)
                            break
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
        if hard_total > 500:
            display_text(screen, font, "You finished with more than what you started with!", (30, random_offset), (0, 255, 0))
            random_offset += 25
        elif hard_total < 500 and hard_total > 0:
            display_text(screen, font, "You finished with less than what you started with!", (30, random_offset), (255, 0, 0))
            random_offset += 25
        elif hard_total < 0:
            display_text(screen, font, "You finished and you are in debt :(", (30, random_offset), (255, 0, 0))
            random_offset += 25
        
        running = True
        reset = None
        display_text(screen, font, "Press r to reset the game and play again! or press esc to exit.", (30, random_offset)) 
        while running:
            reset = reset_game()
            if reset:
                break

            pygame.display.flip()

        if(reset == 2):
            main()
        elif(reset == 1):
            pygame.quit()
            sys.exit()   


    pygame.display.flip()
    
    # Continue running until escape key is pressed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    

main()
