import pygame

MOSTAZA = (247, 181, 131)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)


class FichaSprite(pygame.sprite.Sprite):
    def __init__(self, ventana, letra,width, height, x, y ):
        super().__init__()
        self.ventana = ventana
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = MOSTAZA
        self.letra = letra
        self.dibujar()

    def dibujar(self):
        self.image.fill(self.color)
        pygame.draw.rect(self.image, NEGRO, self.rect, 1)
        font = pygame.font.SysFont(None, 30)
        text = font.render(self.letra, True, NEGRO)
        text_rect = text.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
        self.image.blit(text, text_rect)
        self.ventana.blit(self.image, self.rect.topleft)