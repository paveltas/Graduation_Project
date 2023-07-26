import pygame

pygame.init()

# Установка разрения экрана
screen = pygame.display.set_mode((1920, 1080))

# Загрузка фонового изображения
background_image = pygame.image.load("game/assets/images/background.jpg").convert()

# Загрузка стилизованных шрифтов
font_title = pygame.font.Font("game/assets/fonts/Oswald-Light.ttf", 72)
font_label = pygame.font.Font("game/assets/fonts/Oswald-Light.ttf", 36)
font_input = pygame.font.Font("game/assets/fonts/Oswald-Light.ttf", 36)

# Цвета
WHITE = (255, 255, 255)

# Переменные для хранения данных пользователя
username = ""
password = ""
active_input_box = None

input_boxes = [
    {
        'rect': pygame.Rect(800, 400, 400, 50),  # Поле ввода для username
        'text': '',
        'active': False  # Флаг активности поля ввода
    },
    {
        'rect': pygame.Rect(800, 500, 400, 50),  # Поле ввода для password
        'text': '',
        'active': False
    }
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левая кнопка мыши
            mouse_pos = pygame.mouse.get_pos()
            for box in input_boxes:
                if box['rect'].collidepoint(mouse_pos):
                    box['active'] = True
                    active_input_box = box
                else:
                    box['active'] = False
                    active_input_box = None

        elif event.type == pygame.KEYDOWN:
            if active_input_box:
                if event.key == pygame.K_RETURN:
                    # Обработка введенных данных пользователя
                    if active_input_box['rect'] == input_boxes[0]['rect']:
                        username = active_input_box['text']
                    elif active_input_box['rect'] == input_boxes[1]['rect']:
                        password = active_input_box['text']
                    active_input_box['text'] = ""  # Сброс текста поля ввода
                elif event.key == pygame.K_BACKSPACE:
                    active_input_box['text'] = active_input_box['text'][:-1]
                elif len(active_input_box['text']) < 20:
                    active_input_box['text'] += event.unicode

    screen.blit(background_image, (0, 0))

    # Отрисовка заголовка
    title_text = font_title.render("Авторизация", True, WHITE)
    screen.blit(title_text, (750, 100))

    # Отрисовка полей для ввода
    username_label = font_label.render("Username:", True, WHITE)
    password_label = font_label.render("Password:", True, WHITE)
    screen.blit(username_label, (600, 400))
    screen.blit(password_label, (600, 500))

    # Отрисовка рамок вокруг активных полей ввода
    for box in input_boxes:
        color = (255, 0, 0) if box['active'] else (0, 0, 0)
        pygame.draw.rect(screen, color, box['rect'], 2)

    # Отрисовка введенного текста
    username_input = font_input.render(input_boxes[0]['text'], True, WHITE)
    password_input = font_input.render("*" * len(input_boxes[1]['text']), True, WHITE)
    screen.blit(username_input, (800, 400))
    screen.blit(password_input, (800, 500))

    pygame.display.flip()

pygame.quit()
