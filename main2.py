import pygame
import pygame_menu
import sys
from Jugador import Jugador
from botones import Boton
from tablero2 import Tablero
from fichasGrafica import FichasGrafica

AZUL = (0, 25, 139)
AZULCLARO = (0, 40, 150)
NEGRO = (0, 0, 0)
ancho = 600
alto = 700
screen = pygame.display.set_mode((ancho, alto))
BLANCO = (255, 255, 255)

pygame.init()

tablero = Tablero(screen)
boton1 = Boton("Colocar", (85), (alto - 50), 100, 40, AZUL, AZULCLARO, accion=None)
boton2 = Boton("CambiarF", (85 + 110), (alto - 50), 100, 40, AZUL, AZULCLARO, accion=None)
boton3 = Boton("Pasar Turno", (195 + 110), (alto - 50), 100, 40, AZUL, AZULCLARO, accion=None)
boton4 = Boton("Deshacer", (305 + 110), (alto - 50), 100, 40, AZUL, AZULCLARO, accion=None)

fichasgraphic = FichasGrafica(screen, ancho, alto, 120, 605)
ficha_seleccionada = None
ListaTemp = []


def ListarJugadores():
    ListaJugadores = []
    for i in range(2):
        jugador = Jugador()
        ListaJugadores.append(jugador)
    return ListaJugadores


def accion_boton_deshacer(screen, jugador: Jugador):
    pass


def accion_boton_pasar_turno(screen, jugador: Jugador):
    pass


def start_the_game():
    listaJugadores = ListarJugadores()
    indice_jugador_actual = 0
    global ficha_seleccionada
    global ListaTemp

    while True:
        tablero.dibujar()
        boton1.dibujar(screen)
        boton2.dibujar(screen)
        boton3.dibujar(screen)
        boton4.dibujar(screen)

        jugador_actual: Jugador = listaJugadores[indice_jugador_actual]
        ListaTemp = fichasgraphic.dibujar(indice_jugador_actual, jugador_actual.ListFichaJ, (40, 40))

        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEMOTION:
                if boton3.rect.collidepoint(evento.pos):
                    boton3.color_actual = boton3.color_resaltado
                else:
                    boton3.color_actual = boton3.color_normal

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = evento.pos
                ficha_rect, ficha = fichasgraphic.detectar_ficha(pos)
                if ficha_rect:
                    fichasgraphic.ficha_seleccionada = (ficha_rect, ficha)
                    fichasgraphic.offset_x = pos[0] - ficha_rect.x
                    fichasgraphic.offset_y = pos[1] - ficha_rect.y

                if boton3.rect.collidepoint(evento.pos):
                    indice_jugador_actual = (indice_jugador_actual + 1) % len(listaJugadores)
                elif boton4.rect.collidepoint(evento.pos):
                    accion_boton_deshacer(tablero.ventana, jugador_actual)

            elif evento.type == pygame.MOUSEMOTION:
                if fichasgraphic.ficha_seleccionada:
                    pos = pygame.mouse.get_pos()
                    fichasgraphic.mover_ficha(pos)

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


Menu_screen = pygame.display.set_mode((600, 700))

pygame.display.set_caption("Menu_Scrabble")

apariencia = pygame_menu.Theme(
    background_color=(0, 0, 128),
    title_background_color=(0, 0, 0),
    title_font_shadow=True,
    title_font=pygame_menu.font.FONT_BEBAS,
    widget_font=pygame_menu.font.FONT_FRANCHISE,
    widget_font_color=(255, 255, 255),
    widget_margin=(0, 30),
    selection_color=(255, 165, 0)
)

menu = pygame_menu.Menu('SCRABBLE_Menu', 600, 700, theme=apariencia)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
while True:
    Menu_screen.fill(NEGRO)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if menu.is_enabled():
        menu.update(events)
        menu.draw(Menu_screen)
    pygame.display.flip()
