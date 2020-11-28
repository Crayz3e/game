import pygame
import os
import game.main_menu.menu as menu

pygame.init()

current_path = os.path.dirname(__file__)

display_width = 1920
display_height = 1080

path_map1 = [[(1210, 265), (1210, 265), (1210, 265), (1137, 435), (1137, 435), (1137, 435), (974, 568), (974, 568), (974, 568), (974, 760), (974, 760), (974, 760), (1219, 809), (1219, 809), (1219, 809), (1456, 852), (1456, 852), (1772, 894), (1772, 894), (1915, 903), (1915, 903), (1915, 903), (1919, 894), (1919, 894)]
, [(1210, 254), (1210, 254), (1146, 396), (1146, 396), (1036, 540), (922, 558), (922, 558), (784, 489), (784, 489), (784, 489), (633, 426), (633, 426), (633, 426), (587, 303), (587, 303), (512, 153), (512, 153), (512, 153), (318, 113), (318, 113), (318, 113), (264, 32), (264, 32), (264, 32), (258, 0), (258, 0), (258, 0), (258, 0), (258, 0)]
, [(1215, 260), (1215, 260), (1151, 352), (1151, 352), (1151, 352), (1109, 473), (1109, 473), (976, 552), (976, 552), (847, 519), (847, 519), (693, 463), (693, 463), (554, 412), (554, 412), (442, 404), (442, 404), (357, 516), (357, 516), (195, 725), (195, 725), (195, 725), (51, 732), (51, 732), (0, 732), (0, 732), (0, 732)]
]

display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption('For!')

difficulty = [1, 2, 4]

map_image = [pygame.image.load(current_path + f"/images/td-tileset3/PNG/game_background_{str(i)}"
                                              f"/game_background_{str(i)}.png")
             for i in range(1, 5)]


def run_game():
    game = True
    menu_true = True

    bg = pygame.image.load(current_path + "/images/bg1.jpg")

    while game:
        pygame.time.delay(30)
        display.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                break

        if menu_true:
            menu1 = menu.Menu(display)

            map_ind, dif_img, music_img, menu_true = menu1.run_menu()
            bg = map_image[map_ind]

        pygame.display.flip()

    pygame.quit()


run_game()
