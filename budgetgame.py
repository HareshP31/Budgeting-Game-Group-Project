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
            if event.key == pygame.K_e:
                return "easy"
            elif event.key == pygame.K_m:
                return "medium"
            elif event.key == pygame.K_h:
                return "hard"
            else:
                print("Please enter 'e', 'm', or 'h'")

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

        pygame.display.flip()

        # Check for events
        difficulty = handle_events()
        if difficulty:
            break

    if difficulty == "easy":
        easy()
    elif difficulty == "medium":
        medium()
    elif difficulty == "hard":
        hard()

    pygame.quit()

def easy():
    print("Easy selected")

def medium():
    print("Medium selected")

def hard():
    print("Hard selected")

main()