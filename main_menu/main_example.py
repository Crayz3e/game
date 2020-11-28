import pygame
import os
import main_menu.menu as menu

pygame.init()

current_path = os.path.dirname(__file__)

ind = current_path.find("main_menu/")

current_path = current_path[:ind - len("main_menu/") + 1:]

display_width = 1920
display_height = 1080

display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption('For!')

map_image = [pygame.image.load(current_path + f"/images/td-tileset3/PNG/game_background_{str(i)}"
                                              f"/game_background_{str(i)}.png")
             for i in range(1, 5)]

# bg = pygame.image.load(current_path + "/images/td-gui/PNG/menu/bg.png")


def run_game():
    game = True
    menu_true = True

    bg = pygame.image.load(current_path + "/images/bg1.jpg")

    while game:
        pygame.time.delay(30)
        display.fill([255, 255, 255])
        display.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                break

        if menu_true:

            menu1 = menu.Menu(display)

            map_img, dif_img, music_img, menu_true = menu1.run_menu()
            bg = map_image[map_img]

        pygame.display.flip()

    pygame.quit()


run_game()
