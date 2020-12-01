import pygame
import os
import math
import main_menu.menu as menu
import main_menu.button as button
from enemy.enemy import Enemy
from tower.tower_archer import ArcherTower

pygame.init()

current_path = os.path.dirname(__file__)

display_width = 1920
display_height = 1080

path_map1 = [[(1, 726), (208, 729), (294, 693), (341, 592), (371, 473), (467, 397), (583, 396), (685, 460), (815, 479),
              (900, 572), (1001, 565), (1104, 522), (1145, 425), (1159, 327), (1184, 273), (1234, 249)]]

path_map2 = [[(0, 630), (290, 618), (650, 646), (1040, 600), (1358, 687), (1611, 484), (1752, 363), (1919, 377),
              (1844, 77)]]

path_map3 = [[(0, 134), (79, 277), (166, 450), (435, 496), (661, 541), (891, 583), (1028, 650), (1213, 588),
              (1311, 391), (1515, 319), (1737, 322), (1919, 405), (1853, 109)]]

path_map4 = [[(0, 835), (292, 795), (338, 568), (545, 470), (827, 496), (948, 685), (1132, 637), (1185, 449),
              (1422, 388), (1738, 434), (1919, 496), (1845, 103)]]

display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

map_image = [pygame.image.load(current_path + f"/images/td-tileset3/PNG/game_background_{str(i)}"
                                              f"/game_background_{str(i)}.png")
             for i in range(1, 5)]

number_images = [pygame.image.load(current_path + f"/images/td-gui/PNG/levels/num_{i}.png") for i in range(10)]

interface_images = [pygame.image.load(current_path + f"/images/td-gui/PNG/interface_game/{i}.png")
                    for i in ["table", "bg_bar", "bar_1", "bar_2", "bar_4", "table_down"]]

resources_images = [pygame.image.load(current_path + f"/images/td-gui/PNG/interface_game/{i}.png")
                    for i in ["zip", "je", "heart"]]

mini_menu_image = pygame.image.load(current_path + f"/images/td-gui/PNG/win/button_menu.png")

tower_attack_img = [pygame.image.load(current_path + f"/images/archers/{i}.png") for i in range(38, 44)]

enemy_imgs = [pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_0{i}.png")
              for i in ["00", "02", "04", "05", "06", "07", "09", "11", "13", "15", "17", "19"]]

enemy_die_img = [pygame.transform.scale
                 (pygame.image.load
                  (current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_0{i}.png"), (150, 130))
                 for i in ["00", "02", "04", "05", "06", "07", "09", "11", "13", "15", "17", "19"]]

fire_img = [pygame.transform.scale
            (pygame.image.load(current_path + f"/images/magic-effects-game-sprite/PNG/fire/1_effect_fire_0{i}.png"),
             (900, 2080))
            for i in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
                      "16", "17", "18"]]

lightning_img = [pygame.transform.scale
            (pygame.image.load(current_path + f"/images/magic-effects-game-sprite/PNG/zip/1_effect_zip_0{i}.png"),
             (900, 2080))
            for i in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]]

arm_img = [pygame.transform.scale
            (pygame.image.load(current_path + f"/images/magic-effects-game-sprite/PNG/def/1_effect_def_0{i}.png"),
             (900, 2080))
           for i in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]]

acid_img = [pygame.transform.scale
            (pygame.image.load(current_path + f"/images/magic-effects-game-sprite/PNG/rain/1_effect_rain_0{i}.png"),
             (900, 2080))
            for i in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
                      "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31",
                      "32", "33", "34", "35", "36", "37", "38", "39"]]

freeze_img = [pygame.transform.scale
            (pygame.image.load(current_path + f"/images/magic-effects-game-sprite/PNG/freeze/1_effect_freeze_0{i}.png"),
             (900, 2080))
            for i in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]]

time_img = [pygame.transform.scale
            (pygame.image.load(current_path + f"/images/magic-effects-game-sprite/PNG/time/1_effect_time_0{i}.png"),
             (900, 2080))
            for i in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]]

