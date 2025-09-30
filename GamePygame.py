import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LearnItalian.org")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ITALIAN_RED = (206, 17, 38)
ITALIAN_GREEN = (0, 146, 70)
ITALIAN_BLUE = (0, 0, 255)
BG_COLOR = (240, 240, 240)

# Fonts
font_title = pygame.font.SysFont("comicsansms", 40, bold=True)
font_text = pygame.font.SysFont("comicsansms", 28)
font_small = pygame.font.SysFont("comicsansms", 22)

# Text rendering function
def draw_text(text, font, color, y_offset=0, center=True):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        rendered = font.render(line, True, color)
        rect = rendered.get_rect()
        if center:
            rect.center = (WIDTH // 2, HEIGHT // 2 + y_offset + i * 40)
        else:
            rect.topleft = (50, 50 + i * 40)
        screen.blit(rendered, rect)

# Display sequence
def display_sequence(messages, font, color, delay=2):
    for msg in messages:
        screen.fill(BG_COLOR)
        draw_text(msg, font, color)
        pygame.display.flip()
        pygame.time.wait(delay * 1000)

# Main loop
def main():
    name = ""
    question = ""
    running = True
    stage = 0

    intro = [
        "Welcome to learnitalian.org!",
        "You want to learn Italian?",
        "Perhaps you have come to the right place!",
        "What is your name?"
    ]

    basic_phrases = [
        "Let's learn some basic phrases:",
        "Hello - Ciao",
        "Goodbye - Arrivederci",
        "Please - Per favore",
        "Thank you - Grazie",
        "Yes - Sì",
        "No - No",
        "Excuse me - Mi scusi"
    ]

    intermediate_words = [
        "Let's start with intermediate words:",
        "Tutto bene - All good",
        "Come stai? - How are you?",
        "Sto bene - I am good",
        "Mi chiamo... - My name is...",
        "Piacere di conoscerti - Nice to meet you",
        "Dove - Where",
        "Quando - When",
        "Perché - Why",
        "Chi - Who",
        "Come - How",
        "Quanto costa? - How much does it cost?",
        "Aiuto! - Help!",
        "Buon appetito - Enjoy your meal"
    ]

    advanced_words = [
        "Now we will learn some advanced words:",
        "Famiglia - Family",
        "Amico - Friend",
        "Scuola - School",
        "Lavoro - Work",
        "Città - City",
        "Paese - Country",
        "Libro - Book",
        "Cibo - Food",
        "Acqua - Water",
        "Tempo - Time",
        "Giorno - Day",
        "Notte - Night",
        "Settimana - Week",
        "Mese - Month",
        "Anno - Year",
        "Oggi - Today",
        "Domani - Tomorrow"
    ]

    basic_sentences = [
        "Let's learn some basic sentences:",
        "Come ti chiami? - What is your name?",
        "Mi chiamo... - My name is...",
        "Di dove sei? - Where are you from?",
        "Sono di... - I am from...",
        "Quanti anni hai? - How old are you?",
        "Ho ... anni - I am ... years old",
        "Parli inglese? - Do you speak English?",
        "Sì, parlo inglese - Yes, I speak English",
        "No, non parlo inglese - No, I don't speak English",
        "Non capisco - I don't understand",
        "Puoi aiutarmi? - Can you help me?"
    ]

    while running:
        screen.fill(BG_COLOR)

        if stage == 0:
            display_sequence(intro, font_title, ITALIAN_GREEN)
            name = input("Enter your name: ")
            stage += 1

        elif stage == 1:
            display_sequence([f"Hello {name}!", "Let's get started!"], font_title, ITALIAN_RED)
            display_sequence(basic_phrases, font_text, BLACK)
            question = input("Do you have any questions? ")
            display_sequence([f"Thank you for your question: {question}", "We will get back to you soon!"], font_small, ITALIAN_BLUE)
            stage += 1

        elif stage == 2:
            display_sequence(intermediate_words, font_text, BLACK)
            stage += 1

        elif stage == 3:
            display_sequence(advanced_words, font_text, BLACK)
            stage += 1

        elif stage == 4:
            display_sequence(basic_sentences, font_text, BLACK)
            display_sequence(["You have completed basic sentences!", "Goodbye!"], font_title, ITALIAN_GREEN)
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()