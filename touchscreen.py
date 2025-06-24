import pygame
import sys

distance = 55
length = 268

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
BLACK = (0,0,0)

#Fotos laden
background = pygame.image.load("Wasser.jpg")
original_apfel = pygame.transform.scale( pygame.image.load("Apfel.png"), (length,length))
original_orange = pygame.transform.scale( pygame.image.load("Orange.png"), (length,length))
original_banane = pygame.transform.scale( pygame.image.load("Banane.png"), (length,length))

# Button-Eigenschaften
class Button:
    def __init__(self, x, y, width, height, color, text, picture):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.original_width = width
        self.original_height = height
        self.original_x = x
        self.original_y = y
        self.clicked = False
        self.original_picture = picture
        
    
    def draw(self, screen):
        if self.clicked:
            # Wenn der Button geklickt wurde, verkleinere ihn
            width = self.original_width * 0.9 # 10% kleiner
            height = self.original_height * 0.9 # 10% kleiner
            self.rect.x = self.original_x + self.original_height * 0.05 # Für die Zentrierung
            self.rect.y = self.original_y + self.original_width * 0.05
            picture = pygame.transform.scale(self.original_picture, (width,height))

        else:
            # Ansonsten die Originalgröße
            width = self.original_width
            height = self.original_height
            self.rect.x = self.original_x
            self.rect.y = self.original_y
            picture = self.original_picture
        
        # Button zeichnen
        pygame.draw.rect(screen, self.color, pygame.Rect(self.rect.x, self.rect.y, width, height))
        screen.blit(picture,(self.rect.x,self.rect.y))
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + (width - text_surface.get_width()) // 2, 
                                  self.rect.y + (height - text_surface.get_height()) // 2))
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
    def start_click_effect(self):
        self.clicked = True
    
    def reset_click_effect(self):
        self.clicked = False
        

# Erstelle eine Liste von Buttons
buttons = [
    Button(distance, distance, length, length, BLUE, "Button 1", original_apfel),
    Button(distance+length+distance, distance, length, length, GREEN, "Button 2", original_orange),
    Button(distance * 3 + length * 2, distance, length, length, BLUE, "Button 3", original_banane)
]

flow = False
flowing = pygame.font.Font(None,36).render("Placeholder text", True, BLACK)

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
                    flow = True
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            flow = False
            for button in buttons:
                button.reset_click_effect() # Endet alle Verkleinerungen wenn ein Button nicht mehr geklickt wird

    # Bildschirm löschen
    screen.fill(WHITE)
    screen.blit(background,(0,0))

    # Button zeichnen
    for button in buttons:
        button.draw(screen)

    if flow:
        screen.blit(flowing,(512- flowing.get_width()/2, 450))

    # Bildschirm aktualisieren
    pygame.display.update()

# Pygame beenden
pygame.quit()
sys.exit()
