import pygame
import os
import main_menu.menu as menu
import main_menu.button as button
import enemy.enemy as enemy
import random

pygame.init()

current_path = os.path.dirname(__file__)

display_width = 1920
display_height = 1080

time = 0
enemies = []
diff = 1

path_map1 = [[(1210, 265), (1137, 435), (974, 568), (974, 760), (1219, 809), (1456, 852), (1772, 894), (1915, 903), (1919, 894)]
, [(1210, 254), (1146, 396), (1036, 540), (922, 558), (784, 489), (633, 426), (587, 303), (512, 153), (318, 113), (264, 32), (258, 0)]
, [(1215, 260), (1151, 352), (1109, 473), (976, 552), (847, 519), (693, 463), (554, 412), (442, 404), (357, 516), (195, 725), (51, 732), (0, 732)]
]

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

music_images = [pygame.image.load(current_path + "/images/td-gui/PNG/menu/button_music" + img + ".png")
                for img in ["", "_off"]]

icon_images = [pygame.image.load(current_path + "/images/td-gui/PNG/upgrade/ico_" + str(i) + ".png")
               for i in [5, 9, 13, 17, 18, 19, 20, 21, 22, 24]]

close_imgs = [pygame.image.load(current_path + "/images/td-gui/PNG/" + i + ".png")
              for i in ["settings/button_close", "levels/btton_empty"]]


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

    bg = pygame.image.load(current_path + "/images/bg1.jpg")

    zip_cnt = 100
    je_cnt = 500
    heart_cnt = 100

    while game:
        time += 1
        pygame.time.delay(30)
        display.blit(bg, (0, 0))

        if menu_true:
            menu1 = menu.Menu(display)

            map_img, dif_img, music_img, menu_true = menu1.run_menu()
            bg = map_image[map_img]

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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_close.pressed(mouse_position):
                        game = False
                    if button_archer.pressed(mouse_position):
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

            zip_cnt = min(max(0, zip_cnt), 100)
            je_cnt = min(max(0, je_cnt), 999)
            heart_cnt = min(max(0, heart_cnt), 100)

            if (time % 10 == 0):
                path = random.randint(0, 2)
                new_enemy = enemy.Enemy(path_map1[path][0][0], path_map1[path][0][1], path_map1[path][-1][0], path_map1[path][-1][1], 10 * hard, 1 * hard, path)
                enemies.append(new_enemy)
            if (time % 100 == 0):
                hard += 1
            
            for enemy in enemies:
                if enemy.x == trace[enemy.path][-1][0] and enemy.y == trace[enemy.path][-1][1]:
                    enemies.remove(enemy)
                    heart_cnt -= 10
                enemy.move()

                
        pygame.display.flip()

    pygame.quit()


run_game()