stones_img = [pygame.transform.scale
            (pygame.image.load(current_path + f"/images/magic-effects-game-sprite/PNG/stone/1_effect_stone_0{i}.png"),
             (900, 2080))
            for i in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
                      "16", "17"]]

music_images = [pygame.image.load(current_path + "/images/td-gui/PNG/menu/button_music" + img + ".png")
                for img in ["", "_off"]]

icon_images = [pygame.image.load(current_path + "/images/td-gui/PNG/upgrade/ico_" + str(i) + ".png")
               for i in [5, 9, 13, 17, 18, 19, 20, 21, 22, 24]]

close_imgs = [pygame.image.load(current_path + "/images/td-gui/PNG/" + i + ".png")
              for i in ["settings/button_close", "levels/btton_empty"]]

archer_towers = []


def numbers(n: int):
    arr = []

    if n == 0:
        arr = [0]

    while n != 0:
        arr.append(n % 10)
        n //= 10

    return arr[::-1]


def show_numbers(pos: tuple, n: int):
    arr = numbers(n)

    if len(arr) == 3:
        display.blit(pygame.transform.scale(number_images[arr[0]], (15, 25)), (pos[0] - 52, pos[1]))
        display.blit(pygame.transform.scale(number_images[arr[1]], (15, 25)), (pos[0] - 26, pos[1]))
        display.blit(pygame.transform.scale(number_images[arr[2]], (15, 25)), (pos[0], pos[1]))
    elif len(arr) == 2:
        display.blit(pygame.transform.scale(number_images[arr[0]], (15, 25)), (pos[0] - 26, pos[1]))
        display.blit(pygame.transform.scale(number_images[arr[1]], (15, 25)), pos)
    else:
        display.blit(pygame.transform.scale(number_images[arr[0]], (15, 25)), pos)


