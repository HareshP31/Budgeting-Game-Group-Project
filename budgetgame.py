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
# Run the game through easy mode
def easyMode():
    print("Choose a salary")
    income = chooseIncome(1)
    rent = chooseRent(1)
    
# Run the game through medium mode
def mediumMode():
    print("Choose a salary")
    income = chooseIncome(2)
    rent = chooseRent(2)
# Run the game through hard mode
def hardMode():
    print("Choose a salary")
    income = chooseIncome(3)
    rent = chooseRent(3)
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
    if r==1:
        return 150
    if r==2:
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

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption("Difficulty Selection")

    font = pygame.font.SysFont("comic sans", 20)

    running = True
    difficulty = None

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
        text = font.render("Easy selected!", True, (0, 0, 0))
        screen.blit(text, (30, 150))
        incometext = font.render("Your income is $1,000 a week", True, (0, 0, 0))
        screen.blit(incometext, (30, 170))
        renttext = font.render("Your rent is $150 a week", True, (0, 0, 0))
        screen.blit(renttext, (30, 190))
        random_number = generate_random_number(1)
        randomtext = font.render(f"Random number: {random_number}", True, (0, 0, 0))
        screen.blit(randomtext, (30, 210))

    elif difficulty == "medium":
        text = font.render("Medium selected!", True, (0, 0, 0))
        screen.blit(text, (30, 150))
        incometext = font.render("Your income is $750 a week", True, (0, 0, 0))
        screen.blit(incometext, (30, 170))
        renttext = font.render("Your rent is $150 a week", True, (0, 0, 0))
        screen.blit(renttext, (30, 190))
        random_number = generate_random_number(2)
        randomtext = font.render(f"Random number: {random_number}", True, (0, 0, 0))
        screen.blit(randomtext, (30, 210))
    elif difficulty == "hard":
        text = font.render("Hard selected!", True, (0, 0, 0))
        screen.blit(text, (30, 150))
        incometext = font.render("Your income is $500 a week", True, (0, 0, 0))
        screen.blit(incometext, (30, 170))
        renttext = font.render("Your rent is $200 a week", True, (0, 0, 0))
        screen.blit(renttext, (30, 190))
        random_number = generate_random_number(3)
        randomtext = font.render(f"Random number: {random_number}", True, (0, 0, 0))
        screen.blit(randomtext, (30, 210))

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
