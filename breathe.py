import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("breathe")

font = pygame.font.Font(None, 50)

text_lines = [
    "What's that supposed to be about, baby?",
    "Go free up your vibe, stop acting crazy",
    "Reminiscing on the good times daily",
    "Try and pull that, got me actin shady",
    "What's that supposed to be about, baby?",
    "Go free up your vibe, stop acting crazy",
    "You know I give you that good loving daily",
    "Try and pull that, got me actin shady"
]

RED = (255, 255, 255)
GRAY = (0, 0, 0)
STAR_COLOR = (255, 255, 255) 


x_pos = screen_width
y_pos = 300

speed = 10


line_index = 0

num_stars = 150
stars = []

for _ in range(num_stars):
    star = {
        "x": random.randint(0, screen_width),
        "y": random.randint(0, screen_height),
        "speed": random.randint(1, 3)  
    }
    stars.append(star)


running = True
while running:
    screen.fill(GRAY)  

    for star in stars:
        pygame.draw.circle(screen, STAR_COLOR, (star["x"], star["y"]), 2)

        star["y"] += star["speed"]

        if star["y"] > screen_height:
            star["y"] = 0
            star["x"] = random.randint(0, screen_width)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x_pos -= speed

    if x_pos < -300:
        x_pos = screen_width  
        line_index += 1 
        if line_index >= len(text_lines):  
            line_index = 0
    current_line = text_lines[line_index]
    text_surface = font.render(current_line, True, RED)
    screen.blit(text_surface, (x_pos, y_pos)) 
    
    pygame.display.flip()  

    pygame.time.Clock().tick(30)  

pygame.quit()
sys.exit()
