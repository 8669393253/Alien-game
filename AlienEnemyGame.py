import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
ALIEN_COLUMNS = 10
INITIAL_ALIEN_SPEED = 1
BULLET_SPEED = -10
ALIEN_BULLET_SPEED = 2
SCORE_PER_ALIEN = 10
POINTS_LOST_PER_ALIEN = 5
INITIAL_ENERGY = 100
ALIEN_SPAWN_INTERVAL = 30

player_img = pygame.image.load("assets/player.png")                # Add your own player image
alien_img = pygame.image.load("assets/alien.png")                  # Add your own alien image
background_img = pygame.image.load("assets/background.png")        # Add your own background image
fruit_img = pygame.image.load("assets/fruit.png")                  # Add your own fruit image

player_img = pygame.transform.scale(player_img, (50, 30))
alien_img = pygame.transform.scale(alien_img, (40, 30))
fruit_img = pygame.transform.scale(fruit_img, (30, 30))
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Clone")

class Player:
    def __init__(self):
        self.image = player_img
        self.x = WIDTH // 2
        self.y = HEIGHT - 60
        self.speed = 5
        self.energy = INITIAL_ENERGY

    def move(self, dx):
        self.x += dx
        self.x = max(0, min(self.x, WIDTH - 50))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def update_energy(self):
        self.energy -= 0.1 / FPS
        self.energy = max(0, self.energy)

class Alien:
    def __init__(self, x, y):
        self.image = alien_img
        self.x = x
        self.y = y
        self.alive = True
        self.hit_count = 0

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move_toward_player(self, speed):
        if self.y < HEIGHT:
            self.y += speed

    def shoot(self):
        if random.random() < 0.01:
            return AlienBullet(self.x + 20, self.y + 30)
        return None

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True

    def update(self):
        self.y += BULLET_SPEED
        if self.y < 0:
            self.alive = False

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x + 20, self.y, 5, 10))

class AlienBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.hit_count = 0

    def update(self):
        self.y += ALIEN_BULLET_SPEED
        if self.y > HEIGHT:
            self.alive = False

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x + 15, self.y, 5, 10))

def main():
    player = Player()
    aliens = []
    bullets = []
    alien_bullets = []
    clock = pygame.time.Clock()
    running = True
    score = 0
    alien_spawn_counter = 0

    def create_alien():
        x = random.randint(0, WIDTH - 40)
        return Alien(x, 0)

    for _ in range(ALIEN_COLUMNS):
        aliens.append(create_alien())

    while running:
        screen.blit(background_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-player.speed)
        if keys[pygame.K_RIGHT]:
            player.move(player.speed)
        if keys[pygame.K_SPACE]:
            bullets.append(Bullet(player.x, player.y))

        player.update_energy()
        player.draw()

        for bullet in bullets[:]:
            bullet.update()
            if bullet.alive:
                bullet.draw()
            else:
                bullets.remove(bullet)

        for alien in aliens[:]:
            if alien.alive:
                alien.move_toward_player(INITIAL_ALIEN_SPEED)
                alien.draw()
                bullet = alien.shoot()
                if bullet:
                    alien_bullets.append(bullet)

                if (alien.x < player.x + 50) and (alien.x + 40 > player.x) and (alien.y + 30 >= player.y):
                    print("Game Over!")
                    pygame.quit()
                    return

                if alien.y >= HEIGHT:
                    alien.alive = False
                    score -= POINTS_LOST_PER_ALIEN

        for alien_bullet in alien_bullets[:]:
            alien_bullet.update()
            if alien_bullet.alive:
                alien_bullet.draw()
                if (alien_bullet.x + 15 > player.x) and (alien_bullet.x + 20 < player.x + 50) and (alien_bullet.y + 10 > player.y):
                    print("Game Over!")
                    pygame.quit()
                    return
            else:
                alien_bullets.remove(alien_bullet)

        for bullet in bullets[:]:
            for alien in aliens:
                if (bullet.x + 20 > alien.x) and (bullet.x < alien.x + 40) and (bullet.y < alien.y + 30):
                    alien.hit_count += 1
                    bullets.remove(bullet)
                    if alien.hit_count >= 6:
                        alien.alive = False
                        score += SCORE_PER_ALIEN
                    break

        for bullet in bullets[:]:
            for alien_bullet in alien_bullets[:]:
                if (bullet.x + 20 > alien_bullet.x) and (bullet.x < alien_bullet.x + 5) and (bullet.y < alien_bullet.y + 10):
                    alien_bullet.hit_count += 1
                    bullets.remove(bullet)
                    if alien_bullet.hit_count >= 3:
                        alien_bullet.alive = False
                    break

        aliens = [alien for alien in aliens if alien.alive]
        alien_bullets = [alien_bullet for alien_bullet in alien_bullets if alien_bullet.alive]

        alien_spawn_counter += 1
        if alien_spawn_counter >= ALIEN_SPAWN_INTERVAL:
            aliens.append(create_alien())
            alien_spawn_counter = 0

        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        energy_text = font.render(f"Energy: {int(player.energy)}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(energy_text, (10, 40))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
