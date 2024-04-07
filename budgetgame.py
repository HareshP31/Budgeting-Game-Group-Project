import pygame
import random
import sys

# Function to handle events
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
# Function that generates random number
def generate_random_number(b):
        if(b == 1):
            randnum = random.randint(100, 200)
            return randnum
        elif(b == 2):
            randnum = random.randint(300, 400)
            return randnum
        elif(b == 3):
            randnum = random.randint(500, 600)
            return randnum
# Function to generate phrases
def generate_random_phrase(b):
    good_nochoice = [
        "Congratulations! You won a contest and received groceries worth: (Press space)",
        "You just got a bonus! Worth: (Press space)",
        "Your daughter got a full ride to her dream college and financial aid worth: (Press space)",
        "It is the holiday season! You got a gift card worth: (Press space)",
        "Great news! Your utility bills decreased this month due to energy-saving improvements by: (Press space)",
        "Your job gave you a bonus for working overtime. Worth: (Press space)",
        "Lucky day! Your insurance rewarded you for safe driving with: (Press space)",
        "You received a tax refund from overpaid taxes last year. Worth: (Press space)",
        "A friend paid you back after they owed you for a long time. Worth: (Press space)",
        "Your favorite store is having a clearance sale, and you saved: (Press space)"
    ]
    bad_nochoice = [
        "Your refrigerator stopped working and it will cost: (Press space)",
        "Your car broke down and towing it will cost: (Press space)",
        "Your pet fell ill recently. The cost to see the vet is: (Press space)",
        "You were brushing your teeth in the bathroom when you suddenly felt a drop on your face. Your roof is leaking! To fix it costs: (Press space)",
        "You fell down the stairs and possibly twisted your ankle. A doctor visit costs: (Press space)",
        "Your grandfather needs help to pay for his medical bills worth: (Press space)",
    ]
    yesno = [
        "Your child is going on a school field trip to the Grand Canyon. She’s been wanting to go for the longest time and the cost is: (Y/N?)",
        "Your child's school is hosting a fundraising event, and the suggested donation is: (Y/N?)",
        "Your laptop screen cracked, and replacing it will cost: (Y/N?)",
        "Your water heater malfunctioned, and fixing it will cost: (Y/N?)",
        "Your grandmother is ill and she needs you. The flight to see her costs: (Y/N?)",
        "It is your best friend's birthday; the present costs: (Y/N?)",
        "Your TV broke; a new TV costs: (Y/N?)",
        "Your bed frame broke; a new one costs: (Y/N?)",
        "Your friends invited you to a concert that costs: (Y/N?)",
        "You need a haircut that will cost: (Y/N?)",
        "Your lawn needs mowing which will cost: (Y/N?)"
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
    global key_counter, easytotal, mediumtotal, hardtotal
    key_counter = 0
    easytotal = 0
    mediumtotal = 0
    hardtotal = 0

def main():
    global key_counter, easytotal, mediumtotal, hardtotal
    # Initialize pygame window
    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption("Difficulty Selection")

    font = pygame.font.SysFont("comic sans", 20)

    running = True
    difficulty = None
    # For refreshing window to blank screen
    key_counter = 0
    # total variables
    easytotal = 1000
    mediumtotal = 750
    hardtotal = 500

    while running:
        screen.fill((255, 255, 255))
        
        # Display instructions
        instructions = font.render("Press 'e' for Easy, 'm' for Medium, 'h' for Hard", True, (0, 0, 0))
        spacetext = font.render("Press space to continue (When presented with an option, press Y for Yes or N for No, then space)", True, (0, 0, 0))
        screen.blit(instructions, (30, 100))
        screen.blit(spacetext, (30, 120))

        # Check for events
        difficulty = handle_events()
        if difficulty:
            break

        pygame.display.flip()

    if difficulty == "easy":
        # prints header
        text = font.render("Easy selected!", True, (0, 0, 0))
        screen.blit(text, (30, 150))
        incometext = font.render("Your income is $1,000 a week", True, (0, 0, 0))
        screen.blit(incometext, (30, 170))
        renttext = font.render("Your rent is $150 a week", True, (0, 0, 0))
        screen.blit(renttext, (30, 190))
        weektext = font.render("Week 1: ", True, (0, 0, 0))
        screen.blit(weektext, (30, 210))
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
                            
            randomtext = font.render(f"{phrase} - Value: {rand_num}", True, (0, 0, 0))
            screen.blit(randomtext, (30, random_offset))
            random_offset += 25
            pygame.display.flip()
            # refresh screen to blank at the end of the week
            if(key_counter%7 == 0 and key_counter != 0):
                white = (255, 255, 255)
                screen.fill(white)
                random_offset = 20
                weektext = font.render(f"Week {(i//7)+1}: ", True, (0, 0, 0))
                screen.blit(weektext, (30, 0))
                pygame.display.flip()
            # If it is good phrase and requires no input
            if(y == 1):
                key_counter += 1
                easytotal += rand_num
                totaltext = font.render(f"Your Total: {easytotal}", True, (0, 0, 255))
                screen.blit(totaltext, (30, random_offset))
                random_offset += 25
                if((i+2)%7 == 0 and (i+2) != 0):
                    easytotal += chooseIncome(1)
                    easytotal -= chooseRent(1)
            # If it is bad phrase and requires no input
            elif(y == 2):
                key_counter += 1
                easytotal -= rand_num
                totaltext = font.render(f"Your Total: {easytotal}", True, (0, 0, 255))
                screen.blit(totaltext, (30, random_offset))
                random_offset += 25
                if((i+2)%7 == 0 and (i+2) != 0):
                    easytotal += chooseIncome(1)
                    easytotal -= chooseRent(1)
            # If it is phrase that requires input
            elif(y == 3):
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN:
                        # Y key is pressed
                        if event.key == pygame.K_y:
                            key_counter += 1
                            easytotal -= rand_num
                            totaltext = font.render(f"Your Total: {easytotal}", True, (0, 0, 255))
                            screen.blit(totaltext, (30, random_offset))
                            random_offset += 25
                            # if it is the end of the week 
                            if((i+2)%7 == 0 and (i+2) != 0):
                                easytotal += chooseIncome(1)
                                easytotal -= chooseRent(1)
                            break
                        # N key is pressed
                        elif event.key == pygame.K_n:
                            key_counter += 1
                            totaltext = font.render(f"Your Total: {easytotal}", True, (0, 0, 255))
                            screen.blit(totaltext, (30, random_offset))
                            random_offset += 25
                            # if it is the end of the week 
                            if((i+2)%7 == 0 and (i+2) != 0):
                                easytotal += chooseIncome(1)
                                easytotal -= chooseRent(1)
                            break
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
            if(i==27):
                if(easytotal>1000):
                    finaltext = font.render("You finished with more than what you started with!", True, (0, 255, 0)) 
                    screen.blit(finaltext, (30, random_offset))
                elif(easytotal<1000 and easytotal>0):
                    finaltext = font.render("You finished with less than what you started with!", True, (255, 0, 0))
                    screen.blit(finaltext, (30, random_offset))
                elif(easytotal<0):
                    finaltext = font.render("You finished and you are in debt :(", True, (255, 0, 0))                 
                    screen.blit(finaltext, (30, random_offset))          
        

    elif difficulty == "medium":
        text = font.render("Medium selected!", True, (0, 0, 0))
        screen.blit(text, (30, 150))
        incometext = font.render("Your income is $750 a week", True, (0, 0, 0))
        screen.blit(incometext, (30, 170))
        renttext = font.render("Your rent is $150 a week", True, (0, 0, 0))
        screen.blit(renttext, (30, 190))
        weektext = font.render("Week 1: ", True, (0, 0, 0))
        screen.blit(weektext, (30, 210))
        random_offset = 230
        for i in range(28):
            while True: 
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        phrase, rand_num, y = generate_random_phrase(2)
                        break
            randomtext = font.render(f"{phrase} - Value: {rand_num}", True, (0, 0, 0))
            screen.blit(randomtext, (30, random_offset))
            random_offset += 25
            pygame.display.flip()
            # refresh screen to blank
            if(key_counter%7 == 0 and key_counter != 0):
                white = (255, 255, 255)
                screen.fill(white)
                random_offset = 20
                weektext = font.render(f"Week {(i//7)+1}: ", True, (0, 0, 0))
                screen.blit(weektext, (30, 0))
                pygame.display.flip()
            if(y == 1):
                key_counter += 1
                mediumtotal += rand_num
                totaltext = font.render(f"Your Total: {mediumtotal}", True, (0, 0, 255))
                screen.blit(totaltext, (30, random_offset))
                random_offset += 25
                if((i+2)%7 == 0 and (i+2) != 0):
                    mediumtotal += chooseIncome(2)
                    mediumtotal -= chooseRent(2)
            elif(y == 2):
                key_counter += 1
                mediumtotal -= rand_num
                totaltext = font.render(f"Your Total: {mediumtotal}", True, (0, 0, 255))
                screen.blit(totaltext, (30, random_offset))
                random_offset += 25
                if((i+2)%7 == 0 and (i+2) != 0):
                    mediumtotal += chooseIncome(2)
                    mediumtotal -= chooseRent(2)
            elif(y == 3):
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            key_counter += 1
                            mediumtotal -= rand_num
                            totaltext = font.render(f"Your Total: {mediumtotal}", True, (0, 0, 255))
                            screen.blit(totaltext, (30, random_offset))
                            random_offset += 25
                            if((i+2)%7 == 0 and (i+2) != 0):
                                mediumtotal += chooseIncome(2)
                                mediumtotal -= chooseRent(2)
                            break
                        elif event.key == pygame.K_n:
                            key_counter += 1
                            totaltext = font.render(f"Your Total: {mediumtotal}", True, (0, 0, 255))
                            screen.blit(totaltext, (30, random_offset))
                            random_offset += 25
                            if((i+2)%7 == 0 and (i+2) != 0):
                                mediumtotal += chooseIncome(2)
                                mediumtotal -= chooseRent(2)
                            break
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
            if(i==27):
                if(mediumtotal>1000):
                    finaltext = font.render("You finished with more than what you started with!", True, (0, 255, 0)) 
                    screen.blit(finaltext, (30, random_offset))
                elif(mediumtotal<1000 and mediumtotal>0):
                    finaltext = font.render("You finished with less than what you started with!", True, (255, 0, 0))
                    screen.blit(finaltext, (30, random_offset))
                elif(mediumtotal<0):
                    finaltext = font.render("You finished and you are in debt :(", True, (255, 0, 0))                 
                    screen.blit(finaltext, (30, random_offset))                                

    elif difficulty == "hard":
        text = font.render("Hard selected!", True, (0, 0, 0))
        screen.blit(text, (30, 150))
        incometext = font.render("Your income is $500 a week", True, (0, 0, 0))
        screen.blit(incometext, (30, 170))
        renttext = font.render("Your rent is $200 a week", True, (0, 0, 0))
        screen.blit(renttext, (30, 190))
        weektext = font.render("Week 1: ", True, (0, 0, 0))
        screen.blit(weektext, (30, 210))
        random_offset = 230
        for i in range(28):
            while True: 
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        phrase, rand_num, y = generate_random_phrase(1)
                        break
            randomtext = font.render(f"{phrase} - Value: {rand_num}", True, (0, 0, 0))
            screen.blit(randomtext, (30, random_offset))
            random_offset += 25
            pygame.display.flip()
            # refresh screen to blank
            if(key_counter%7 == 0 and key_counter != 0):
                white = (255, 255, 255)
                screen.fill(white)
                random_offset = 20
                weektext = font.render(f"Week {(i//7)+1}: ", True, (0, 0, 0))
                screen.blit(weektext, (30, 0))
                pygame.display.flip()
            if(y == 1):
                key_counter += 1
                hardtotal += rand_num
                totaltext = font.render(f"Your Total: {hardtotal}", True, (0, 0, 255))
                screen.blit(totaltext, (30, random_offset))
                random_offset += 25
                if((i+2)%7 == 0 and (i+2) != 0):
                    hardtotal += chooseIncome(3)
                    hardtotal -= chooseRent(3)
            elif(y == 2):
                key_counter += 1
                hardtotal -= rand_num
                totaltext = font.render(f"Your Total: {hardtotal}", True, (0, 0, 255))
                screen.blit(totaltext, (30, random_offset))
                random_offset += 25
                if((i+2)%7 == 0 and (i+2) != 0):
                    hardtotal += chooseIncome(3)
                    hardtotal -= chooseRent(3)
            elif(y == 3):
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            key_counter += 1
                            hardtotal -= rand_num
                            totaltext = font.render(f"Your Total: {hardtotal}", True, (0, 0, 255))
                            screen.blit(totaltext, (30, random_offset))
                            random_offset += 25
                            if((i+2)%7 == 0 and (i+2) != 0):
                                hardtotal += chooseIncome(3)
                                hardtotal -= chooseRent(3)
                            break
                        elif event.key == pygame.K_n:
                            key_counter += 1
                            totaltext = font.render(f"Your Total: {hardtotal}", True, (0, 0, 255))
                            screen.blit(totaltext, (30, random_offset))
                            random_offset += 25
                            if((i+2)%7 == 0 and (i+2) != 0):
                                hardtotal += chooseIncome(3)
                                hardtotal -= chooseRent(3)
                            break
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
            if(i==27):
                if(hardtotal>1000):
                    finaltext = font.render("You finished with more than what you started with!", True, (0, 255, 0)) 
                    screen.blit(finaltext, (30, random_offset))
                elif(hardtotal<1000 and hardtotal>0):
                    finaltext = font.render("You finished with less than what you started with!", True, (255, 0, 0))
                    screen.blit(finaltext, (30, random_offset))
                elif(hardtotal<0):
                    finaltext = font.render("You finished and you are in debt :(", True, (255, 0, 0))                 
                    screen.blit(finaltext, (30, random_offset))     


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
