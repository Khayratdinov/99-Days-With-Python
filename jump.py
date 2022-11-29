# importing modules
import pygame
import random
import time

# initializing window


heart = 2
pygame.init()
WIDTH = 800
HEIGHT = 600
black = (0, 0, 0)
white = (255, 255, 255)
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))  # setting game display size
pygame.display.set_caption("DataFlair- Keyboard Jump Game")
background = pygame.image.load("images/start.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # scale image
font = pygame.font.Font("fonts/comic.ttf", 40)


## function to get words randomly
word_speed = 0.5
score = 0


def new_word():
    global displayword, yourword, x_cor, y_cor, text, word_speed
    x_cor = random.randint(300, 700)  # randomly choose x-cor between 300-700
    y_cor = 200  # y-cor
    word_speed += 0.10
    yourword = ""
    words = open("words.txt").read().split(", ")
    displayword = random.choice(words)


new_word()


# function to draw text
font_name = pygame.font.match_font("fonts/comic.ttf")


def draw_text(display, text, size, x, y, color=black):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)


# def sleep_new_word(func):
#     def wrapper():
#         pygame.time.wait(1000)

#     return wrapper



# function to show front screen and gameover screen
def game_front_screen():
    gameDisplay.blit(background, (0, 0))
    if not game_over:
        gameOverDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
        background_g = pygame.image.load("images/game-over.jpg")
        background_g = pygame.transform.scale(background_g, (WIDTH, HEIGHT))
        gameOverDisplay.blit(background_g, (0, 0))
        draw_text(gameDisplay, "GAME OVER!", 90, WIDTH / 2, HEIGHT / 4, color=white)
        draw_text(gameDisplay, "Score : " + str(score), 70, WIDTH / 2, HEIGHT / 2, color=white)
    else:
        draw_text(gameDisplay, "Press a key to begin!", 54, WIDTH / 2, 500)
    pygame.display.flip()
    waiting = True
    while waiting:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


# main loop
game_over = True
game_start = True
while True:
    if game_over:
        if game_start:
            game_front_screen()
        game_start = False
    game_over = False

    background = pygame.image.load("images/background4.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    character = pygame.image.load("images/char.png")
    character = pygame.transform.scale(character, (80, 100))
    wood = pygame.image.load("images/wood-.png")
    wood = pygame.transform.scale(wood, (240, 50))
    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(wood, (x_cor - 80, y_cor + 25))
    gameDisplay.blit(character, (x_cor + 80, y_cor - 55))

    # background = pygame.image.load("images/background4.jpg")
    # background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    # character = pygame.image.load("images/char.png")
    # character = pygame.transform.scale(character, (50, 50))
    # wood = pygame.image.load("images/wood-.png")
    # wood = pygame.transform.scale(wood, (90, 50))

    # gameDisplay.blit(background, (0, 0))

    y_cor += word_speed
    # gameDisplay.blit(wood, (x_cor - 50, y_cor + 15))
    # gameDisplay.blit(character, (x_cor - 100, y_cor))
    draw_text(gameDisplay, str(displayword), 40, x_cor, y_cor)
    draw_text(gameDisplay, str(yourword), 40, WIDTH / 2, 500)
    draw_text(gameDisplay, "Score:" + str(score), 40, WIDTH / 2, 5)
    heart_icon = pygame.image.load("images/heart.png")
    heart_icon = pygame.transform.scale(heart_icon, (40, 40))
    gameDisplay.blit(heart_icon, (350, 48))
    draw_text(gameDisplay, str(heart + 1), 40, WIDTH / 2, 55)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            yourword += pygame.key.name(event.key)
            if displayword.startswith(yourword):
                if displayword == yourword:
                    score += len(displayword)
                    new_word()
            elif heart == 0:
                game_front_screen()
                time.sleep(2)
                pygame.quit()
            else:
                heart -= 1
                new_word()

    if y_cor < HEIGHT - 5:
        pygame.display.update()
    else:
        game_front_screen()
