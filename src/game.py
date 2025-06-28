import os
import pygame
import random


def update_vector_cluster_position_up(cluster, new_pos, dt):
    for vec in cluster:
        vec.y -= new_pos * dt

def update_vector_cluster_position_down(cluster, new_pos, dt):
    for vec in cluster:
        vec.y += new_pos * dt

def update_vector_cluster_position_right(cluster, new_pos, dt):
    for vec in cluster:
        vec.x += new_pos * dt

def update_vector_cluster_position_left(cluster, new_pos, dt):
    for vec in cluster:
        vec.x -= new_pos * dt
    
def load_sounds(asset_paths):
    sounds = []
    for path in asset_paths:
        if(os.path.exists(path)):
            sounds.append(pygame.Sound(path))
        else:
            print(f'Failed to Load Sound From Path: {path}')
    return sounds

def play_sound(sound: pygame.Sound):
    sound.play()
    
def main():

    # APPLICATION INITIALIZATION
    pygame.init()
    pygame.display.set_caption('My First Game')
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # CORE SCENE IMAGES
    background_img = pygame.transform.scale(pygame.image.load("assets/art/background.png"), (1280, 720))

    # VECTORS
    ball_1 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    ball_2 = pygame.Vector2(screen.get_width() / 2 + 45, screen.get_height() / 2)
    ball_3 = pygame.Vector2(screen.get_width() / 2 - 45, screen.get_height() / 2)
    ball_4 = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2 + 45)
    ball_5 = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2 - 45)
    ball_cluster = [ball_1, ball_2, ball_3, ball_4, ball_5]


    target_1 = pygame.Vector2(0, random.randint(20, screen.get_height() - 20))

    # GAME AUDIO
    pygame.mixer.init(48000, -16, 1, 1024)
    pygame.mixer.set_num_channels(6)

    gun_shot1 = pygame.mixer.Sound("assets/audio/guns/m9/m9_shot.mp3")
    gun_shot2 = pygame.mixer.Sound("assets/audio/guns/m9/m9_shot.mp3")
    gun_shot3 = pygame.mixer.Sound("assets/audio/guns/m9/m9_shot.mp3")
    gun_shot4 = pygame.mixer.Sound("assets/audio/guns/m9/m9_shot.mp3")
    gun_shot5 = pygame.mixer.Sound("assets/audio/guns/m9/m9_shot.mp3")
    gun_shot6 = pygame.mixer.Sound("assets/audio/guns/m9/m9_reload.mp3")

    is_reloading = False
    reload_channel = None
    shot_positions = [ gun_shot1, gun_shot2, gun_shot3, gun_shot4, gun_shot5, gun_shot6 ]
    shot_index = 0
    num_shots = len(shot_positions)
    
    
    # GAME LOOP
    while running:

        if is_reloading:
            if reload_channel and not reload_channel.get_busy():
                is_reloading = False

        # Event Polling (X == Quit)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running = False
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    if is_reloading:
                        continue
                    else:
                        print(shot_index % num_shots)
                        channel = shot_positions[shot_index % num_shots].play()
                        if(shot_index % num_shots == 5):
                            reload_channel = channel
                            is_reloading = True
                        shot_index += 1

        # Object Rendering
        screen.fill('white')
        pygame.Surface.blit(screen, background_img)

        # Enemy Screen Traversal Test
        pygame.draw.circle(screen, "white", (target_1), 100)
        target_1.x += 200 * dt
        if(target_1.x > screen.get_width() + 120):
            target_1.x = 0

        for ball in ball_cluster:
            pygame.draw.circle(screen, "purple", ball, 10)
        
        # Controller Logic
        dt = clock.tick(60) / 1000
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            update_vector_cluster_position_up(ball_cluster, 400, dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            update_vector_cluster_position_down(ball_cluster, 400, dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            update_vector_cluster_position_left(ball_cluster, 400, dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            update_vector_cluster_position_right(ball_cluster, 400, dt)
            
        # Object Render Update
        pygame.display.flip()

        
    pygame.quit()

if __name__ == "__main__":
    main()