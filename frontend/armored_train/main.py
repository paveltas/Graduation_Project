import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

background_image = pygame.image.load("game/assets/images/background.jpg").convert()

font_title = pygame.font.Font("game/assets/fonts/Oswald-Light.ttf", 72)
font_label = pygame.font.Font("game/assets/fonts/Oswald-Light.ttf", 36)
font_input = pygame.font.Font("game/assets/fonts/Oswald-Light.ttf", 36)

WHITE = (255, 255, 255)

username = ""
password = ""
active_input_box = None

input_boxes = [
    {
        'rect': pygame.Rect(800, 400, 400, 50),
        'active': False,
        'text': ''
    },
    {
        'rect': pygame.Rect(800, 500, 400, 50),
        'active': False,
        'text': ''
    }
]

auth_button_rect = pygame.Rect(800, 600, 200, 50)
auth_button_active = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                for box in input_boxes:
                    if box['rect'].collidepoint(mouse_pos):
                        box['active'] = True
                        active_input_box = box
                    else:
                        box['active'] = False
                        active_input_box = None
                if auth_button_rect.collidepoint(mouse_pos):
                    username = input_boxes[0]['text']
                    password = input_boxes[1]['text']
                    input_boxes[0]['text'] = ''
                    input_boxes[1]['text'] = ''

        elif event.type == pygame.KEYDOWN:
            if active_input_box:
                if event.key == pygame.K_RETURN:
                    active_input_box['text'] = ''
                elif event.key == pygame.K_BACKSPACE:
                    active_input_box['text'] = active_input_box['text'][:-1]
                elif len(active_input_box['text']) < 20:
                    active_input_box['text'] += event.unicode

    screen.blit(background_image, (0, 0))

    title_text = font_title.render("Авторизация", True, WHITE)
    screen.blit(title_text, (750, 100))

    username_label = font_label.render("Username:", True, WHITE)
    password_label = font_label.render("Password:", True, WHITE)
    screen.blit(username_label, (600, 400))
    screen.blit(password_label, (600, 500))

    for box in input_boxes:
        color = (255, 0, 0) if box['active'] else (0, 0, 0)
        pygame.draw.rect(screen, color, box['rect'], 2)

    username_input = font_input.render(input_boxes[0]['text'], True, WHITE)
    password_input = font_input.render("*" * len(input_boxes[1]['text']), True, WHITE)
    screen.blit(username_input, (800, 400))
    screen.blit(password_input, (800, 500))

    auth_button_color = (255, 0, 0) if auth_button_active else (0, 0, 0)
    pygame.draw.rect(screen, auth_button_color, auth_button_rect, 2)
    auth_button_text = font_label.render("Авторизация", True, WHITE)
    screen.blit(auth_button_text, (810, 610))

    pygame.display.flip()

pygame.quit()
