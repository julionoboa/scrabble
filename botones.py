import pygame
import time

BLANCO = (255, 255, 255)
AZUL = (0, 25, 139)
AZULCLARO = (0, 20, 130)
NEGRO = (0, 0, 0)
screen = pygame.display.set_mode((600, 650))


class Boton:
    def __init__(self, texto, x, y, ancho, alto, color_normal, color_resaltado, accion=None):
        self.texto = texto
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color_normal = color_normal
        self.color_resaltado = color_resaltado
        self.color_actual = color_normal
        self.accion = accion

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color_actual, self.rect)
        font = pygame.font.SysFont(None, 26)
        texto = font.render(self.texto, True, BLANCO)
        text_rect = texto.get_rect(center=self.rect.center)
        pantalla.blit(texto, text_rect)


if __name__ == "__main__":
    pygame.init()
    boton = Boton("Haz clic", 300, 650, 100, 50, AZUL, AZULCLARO, accion=None)
    boton.dibujar(screen)
    pygame.display.flip()
    time.sleep(2.5)
