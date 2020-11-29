import pygame
import os
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

enemy_img0 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_000.png")
enemy_img1 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_002.png")
enemy_img2 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_004.png")
enemy_img3 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_005.png")
enemy_img4 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_006.png")
enemy_img5 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_007.png")
enemy_img6 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_009.png")
enemy_img7 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_011.png")
enemy_img8 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_013.png")
enemy_img9 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_015.png")
enemy_img10 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_017.png")
enemy_img11 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_run_019.png")

enemy_die0 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_000.png")
enemy_die1 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_002.png")
enemy_die2 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_004.png")
enemy_die3 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_005.png")
enemy_die4 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_006.png")
enemy_die5 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_007.png")
enemy_die6 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_009.png")
enemy_die7 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_011.png")
enemy_die8 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_013.png")
enemy_die9 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_015.png")
enemy_die10 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_017.png")
enemy_die11 = pygame.image.load(current_path + f"/images/monster-enemy-game-sprites/PNG/1/1_enemies_1_die_019.png")

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


def add_tower(event):
    tower_img = pygame.image.load(current_path + "/images/arch_towers/11.png")
    not_clicked = True

    while not_clicked:
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            display.blit(tower_img, (x, y))

            if event.type == pygame.MOUSEBUTTONUP:
                tw = ArcherTower(x - tower_img.get_width(), y - tower_img.get_height())
                archer_towers.append(tw)
                not_clicked = False


def run_game():
    game = True
    menu_true = True

    bg = pygame.image.load(current_path + "/images/bg1.jpg")

    zip_cnt = 50
    je_cnt = 300
    heart_cnt = 100

    time = 0
    enemies = []
    hard = 1
    position = 0

    while game:
        time += 1
        pygame.time.delay(30)
        display.blit(bg, (0, 0))

        if not heart_cnt:
            failed = pygame.image.load(current_path + "/images/td-gui/PNG/failed/header_failed.png")
            display.blit(failed, (960 - failed.get_width() / 2, 540 - failed.get_height() / 2))
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

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if button_close.pressed(mouse_position):
                        game = False
                    if button_archer.pressed(mouse_position):
                        if zip_cnt >= 50:
                            zip_cnt -= 50
                            add_tower(event)
                        print('archer')
                    if button_magic.pressed(mouse_position):
                        print('magic')
                    if button_stone.pressed(mouse_position):
                        print('stones')
                    if button_fire.pressed(mouse_position):
                        print('fire')
                    if button_lightning.pressed(mouse_position):
                        print('lightning')
                    if button_armour_red.pressed(mouse_position):
                        print('armour redaction')
                    if button_acid.pressed(mouse_position):
                        print('acid')
                    if button_freeze.pressed(mouse_position):
                        print('freeze')
                    if button_time.pressed(mouse_position):
                        print('time stop')
                    if button_stones.pressed(mouse_position):
                        print('stones')

            if time % 100:
                zip_cnt += (3 - dif_ind)
                je_cnt += (3 - dif_ind)

            zip_cnt = min(max(0, zip_cnt), 100)
            je_cnt = min(max(0, je_cnt), 999)
            heart_cnt = min(max(0, heart_cnt), 100)

            if time % 70 == 0:
                path = 0
                new_enemy = Enemy(path_map1[path][0][0], path_map1[path][0][1], path_map1[path][-1][0],
                                  path_map1[path][-1][1], 50 * hard, 5 * hard, 0, path)
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
                    display.blit(pygame.transform.scale(enemy_die0, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
                    display.blit(pygame.transform.scale(enemy_die1, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
                    display.blit(pygame.transform.scale(enemy_die2, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
                    display.blit(pygame.transform.scale(enemy_die3, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
                    display.blit(pygame.transform.scale(enemy_die4, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
                    display.blit(pygame.transform.scale(enemy_die5, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
                    display.blit(pygame.transform.scale(enemy_die6, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
                    display.blit(pygame.transform.scale(enemy_die7, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
                    display.blit(pygame.transform.scale(enemy_die8, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
                    display.blit(pygame.transform.scale(enemy_die9, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
                    display.blit(pygame.transform.scale(enemy_die10, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
                    display.blit(pygame.transform.scale(enemy_die11, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
                    enemies.remove(enemy1)

            if position % 12 == 0:
                for enemy1 in enemies:
                    display.blit(pygame.transform.scale(enemy_img0, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
            elif position % 12 == 1:
                for enemy1 in enemies:
                    display.blit(pygame.transform.scale(enemy_img1, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
            elif position % 12 == 2:
                for enemy1 in enemies:
                    display.blit(pygame.transform.scale(enemy_img2, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
            elif position % 12 == 3:
                for enemy1 in enemies:
                    display.blit(pygame.transform.scale(enemy_img3, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
            elif position % 12 == 4:
                for enemy1 in enemies:
                    display.blit(pygame.transform.scale(enemy_img4, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
            elif position % 12 == 5:
                for enemy1 in enemies:
                    display.blit(pygame.transform.scale(enemy_img5, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
            elif position % 12 == 6:
                for enemy1 in enemies:
                    display.blit(pygame.transform.scale(enemy_img6, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
            elif position % 12 == 7:
                for enemy1 in enemies:
                    display.blit(pygame.transform.scale(enemy_img7, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
            elif position % 12 == 8:
                for enemy1 in enemies:
                    display.blit(pygame.transform.scale(enemy_img8, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
            elif position % 12 == 9:
                for enemy1 in enemies:
                    display.blit(pygame.transform.scale(enemy_img9, (150, 130)), (enemy1.x - 70, enemy1.y - 70))
            elif position % 12 == 10:
                for enemy1 in enemies:
                    display.blit(pygame.transform.scale(enemy_img10, (150, 130)), (enemy1.x - 70, enemy1.y - 70))              
            elif position % 12 == 11:
                for enemy1 in enemies:
                    display.blit(pygame.transform.scale(enemy_img11, (150, 130)), (enemy1.x - 70, enemy1.y - 70))  
            position += 1

        pygame.display.flip()

    pygame.quit()


run_game()
