import pygame
import sys
from gun import Gun
from bullet import Bullet
from star import Star

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Космическая война")
    bg_color = (0, 0, 0)
    clock = pygame.time.Clock()
    gun = Gun(screen)
    bullets = pygame.sprite.Group()
    stars = pygame.sprite.Group()
    score = 0
    font = pygame.font.SysFont(None, 48)

    # Таймер появления новых звёздочек
    STAR_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(STAR_EVENT, 1000)

    def check_collisions(bullets, stars, score):
        collisions = pygame.sprite.groupcollide(stars, bullets, True, True)
        if collisions:
            score += 1
        return score

    def show_score(score):
        text = font.render(f"Счёт: {score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == STAR_EVENT:
                new_star = Star(screen)
                stars.add(new_star)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)
                elif event.key == pygame.K_RIGHT:
                    gun.moving_right = True
                elif event.key == pygame.K_LEFT:
                    gun.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    gun.moving_right = False
                elif event.key == pygame.K_LEFT:
                    gun.moving_left = False

        # Обновление объектов
        gun.update()
        bullets.update()
        stars.update()
        score = check_collisions(bullets, stars, score)

        # Отрисовка
        screen.fill(bg_color)
        gun.output()
        bullets.draw(screen)
        stars.draw(screen)
        show_score(score)
        pygame.display.flip()

# Запуск игры
run()