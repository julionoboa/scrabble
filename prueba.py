import random
import os

class Scrabble:
    def __init__(self):
        self.board = [[" " for _ in range(15)] for _ in range(15)]
        self.letters = list("AAAAAAAEEEEEEIIIOOOUUBBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUUVVWWXXYYZZ  ")
        random.shuffle(self.letters)
        self.players = []
        self.actual_turn = 0
        self.scores = []
        self.first_move = True

        self.letter_values = {
            "A": 1, "B": 3, "C": 3, "D": 2, "E": 1,
            "F": 4, "G": 2, "H": 4, "I": 1, "J": 8,
            "K": 5, "L": 1, "M": 3, "N": 1, "O": 1,
            "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1,
            "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10, " ": 0
        }

        self.special_squares = {
            (0, 0): "TW", (0, 7): "TW", (0, 14): "TW",
            (7, 0): "TW", (7, 14): "TW",
            (14, 0): "TW", (14, 7): "TW", (14, 14): "TW",
            (1, 1): "DW", (2, 2): "DW", (3, 3): "DW", (4, 4): "DW",
            (10, 10): "DW", (11, 11): "DW", (12, 12): "DW", (13, 13): "DW",
            (1, 13): "DW", (2, 12): "DW", (3, 11): "DW", (4, 10): "DW",
            (10, 4): "DW", (11, 3): "DW", (12, 2): "DW", (13, 1): "DW",
            (1, 5): "TL", (1, 9): "TL", (5, 1): "TL", (5, 5): "TL",
            (5, 9): "TL", (5, 13): "TL", (9, 1): "TL", (9, 5): "TL",
            (9, 9): "TL", (9, 13): "TL", (13, 5): "TL", (13, 9): "TL",
            (0, 3): "DL", (0, 11): "DL", (2, 6): "DL", (2, 8): "DL",
            (3, 0): "DL", (3, 7): "DL", (3, 14): "DL", (6, 2): "DL",
            (6, 6): "DL", (6, 8): "DL", (6, 12): "DL", (7, 3): "DL",
            (7, 11): "DL", (8, 2): "DL", (8, 6): "DL", (8, 8): "DL",
            (8, 12): "DL", (11, 0): "DL", (11, 7): "DL", (11, 14): "DL",
            (12, 6): "DL", (12, 8): "DL", (14, 3): "DL", (14, 11): "DL"
        }

    def add_player(self, name):
        tiles = self.draw_tiles(7)
        self.players.append({"name": name, "tiles": tiles})
        self.scores.append(0)

    def draw_tiles(self, num):
        tiles = []
        for _ in range(num):
            if self.letters:
                tiles.append(self.letters.pop())
        return tiles

    def start_game(self):
        for player in self.players:
            print(f"Fichas de {player['name']}: {', '.join(player['tiles'])}")

    def display_board(self):
        print("   " + "  ".join([str(i).zfill(2) for i in range(15)]))
        print("  +" + "---+" * 15)
        for idx, row in enumerate(self.board):
            print(str(idx).zfill(2) + " | " + " | ".join(row) + " |")
            print("  +" + "---+" * 15)

    def calculate_word_score(self, word, row, col, direction):
        word_score = 0
        word_multiplier = 1

        if direction == 'horizontal':
            for i, letter in enumerate(word):
                if letter == " ":
                    continue
                letter_value = self.letter_values[letter]
                letter_row, letter_col = row, col + i

                if (letter_row, letter_col) in self.special_squares:
                    square = self.special_squares[(letter_row, letter_col)]
                    if square == "DL":
                        letter_value *= 2
                    elif square == "TL":
                        letter_value *= 3
                    elif square == "DW":
                        word_multiplier *= 2
                    elif square == "TW":
                        word_multiplier *= 3

                word_score += letter_value
        else:
            for i, letter in enumerate(word):
                if letter == " ":
                    continue
                letter_value = self.letter_values[letter]
                letter_row, letter_col = row + i, col

                if (letter_row, letter_col) in self.special_squares:
                    square = self.special_squares[(letter_row, letter_col)]
                    if square == "DL":
                        letter_value *= 2
                    elif square == "TL":
                        letter_value *= 3
                    elif square == "DW":
                        word_multiplier *= 2
                    elif square == "TW":
                        word_multiplier *= 3

                word_score += letter_value

        return word_score * word_multiplier

    def place_word(self, player_idx, word, row, col, direction):
        player_tiles = self.players[player_idx]['tiles']

        # Validar que la palabra usa solo letras disponibles en las fichas del jugador
        while not all(word.count(letter) <= player_tiles.count(letter) for letter in word):
            print("¡Palabra inválida! Contiene letras que no tienes.")
            word = input("Ingresa una palabra válida: ").upper()

        # Validar la dirección hasta que sea correcta
        while direction not in ['horizontal', 'vertical', 'h', 'v']:
            print("¡Dirección inválida! Usa 'horizontal' o 'vertical'.")
            direction = input("Ingresa la dirección nuevamente (horizontal/vertical/h/v): ").lower()

        if self.first_move:
            # Verificar si la palabra pasa por el centro del tablero (7,7)
            if not ((direction in ['horizontal', 'h'] and col <= 7 < col + len(word)) or
                    (direction in ['vertical', 'v'] and row <= 7 < row + len(word))):
                print("La primera palabra debe pasar por el centro del tablero.")
                return False

        # Verificar si la palabra cabe en el tablero
        if (direction in ['horizontal', 'h'] and col + len(word) > 15) or (
                direction in ['vertical', 'v'] and row + len(word) > 15):
            print("¡La palabra no cabe en el tablero!")
            return False

        # Verificar si hay conflictos con letras existentes en el tablero
        if direction in ['horizontal', 'h']:
            for i, letter in enumerate(word):
                if self.board[row][col + i] not in [' ', letter]:
                    print("¡La palabra entra en conflicto con letras en el tablero!")
                    return False
        else:
            for i, letter in enumerate(word):
                if self.board[row + i][col] not in [' ', letter]:
                    print("¡La palabra entra en conflicto con letras en el tablero!")
                    return False

        # Colocar la palabra en el tablero
        if direction in ['horizontal', 'h']:
            for i, letter in enumerate(word):
                self.board[row][col + i] = letter
        else:
            for i, letter in enumerate(word):
                self.board[row + i][col] = letter

        # Calcular y actualizar puntaje
        word_score = self.calculate_word_score(word, row, col, direction)
        self.scores[player_idx] += word_score
        self.first_move = False

        # Remover fichas usadas y reponer nuevas
        for letter in word:
            if letter in player_tiles:
                player_tiles.remove(letter)
            elif " " in player_tiles:  # Permitir uso de fichas en blanco como comodín
                player_tiles.remove(" ")

        new_tiles = self.draw_tiles(7 - len(player_tiles))
        self.players[player_idx]['tiles'].extend(new_tiles)

        return True

    def change_tiles(self, player_idx):
        player_tiles = self.players[player_idx]['tiles']
        print(f"Tus fichas actuales: {', '.join(player_tiles)}")
        tiles_to_change = input("Ingresa las letras que deseas cambiar (sin espacios, por ejemplo, 'AEIOU'): ").upper()

        if not all(letter in player_tiles or letter == " " for letter in tiles_to_change):
            print("Algunas de las letras ingresadas no están en tus fichas.")
            return False

        # Remove the specified tiles from the player's hand
        for letter in tiles_to_change:
            if letter in player_tiles:
                player_tiles.remove(letter)
            elif " " in player_tiles:
                player_tiles.remove(" ")  # Tratar fichas en blanco como cualquier letra
            self.letters.append(letter)

        # Shuffle the letter bag and draw new tiles
        random.shuffle(self.letters)
        new_tiles = self.draw_tiles(len(tiles_to_change))
        player_tiles.extend(new_tiles)

        return True

    def next_turn(self):
        self.actual_turn = (self.current_turn + 1) % len(self.players)

    def play_game(self):
        self.start_game()
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.display_board()
            current_player = self.players[self.current_turn]
            print(f"Turno de {current_player['name']}!")
            print(f"Fichas restantes: {', '.join(current_player['tiles'])}")

            # Asegurar que la entrada sea válida
            while True:
                action = input("Elige una acción: (1) Colocar palabra (2) Cambiar letras (3) Pasar turno: ")

                if action.isdigit():  # Verifica si es un número
                    action = int(action)
                    if 1 <= action <= 3:  # Solo acepta 1, 2 o 3
                        break
                    else:
                        print("Número fuera de rango. Debe ser 1, 2 o 3.")
                else:
                    print("Entrada inválida. Debes ingresar un número (1, 2 o 3).")

            # Ejecutar la acción seleccionada
            if action == 1:
                word = input("Ingresa la palabra a colocar: ").upper()
                row = int(input("Ingresa la fila (0-14): "))
                col = int(input("Ingresa la columna (0-14): "))
                direction = input("Ingresa la dirección (horizontal/vertical): ").lower()

                if self.place_word(self.current_turn, word, row, col, direction):
                    print(f"¡Palabra colocada exitosamente por {current_player['name']}!")
                    self.scores[self.current_turn] += 50 if len(word) == 7 else 0  # Bonus por usar todas las fichas
                else:
                    print("No se pudo colocar la palabra.")
            elif action == 2:
                if not self.change_tiles(self.current_turn):
                    print("No se pudieron cambiar las letras.")
            elif action == 3:
                print(f"{current_player['name']} pasa su turno.")

            # **Cambio de turno**
            self.actual_turn = (self.actual_turn + 1) % len(self.players)

            # Opción para salir del juego
            if input("Escribe 'salir' para terminar el juego o presiona Enter para continuar: ").lower() == 'salir':
                break

        self.end_game()

    def end_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("¡Juego terminado!")
        for i, player in enumerate(self.players):
            print(f"Puntaje de {player['name']}: {self.scores[i]}")
        winner = self.players[self.scores.index(max(self.scores))]['name']
        print(f"El ganador es {winner}!")

# Inicializando el juego
game = Scrabble()
game.add_player("Jugador 1")
game.add_player("Jugador 2")
game.play_game()