def run_game():
    game = True
    menu_true = True

    fire = False
    lig = False
    arm = False
    acid = False
    freeze = False
    time_magic = False
    stone_magic = False

    bg = pygame.image.load(current_path + "/images/bg1.jpg")

    zip_cnt = 50
    je_cnt = 300
    heart_cnt = 100

    time = 0
    enemies = []
    hard = 1
    position = 0

    not_clicked_archer = False
    not_clicked_stone = False
    not_clicked_magic = False

    while game:
        time += 1
        pygame.time.delay(30)
        display.blit(bg, (0, 0))

        if not heart_cnt:
            if enemies[0].speed:
                t = time
            for enemy1 in enemies:
                enemy1.speed = 0
            failed = pygame.image.load(current_path + "/images/td-gui/PNG/failed/header_failed.png")
            display.blit(failed, (960 - failed.get_width() / 2, 540 - failed.get_height()))

            if time - t == 100:
                game = False

        if menu_true:
            menu1 = menu.Menu(display)

            map_ind, dif_ind, music_img, menu_true = menu1.run_menu()
            bg = map_image[map_ind]

        else:
            table_1_position = (10, 10)
            display.blit(pygame.transform.scale(interface_images[0], (interface_images[0].get_width(), 290)),
                         table_1_position)

            zip_pos = (50, 30)
            je_pos = (50, 120)
            heart_pos = (50, 210)

            bar_zip_pos = (110, 30)
            bar_je_pos = (110, 120)
            bar_heart_pos = (110, 210)

            zip_number_pos = (450, 75)
            je_number_pos = (450, 165)
            heart_number_pos = (450, 255)

            close_pos = (1740, 10)

            table_down_pos = (-25, 955)

            icon_pos = (80, 1070 - icon_images[0].get_height())

            button_close = button.Button(close_pos, close_imgs[1].get_width(),
                                         close_imgs[1].get_height(), close_imgs[1])

            button_archer = button.Button(icon_pos, icon_images[0].get_width(),
                                          icon_images[0].get_height(), icon_images[0])

            button_stone = button.Button((icon_pos[0] + 176 * 1, icon_pos[1]), icon_images[0].get_width(),
                                         icon_images[0].get_height(), icon_images[1])

            button_magic = button.Button((icon_pos[0] + 176 * 2, icon_pos[1]), icon_images[0].get_width(),
                                         icon_images[0].get_height(), icon_images[2])

            button_fire = button.Button((icon_pos[0] + 176 * 3, icon_pos[1]), icon_images[0].get_width(),
                                        icon_images[0].get_height(), icon_images[3])

            button_lightning = button.Button((icon_pos[0] + 176 * 4, icon_pos[1]), icon_images[0].get_width(),
                                             icon_images[0].get_height(), icon_images[4])

            button_armour_red = button.Button((icon_pos[0] + 176 * 5, icon_pos[1]), icon_images[0].get_width(),
                                              icon_images[0].get_height(), icon_images[5])

            button_acid = button.Button((icon_pos[0] + 176 * 6, icon_pos[1]), icon_images[0].get_width(),
                                        icon_images[0].get_height(), icon_images[6])

            button_freeze = button.Button((icon_pos[0] + 176 * 7, icon_pos[1]), icon_images[0].get_width(),
                                          icon_images[0].get_height(), icon_images[7])

            button_time = button.Button((icon_pos[0] + 176 * 8, icon_pos[1]), icon_images[0].get_width(),
                                        icon_images[0].get_height(), icon_images[8])

            button_stones = button.Button((icon_pos[0] + 176 * 9, icon_pos[1]), icon_images[0].get_width(),
                                          icon_images[0].get_height(), icon_images[9])

            display.blit(close_imgs[1], close_pos)
            display.blit(close_imgs[0], (close_pos[0] + 35, close_pos[1] + 32))

            display.blit(interface_images[5], table_down_pos)

            display.blit(resources_images[0], zip_pos)
            display.blit(resources_images[1], je_pos)
            display.blit(resources_images[2], heart_pos)

            display.blit(interface_images[1], (105, 23))
            display.blit(interface_images[1], (105, 113))
            display.blit(interface_images[1], (105, 203))

            show_numbers(zip_number_pos, zip_cnt)
            show_numbers(je_number_pos, je_cnt)
            show_numbers(heart_number_pos, heart_cnt)

            display.blit(pygame.transform.scale(
                interface_images[2], (int(interface_images[2].get_width() / 100 * zip_cnt),
                                      interface_images[2].get_height())), bar_zip_pos)

            display.blit(pygame.transform.scale(
                interface_images[3], (int(interface_images[2].get_width() / 999 * je_cnt),
                                      interface_images[2].get_height())), bar_je_pos)

            display.blit(pygame.transform.scale(
                interface_images[4], (int(interface_images[2].get_width() / 100 * heart_cnt),
                                      interface_images[2].get_height())), bar_heart_pos)

            button_archer.draw(display)
            button_magic.draw(display)
            button_stone.draw(display)
            button_fire.draw(display)
            button_lightning.draw(display)
            button_armour_red.draw(display)
            button_acid.draw(display)
            button_freeze.draw(display)
            button_time.draw(display)
            button_stones.draw(display)

            for event in pygame.event.get():

                mouse_position = pygame.mouse.get_pos()

                if button_archer.direct():
                    show_numbers((icon_pos[0] + 176 * 0 + 90, icon_pos[1] - 30), 50)
                if button_stone.direct():
                    show_numbers((icon_pos[0] + 176 * 1 + 90, icon_pos[1] - 30), 75)
                if button_magic.direct():
                    show_numbers((icon_pos[0] + 176 * 2 + 100, icon_pos[1] - 30), 100)
                if button_fire.direct():
                    show_numbers((icon_pos[0] + 176 * 3 + 100, icon_pos[1] - 30), 100)
                if button_lightning.direct():
                    show_numbers((icon_pos[0] + 176 * 4 + 100, icon_pos[1] - 30), 100)
                if button_armour_red.direct():
                    show_numbers((icon_pos[0] + 176 * 5 + 90, icon_pos[1] - 30), 50)
                if button_acid.direct():
                    show_numbers((icon_pos[0] + 176 * 6 + 100, icon_pos[1] - 30), 100)
                if button_freeze.direct():
                    show_numbers((icon_pos[0] + 176 * 7 + 100, icon_pos[1] - 30), 75)
                if button_time.direct():
                    show_numbers((icon_pos[0] + 176 * 8 + 90, icon_pos[1] - 30), 75)
                if button_stones.direct():
                    show_numbers((icon_pos[0] + 176 * 9 + 90, icon_pos[1] - 30), 50)

                if event.type == pygame.MOUSEBUTTONUP:

                    if button_close.pressed(mouse_position):
                        game = False
                    if button_archer.pressed(mouse_position) or not_clicked_archer:
                        if je_cnt >= 50:
                            je_cnt -= 50
                            not_clicked_archer = True

                            tower_img = pygame.image.load(current_path + "/images/arch_towers/11.png")
                            display.blit(tower_img, mouse_position)

                            if event.type == pygame.MOUSEBUTTONDOWN and not button_archer.pressed(mouse_position):
                                tw = ArcherTower(mouse_position[0] - tower_img.get_width(),
                                                 mouse_position[1] - tower_img.get_height())
                                archer_towers.append(tw)
                                not_clicked_archer = False
                    if button_magic.pressed(mouse_position) or not_clicked_stone:
                        if je_cnt >= 75:
                            je_cnt -= 75
                            not_clicked_stone = True

                            tower_img = pygame.image.load(current_path + "/images/arch_towers/11.png")
                            display.blit(tower_img, mouse_position)

                            if event.type == pygame.MOUSEBUTTONDOWN and not button_archer.pressed(mouse_position):
                                tw = ArcherTower(mouse_position[0] - tower_img.get_width(),
                                                 mouse_position[1] - tower_img.get_height())
                                archer_towers.append(tw)
                                not_clicked_stone = False
                    if button_stone.pressed(mouse_position) or not_clicked_magic:
                        if je_cnt >= 100:
                            je_cnt -= 100
                            not_clicked_magic = True

                            tower_img = pygame.image.load(current_path + "/images/arch_towers/11.png")
                            display.blit(tower_img, mouse_position)

                            if event.type == pygame.MOUSEBUTTONDOWN and not button_archer.pressed(mouse_position):
                                tw = ArcherTower(mouse_position[0] - tower_img.get_width(),
                                                 mouse_position[1] - tower_img.get_height())
                                archer_towers.append(tw)
                                not_clicked_magic = False
                    if button_fire.pressed(mouse_position):
                        if zip_cnt >= 100:
                            zip_cnt -= 100
                            fire_it = 1
                            fire = True
                    if button_lightning.pressed(mouse_position):
                        if zip_cnt >= 100:
                            zip_cnt -= 100
                            lig_it = 1
                            lig = True
                    if button_armour_red.pressed(mouse_position):
                        if zip_cnt >= 50:
                            zip_cnt -= 50
                            arm_it = 1
                            arm = True
                    if button_acid.pressed(mouse_position):
                        if zip_cnt >= 100:
                            zip_cnt -= 100
                            acid_it = 1
                            acid = True
                    if button_freeze.pressed(mouse_position):
                        if zip_cnt >= 75:
                            zip_cnt -= 750
                            freeze_it = 1
                            freeze = True
                    if button_time.pressed(mouse_position):
                        if zip_cnt >= 75:
                            zip_cnt -= 75
                            time_it = 1
                            time_magic = True
                    if button_stones.pressed(mouse_position):
                        if zip_cnt >= 50:
                            zip_cnt -= 50
                            stones_it = 1
                            stone_magic = True

            if time % 7 == 0:
                zip_cnt += (3 - dif_ind)
                je_cnt += (4 - dif_ind)

            zip_cnt = min(max(0, zip_cnt), 100)
            je_cnt = min(max(0, je_cnt), 999)
            heart_cnt = min(max(0, heart_cnt), 100)

            if fire:
                display.blit(fire_img[fire_it], (600, -1300))
                fire_it += 1
                if fire_it % 19 == 0:
                    fire = False
                    for enemy1 in enemies:
                        enemy1.hp = 0
            if lig:
                display.blit(lightning_img[lig_it], (600, -1300))
                lig_it += 1
                if lig_it % 14 == 0:
                    lig = False
                    for enemy1 in enemies:
                        enemy1.hp = 0
            if arm:
                display.blit(arm_img[arm_it], (600, -1300))
                arm_it += 1
                if arm_it % 10 == 0:
                    arm = False
                    for enemy1 in enemies:
                        enemy1.hp = 0
            if acid:
                display.blit(acid_img[acid_it], (600, -1100))
                acid_it += 1
                if acid_it % 39 == 0:
                    acid = False
                    for enemy1 in enemies:
                        enemy1.hp = 0
            if freeze:
                display.blit(freeze_img[freeze_it], (600, -1300))
                freeze_it += 1
                if freeze_it % 16 == 0:
                    freeze = False
                    for enemy1 in enemies:
                        enemy1.hp = 0
            if time_magic:
                display.blit(time_img[time_it], (600, -1500))
                time_it += 1
                if time_it % 14 == 0:
                    time_magic = False
                    for enemy1 in enemies:
                        enemy1.hp = 0
            if stone_magic:
                display.blit(stones_img[stones_it], (600, -1300))
                stones_it += 1
                if stones_it % 18 == 0:
                    stone_magic = False
                    for enemy1 in enemies:
                        enemy1.hp = 0

            if time % 70 == 0:
                path = 0
                new_enemy = Enemy(path_map1[path][0][0], path_map1[path][0][1], path_map1[path][-1][0],
                                  path_map1[path][-1][1], 100 * hard, 5 * hard, 0, path)
                enemies.append(new_enemy)

            if time % 1000 == 0:
                hard += 1
            
            for enemy1 in enemies:
                if enemy1.x == path_map1[enemy1.path][-1][0] and enemy1.y == path_map1[enemy1.path][-1][1]:
                    enemies.remove(enemy1)
                    heart_cnt -= 10
                    continue
                enemy1.move(path_map1[enemy1.path], enemy1.speed)

            for enemy1 in enemies:
                if enemy1.hp <= 0:
                    display.blit(enemy_die_img[time % 11], (enemy1.x - 70, enemy1.y - 70))
                    enemies.remove(enemy1)

            for enemy1 in enemies:
                display.blit(pygame.transform.scale(enemy_imgs[position % 12], (150, 130)),
                             (enemy1.x - 70, enemy1.y - 70))

            position += 1

            for tw in archer_towers:
                display.blit(pygame.image.load(current_path + "/images/arch_towers/11.png"), (tw.x + 170, tw.y))

                if tw.attack(enemies):
                    display.blit(tower_attack_img[0 + time % 6], (tw.x + 220, tw.y - 15))
                    if time % 6 == 1 or time % 6 == 2 or time % 6 == 3:
                        display.blit(pygame.image.load(current_path + "/images/archers/37.png"),
                                     (tw.x + 270, tw.y - 15))
                else:
                    display.blit(pygame.image.load(current_path + "/images/archers/38.png"), (tw.x + 220, tw.y - 15))

            if time >= 10000:
                for enemy1 in enemies:
                    enemy1.hp = 0

                win = pygame.image.load(current_path + f"/images/td-gui/PNG/win/header_win.png")
                display.blit(win, (960 - win.get_width() / 2, 540 - win.get_height()))

            if time >= 10100:
                game = False

        pygame.display.flip()

    pygame.quit()


run_game()
