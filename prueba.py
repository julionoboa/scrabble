import pygame_textinput
import pygame
pygame.init()

# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer()

screen = pygame.display.set_mode((600, 650))
clock = pygame.time.Clock()

while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.surface, (100, 610))

    for event in events:
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    clock.tick(30)