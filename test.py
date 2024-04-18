import unittest
from unittest.mock import MagicMock
from sprites import Player, SlowCar
from gameImport import mousePos, mouseButtons, Button
from scoreboard import Button, Score, getScores, setScores, setScore, updateScoreboard, scoreboardRun
import pygame as pg
import pygame
from settings import Button, mousePosScore, mouseButtonsScore, Settings, settingsRun


class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.button = Button((255, 255, 255), 100, 100, 200, 50)

    def test_button_attributes(self):
        self.assertEqual(self.button.color, (255, 255, 255))
        self.assertEqual(self.button.x, 100)
        self.assertEqual(self.button.y, 100)
        self.assertEqual(self.button.width, 200)
        self.assertEqual(self.button.height, 50)

    def test_button_draw(self):
        self.screen.fill((0, 0, 0))
        self.button.draw(self.screen)
        pygame.display.flip()
        # Manually inspect if the button is drawn

    def test_button_isOver(self):
        self.assertTrue(self.button.isOver((150, 125)))
        self.assertFalse(self.button.isOver((50, 50)))

    def test_mousePosScore(self):
        # Mocking pygame.mouse.get_pos() to return a fixed value
        pygame.mouse.get_pos = MagicMock(return_value=(400, 300))
        self.assertEqual(mousePosScore(), (400, 300))

    def test_mouseButtonsScore(self):
        # Mocking pygame.mouse.get_pressed() to return a fixed value
        pygame.mouse.get_pressed = MagicMock(return_value=(1, 0, 0))
        self.assertEqual(mouseButtonsScore(), (1, 0, 0))


class TestSettings(unittest.TestCase):
    def setUp(self):
        self.settings = Settings()

    def test_settings_attributes(self):
        self.assertEqual(self.settings.car_type, "12")
        self.assertEqual(self.settings.n, 12)
        self.assertEqual(self.settings.accelConstantHolder, 0.0015)

    def test_get_car(self):
        self.assertEqual(self.settings.get_car(), "12")

    def test_set_car(self):
        self.settings.set_car("37")
        self.assertEqual(self.settings.car_type, "37")

    def test_get_n(self):
        self.assertEqual(self.settings.get_n(), 12)

    def test_set_n(self):
        self.settings.set_n(20)
        self.assertEqual(self.settings.n, 20)

    def test_add_n(self):
        self.settings.add_n(5)
        self.assertEqual(self.settings.n, 17)

    def test_subtract_n(self):
        self.settings.subtract_n(5)
        self.assertEqual(self.settings.n, 7)

    def test_get_accConst(self):
        self.assertEqual(self.settings.get_accConst(), 0.0015)

    def test_set_accConst(self):
        self.settings.set_accConst(0.02)
        self.assertEqual(self.settings.accelConstantHolder, 0.02)



class TestScore(unittest.TestCase):

    def test_initialization(self):
        score = Score()
        self.assertEqual(score.score, 0)
        self.assertEqual(score.max_distance, 1)
        self.assertEqual(score.speed, 1)

    def test_get_board_info(self):
        score = Score(10, 20, 30)
        info = score.get_board_info()
        self.assertEqual(info, (10, 20, 30))

    def test_set_board_info(self):
        score = Score()
        score.set_board_info(10, 20, 30)
        self.assertEqual(score.score, 10)
        self.assertEqual(score.max_distance, 20)
        self.assertEqual(score.speed, 30)


class TestButton(unittest.TestCase):

    def test_mousePos(self):
        # Simply test that the function returns a tuple
        self.assertIsInstance(mousePos(), tuple)

    def test_mouseButtons(self):
        # Test that the function returns a tuple of booleans
        self.assertIsInstance(mouseButtons(), tuple)
        self.assertTrue(all(isinstance(b, bool) for b in mouseButtons()))


class TestPlayer(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.game_mock = MagicMock()
        self.game_mock.all_sprites = pg.sprite.Group()
        self.game_mock.collision = False
        self.player = Player(self.game_mock, 0, 0, 1)

    def test_player_initialization(self):
        self.assertIsInstance(self.player, Player)
        self.assertEqual(self.player.x, 0)
        self.assertEqual(self.player.y, 0)


    def test_player_move(self):
        pg.key.get_pressed = MagicMock(return_value={pg.K_RIGHT: True})

        initial_x = self.player.rect.x
        self.player.move()
        self.assertGreater(self.player.rect.x, initial_x)


class TestSlowCar(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.game_mock = MagicMock()
        self.game_mock.all_sprites = pg.sprite.Group()
        self.slow_car = SlowCar(self.game_mock, 0, 0)

    def test_slow_car_initialization(self):
        self.assertIsInstance(self.slow_car, SlowCar)
        self.assertEqual(self.slow_car.x, 0)
        self.assertEqual(self.slow_car.y, 0)

    def test_slow_car_move(self):
        initial_y = self.slow_car.rect.y
        self.slow_car.move()
        self.assertGreater(self.slow_car.rect.y, initial_y)


if __name__ == '__main__':
    unittest.main()
