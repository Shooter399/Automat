import pygame
import sys

# Pygame initialisieren
pygame.init()

# Bildschirmgröße und Fenster erstellen
screen = pygame.display.set_mode((1024, 600))  # Beispielgröße für Touchscreen
pygame.display.set_caption("Touchscreen Test")

# Farben definieren
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255,0,0)
GREEN = (0, 255, 0)

# Button-Eigenschaften
distance = 55
length = 268
class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.original_width = width
        self.original_height = height
        self.clicked = False
    
    def draw(self, screen):
        if self.clicked:
            # Wenn der Button geklickt wurde, verkleinere ihn
            width = self.original_width * 0.9 # 10% kleiner
            height = self.original_height * 0.9 # 10% kleiner
        else:
            # Ansonsten die Originalgröße
            width = self.original_width
            height = self.original_height
        
        # Button zeichnen
        pygame.draw.rect(screen, self.color, pygame.Rect(self.rect.x, self.rect.y, width, height))
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + (width - text_surface.get_width()) // 2, 
                                  self.rect.y + (height - text_surface.get_height()) // 2))
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
    def start_click_effect(self):
        self.clicked = True
        pygame.time.set_timer(pygame.USEREVENT, 200)  # Setze einen Timer, um den Effekt zu beenden nach 200 ms
    
    def reset_click_effect(self):
        self.clicked = False
        pygame.time.set_timer(pygame.USEREVENT, 0)  # Timer stoppen
        

# Erstelle eine Liste von Buttons
buttons = [
    Button(distance, distance, length, 80, BLUE, "Button 1"),
    Button(distance+length+distance, distance, length, 80, GREEN, "Button 2"),
    Button(distance+length+distance+length+distance, distance, length, 80, BLUE, "Button 3")
]

# Haupt-Game-Loop
running = True
while running:
    # Ereignisse überprüfen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # Position des Klicks / Tap
            # Überprüfe, ob ein Button geklickt wurde
            for button in buttons:
                if button.is_clicked(mouse_pos):
                    print(f"{button.text} wurde gedrückt!")
                    button.start_click_effect()  # Startet die Verkleinerung des Buttons
        elif event.type == pygame.USEREVENT:
            # Setze den Button zurück, wenn der Timer abgelaufen ist
            for button in buttons:
                button.reset_click_effect()

    # Bildschirm löschen
    screen.fill(WHITE)

    # Button zeichnen
    for button in buttons:
        button.draw(screen)

    # Bildschirm aktualisieren
    pygame.display.update()

# Pygame beenden
pygame.quit()
sys.exit()
