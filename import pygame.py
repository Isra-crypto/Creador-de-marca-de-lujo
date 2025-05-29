import pygame
import sys

pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Crea tu Marca de Lujo")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (212, 175, 55)
SILVER = (192, 192, 192)
CELESTE = (173, 216, 230)
GREEN = (0, 255, 0)

# Fuentes
font = pygame.font.SysFont('Times New Roman', 24)
big_font = pygame.font.SysFont('Times New Roman', 32, bold=True)

# Estados
SELECT_COLOR, SELECT_EMOTION, SELECT_SYMBOL, SELECT_STYLE, SHOW_RESULT = "color", "emotion", "symbol", "style", "result"
state = SELECT_COLOR

# Variables de selección
selected_color = None
selected_emotion = None
selected_symbol = None
selected_style = None

# Emociones por color
color_emotions = {
    "Dorado": ["Éxito", "Elegancia", "Exclusividad"],
    "Negro": ["Poder", "Misterio", "Lujo extremo"],
    "Blanco": ["Paz", "Pureza", "Sofisticación"],
    "Plateado": ["Tecnología", "Modernidad", "Frialdad elegante"],
    "Celeste diamante": ["Calma", "Sueño", "Brillo eterno"]
}

# Símbolos de lujo
luxury_symbols = ["Corona", "Diamante", "Reloj de lujo", "Auto deportivo", "Castillo"]

# Estilos de diseño
design_styles = ["Minimalista", "Clásico", "Futurista", "Artístico", "Artesanal"]

# Mensajes base
result_messages = {
    ("Dorado", "Éxito"): "Tu marca refleja el éxito alcanzado con esfuerzo y dedicación.",
    ("Dorado", "Elegancia"): "Tu marca irradia elegancia atemporal.",
    ("Dorado", "Exclusividad"): "Tu marca representa algo reservado solo para unos pocos.",
    ("Negro", "Poder"): "Una marca con carácter dominante y firmeza.",
    ("Negro", "Misterio"): "Tu marca está envuelta en un aura de misterio irresistible.",
    ("Negro", "Lujo extremo"): "Tu marca alcanza la cúspide del lujo y lo inalcanzable.",
    ("Blanco", "Paz"): "Una marca que transmite serenidad y equilibrio.",
    ("Blanco", "Pureza"): "Transparencia, claridad y belleza pura definen tu marca.",
    ("Blanco", "Sofisticación"): "Tu marca es la esencia de la sofisticación sutil.",
    ("Plateado", "Tecnología"): "Tu marca representa innovación de alto nivel.",
    ("Plateado", "Modernidad"): "Tu marca proyecta una visión de futuro estilizada.",
    ("Plateado", "Frialdad elegante"): "Tu marca mezcla distinción con precisión.",
    ("Celeste diamante", "Calma"): "Tu marca es un oasis de lujo sereno.",
    ("Celeste diamante", "Sueño"): "Tu marca inspira a alcanzar sueños altos.",
    ("Celeste diamante", "Brillo eterno"): "Una marca que brilla con luz propia."
}

