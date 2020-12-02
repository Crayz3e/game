import pygame
import os
from main_menu.button import Button

current_path = os.path.dirname(__file__)

ind = current_path.find("main_menu/")

current_path = current_path[:ind - len("main_menu/") + 1:]

map_image = [pygame.transform.scale(pygame.image.load(current_path + f"/images/td-tileset3/PNG/game_background_{str(i)}"
                                                                     f"/game_background_{str(i)}.png"), (250, 150))
             for i in range(1, 5)]

battle_image = pygame.image.load(current_path + "/images/td-gui/PNG/interface_game/button_start.png")

difficulty_image = [
    pygame.image.load(current_path + "/images/td-gui/PNG/difficulty/button_" + dif + ".png")
    for dif in ["easy", "normal", "hard"]]


chose_image = [
    pygame.image.load(current_path + "/images/td-gui/PNG/levels/button_" + img + ".png") for img in ["right", "left"]]

menu_images = [pygame.image.load(current_path + "/images/td-gui/PNG/menu/" + img + ".png")
               for img in ["logo", "bg", "button_play", "rope_small"]]

settings_images = [pygame.image.load(current_path + "/images/td-gui/PNG/settings/" + img + ".png")
                   for img in ["table", "button_close"]]

music_images = [pygame.image.load(current_path + "/images/td-gui/PNG/menu/button_music" + img + ".png")
                for img in ["", "_off"]]


