import pygame
import math
import random
import time, os.path
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

def generate_random_phrase(b):
    phrases = [
    "Your pet fell ill recently. The cost to see the vet is:",
    "Your child is going on a school field trip to the Grand Canyon. She’s been wanting to go for the longest time and the cost is:",
    "You were brushing your teeth in the bathroom when you suddenly felt a drop on your face. Your roof is leaking! To fix it costs:",
    "Your child's school is hosting a fundraising event, and the suggested donation is:",
    "Your laptop screen cracked, and replacing it will cost:",
    "Your water heater malfunctioned, and fixing it will cost:",
    "You fell down the stairs and possibly twisted your ankle. A doctor visit costs:",
    "Your car broke down and towing it will cost:",
    "Your refrigerator stopped working and it will cost:",
    "You just got a bonus! Worth:",
    "Your daughter got a full ride to her dream college and financial aid worth:",
    "It is the holiday season! You got a gift card worth:",
    "Congratulations! You won a contest and received groceries worth:",
    "Great news! Your utility bills decreased this month due to energy-saving improvements by:",
    "Your job gave you a bonus for working overtime. Worth:",
    "Lucky day! Your insurance rewarded you for safe driving with:",
    "You received a tax refund from overpaid taxes last year. Worth:",
    "A friend paid you back after they owed you for a long time. Worth:",
    "Your favorite store is having a clearance sale, and you saved:"
    ]

    if b == 1:
        random_number = random.randint(100, 200)
    elif b == 2:
        random_number = random.randint(300, 400)
    elif b == 3:
        random_number = random.randint(500, 600)
    phrase = random.choice(phrases)
    return phrase, random_number

def main():
    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption("Difficulty Selection")

    font = pygame.font.SysFont("comic sans", 20)

    running = True
    difficulty = None
    key_counter = 0

    while running:
        screen.fill((255, 255, 255))
        
        # Display instructions
        instructions = font.render("Type 'e' for Easy, 'm' for Medium, 'h' for Hard", True, (0, 0, 0))
        screen.blit(instructions, (30, 100))

        # Check for events
        difficulty = handle_events()
        if difficulty:
            break

        pygame.display.flip()

    if difficulty == "easy":
        easytotal = 1000
        text = font.render("Easy selected!", True, (0, 0, 0))
        screen.blit(text, (30, 150))
        incometext = font.render("Your income is $1,000 a week", True, (0, 0, 0))
        screen.blit(incometext, (30, 170))
        renttext = font.render("Your rent is $150 a week", True, (0, 0, 0))
        screen.blit(renttext, (30, 190))
        weektext = font.render("Week 1: ", True, (0, 0, 0))
        screen.blit(weektext, (30, 210))
        random_offset = 230
        for i in range(28):
            phrase, rand_num = generate_random_phrase(1)
            randomtext = font.render(f"{phrase} - Value: {rand_num}", True, (0, 0, 0))
            screen.blit(randomtext, (30, random_offset))
            random_offset += 25
            pygame.display.flip()
            if(key_counter%7 == 0 and key_counter != 0):
                white = (255, 255, 255)
                screen.fill(white)
                random_offset = 20
                weektext = font.render(f"Week {(i//7)+1}: ", True, (0, 0, 0))
                screen.blit(weektext, (30, 0))
                pygame.display.flip()
            while True:
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        key_counter += 1
                        easytotal += rand_num
                        totaltext = font.render(f"Your Total: {easytotal}", True, (0, 0, 0))
                        screen.blit(totaltext, (30, random_offset))
                        random_offset += 25
                        if((i+2)%7 == 0 and (i+2) != 0):
                            easytotal += chooseIncome(1)
                            easytotal -= chooseRent(1)
                        break
                    elif event.key == pygame.K_n:
                        key_counter += 1
                        totaltext = font.render(f"Your Total: {easytotal}", True, (0, 0, 0))
                        screen.blit(totaltext, (30, random_offset))
                        random_offset += 25
                        if((i+2)%7 == 0 and (i+2) != 0):
                            easytotal += chooseIncome(1)
                            easytotal -= chooseRent(1)
                        break
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
        

    elif difficulty == "medium":
        mediumtotal = 750
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
            phrase, rand_num = generate_random_phrase(2)
            randomtext = font.render(f"{phrase} - Value: {rand_num}", True, (0, 0, 0))
            screen.blit(randomtext, (30, random_offset))
            random_offset += 25
            pygame.display.flip()
            if(key_counter%7 == 0 and key_counter != 0):
                white = (255, 255, 255)
                screen.fill(white)
                random_offset = 20
                weektext = font.render(f"Week {(i//7)+1}: ", True, (0, 0, 0))
                screen.blit(weektext, (30, 0))
                pygame.display.flip()
            while True:
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        key_counter += 1
                        mediumtotal += rand_num
                        totaltext = font.render(f"Your Total: {mediumtotal}", True, (0, 0, 0))
                        screen.blit(totaltext, (30, random_offset))
                        random_offset += 25
                        if((i+2)%7 == 0 and (i+2) != 0):
                            mediumtotal += chooseIncome(1)
                            mediumtotal -= chooseRent(1)
                        break
                    elif event.key == pygame.K_n:
                        key_counter += 1
                        totaltext = font.render(f"Your Total: {mediumtotal}", True, (0, 0, 0))
                        screen.blit(totaltext, (30, random_offset))
                        random_offset += 25
                        if((i+2)%7 == 0 and (i+2) != 0):
                            mediumtotal += chooseIncome(1)
                            mediumtotal -= chooseRent(1)
                        break
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    elif difficulty == "hard":
        hardtotal = 500
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
            phrase, rand_num = generate_random_phrase(3)
            randomtext = font.render(f"{phrase} - Value: {rand_num}", True, (0, 0, 0))
            screen.blit(randomtext, (30, random_offset))
            random_offset += 25
            pygame.display.flip()
            if(key_counter%7 == 0 and key_counter != 0):
                white = (255, 255, 255)
                screen.fill(white)
                random_offset = 20
                weektext = font.render(f"Week {(i//7)+1}: ", True, (0, 0, 0))
                screen.blit(weektext, (30, 0))
                pygame.display.flip()
            while True:
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        key_counter += 1
                        hardtotal += rand_num
                        totaltext = font.render(f"Your Total: {hardtotal}", True, (0, 0, 0))
                        screen.blit(totaltext, (30, random_offset))
                        random_offset += 25
                        if((i+2)%7 == 0 and (i+2) != 0):
                            hardtotal += chooseIncome(1)
                            hardtotal -= chooseRent(1)
                        break
                    elif event.key == pygame.K_n:
                        key_counter += 1
                        totaltext = font.render(f"Your Total: {hardtotal}", True, (0, 0, 0))
                        screen.blit(totaltext, (30, random_offset))
                        random_offset += 25
                        if((i+2)%7 == 0 and (i+2) != 0):
                            hardtotal += chooseIncome(1)
                            hardtotal -= chooseRent(1)
                        break
                    elif event.key == pygame.K_ESCAPE:
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
