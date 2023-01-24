import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    # Initialize game , settings and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(size=(ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)

    bullets = Group()
    aliens = Group()
    play_button = Button(ai_settings, screen, "Play")
    # Start main loop for the game
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullet(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings,screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


if __name__ == "__main__":
    run_game()
