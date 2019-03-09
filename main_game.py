import pygame

pygame.init()

width = 750                                         #width of the app window
height = 500                                        #height of the app window
window = pygame.display.set_mode((width, height))   #setting a game window
pygame.display.set_caption('Pong-game')             #name of the app

ball_direction_factor = 1
reflection_angle = 0

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
player_1 = paddle(window, (0, 100, 100), width / 8, height / 50, int(width / 2), 0 + int(height / 20), width/50)
player_2 = paddle(window, (0, 100, 100), width / 8, height / 50, int(width / 2), int(height) - int(height / 20), width/50)

def game_window_redraw():
    window.fill((0,0,0))
    pong_ball.draw(new_ball)
    paddle.draw(player_1)
    paddle.draw(player_2)
    pygame.display.update()

def changing_ball_direction():
    global ball_direction_factor
    global reflection_angle
    if new_ball.y <= player_1.y:
        if new_ball.x >= player_1.x - player_1.width/2 and new_ball.x <= player_1.x - player_1.width / 4:
            ball_direction_factor *= -1
            reflection_angle = -0.5
        elif new_ball.x > player_1.x - player_1.width / 4 and new_ball.x <= player_1.x + player_1.width / 4:
            ball_direction_factor *= -1
            reflection_angle = 0
        elif new_ball.x > player_1.x - player_1.width / 4 and new_ball.x <= player_1.x + player_1.width / 2:
            ball_direction_factor *= -1
            reflection_angle = 0.5
        else:
            ball_direction_factor *= 0
            reflection_angle = 0
    if new_ball.y >= player_2.y:
        if new_ball.x >= player_2.x - player_2.width/2 and new_ball.x <= player_2.x - player_2.width / 4:
            ball_direction_factor *= -1
            reflection_angle = -0.5
        elif new_ball.x > player_2.x - player_2.width / 4 and new_ball.x <= player_2.x + player_2.width / 4:
            ball_direction_factor *= -1
            reflection_angle = 0
        elif new_ball.x > player_2.x - player_2.width / 4 and new_ball.x <= player_2.x + player_2.width / 2:
            ball_direction_factor *= -1
            reflection_angle = 0.5
        else:
            ball_direction_factor *= 0
            reflection_angle = 0
    if new_ball.x <=0:
        reflection_angle *= -1

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if player_1.x > 0 + player_1.width/2:
            player_1.x -= player_1.velocity
    if keys[pygame.K_RIGHT]:
        if player_1.x < width - player_1.width/2:
            player_1.x += player_1.velocity
    if keys[pygame.K_a]:
        if player_2.x > 0 + player_2.width/2:
            player_2.x -= player_2.velocity
    if keys[pygame.K_d]:
        if player_2.x < width - player_2.width/2:
            player_2.x += player_2.velocity

    changing_ball_direction()

    new_ball.y += ball_direction_factor * new_ball.velocity
    new_ball.x += round(reflection_angle * new_ball.velocity)

    game_window_redraw()

pygame.quit()
