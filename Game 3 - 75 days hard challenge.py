import pygame
from sys import exit


class PLAYER(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # front
        player_front_1 = pygame.image.load('../Assets/graphics/guy_front.png').convert_alpha()
        player_front_2 = pygame.image.load('../Assets/graphics/guy_front_walking_1.png').convert_alpha()
        player_front_3 = pygame.image.load('../Assets/graphics/guy_front_2.png').convert_alpha()
        player_front_4 = pygame.image.load('../Assets/graphics/guy_front_walking_2.png').convert_alpha()
        self.front_walk = [player_front_1, player_front_2, player_front_3, player_front_4]
        # right
        player_right_1 = pygame.image.load('../Assets/graphics/guy_right.png').convert_alpha()
        player_right_2 = pygame.image.load('../Assets/graphics/guy_right_walking_1.png').convert_alpha()
        player_right_3 = pygame.image.load('../Assets/graphics/guy_right.png').convert_alpha()
        player_right_4 = pygame.image.load('../Assets/graphics/guy_right_walking_2.png').convert_alpha()
        self.right_walk = [player_right_1, player_right_2, player_right_3, player_right_4]
        # left
        player_left_1 = pygame.image.load('../Assets/graphics/guy_left.png').convert_alpha()
        player_left_2 = pygame.image.load('../Assets/graphics/guy_left_walking_1.png').convert_alpha()
        player_left_3 = pygame.image.load('../Assets/graphics/guy_left_2.png').convert_alpha()
        player_left_4 = pygame.image.load('../Assets/graphics/guy_left_walking_2.png').convert_alpha()
        self.left_walk = [player_left_1, player_left_2, player_left_3, player_left_4]
        # Back
        player_back_1 = pygame.image.load('../Assets/graphics/guy_back.png').convert_alpha()
        player_back_2 = pygame.image.load('../Assets/graphics/guy_backwards_walking_1.png').convert_alpha()
        player_back_3 = pygame.image.load('../Assets/graphics/guy_back_2.png').convert_alpha()
        player_back_4 = pygame.image.load('../Assets/graphics/guy_backwards_walking_2.png').convert_alpha()
        self.backwards_walk = [player_back_1, player_back_2, player_back_3, player_back_4]
        self.player_index = 0

        self.image = self.front_walk[self.player_index]
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(midbottom=(350, 250))

    def player_animation(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.player_index += 0.1
            if self.player_index >= len(self.right_walk):
                self.player_index = 0
            self.image = self.right_walk[int(self.player_index)]
            self.image = pygame.transform.scale2x(self.image)
        if keys[pygame.K_LEFT]:
            self.player_index += 0.1
            self.player_index += 0.1
            if self.player_index >= len(self.left_walk):
                self.player_index = 0
            self.image = self.left_walk[int(self.player_index)]
            self.image = pygame.transform.scale2x(self.image)
        if keys[pygame.K_UP]:
            self.player_index += 0.1
            self.player_index += 0.1
            if self.player_index >= len(self.backwards_walk):
                self.player_index = 0
            self.image = self.backwards_walk[int(self.player_index)]
            self.image = pygame.transform.scale2x(self.image)
        if keys[pygame.K_DOWN]:
            self.player_index += 0.1
            self.player_index += 0.1
            if self.player_index >= len(self.front_walk):
                self.player_index = 0
            self.image = self.front_walk[int(self.player_index)]
            self.image = pygame.transform.scale2x(self.image)

    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.rect.x > 0:
                self.rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            if self.rect.x < 1350:
                self.rect.x += player_speed
        if keys[pygame.K_DOWN]:
            if self.rect.y < 640:
                self.rect.y += player_speed
        if keys[pygame.K_UP]:
            if self.rect.y > 2:
                self.rect.y -= player_speed

    def player_collision(self):
        global player_speed, car_speed, slide, start_time, strenght, strenght_text

        # home 1
        if slide == 1:
            if home_collision_rect1.top <= self.rect.y <= home_collision_rect1.bottom:
                if self.rect.left <= home_collision_rect1.right <= self.rect.right:
                    self.rect.x = self.rect.x + 4
            if home_collision_rect1.left <= self.rect.x <= home_collision_rect1.right:
                if self.rect.top <= home_collision_rect1.bottom:
                    self.rect.y = self.rect.y + 4
            if home_collision_rect1.top <= self.rect.y <= home_collision_rect1.bottom:
                if home_collision_rect1.left <= self.rect.right <= home_collision_rect1.right:
                    self.rect.x = self.rect.x - 4
            if home_collision_rect1.left <= self.rect.x <= home_collision_rect1.right:
                if home_collision_rect1.top <= self.rect.bottom <= home_collision_rect1.bottom:
                    self.rect.y = self.rect.y - 4
            # home 2
            if home_collision_rect2.top <= self.rect.y <= home_collision_rect2.bottom:
                if self.rect.left <= home_collision_rect2.right <= self.rect.right:
                    self.rect.x = self.rect.x + 4
            if home_collision_rect2.left <= self.rect.x <= home_collision_rect2.right:
                if self.rect.top <= home_collision_rect2.bottom:
                    self.rect.y = self.rect.y + 4
            if home_collision_rect2.top <= self.rect.y <= home_collision_rect2.bottom:
                if home_collision_rect2.left <= self.rect.right <= home_collision_rect2.right:
                    self.rect.x = self.rect.x - 4
            if home_collision_rect2.left <= self.rect.x <= home_collision_rect2.right:
                if home_collision_rect2.top <= self.rect.bottom <= home_collision_rect2.bottom:
                    self.rect.y = self.rect.y - 4

            # home 3
            if home_collision_rect3.top <= self.rect.y <= home_collision_rect3.bottom:
                if self.rect.left <= home_collision_rect3.right <= self.rect.right:
                    self.rect.x = self.rect.x + 4
            if home_collision_rect3.left <= self.rect.x <= home_collision_rect3.right:
                if self.rect.bottom >= home_collision_rect3.bottom:
                    self.rect.y = self.rect.y + 4
            if home_collision_rect3.top <= self.rect.y <= home_collision_rect3.bottom:
                if home_collision_rect3.left <= self.rect.right <= home_collision_rect3.right:
                    self.rect.x = self.rect.x - 4
            if home_collision_rect3.left <= self.rect.x <= home_collision_rect3.right:
                if home_collision_rect3.top <= self.rect.bottom <= home_collision_rect3.bottom:
                    self.rect.y = self.rect.y - 4

            # home 4
            if home_collision_rect4.top <= self.rect.y <= home_collision_rect4.bottom:
                if self.rect.left <= home_collision_rect4.right <= self.rect.right:
                    self.rect.x = self.rect.x + 4
            if home_collision_rect4.left <= self.rect.x <= home_collision_rect4.right:
                if self.rect.bottom >= home_collision_rect4.bottom:
                    self.rect.y = self.rect.y + 4
            if home_collision_rect4.top <= self.rect.y <= home_collision_rect4.bottom:
                if home_collision_rect4.left <= self.rect.right <= home_collision_rect4.right:
                    self.rect.x = self.rect.x - 4
            if home_collision_rect4.left <= self.rect.x <= home_collision_rect4.right:
                if home_collision_rect4.top <= self.rect.bottom <= home_collision_rect4.bottom:
                    self.rect.y = self.rect.y - 4

            # home 5
            if home_collision_rect5.top <= self.rect.y <= home_collision_rect5.bottom:
                if self.rect.left <= home_collision_rect5.right <= self.rect.right:
                    self.rect.x = self.rect.x + 4
            if home_collision_rect5.left <= self.rect.x <= home_collision_rect5.right:
                if self.rect.top <= home_collision_rect5.bottom:
                    self.rect.y = self.rect.y + 4
            if home_collision_rect5.top <= self.rect.y <= home_collision_rect5.bottom:
                if home_collision_rect5.left <= self.rect.right <= home_collision_rect5.right:
                    self.rect.x = self.rect.x - 4
            if home_collision_rect5.left <= self.rect.x <= home_collision_rect5.right:
                if home_collision_rect5.top <= self.rect.bottom <= home_collision_rect5.bottom:
                    self.rect.y = self.rect.y - 4

            # home 6
            if home_collision_rect6.top <= self.rect.y <= home_collision_rect6.bottom:
                if self.rect.left <= home_collision_rect6.right <= self.rect.right:
                    self.rect.x = self.rect.x + 4
            if home_collision_rect6.left <= self.rect.x <= home_collision_rect6.right:
                if self.rect.top <= home_collision_rect6.bottom:
                    self.rect.y = self.rect.y + 4
            if home_collision_rect6.top <= self.rect.y <= home_collision_rect6.bottom:
                if home_collision_rect6.left <= self.rect.right <= home_collision_rect6.right:
                    self.rect.x = self.rect.x - 4
            if home_collision_rect6.left <= self.rect.x <= home_collision_rect6.right:
                if home_collision_rect6.top <= self.rect.bottom <= home_collision_rect6.bottom:
                    self.rect.y = self.rect.y - 4

            # home 7
            if home_collision_rect7.top <= self.rect.y <= home_collision_rect7.bottom:
                if self.rect.left <= home_collision_rect7.right <= self.rect.right:
                    self.rect.x = self.rect.x + 4
            if home_collision_rect7.left <= self.rect.x <= home_collision_rect7.right:
                if self.rect.top <= home_collision_rect6.bottom:
                    self.rect.y = self.rect.y + 4
            if home_collision_rect7.top <= self.rect.y <= home_collision_rect7.bottom:
                if home_collision_rect7.left <= self.rect.right <= home_collision_rect7.right:
                    self.rect.x = self.rect.x - 4
            if home_collision_rect7.left <= self.rect.x <= home_collision_rect7.right:
                if home_collision_rect7.top <= self.rect.bottom <= home_collision_rect7.bottom:
                    self.rect.y = self.rect.y - 4

            # home 8
            if home_collision_rect8.top <= self.rect.y <= home_collision_rect8.bottom:
                if self.rect.left <= home_collision_rect8.right <= self.rect.right:
                    self.rect.x = self.rect.x + 4
            if home_collision_rect8.left <= self.rect.x <= home_collision_rect8.right:
                if self.rect.top <= home_collision_rect8.bottom:
                    self.rect.y = self.rect.y + 4
            if home_collision_rect8.top <= self.rect.y <= home_collision_rect8.bottom:
                if home_collision_rect8.left <= self.rect.right <= home_collision_rect8.right:
                    self.rect.x = self.rect.x - 4
            if home_collision_rect8.left <= self.rect.x <= home_collision_rect8.right:
                if home_collision_rect8.top <= self.rect.bottom <= home_collision_rect8.bottom:
                    self.rect.y = self.rect.y - 4

            # home 9
            if home_collision_rect9.top <= self.rect.y <= home_collision_rect9.bottom:
                if self.rect.left <= home_collision_rect9.right <= self.rect.right:
                    self.rect.x = self.rect.x + 4
            if home_collision_rect9.left <= self.rect.x <= home_collision_rect9.right:
                if self.rect.bottom >= home_collision_rect4.bottom:
                    self.rect.y = self.rect.y + 4
            if home_collision_rect9.top <= self.rect.y <= home_collision_rect9.bottom:
                if home_collision_rect9.left <= self.rect.right <= home_collision_rect9.right:
                    self.rect.x = self.rect.x - 4
            if home_collision_rect9.left <= self.rect.x <= home_collision_rect9.right:
                if home_collision_rect9.top <= self.rect.bottom <= home_collision_rect9.bottom:
                    self.rect.y = self.rect.y - 4

            # home 10
            if home_collision_rect10.top <= self.rect.y <= home_collision_rect10.bottom:
                if self.rect.left <= home_collision_rect10.right <= self.rect.right:
                    self.rect.x = self.rect.x + 4
            if home_collision_rect10.left <= self.rect.x <= home_collision_rect10.right:
                if self.rect.bottom >= home_collision_rect10.bottom:
                    self.rect.y = self.rect.y + 4
            if home_collision_rect10.top <= self.rect.y <= home_collision_rect10.bottom:
                if home_collision_rect10.left <= self.rect.right <= home_collision_rect10.right:
                    self.rect.x = self.rect.x - 4
            if home_collision_rect10.left <= self.rect.x <= home_collision_rect10.right:
                if home_collision_rect10.top <= self.rect.bottom <= home_collision_rect10.bottom:
                    self.rect.y = self.rect.y - 4

            # home 11
            if home_collision_rect11.top <= self.rect.y <= home_collision_rect11.bottom:
                if self.rect.left <= home_collision_rect11.right <= self.rect.right:
                    self.rect.x = self.rect.x + 4
            if home_collision_rect11.left <= self.rect.x <= home_collision_rect11.right:
                if self.rect.bottom >= home_collision_rect11.bottom:
                    self.rect.y = self.rect.y + 4
            if home_collision_rect11.top <= self.rect.y <= home_collision_rect11.bottom:
                if home_collision_rect11.left <= self.rect.right <= home_collision_rect11.right:
                    self.rect.x = self.rect.x - 4
            if home_collision_rect11.left <= self.rect.x <= home_collision_rect11.right:
                if home_collision_rect11.top <= self.rect.bottom <= home_collision_rect11.bottom:
                    self.rect.y = self.rect.y - 4

            # home 12
            if home_collision_rect12.top <= self.rect.y <= home_collision_rect12.bottom:
                if self.rect.left <= home_collision_rect12.right <= self.rect.right:
                    self.rect.x = self.rect.x + 4
            if home_collision_rect12.left <= self.rect.x <= home_collision_rect12.right:
                if self.rect.bottom >= home_collision_rect12.bottom:
                    self.rect.y = self.rect.y + 4
            if home_collision_rect12.top <= self.rect.y <= home_collision_rect12.bottom:
                if home_collision_rect12.left <= self.rect.right <= home_collision_rect12.right:
                    self.rect.x = self.rect.x - 4
            if home_collision_rect12.left <= self.rect.x <= home_collision_rect12.right:
                if home_collision_rect12.top <= self.rect.bottom <= home_collision_rect12.bottom:
                    self.rect.y = self.rect.y - 4

            if self.rect.left > 1300:
                slide = 2
                self.rect.left = 0

            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= 620:
                self.rect.bottom = 620

            keys = pygame.key.get_pressed()
            if self.rect.colliderect(car_rect):
                screen.blit(black_screen, (0, 0))
                screen.blit(dead_text, (400, 300))
                screen.blit(reset_text, (500, 500))
                player_speed = 0
                car_speed = 0
                if keys[pygame.K_SPACE]:
                    self.rect = self.image.get_rect(midbottom=(350, 250))
                    car_rect.x = -200
                    start_time = int(pygame.time.get_ticks() / 1000)
                    slide = 0
        elif slide == 2:
            if self.rect.colliderect(gym_rect):
                strenght += 1
                strenght_text = font_text.render(f'STRENGHT: {strenght}', False, 'white')

    def update(self):
        self.player_movement()
        self.player_animation()
        self.player_collision()


pygame.init()

# screen
screen = pygame.display.set_mode((1300, 620))

pygame.display.set_caption('75 Days Hard')
clock = pygame.time.Clock()

# variables
slide = 999
player_speed = 4
car_speed = 10
strenght = 1

# images
gym = pygame.image.load('../Assets/graphics/gym.png').convert_alpha()
gym_rect = gym.get_rect(midbottom=(1000, 400))

floor = pygame.image.load('../Assets/graphics/floor.jpg').convert_alpha()
floor = pygame.transform.scale(floor, (100, 620))

road = pygame.image.load('../Assets/graphics/OIP (1).jpg').convert_alpha()
road = pygame.transform.rotate(road, 90)

home = pygame.image.load('../Assets/graphics/HOUSE.png').convert_alpha()
bottom_home = pygame.transform.rotate(home, 180)

car = pygame.image.load('../Assets/graphics/Carro.png').convert_alpha()
car = pygame.transform.rotozoom(car, 0, 0.3)
car_rect = car.get_rect(midbottom=(200, 380))

black_screen = pygame.surface.Surface((1300, 620))

background = pygame.image.load('../Assets/graphics/background.png').convert_alpha()

# collisions

home_collision_rect1 = home.get_rect(topleft=(100, -30))
home_collision_rect1.bottom -= 30
home_collision_rect1.width -= 30

home_collision_rect2 = home.get_rect(topleft=(300, -30))
home_collision_rect2.width = home_collision_rect2.width - 30
home_collision_rect2.height = home_collision_rect2.height - 30

home_collision_rect3 = home.get_rect(topleft=(100, 500))
home_collision_rect3.left += 30
home_collision_rect3.width -= 30

home_collision_rect4 = home.get_rect(topleft=(300, 500))
home_collision_rect4.left += 30
home_collision_rect4.width -= 30

home_collision_rect5 = home.get_rect(topleft=(500, -30))
home_collision_rect5.width -= 30
home_collision_rect5.bottom -= 30

home_collision_rect6 = home.get_rect(topleft=(700, -30))
home_collision_rect6.width -= 30
home_collision_rect6.bottom -= 30

home_collision_rect7 = home.get_rect(topleft=(900, -30))
home_collision_rect7.width -= 30
home_collision_rect7.bottom -= 30

home_collision_rect8 = home.get_rect(topleft=(1100, -30))
home_collision_rect8.width -= 30
home_collision_rect8.bottom -= 30

home_collision_rect9 = home.get_rect(topleft=(500, 500))
home_collision_rect9.left += 30
home_collision_rect9.width -= 30

home_collision_rect10 = home.get_rect(topleft=(700, 500))
home_collision_rect10.left += 30
home_collision_rect10.width -= 30

home_collision_rect11 = home.get_rect(topleft=(900, 500))
home_collision_rect11.left += 30
home_collision_rect11.width -= 30

home_collision_rect12 = home.get_rect(topleft=(1100, 500))
home_collision_rect12.left += 30
home_collision_rect12.width -= 30

# text
font = pygame.font.Font('../Assets/font/Pixeltype.ttf', 200)
font_text = pygame.font.Font('../Assets/font/Pixeltype.ttf', 50)

day1_text = font.render('Day 1', False, 'white')
gym_text = font.render('gym', False, 'white')

start_button = pygame.surface.Surface((250, 50))
start_button_rect = start_button.get_rect(midbottom=(1300 / 2, 700 / 2))
start_button.fill('grey')
start_button_text = font_text.render('Start', False, 'black')
start_button_text_rect = start_button_text.get_rect(midbottom=(1300 / 2, 700 / 2))

quit_button = pygame.surface.Surface((250, 50))
quit_button_rect = quit_button.get_rect(midbottom=(1300 / 2, 900 / 2))
quit_button.fill('grey')
quit_button_text = font_text.render('Quit', False, 'black')
quit_button_text_rect = start_button_text.get_rect(midbottom=(1300 / 2, 900 / 2))

dead_text = font.render('You Died...', False, 'red')
reset_text = font_text.render('[SPACE TO RESET]', False, 'red')

space_to_enter_text = font_text.render('[ SPACE TO ENTER ]', False, 'white')
space_to_enter_text_rect = space_to_enter_text.get_rect(midbottom=(1300 / 2, 620))

goal_text = font_text.render('GOAL: 500 STRENGHT', False, 'white')
strenght_text = font_text.render(f'STRENGHT: {strenght}', False, 'white')

win_text = font_text.render('YOU WON!', False, 'white')

# time
start_time = 0

# Sprite groups
player_group = pygame.sprite.GroupSingle()
player_group.add(PLAYER())

# random
deaths = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if slide == 999:
        key = pygame.key.get_pressed()
        screen.blit(background, (0, 0))
        screen.blit(start_button, start_button_rect)
        pygame.draw.rect(screen, 'black', start_button_rect, 5)
        screen.blit(start_button_text, start_button_text_rect)

        screen.blit(quit_button, quit_button_rect)
        pygame.draw.rect(screen, 'black', quit_button_rect, 5)
        screen.blit(quit_button_text, quit_button_text_rect)

        if event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(event.pos):
            slide = 0

        if event.type == pygame.MOUSEBUTTONDOWN and quit_button_rect.collidepoint(event.pos):
            pygame.quit()
            exit()

    elif slide == 1:
        for position in range(0, 14):
            screen.blit(floor, (position * 100, 0))
        for position in range(0, 9):
            screen.blit(road, (road.get_width() * position, 300))
        screen.blit(bottom_home, (100, 500))
        screen.blit(bottom_home, (300, 500))
        screen.blit(bottom_home, (500, 500))
        screen.blit(bottom_home, (700, 500))
        screen.blit(bottom_home, (900, 500))
        screen.blit(bottom_home, (1100, 500))
        screen.blit(home, (100, -30))
        screen.blit(home, (300, -30))
        screen.blit(home, (500, -30))
        screen.blit(home, (700, -30))
        screen.blit(home, (900, -30))
        screen.blit(home, (1100, -30))

        screen.blit(goal_text, (20, 20))

        screen.blit(car, car_rect)
        car_rect.x += car_speed
        if car_rect.x >= 1500:
            car_rect.x = -200

        player_group.draw(screen)
        player_group.update()

    elif slide == 0:
        car_speed = 10
        player_speed = 4
        screen.blit(black_screen, (0, 0))
        screen.blit(day1_text, (550, 300))
        current_time = int(pygame.time.get_ticks() / 1000) - start_time
        if current_time >= 3:
            slide += 1

    elif slide == 2:
        for position in range(0, 14):
            screen.blit(floor, (position * 100, 0))

        screen.blit(goal_text, (20, 20))
        screen.blit(strenght_text, (20, 80))

        player_group.draw(screen)
        player_group.update()
        screen.blit(gym, gym_rect)
        if strenght >= 500:
            screen.blit(background, (0, 0))
            screen.blit(win_text, (600, 400))

    pygame.display.update()
    clock.tick(60)
