import pygame

pygame.init()

width = 750                                         #width of the app window
height = 500                                        #height of the app window
window = pygame.display.set_mode((width, height))   #setting a game window
pygame.display.set_caption('Pong-game')             #name of the app


class pong_ball():

    def __init__(self, window, colourRGB, x, y, radius, velocity):
        self.window = window
        self.colourRGB = colourRGB
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = velocity

    def draw(self): #drawing a ball in the window
        pygame.draw.circle(self.window, self.colourRGB, (self.x, self.y), self.radius)

class paddle():
    def __init__(self, window, colourRGB, width, height, x, y, velocity):
        self.window = window
        self.colourRGB = colourRGB
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.velocity = velocity

    def draw(self):
        pygame.draw.rect(self.window, self.colourRGB, (self.x - self.width / 2, self.y, self.width, self.height))


new_ball = pong_ball(window, (255, 0, 100), int(width / 2), int(height / 2), 10, 15) #new pong ball
player_1 = paddle(window, (0, 100, 100), width / 8, height / 50, int(width / 2), 0 + int(height / 20), width/30)
player_2 = paddle(window, (0, 100, 100), width / 8, height / 50, int(width / 2), int(height) - int(height / 20), width/30)

def game_window_redraw():
    window.fill((0,0,0))
    pong_ball.draw(new_ball)
    paddle.draw(player_1)
    paddle.draw(player_2)
    pygame.display.update()

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_1.x -= player_1.velocity
    if keys[pygame.K_RIGHT]:
        player_1.x += player_1.velocity
    if keys[pygame.K_a]:
        player_2.x -= player_2.velocity
    if keys[pygame.K_d]:
        player_2.x += player_2.velocity

    ball_direction = 1
    if new_ball.y <= player_1.y or new_ball.y >= player_2.y:
        ball_direction *= -1
    else:
        pass
    new_ball.y += ball_direction * new_ball.velocity

    game_window_redraw()

pygame.quit()
