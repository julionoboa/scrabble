import pygame
from casillaTablero import casillaTablero
from botones import Boton
import time
import sys

# Define colors
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS_CLARO = (230, 230, 230)
ROJO = (236, 4, 0)
AZUL = (0, 22, 142)
VERDE = (76, 194, 194)
MOSTAZA = (247, 181, 131)

NUM_BONUS_TRIPLE_PALABRA = 3
NUM_BONUS_DOBLE_PALABRA = 2
NUM_BONUS_TRIPLE_LETRA = 3
NUM_BONUS_DOBLE_LETRA = 2

# Bonus positions
BONUS_TRIPLE_PALABRA = [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)]
BONUS_DOBLE_PALABRA = [(1, 1), (2, 2), (3, 3), (4, 4), (7, 7), (10, 10), (11, 11), (12, 12), (13, 13), (1, 13), (2, 12),
                       (3, 11), (4, 10), (10, 4), (11, 3), (12, 2), (13, 1)]
BONUS_TRIPLE_LETRA = [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5),
                      (13, 9)]
BONUS_DOBLE_LETRA = [(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3),
                     (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3),
                     (14, 11)]

screen = pygame.display.set_mode((600, 700))


class Tablero:
    def __init__(self, screen):
        pygame.init()
        self.ventana = screen
        self.dimens = 15
        self.t_celda = 600 // self.dimens

    def dibujar(self):
        self.ventana.fill(BLANCO)

        # boton = Boton("Deshacer", 320, 620, 120, 50, AZUL, BLANCO, accion=None)
        # boton.dibujar(self.ventana)

        for fila in range(self.dimens):
            for col in range(self.dimens):
                color = GRIS_CLARO
                numero = None
                if (fila, col) in BONUS_TRIPLE_PALABRA:
                    color = ROJO
                    numero = NUM_BONUS_TRIPLE_PALABRA
                elif (fila, col) in BONUS_DOBLE_PALABRA:
                    color = MOSTAZA
                    numero = NUM_BONUS_DOBLE_PALABRA
                elif (fila, col) in BONUS_TRIPLE_LETRA:
                    color = AZUL
                    numero = NUM_BONUS_TRIPLE_LETRA
                elif (fila, col) in BONUS_DOBLE_LETRA:
                    color = VERDE
                    numero = NUM_BONUS_DOBLE_LETRA

                casilla = casillaTablero(self.t_celda, self.t_celda, col * self.t_celda, fila * self.t_celda)
                pygame.draw.rect(self.ventana, color, casilla.rect)
                pygame.draw.rect(self.ventana, NEGRO, casilla.rect, 1)
                if numero is not None:
                    font = pygame.font.SysFont(None, 30)
                    text = font.render(f"x{numero}", True, BLANCO)
                    text_rect = text.get_rect(center=(self.t_celda * col + self.t_celda // 2,
                                                      self.t_celda * fila + self.t_celda // 2))
                    self.ventana.blit(text, text_rect)

    # def ejecutar (self,boton: Boton):
    #     while True:
    #         for evento in pygame.event.get():
    #             if evento.type == pygame.QUIT:
    #                 pygame.quit()
    #         self.dibujar()
    #         boton.dibujar(self.ventana)
    #         pygame.display.flip()
    #     pygame.quit()
    #     sys.exit()


if __name__ == "__main__":
    tablero = Tablero(screen)
    tablero.dibujar()
    pygame.display.flip()
    time.sleep(2.0)

