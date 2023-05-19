import pygame, sys, random, datetime

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos,550))
    screen.blit(floor_surface, (floor_x_pos + 360, 550))

def create_pipe():
    random_pipe_pos = random.randrange(250,500)
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (500,random_pipe_pos - 250))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 640:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)

def check_collison(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 550:
        return False
    
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird,-bird_movement*3,1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird,new_bird_rect

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)),True,(0,0,0))
        score_rect = score_surface.get_rect(center = (180,40))
        screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f"Score: {int(score)}",True,(0,0,0))
        score_rect = score_surface.get_rect(center = (180,40))
        screen.blit(score_surface,score_rect)

        high_score_surface = game_font.render(f"High Score: {int(high_score)}",True,(255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (180,515))
        screen.blit(high_score_surface,high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
pygame.init()
WIDTH = 360
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.TTF',30)
now = datetime.datetime.now()
current_time = int(now.strftime("%H"))

pygame.display.set_caption("Flappy Bird")
#icon = pygame.image.load('assets/yellowbird-midflap.png')
#pygame.display.set_icon(icon)

# Game Varibles
gravity = 0.15
bird_movement = 0
game_active = False
score = 0
high_score = 0

bg_surface = pygame.image.load('assets/thedeep.jpg').convert()
bg_surface = pygame.transform.scale(bg_surface, (WIDTH, HEIGHT))
bg_night_surface = pygame.image.load('assets/background-night.png').convert()
bg_night_surface = pygame.transform.scale(bg_night_surface, (WIDTH, HEIGHT))

#floor_surface = pygame.image.load('assets/homeland.jpg').convert()
floor_surface = pygame.image.load('assets/lava.jpg').convert()
floor_surface = pygame.transform.scale(floor_surface, (WIDTH, floor_surface.get_height()))
floor_x_pos = 0

# Flying Pikachu Sprites
bird_downflap = pygame.transform.scale((pygame.image.load('assets/Flying_Pikachu_Dash.png').convert_alpha()), (32*2, 32*2))
bird_midflap = pygame.transform.scale((pygame.image.load('assets/Flying_Pikachu_Dash.png').convert_alpha()), (32*2, 32*2))
bird_upflap = pygame.transform.scale((pygame.image.load('assets/Flying_Pikachu_Dash.png').convert_alpha()), (32*2, 32*2))

#bird_downflap = pygame.transform.scale((pygame.image.load('assets/yellowbird-downflap.png').convert_alpha()), (34*1.5, 24*1.5))
#bird_midflap = pygame.transform.scale((pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()), (34*1.5, 24*1.5))
#bird_upflap = pygame.transform.scale((pygame.image.load('assets/yellowbird-upflap.png').convert_alpha()), (34*1.5, 24*1.5))
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100, 200))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP,200)

#bird_surface = pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
#bird_surface = pygame.transform.scale(bird_surface, (bird_surface.get_width()*1.5, bird_surface.get_height()*1.5))
#bird_rect = bird_surface.get_rect(center = (100, 320))

pipe_surface = pygame.image.load('assets/pipe-murder.png').convert_alpha()
pipe_surface = pygame.transform.scale(pipe_surface, (pipe_surface.get_width(), pipe_surface.get_height()))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)

game_over_surface = pygame.transform.scale((pygame.image.load('assets/message.png').convert_alpha()), (187*1.5, 267*1.5))
game_over_rect = game_over_surface.get_rect(center = (180,275))

flap_sound = pygame.mixer.Sound('assets/audio/wing.wav')
death_sound = pygame.mixer.Sound('assets/audio/hit.wav')
score_sound = pygame.mixer.Sound('assets/audio/point.wav')
score_sound_countdown = 100

pygame.mixer.music.load('assets/audio/mainloop.mp3')
#pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 5
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 200)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface,bird_rect = bird_animation()

    if current_time < 17:
        screen.blit(bg_surface, (0,0))
    else:
        screen.blit(bg_night_surface, (0,0))

    if game_active:
        # Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird,bird_rect)
        game_active = check_collison(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        score += 0.01
        score_display('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score = update_score(score,high_score)
        score_display('game_over')

    #Floor
    floor_x_pos -= 2
    draw_floor()
    if floor_x_pos <= -360:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(144)