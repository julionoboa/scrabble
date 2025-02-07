import pygame
import time

# Colores:
MOSTAZA = (247, 181, 131)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

dimension = 7
ancho = 40
alto = 40

screen = pygame.display.set_mode((600, 700))

ListaPrueba = ["A", "B", "C", "D", "E", "F", "G"]


class FichasGrafica:
    def __init__(self, ventana, width, height, x, y):
        self.ventana = ventana
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = MOSTAZA
        self.fichas_rects = []
        self.ficha_seleccionada = None
        self.offset_x = 0
        self.offset_y = 0

    def dibujar(self, indice_actual, ListaFichasJ, ficha_size):
        self.fichas_rects.clear()
        x_offset = self.x
        y_offset = self.y

        for ficha in ListaFichasJ:
            ficha_rect = pygame.Rect(x_offset, y_offset, ficha_size[0], ficha_size[1])
            self.fichas_rects.append((ficha_rect, ficha))
            pygame.draw.rect(self.ventana, self.color, ficha_rect)

            # Borde negro
            pygame.draw.rect(self.ventana, NEGRO, ficha_rect, 1)

            font = pygame.font.SysFont(None, 30)
            text = font.render(ficha, True, NEGRO)
            text_rect = text.get_rect(center=(x_offset + ficha_size[0] // 2, y_offset + ficha_size[1] // 2))
            self.ventana.blit(text, text_rect)

            x_offset += ficha_size[0] + 10

        if indice_actual == 0:
            font = pygame.font.Font(None, 30)
            win_text = font.render("J-1", True, NEGRO)
            size = win_text.get_rect(center=(100, 622))
            self.ventana.blit(win_text, size)
        elif indice_actual == 1:
            font = pygame.font.Font(None, 30)
            win_text = font.render("J-2", True, NEGRO)
            size = win_text.get_rect(center=(100, 622))
            self.ventana.blit(win_text, size)

        pygame.display.flip()

    def detectar_ficha(self, pos):
        for ficha_rect, ficha in self.fichas_rects:
            if ficha_rect.collidepoint(pos):
                return ficha_rect, ficha
        return None, None

    def mover_ficha(self, pos):
        if self.ficha_seleccionada:
            self.ficha_seleccionada[0].x = pos[0] - self.offset_x
            self.ficha_seleccionada[0].y = pos[1] - self.offset_y


if __name__ == "__main__":
    pygame.init()
    screen.fill(BLANCO)
    Fichagraf = FichasGrafica(screen, ancho, alto, 120, 600)
    Fichagraf.dibujar(0, ListaPrueba, (40, 40))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                ficha_rect, ficha = Fichagraf.detectar_ficha(pos)
                if ficha_rect:
                    Fichagraf.ficha_seleccionada = (ficha_rect, ficha)
                    Fichagraf.offset_x = pos[0] - ficha_rect.x
                    Fichagraf.offset_y = pos[1] - ficha_rect.y

            elif event.type == pygame.MOUSEBUTTONUP:
                Fichagraf.ficha_seleccionada = None

            elif event.type == pygame.MOUSEMOTION:
                if Fichagraf.ficha_seleccionada:
                    pos = pygame.mouse.get_pos()
                    Fichagraf.mover_ficha(pos)
                    screen.fill(BLANCO)
                    Fichagraf.dibujar(0, [ficha for _, ficha in Fichagraf.fichas_rects], (40, 40))

        pygame.display.flip()
    pygame.quit()