# Función para crear botones
def draw_button(text, x, y, w, h, color, return_value=None):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    text_surf = font.render(text, True, BLACK)
    screen.blit(text_surf, (x + (w - text_surf.get_width()) // 2, y + (h - text_surf.get_height()) // 2))
    return rect, return_value

# Función para construir el mensaje final
def build_result_message(color, emotion, symbol, style):
    base = result_messages.get((color, emotion), "Una identidad única.")
    symbol_phrase = f" Se representa con un símbolo como un {symbol.lower()}, que evoca estatus y deseo."
    style_phrase = f" El estilo de diseño {style.lower()} transmite un enfoque visual auténtico, distintivo y aspiracional."
    return base + symbol_phrase + style_phrase

# Función para dividir texto largo
def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        test_line = line + word + " "
        if font.size(test_line)[0] <= max_width:
            line = test_line
        else:
            lines.append(line.strip())
            line = word + " "
    lines.append(line.strip())
    return lines

# Reemplaza la función draw_button con esta versión corregida
def draw_button(text, x, y, w, h, color, return_value=None):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    # Cambia el color del texto según el fondo
    text_color = WHITE if color == BLACK else BLACK

    text_surf = font.render(text, True, text_color)
    screen.blit(text_surf, (x + (w - text_surf.get_width()) // 2, y + (h - text_surf.get_height()) // 2))
    return rect, return_value

# Función principal
def main():
    global state, selected_color, selected_emotion, selected_symbol, selected_style

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        if state == SELECT_COLOR:
            title = big_font.render("1. Elige un color para tu marca", True, BLACK)
            screen.blit(title, ((800 - title.get_width()) // 2, 40))
            colors = [
                ("Dorado", GOLD),
                ("Negro", BLACK),
                ("Blanco", WHITE),
                ("Plateado", SILVER),
                ("Celeste diamante", CELESTE)
            ]
            for i, (name, color) in enumerate(colors):
                y = 120 + i * 65
                btn_rect, value = draw_button(name, 250, y, 300, 50, color, name)
                if btn_rect.collidepoint(mouse_pos) and mouse_click:
                    selected_color = value
                    state = SELECT_EMOTION
                    pygame.time.delay(200)

        elif state == SELECT_EMOTION:
            title = big_font.render(f"2. Emociones del color {selected_color}", True, BLACK)
            screen.blit(title, ((800 - title.get_width()) // 2, 40))
            emotions = color_emotions[selected_color]
            for i, emotion in enumerate(emotions):
                y = 120 + i * 55
                btn_rect, value = draw_button(emotion, 250, y, 300, 45, CELESTE, emotion)
                if btn_rect.collidepoint(mouse_pos) and mouse_click:
                    selected_emotion = value
                    state = SELECT_SYMBOL
                    pygame.time.delay(200)

        elif state == SELECT_SYMBOL:
            title = big_font.render("3. Elige un símbolo de lujo", True, BLACK)
            screen.blit(title, ((800 - title.get_width()) // 2, 40))
            for i, symbol in enumerate(luxury_symbols):
                y = 120 + i * 55
                btn_rect, value = draw_button(symbol, 250, y, 300, 45, GOLD, symbol)
                if btn_rect.collidepoint(mouse_pos) and mouse_click:
                    selected_symbol = value
                    state = SELECT_STYLE
                    pygame.time.delay(200)

        elif state == SELECT_STYLE:
            title = big_font.render("4. Elige un estilo de diseño", True, BLACK)
            screen.blit(title, ((800 - title.get_width()) // 2, 40))
            for i, style in enumerate(design_styles):
                y = 120 + i * 55
                btn_rect, value = draw_button(style, 250, y, 300, 45, BLACK, style)
                if btn_rect.collidepoint(mouse_pos) and mouse_click:
                    selected_style = value
                    state = SHOW_RESULT
                    pygame.time.delay(200)

        elif state == SHOW_RESULT:
            result = build_result_message(selected_color, selected_emotion, selected_symbol, selected_style)
            title = big_font.render("Resultado final", True, BLACK)
            screen.blit(title, ((800 - title.get_width()) // 2, 30))
            wrapped_text = wrap_text(result, font, 600)
            start_y = 120
            for i, line in enumerate(wrapped_text):
                line_surface = font.render(line, True, BLACK)
                x = (800 - line_surface.get_width()) // 2
                y = start_y + i * 35
                screen.blit(line_surface, (x, y))

            btn_rect, _ = draw_button("Crear otra marca", 300, 500, 200, 50, GOLD, None)
            if btn_rect.collidepoint(mouse_pos) and mouse_click:
                state = SELECT_COLOR
                selected_color = selected_emotion = selected_symbol = selected_style = None
                pygame.time.delay(200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Iniciar juego
if __name__ == "__main__":
    main()