class Menu:
    def __init__(self, display):
        self.display = display
        self.width = self.display.get_width()
        self.height = self.display.get_height()
        self.game_name = pygame.image.load(current_path + "/images/New-Project.png")
        self.play_image = pygame.transform.scale(pygame.image.load(current_path + "/images/play.png"), (300, 300))
        self.bg = pygame.image.load(current_path + "/images/bg1.jpg")
        self.table_image = pygame.transform.scale(settings_images[0], (1200, 780))
        self.map_images = map_image
        self.difficulty_images = difficulty_image
        self.rope_image = menu_images[3]
        self.start_image = battle_image
        self.chose_images = chose_image
        self.close_image = settings_images[1]
        self.empty_image = pygame.transform.scale(
            pygame.image.load(current_path + "/images/td-gui/PNG/levels/table.png"), (270, 170))
        self.empty_button = pygame.image.load(current_path + "/images/td-gui/PNG/levels/btton_empty.png")
        self.music_images = music_images

    def run_menu(self):
        run = True
        level_table = False

        self.display.blit(self.bg, (0, 0))

        name_position = (20, self.height / 2 - self.game_name.get_height() - 150)
        self.display.blit(self.game_name, name_position)

        play_pos = (20 + self.game_name.get_width() / 2 - self.play_image.get_width() / 2,
                    self.height / 2 + self.play_image.get_height() / 2)

        button_play = Button(play_pos, self.play_image.get_width(), self.play_image.get_height(), self.play_image)
        button_play.draw(self.display)

        ind_map = 0
        ind_dif = 1
        ind_music = 0

        pygame.mixer.music.load(current_path + "/music/Rihanna.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                mouse_position = pygame.mouse.get_pos()

                button_play = Button(play_pos, self.play_image.get_width(), self.play_image.get_height(),
                                     self.play_image)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_play.pressed(mouse_position):
                        del button_play
                        self.play(name_position, play_pos)

                        level_table = self.level()

                if level_table:
                    start_position = (self.width / 2 - self.start_image.get_width() / 2,
                                      self.height / 2 + self.table_image.get_height() / 2
                                      - 1.5 * self.start_image.get_height())

                    close_frame_position = (self.width / 2 + self.music_images[0].get_width() + 50,
                                            self.height / 2 + self.table_image.get_height() / 2
                                            - 1.5 * self.start_image.get_height())

                    next1_position = (self.width / 2 + self.music_images[0].get_width() + 50,
                                      self.height / 2 - self.table_image.get_height() + 321 + self.map_images[
                                          0].get_height())

                    prev1_position = (self.width / 2 - self.music_images[0].get_width() * 2 - 50,
                                      self.height / 2 - self.table_image.get_height() + 321 + self.map_images[
                                          0].get_height())

                    next2_position = (self.width / 2 + self.music_images[0].get_width() + 50,
                                      self.height / 2 - self.difficulty_images[1].get_height() / 2)

                    prev2_position = (self.width / 2 - self.music_images[0].get_width() * 2 - 50,
                                      self.height / 2 - self.difficulty_images[1].get_height() / 2)

                    button_start = Button(start_position, self.start_image.get_width(),
                                          self.start_image.get_height(), self.start_image)

                    button_close = Button(close_frame_position, self.empty_button.get_width(),
                                          self.empty_button.get_height(), self.empty_button)

                    button_next_1 = Button(next1_position, self.chose_images[0].get_width(),
                                           self.chose_images[0].get_height(), self.chose_images[0])

                    button_prev_1 = Button(prev1_position, self.chose_images[0].get_width(),
                                           self.chose_images[0].get_height(), self.chose_images[1])

                    button_next_2 = Button(next2_position, self.chose_images[0].get_width(),
                                           self.chose_images[0].get_height(), self.chose_images[0])

                    button_prev_2 = Button(prev2_position, self.chose_images[0].get_width(),
                                           self.chose_images[0].get_height(), self.chose_images[1])

                    music_position = (self.width / 2 - self.music_images[0].get_width() * 2 - 50,
                                      self.height / 2 + self.table_image.get_height() / 2 -
                                      1.5 * self.start_image.get_height())

                    button_music = Button(music_position, self.music_images[0].get_width(),
                                          self.music_images[0].get_height(), self.music_images[0])

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if button_close.pressed(mouse_position):
                            self.display.blit(pygame.image.load(current_path + "/images/bg.jpg"), (0, 0))
                            run = False

                        if button_next_1.pressed(mouse_position):
                            ind_map = (ind_map + 1) % 4
                            self.draw_menu(ind_map, ind_dif, ind_music)

                        if button_prev_1.pressed(mouse_position):
                            ind_map = (ind_map - 1) % 4
                            self.draw_menu(ind_map, ind_dif, ind_music)

                        if button_next_2.pressed(mouse_position):
                            ind_dif = (ind_dif + 1) % 3
                            self.draw_menu(ind_map, ind_dif, ind_music)

                        if button_prev_2.pressed(mouse_position):
                            ind_dif = (ind_dif - 1) % 3
                            self.draw_menu(ind_map, ind_dif, ind_music)

                        if button_music.pressed(mouse_position):
                            ind_music = (ind_music + 1) % 2
                            if ind_music:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()
                            self.draw_menu(ind_map, ind_dif, ind_music)

                        if button_start.pressed(mouse_position):
                            del button_close
                            del button_music
                            del button_next_2
                            del button_next_1
                            del button_prev_1
                            del button_prev_2
                            del button_start

                            self.game_name = None
                            self.play_image = None
                            self.bg = None
                            self.table_image = None
                            self.map_images = None
                            self.difficulty_images = None
                            self.rope_image = None
                            self.start_image = None
                            self.chose_images = None
                            self.close_image = None
                            self.empty_image = None
                            self.empty_button = None
                            self.music_images = None

                            return ind_map, ind_dif, False, True

            pygame.display.flip()

        return ind_map, ind_dif, False, False

        pygame.quit()

    def level(self):
        table_y0 = -900  # -3600 for chain
        table_y = self.height / 2 - self.table_image.get_height() / 2

        while table_y0 <= table_y:
            self.display.blit(self.bg, (0, 0))
            dy = table_y0 - table_y

            table_position = (self.width / 2 - self.table_image.get_width() / 2,
                              self.height / 2 - self.table_image.get_height() / 2 + dy)
            self.display.blit(self.table_image, table_position)

            rope1_position = (self.width / 2 - self.table_image.get_width() / 2 + 40,
                              self.height / 2 - self.table_image.get_height() + 80 + dy)
            self.display.blit(self.rope_image, rope1_position)

            rope2_position = (self.width / 2 + self.table_image.get_width() / 2 - 80,
                              self.height / 2 - self.table_image.get_height() + 80 + dy)
            self.display.blit(self.rope_image, rope2_position)

            empty_position = (self.width / 2 - self.empty_image.get_width() / 2 + 1,
                              self.height / 2 - self.table_image.get_height() + 321 + self.map_images[
                                  0].get_height() + dy)
            self.display.blit(self.empty_image, empty_position)

            map_position = (self.width / 2 - self.map_images[0].get_width() / 2,
                            self.height / 2 - self.table_image.get_height() + self.map_images[0].get_height()
                            + 329 + dy)
            self.display.blit(self.map_images[0], map_position)

            dif_position = (self.width / 2 - self.difficulty_images[0].get_width() / 2,
                            self.height / 2 - self.difficulty_images[1].get_height() / 2 + dy)
            self.display.blit(self.difficulty_images[1], dif_position)

            start_position = (self.width / 2 - self.start_image.get_width() / 2,
                              self.height / 2 - self.table_image.get_height() / 2 + self.table_image.get_height()
                              - 1.5 * self.start_image.get_height() + dy)
            self.display.blit(self.start_image, start_position)

            music_position = (self.width / 2 - self.music_images[0].get_width() * 2 - 50,
                              self.height / 2 + self.table_image.get_height() / 2 -
                              1.5 * self.start_image.get_height() + dy)
            self.display.blit(self.music_images[0], music_position)

            close_frame_position = (self.width / 2 + self.music_images[0].get_width() + 50,
                                    self.height / 2 + self.table_image.get_height() / 2 -
                                    1.5 * self.start_image.get_height() + dy)
            self.display.blit(self.empty_button, close_frame_position)

            close_position = (self.width / 2 + self.music_images[0].get_width() + 85,
                              self.height / 2 + self.table_image.get_height() / 2 -
                              1.5 * self.start_image.get_height() + 32 + dy)
            self.display.blit(self.close_image, close_position)

            next1_position = (self.width / 2 + self.music_images[0].get_width() + 50,
                              self.height / 2 - self.table_image.get_height() + 321
                              + self.map_images[0].get_height() + dy)
            self.display.blit(self.chose_images[0], next1_position)

            prev1_position = (self.width / 2 - self.music_images[0].get_width() * 2 - 50,
                              self.height / 2 - self.table_image.get_height() + 321
                              + self.map_images[0].get_height() + dy)
            self.display.blit(self.chose_images[1], prev1_position)

            next2_position = (self.width / 2 + self.music_images[0].get_width() + 50,
                              self.height / 2 - self.difficulty_images[1].get_height() / 2 + dy)
            self.display.blit(self.chose_images[0], next2_position)

            prev2_position = (self.width / 2 - self.music_images[0].get_width() * 2 - 50,
                              self.height / 2 - self.difficulty_images[1].get_height() / 2 + dy)
            self.display.blit(self.chose_images[1], prev2_position)

            table_y0 += 30

            pygame.display.flip()
        else:
            return True

    def play(self, position1: tuple, position2: tuple):
        speed = 30
        p1 = position1[1]
        p2 = position2[1]

        while (p1 + self.game_name.get_height()) > 0 or p2 < 1080:
            self.display.blit(self.bg, (0, 0))
            self.display.blit(self.game_name, (position1[0], p1))
            self.display.blit(self.play_image, (position2[0], p2))

            p1 -= speed
            p2 += speed

            pygame.display.flip()

    def draw_menu(self, ind_map: int, ind_dif: int, ind_music: int):
        self.display.blit(self.bg, (0, 0))

        table_position = (self.width / 2 - self.table_image.get_width() / 2,
                          self.height / 2 - self.table_image.get_height() / 2)
        self.display.blit(self.table_image, table_position)

        rope1_position = (self.width / 2 - self.table_image.get_width() / 2 + 40,
                          self.height / 2 - self.table_image.get_height() + 80)
        self.display.blit(self.rope_image, rope1_position)

        rope2_position = (self.width / 2 + self.table_image.get_width() / 2 - 80,
                          self.height / 2 - self.table_image.get_height() + 80)
        self.display.blit(self.rope_image, rope2_position)

        empty_position = (self.width / 2 - self.empty_image.get_width() / 2 + 1,
                          self.height / 2 - self.table_image.get_height() + 321 + self.map_images[0].get_height())
        self.display.blit(self.empty_image, empty_position)

        map_position = (self.width / 2 - self.map_images[0].get_width() / 2,
                        self.height / 2 - self.table_image.get_height() + self.map_images[0].get_height() + 329)
        self.display.blit(self.map_images[ind_map], map_position)

        dif_position = (self.width / 2 - self.difficulty_images[0].get_width() / 2,
                        self.height / 2 - self.difficulty_images[1].get_height() / 2)
        self.display.blit(self.difficulty_images[ind_dif], dif_position)

        start_position = (self.width / 2 - self.start_image.get_width() / 2,
                          self.height / 2 - self.table_image.get_height() / 2 + self.table_image.get_height()
                          - 1.5 * self.start_image.get_height())
        self.display.blit(self.start_image, start_position)

        music_position = (self.width / 2 - self.music_images[0].get_width() * 2 - 50,
                          self.height / 2 + self.table_image.get_height() / 2 -
                          1.5 * self.start_image.get_height())
        self.display.blit(self.music_images[ind_music], music_position)

        close_frame_position = (self.width / 2 + self.music_images[0].get_width() + 50,
                                self.height / 2 + self.table_image.get_height() / 2 -
                                1.5 * self.start_image.get_height())
        self.display.blit(self.empty_button, close_frame_position)

        close_position = (self.width / 2 + self.music_images[0].get_width() + 85,
                          self.height / 2 + self.table_image.get_height() / 2 -
                          1.5 * self.start_image.get_height() + 32)
        self.display.blit(self.close_image, close_position)

        next1_position = (self.width / 2 + self.music_images[0].get_width() + 50,
                          self.height / 2 - self.table_image.get_height() + 321
                          + self.map_images[0].get_height())
        self.display.blit(self.chose_images[0], next1_position)

        prev1_position = (self.width / 2 - self.music_images[0].get_width() * 2 - 50,
                          self.height / 2 - self.table_image.get_height() + 321
                          + self.map_images[0].get_height())
        self.display.blit(self.chose_images[1], prev1_position)

        next2_position = (self.width / 2 + self.music_images[0].get_width() + 50,
                          self.height / 2 - self.difficulty_images[1].get_height() / 2)
        self.display.blit(self.chose_images[0], next2_position)

        prev2_position = (self.width / 2 - self.music_images[0].get_width() * 2 - 50,
                          self.height / 2 - self.difficulty_images[1].get_height() / 2)
        self.display.blit(self.chose_images[1], prev2_position)

        pygame.display.flip()
