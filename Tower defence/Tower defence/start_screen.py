import pygame as pg
import json
import time

# Initialize pygame
pg.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Screen size remains the same
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set video mode BEFORE loading images
FONT = pg.font.SysFont("Consolas", 24)

# Load and scale background image to fill the screen size
BACKGROUND_IMAGE = pg.image.load("Tower defence/assets/images/Graphics User Interface/background.png").convert()
BACKGROUND_IMAGE = pg.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale to screen size

# Load button images
begin_image = pg.image.load("Tower defence/assets/images/button/begin.png").convert_alpha()
ranking_image = pg.image.load("Tower defence/assets/images/button/ranking2.png").convert_alpha()

# Adjust vertical size (stretch the height) while keeping width constant
def scale_image_vertically(image, scale_factor):
    rect = image.get_rect()
    new_width = rect.width
    new_height = int(rect.height * scale_factor)
    return pg.transform.scale(image, (new_width, new_height))

# Adjust horizontal size (stretch the width) while keeping height constant
def scale_image_horizontally(image, scale_factor):
    rect = image.get_rect()
    new_height = rect.height
    new_width = int(rect.width * scale_factor)
    return pg.transform.scale(image, (new_width, new_height))

# Scale the Begin button vertically (make it 90% of original height)
scale_factor_begin = 0.9  # Smaller scaling factor to make Begin button appropriately sized
begin_image = scale_image_vertically(begin_image, scale_factor_begin)

# Apply both horizontal and vertical scaling to the ranking image
ranking_horizontal_scale_factor = 0.2 # Reduce the width by 50%
ranking_vertical_scale_factor = 0.18 # Reduce the height by 30%

# First, apply the horizontal scaling, then apply vertical scaling
ranking_image = scale_image_horizontally(ranking_image, ranking_horizontal_scale_factor)
ranking_image = scale_image_vertically(ranking_image, ranking_vertical_scale_factor)

# Global variables
player_name = ""
viewing_stats = False
game_started = False
start_time = 0
player_stats = {}

# Load stats from file
try:
    with open("player_stats.json", "r") as file:
        player_stats = json.load(file)
except FileNotFoundError:
    player_stats = {}


# Draw text centered horizontally
def draw_text_centered(screen, text, font, color, y):
    img = font.render(text, True, color)
    x = (SCREEN_WIDTH - img.get_width()) // 2  # Center text horizontally
    screen.blit(img, (x, y))

# Function to draw text
def draw_text(screen, text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Button class definition
class Button():
    def __init__(self, x, y, image, single_click):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.single_click = single_click

    def draw(self, surface):
        action = False
        # Get mouse position
        pos = pg.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                # If button is a single click type, then set clicked to True
                if self.single_click:
                    self.clicked = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        surface.blit(self.image, self.rect)

        return action

# Start screen function
def start_screen():
    global player_name, viewing_stats, game_started, start_time
    screen.fill((0, 0, 0))  # Fill the screen with black first (clear previous frame)

    # Draw the scaled background image
    screen.blit(BACKGROUND_IMAGE, (0, 0))  # Background now fills the entire screen

    # Draw buttons: Begin and Player Stats, with adjusted Y positions
    play_button = Button(320, 230, begin_image, True)  # Move "Begin" button higher (Y = 230)
    stats_button = Button(320, 310, ranking_image, True)  # Move "Ranking" button higher (Y = 310)

    if play_button.draw(screen):
        # Start the game immediately on 'Begin' click
        game_started = True
        start_time = time.time()  # Start timing the game

    if stats_button.draw(screen):
        viewing_stats = True

# Handle name input and move to game when "Enter" is pressed
def handle_name_input():
    global player_name, game_started
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()  # Ensure the game exits completely
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                player_name = player_name[:-1]  # Remove the last character
            elif event.key == pg.K_RETURN:  # Proceed only if the name is valid
                if player_name.strip():  # Ensure the name isn't just whitespace
                    game_started = True
            elif len(player_name) < 20:  # Allow typing up to 20 characters
                player_name += event.unicode


# View stats screen function
def view_stats():
    screen.fill("black")
    draw_text(screen, "Player Stats", FONT, "white", 20, 20)

    y_offset = 80
    for name, stats in player_stats.items():
        draw_text(screen, f"{name}: {stats['rounds']} rounds, {stats['total_time']:.2f}s", FONT, "white", 50, y_offset)
        y_offset += 40

    back_button = Button(320, 500, begin_image, True)
    if back_button.draw(screen):
        global viewing_stats
        viewing_stats = False

# Update stats
def update_stats(name, time_taken):
    if name not in player_stats:
        player_stats[name] = {"rounds": 0, "total_time": 0.0}
    player_stats[name]["rounds"] += 1
    player_stats[name]["total_time"] += time_taken
    with open("player_stats.json", "w") as file:
        json.dump(player_stats, file)

# Game loop
run = True
while run:
    screen.fill((0, 0, 0))  # Clear the screen at the beginning of each loop

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    if not game_started:
        if viewing_stats:
            view_stats()
        else:
            start_screen()
    else:
        # Only show the name input prompt once 'Begin' is clicked
       # Name input phase
        if player_name == "":
            screen.fill((0, 0, 0))  # Clear screen
            # Instructions at the top
            draw_text_centered(screen, "Press ENTER and close the tab after inputting your name.", FONT, "gray", 50)

            # Prompt and input field
           # Prompt and input field
            draw_text(screen, "Enter your name: ", FONT, "white", 250, 250)  # Prompt
            draw_text(screen, player_name, FONT, "white", 460, 250)  # Player name displayed to the right

            # Reassurance at the bottom
            draw_text_centered(screen, "Don't worry if the name doesn't show, it will be saved.", FONT, "gray", 550)

            if not handle_name_input():
                game_started = True


        else:
            # Game logic and rendering (existing game code)
            draw_text(screen, "Game Started!", FONT, "white", 320, 250)
            # Simulate game over and stats update for now
            game_over = True  # Simulate game over condition
            if game_over:
                end_time = time.time()
                update_stats(player_name, end_time - start_time)
                game_started = False  # Return to start screen

    pg.display.flip()

pg.quit()
