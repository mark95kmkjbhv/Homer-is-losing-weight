# Імпортуємо клас App — основний клас для створення Kivy-програми
from kivy.app import App

# Імпортуємо Screen для створення окремих екранів
# та ScreenManager для керування і перемикання між екранами
from kivy.uix.screenmanager import Screen, ScreenManager

# Імпортуємо Window для налаштування вікна програми
from kivy.core.window import Window

# Імпортуємо Builder для роботи з KV-розміткою
from kivy.lang import Builder

# Імпортуємо Animation для створення анімацій
from kivy.animation import Animation

# Імпортуємо sp та dp для роботи з розмірами
from kivy.metrics import sp, dp

# Імпортуємо Image для роботи із зображеннями
from kivy.uix.image import Image

# Імпортуємо platform для визначення операційної системи
from kivy import platform

# Імпортуємо NumericProperty для створення числових властивостей Kivy
from kivy.properties import NumericProperty, BooleanProperty, StringProperty

# Імпортуємо Clock для виконання функцій через певний час
from kivy.clock import Clock

# Імпортуємо SoundLoader для завантаження та відтворення звуків
from kivy.core.audio import SoundLoader
from time import monotonic
import os
from kivy.storage.jsonstore import JsonStore

Builder.load_string(r"""






# Імпортуємо функцію для перетворення HEX-кольору у формат RGBA
#:import from_hex kivy.utils.get_color_from_hex

# Імпортуємо функцію rgba
#:import to_rgba kivy.utils.rgba

# Імпортуємо словник готових кольорів Kivy
#:import colormap kivy.utils.colormap


# Створюємо змінну з основним кольором кнопок
#:set main_color '#ffba00'

# Створюємо змінну з темнішим кольором кнопок
#:set main_color_dark "ffa500"


# Задаємо шрифт для віджетів
<Widget>:

    # Встановлюємо шрифт Lemon-Regular.ttf
    font_name: 'Roboto'


# Створюємо власний тип кнопки ButtonMenu
# @Button означає, що ButtonMenu успадковує Button
<ButtonMenu@Button>:

    # Встановлюємо розмір тексту кнопки
    font_size: "56sp"

    # Робимо текст жирним
    bold: True

    # Робимо стандартний фон кнопки повністю прозорим
    background_color: 0, 0, 0, 0

    # Вимикаємо автоматичне визначення розміру
    size_hint: None, None

    # Розміщуємо кнопку по центру горизонтально
    pos_hint: {"center_x": 0.5}

    # Встановлюємо ширину кнопки
    # texture_size[0] — ширина тексту
    # dp(40) — додатковий простір навколо тексту
    width: self.texture_size[0] + dp(40)


    # Малюємо власний фон кнопки перед самою кнопкою
    canvas.before:

        # Встановлюємо білий колір
        Color:
            rgba: colormap['white']

        # Створюємо зовнішній білий заокруглений прямокутник
        RoundedRectangle:

            # Розмір дорівнює розміру кнопки
            size: self.size

            # Позиція дорівнює позиції кнопки
            pos: self.pos

            # Заокруглюємо кути
            radius: [self.font_size]


        # Встановлюємо колір внутрішнього прямокутника
        # Якщо кнопка не натиснута — використовуємо main_color
        # Якщо кнопка натиснута — використовуємо main_color_dark
        Color:
            rgba: from_hex(main_color) if self.state == 'normal' else from_hex(main_color_dark)

        # Створюємо внутрішній заокруглений прямокутник
        RoundedRectangle:

            # Робимо його трохи меншим за зовнішній прямокутник
            size: self.size[0] - dp(6), self.size[1] - dp(6)

            # Зміщуємо його на 3dp,
            # щоб утворилася біла рамка
            pos: self.pos[0] + dp(3), self.pos[1] + dp(3)

            # Заокруглюємо кути
            radius: [self.font_size]


# Створюємо тип кнопки для іконок
# ButtonIcon успадковує всі властивості ButtonMenu
<ButtonIcon@ButtonMenu>:

    # Для кнопки використовуємо шрифт з іконками
    font_name: 'assets/typicons.ttf'


# Налаштовуємо екран головного меню
<Menu>:

    # Створюємо вертикальний контейнер
    BoxLayout:

        # Розташовуємо елементи зверху вниз
        orientation: "vertical"

        # Відступи від країв контейнера
        padding: "30dp"

        # Відстань між елементами
        spacing: "20dp"


        # Створюємо фон меню
        canvas:

            # Малюємо прямокутник із фоновою картинкою
            Rectangle:

                # Вказуємо шлях до картинки
                source: 'assets/images/level1.jpg'

                # Встановлюємо ширину фону 750dp
                # Висота дорівнює висоті контейнера
                size: self.size

                # Розташовуємо фон по центру
                pos: self.pos


        # Порожній віджет для створення відступу зверху
        Widget:

            # Він займає 5% доступної висоти
            size_hint_y: 0.05


        # Заголовок гри
        Label:

            # Текст заголовка
            # \n переносить текст на новий рядок
            text: "Homer\nis losing weight"
            
            color: 0,0,0,1
            bold:True

            # Розмір тексту
            font_size: "54sp"

            # Вирівнюємо текст по центру
            halign: "center"

            # Заголовок займає 15% висоти
            size_hint_y: 0.15


        # Зображення заголовка/логотипа
        Image:

            # Вказуємо шлях до картинки
            source: "assets/images/title.png"

            # Дозволяємо розтягувати зображення
            allow_stretch: True

            # Зображення займає 50% висоти
            size_hint_y: 0.5


        # Кнопка PLAY
        ButtonMenu:

            # Текст кнопки
            text: "ГРАТИ"

            # Кнопка займає 15% висоти
            size_hint_y: 0.15


            # Відкриваємо вибір рівня
            on_press: root.go_levels()


        # Контейнер для нижніх кнопок
        BoxLayout:

            # Контейнер займає 15% висоти
            size_hint_y: 0.15


            # Кнопка Settings
            ButtonIcon:

                # Unicode-код іконки налаштувань
                text: "\uE04F"

                # Викликаємо метод go_settings()
                on_press:
                    root.go_settings()


            # Порожній Widget створює простір між кнопками
            Widget:


            # Кнопка Exit
            ButtonIcon:

                # Unicode-код іконки виходу
                text: "\uE121"

                # Закриваємо програму
                on_press:
                    app.stop()


# Екран вибору рівня
<LevelSelect>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                source: "assets/images/level1.jpg"
                pos: self.pos
                size: self.size

        orientation: "vertical"
        padding: dp(24)
        spacing: dp(12)

        Label:
            text: "ОБЕРИ РІВЕНЬ"
            font_size: "36sp"
            size_hint_y: 0.18
            
            color: 0,0,0,1
            bold:True

        Label:
            text: "Пончики здобуто: " + str(app.donuts) + "\nПройди рівень за 60 с — отримай пончик"
            font_size: "18sp"
            size_hint_y: 0.16
            
            color: 0,0,0,1
            bold:True

        BoxLayout:
            size_hint_y: 0.15
            spacing: dp(12)
            ButtonMenu:
                text: "Рівень 1"
                font_size: "32sp"
                size_hint: 0.78, 1
                on_release: root.select_level(0)
            Image:
                id: level_donut_0
                source: "assets/images/donut.png"
                allow_stretch: True
                keep_ratio: True
                opacity: 1 if 0 in app.donut_levels else 0
                size_hint_x: 0.22

        BoxLayout:
            size_hint_y: 0.15
            spacing: dp(12)
            ButtonMenu:
                text: "Рівень 2"
                font_size: "32sp"
                size_hint: 0.78, 1
                on_release: root.select_level(1)
            Image:
                id: level_donut_1
                source: "assets/images/donut.png"
                allow_stretch: True
                keep_ratio: True
                opacity: 1 if 1 in app.donut_levels else 0
                size_hint_x: 0.22

        BoxLayout:
            size_hint_y: 0.15
            spacing: dp(12)
            ButtonMenu:
                text: "Рівень 3"
                font_size: "32sp"
                size_hint: 0.78, 1
                on_release: root.select_level(2)
            Image:
                id: level_donut_2
                source: "assets/images/donut.png"
                allow_stretch: True
                keep_ratio: True
                opacity: 1 if 2 in app.donut_levels else 0
                size_hint_x: 0.22

        ButtonMenu:
            text: "Назад"
            font_size: "30sp"
            size_hint_y: 0.14
            on_release: root.go_menu()


# Налаштування звуку та прогресу
<Settings>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                source: "assets/images/back_menu.jpg"
                pos: self.pos
                size: self.size

        orientation: "vertical"
        padding: dp(24)
        spacing: dp(10)

        Label:
            text: "Налаштування"
            font_size: "34sp"
            size_hint_y: 0.18

        Label:
            text: "Гучність: " + str(int(app.sound_volume * 100)) + "%"
            font_size: "25sp"
            size_hint_y: None
            height: dp(44)

        Slider:
            min: 0
            max: 1
            step: 0.1
            value: app.sound_volume
            size_hint_y: None
            height: dp(52)
            on_value: app.set_sound_volume(self.value)

        ButtonMenu:
            text: "Усі звуки: увімкнено" if app.sound_enabled else "Усі звуки: вимкнено"
            font_size: "23sp"
            size_hint: 1, 0.18
            on_release: app.toggle_sound()

        ButtonMenu:
            text: "Скинути прогрес"
            font_size: "24sp"
            size_hint: 1, 0.18
            on_release: root.reset_progress()

        ButtonMenu:
            text: "Назад"
            font_size: "28sp"
            size_hint_y: 0.16
            on_release: root.go_menu()


# Налаштування класу RotatedImage
<RotatedImage>:

    # Малюємо трансформацію перед зображенням
    canvas.before:

        # Зберігаємо поточну матрицю трансформації
        PushMatrix

        # Створюємо обертання
        Rotate:

            # Кут обертання беремо з властивості angle
            angle: self.angle

            # Обертання навколо осі Z
            axis: 0, 0, 1

            # Обертання відбувається навколо центру картинки
            origin: self.center


    # Код після малювання зображення
    canvas.after:

        # Повертаємо попередню матрицю трансформації
        PopMatrix


# Налаштовуємо клас Character
<Character>:

    # Початкове зображення персонажа
    source: 'assets/images/fish_01.png'

    # Розмір не буде визначатися автоматично
    size_hint: None, None

    # Встановлюємо розмір персонажа 200×200dp
    size: dp(200), dp(200)

    # Дозволяємо розтягувати зображення
    allow_stretch: True

    # Робимо персонаж невидимим на початку
    opacity: 0


# Налаштовуємо екран гри
<Game>:

    # Створюємо головний вертикальний контейнер
    BoxLayout:

        # Елементи розташовуються вертикально
        orientation: "vertical"

        # Відступи від країв
        padding: "30dp"

        # Відстань між елементами
        spacing: "20dp"


        # Малюємо фон гри
        canvas:

            # Створюємо прямокутник із фоновою картинкою
            Rectangle:

                # Шлях до фонового зображення
                source: app.LEVEL_BACKGROUNDS[app.LEVEL]

                # Позиція фону
                pos: self.pos
                

                # Розмір фону
                size: self.size




        # Рахунок, таймер і кнопка повернення додому
        BoxLayout:
            size_hint_y: 0.12
            Label:
            
                color:0,0,0,1
                bold: True
            
                text: str(root.score)
                font_size: "38sp"
                size_hint_x: 0.4
            Label:
                text: root.timer_text
                font_size: "26sp"
                size_hint_x: 0.4
                
                color:0,0,0,1
                bold: True
    
            ButtonIcon:
                text: '\uE08A'
                on_press: root.go_home()


        # Основна ігрова область
        FloatLayout:

            # Ігрова область займає 76% висоти
            size_hint_y: 0.76

            # ID дозволяє звертатися до цього віджета з Python
            id: game_window


            # Заголовок поточного рівня
            Label:

                # ID заголовка
                id: level_title

                # Текст заголовка
                text: 'Рівень 1'

                # Розмір тексту
                font_size: '60sp'

                # Висоту задаємо вручну
                size_hint_y: None

                # Висота залежить від фактичного розміру тексту
                height: self.texture_size[1]

                # Розташовуємо заголовок по центру горизонтально
                x: root.width / 2 - self.width / 2

                # Встановлюємо початкову позицію по вертикалі
                y: '130dp'


            # Створюємо персонажа
            Character:

                # ID персонажа
                id: character

                # Розташовуємо персонажа по центру
                center: root.center


            # Напис, який показується після завершення рівня
            Label:

                # ID напису
                id: level_complete

                # Текст напису
                # \n переносить текст на новий рядок
                text: ''

                # Встановлюємо колір через HEX
                color: from_hex('#12F3AF')

                # Розмір тексту
                font_size: '50sp'

                # Висоту задаємо вручну
                size_hint_y: None

                # Встановлюємо висоту відповідно до розміру тексту
                height: self.texture_size[1]

                # Розташовуємо напис по центру горизонтально
                x: root.width / 2 - self.width / 2

                # Розташовуємо напис по центру вертикально
                # + dp(100) зміщує його вгору
                y: root.height / 2 - self.height / 2 + dp(100)

                # На початку напис невидимий
                opacity: 0

                        # Пончик залітає у вікно, коли рівень пройдено швидко
            Image:
                id: donut_reward
                source: "assets/images/donut.png"
                allow_stretch: True
                keep_ratio: True
                size_hint: None, None
                size: dp(145), dp(145)
                opacity: 0

            # Кнопка переходу на наступний рівень або завершення гри
            ButtonMenu:
                id: next_level_button
                text: "Далі"
                pos_hint: {"center_x": 0.5, "y": 0.03}
                opacity: 0
                disabled: self.opacity == 0
                on_release: root.next_level()


        # Нижнє меню гри
        BoxLayout:

            # Нижнє меню займає 12% висоти
            size_hint_y: 0.12


            # Кнопка налаштувань
            ButtonIcon:

                # Unicode-код іконки налаштувань
                text: '\uE04F'

                # Розташовуємо кнопку внизу
                pos_hint: {'y': 0}

                # Відкриваємо налаштування
                on_release: root.open_settings()






""")


# Створюємо клас головного меню
# Клас успадковує властивості та методи Screen
class Menu(Screen):

    # Конструктор класу Menu
    # **kw приймає додаткові іменовані аргументи
    def __init__(self, **kw):
        # Викликаємо конструктор батьківського класу Screen
        super().__init__(**kw)

    # Метод для переходу до екрана гри
    # *args дозволяє приймати додаткові аргументи від події Kivy
    def go_game(self, *args):
        # Встановлюємо екран "game" як поточний
        self.manager.current = "game"

        # Встановлюємо напрямок анімації переходу — вліво
        self.manager.transition.direction = "left"

    # Починаємо нову гру з першого рівня
    def start_game(self, *args):
        app.LEVEL = 0
        self.manager.current = "game"
        self.manager.transition.direction = "left"

    # Відкриваємо екран вибору рівня
    def go_levels(self, *args):
        self.manager.transition.direction = "left"
        self.manager.current = "level_select"

    # Метод для переходу до екрана налаштувань
    def go_settings(self, *args):
        # Після налаштувань повертаємося до меню
        self.manager.get_screen("settings").return_screen = "menu"
        self.manager.current = "settings"

        # Встановлюємо напрямок анімації переходу — вгору
        self.manager.transition.direction = "up"

    # Метод для виходу з програми
    def exit_app(self, *args):
        # Зупиняємо запущену програму
        app.stop()


# Екран, з якого гравець запускає вибраний рівень
class LevelSelect(Screen):

    def on_pre_enter(self, *args):
        self.refresh_donuts()
        return super().on_pre_enter(*args)

    def refresh_donuts(self):
        app = App.get_running_app()
        for level_index in range(3):
            self.ids[f"level_donut_{level_index}"].opacity = (
                1 if level_index in app.donut_levels else 0
            )

    def select_level(self, level_index):
        app.LEVEL = level_index
        self.manager.transition.direction = "left"
        self.manager.current = "game"

    def go_menu(self):
        self.manager.transition.direction = "right"
        self.manager.current = "menu"


# Створюємо клас екрана налаштувань
class Settings(Screen):

    # Конструктор класу Settings
    # **kwargs приймає додаткові іменовані аргументи
    def __init__(self, **kwargs):
        # Викликаємо конструктор батьківського класу Screen
        super().__init__(**kwargs)

    # Екран для повернення після налаштувань
    return_screen = "menu"

    def go_menu(self, *args):
        self.manager.transition.direction = "down" if self.return_screen == "menu" else "right"
        self.manager.current = self.return_screen

    # Скидаємо зібрані пончики
    def reset_progress(self):
        app = App.get_running_app()
        app.donuts = 0
        app.donut_levels.clear()
        app.LEVEL = 0
        app.save_progress()
        if app.root:
            app.root.get_screen("level_select").refresh_donuts()


# Створюємо клас для зображень, які можна обертати
class RotatedImage(Image):
    # Три крапки означають, що клас поки не містить додаткового коду
    ...


# Закоментований код — зараз він не виконується
# Тут планувалося створити пульсацію віджета
# через його збільшення та зменшення
# def polse_widget(self):

# Три крапки означали б порожню реалізацію методу
#     ...


# Створюємо клас Character для роботи з персонажем
# Character успадковує можливості RotatedImage
class Character(RotatedImage):
    # Зберігаємо інформацію про те,
    # чи зараз програється анімація кліку
    anim_play = False

    # Забороняємо взаємодію з персонажем на початку
    interaction_block = True

    # Коефіцієнт збільшення персонажа під час анімації
    COEF_MULT = 1.5

    # Тут буде зберігатися назва поточного персонажа
    character_current = None

    # Індекс поточного персонажа у списку рівня
    character_index = 0

    # Тут буде зберігатися поточна кількість HP персонажа
    hp_current = None

    # Створюємо числову властивість для кута повороту
    # Початковий кут — 0 градусів
    angle = NumericProperty(0)

    # Завантажуємо звук кліку по персонажу
    click_music = SoundLoader.load('assets/audios/doh1.mp3')

    # Завантажуємо звук перемоги над персонажем
    defeate_music = SoundLoader.load('assets/audios/fish_def.ogg')

    # Метод викликається після створення KV-властивостей віджета
    def on_kv_post(self, base_widget):

        # Отримуємо посилання на екран гри
        # parent — батьківський віджет
        # Кілька parent потрібні, щоб піднятися до Game
        self.GAME_SCREEN = self.parent.parent.parent

        # Викликаємо метод on_kv_post батьківського класу
        return super().on_kv_post(base_widget)

    # Метод створює та налаштовує нового персонажа
    def new_character(self, *args):

        # Отримуємо назву персонажа з поточного рівня
        # app.LEVEL — номер рівня
        # self.character_index — номер персонажа
        self.character_current = app.LEVELS[app.LEVEL][self.character_index]

        # Встановлюємо шлях до зображення поточного персонажа
        self.source = app.CHARACTERS[self.character_current]['source']

        # Встановлюємо HP поточного персонажа
        self.hp_current = app.CHARACTERS[self.character_current]['hp']

        # Запускаємо анімацію появи та руху персонажа
        self.swim()

    # Метод відповідає за переміщення персонажа на екран
    def swim(self):

        # Розміщуємо персонажа за лівою межею ігрового екрана
        self.pos = (
            self.GAME_SCREEN.x - self.width,
            self.GAME_SCREEN.height / 2 - dp(100)
        )

        # Робимо персонажа повністю видимою
        self.opacity = 1

        # Створюємо анімацію руху персонажа до центру
        # x визначає кінцеву координату по горизонталі
        # duration=1 означає, що анімація триває 1 секунду
        swim = Animation(
            x=self.GAME_SCREEN.width / 2 - self.width / 2,
            duration=1
        )

        # Запускаємо анімацію на персонажі
        swim.start(self)

        # Після завершення анімації
        # дозволяємо взаємодію з персонажем
        swim.bind(
            on_complete=lambda w, a:
            setattr(self, "interaction_block", False)
        )

    # Метод викликається після перемоги над персонажем
    def defeated(self):

        # Блокуємо натискання на персонажа
        self.interaction_block = True

        # Створюємо анімацію обертання персонажа
        # angle збільшується на 360 градусів
        # d=1 — тривалість анімації 1 секунда
        # in_cubic — тип плавності анімації
        anim = Animation(
            angle=self.angle + 360,
            d=1,
            t='in_cubic'
        )

        # Зберігаємо старий розмір персонажа
        old_size = self.size.copy()

        # Зберігаємо стару позицію персонажа
        old_pos = self.pos.copy()

        # Розраховуємо новий розмір персонажа
        # Збільшуємо ширину та висоту у COEF_MULT * 3 рази
        new_size = (
            self.size[0] * self.COEF_MULT * 3,
            self.size[1] * self.COEF_MULT * 3
        )

        # Розраховуємо нову позицію персонажа
        # Це потрібно, щоб збільшення відбувалося приблизно від центру
        new_pos = (
            self.pos[0] - (new_size[0] - self.size[0]) / 2,
            self.pos[1] - (new_size[0] - self.size[1]) / 2
        )

        # Додаємо до анімації збільшення персонажа
        # а потім повернення до старого розміру
        anim &= (
                Animation(
                    size=(new_size),
                    t='in_out_bounce'
                )
                + Animation(
            size=(old_size),
            duration=0
        )
        )

        # Додаємо до анімації зміну позиції
        # а потім повернення на стару позицію
        anim &= (
                Animation(
                    pos=(new_pos),
                    t='in_out_bounce'
                )
                + Animation(
            pos=(old_pos),
            duration=0
        )
        )

        # Цей рядок створював би анімацію збільшення у 2 рази
        # та повернення до старого розміру
        # Зараз він закоментований і не виконується
        # anim = Animation(size=(self.size[0] * self.COEF_MULT * 2, self.size[1] * self.COEF_MULT * 2)) + Animation(size=old_size)

        # Додаємо до загальної анімації поступове зникнення персонажі
        anim &= Animation(opacity=0)

        # Запускаємо анімацію
        anim.start(self)

        # Відтворюємо звук перемоги над персонажем
        self.defeate_music.play()

    # Метод обробляє натискання миші/тачскріна
    def on_touch_down(self, touch):

        # Перевіряємо, чи клік потрапив у персонажа
        # collide_point повертає True, якщо точка знаходиться всередині віджета
        #
        # Також перевіряємо, чи не програється анімація
        # та чи не заблокована взаємодія
        if (
                not self.collide_point(*touch.pos)
                or self.anim_play
                or self.interaction_block
        ):
            # Якщо хоча б одна умова виконується —
            # припиняємо обробку кліку
            return

        # Перевіряємо, що анімація не програється
        # та взаємодія з персонажем дозволена
        if not self.anim_play and not self.interaction_block:

            # Зменшуємо HP персонажа на 1
            self.hp_current -= 1

            # Збільшуємо рахунок гравця на 1
            self.GAME_SCREEN.score += 1

            # Відтворюємо звук кліку по персонажу
            self.click_music.play()

            # Перевіряємо, чи персонаж ще має HP
            if self.hp_current > 0:

                # Зберігаємо поточний розмір персонажа
                old_size = self.size.copy()

                # Зберігаємо поточну позицію персонажа
                old_pos = self.pos.copy()

                # Розраховуємо новий розмір персонажа
                new_size = (
                    self.size[0] * self.COEF_MULT,
                    self.size[1] * self.COEF_MULT
                )

                # Розраховуємо нову позицію
                # щоб збільшення відбувалося приблизно від центру
                new_pos = (
                    self.pos[0] - (new_size[0] - self.size[0]) / 2,
                    self.pos[1] - (new_size[1] - self.size[1]) / 2
                )

                # Створюємо анімацію збільшення
                # та повернення до початкового розміру
                zoom_anim = (
                        Animation(
                            size=(new_size),
                            duration=0.05
                        )
                        + Animation(
                    size=(old_size),
                    duration=0.05
                )
                )

                # Додаємо до анімації зміну позиції
                # та повернення до початкової позиції
                zoom_anim &= (
                        Animation(
                            pos=(new_pos),
                            duration=0.05
                        )
                        + Animation(
                    pos=(old_pos),
                    duration=0.05
                )
                )

                # Запускаємо анімацію кліку
                zoom_anim.start(self)

                # Встановлюємо True,
                # щоб під час анімації не можна було клікнути повторно
                self.anim_play = True

                # Після завершення анімації
                # встановлюємо anim_play назад у False
                zoom_anim.bind(
                    on_complete=lambda *args:
                    setattr(self, "anim_play", False)
                )


            # Якщо HP персонажа стало 0
            else:

                # Запускаємо анімацію перемоги над персонажем
                self.defeated()

                # Перевіряємо, чи є ще персонажі на поточному рівні
                if len(app.LEVELS[app.LEVEL]) > self.character_index + 1:

                    # Переходимо до індексу наступного персонажа
                    self.character_index += 1

                    # Через 1.2 секунди створюємо наступного персонажа
                    Clock.schedule_once(
                        self.new_character,
                        1.2
                    )

                # Якщо наступного персонажа немає
                else:

                    # Через 1.2 секунди завершуємо рівень
                    Clock.schedule_once(
                        self.GAME_SCREEN.level_complete,
                        1.2
                    )

        # Передаємо подію натискання батьківському класу
        return super().on_touch_down(touch)


# Створюємо клас екрана гри
class Game(Screen):
    # Створюємо властивість для зберігання рахунку
    # Початкове значення — 0
    score = NumericProperty(0)
    timer_text = StringProperty("00:00")

    # Завантажуємо фонову музику
    back_sound = SoundLoader.load(
        'assets/audios/Black_Swan_part.mp3'
    )

    # Зациклюємо фонову музику
    # Після завершення вона починається спочатку
    back_sound.loop = True

    # Завантажуємо звук завершення рівня
    level_complete_sound = SoundLoader.load(
        'assets/audios/level_complete.ogg'
    )

    # Метод викликається перед входом на екран Game
    def on_pre_enter(self, *args):
        if getattr(self, "resume_after_settings", False):
            return super().on_pre_enter(*args)

        # Обнуляємо рахунок
        self.score = 0

        # Ховаємо повідомлення та кнопку завершення рівня
        self.ids.level_complete.opacity = 0
        self.ids.level_complete.font_size = dp(50)
        self.ids.next_level_button.opacity = 0
        self.ids.next_level_button.disabled = True
        self.ids.donut_reward.opacity = 0
        self.stop_timer()
        self.timer_text = "00:00"

        # Встановлюємо індекс першого персонажа
        self.ids.character.character_index = 0

        # Викликаємо метод батьківського класу
        return super().on_pre_enter(*args)

    # Метод викликається після входу на екран Game
    def on_enter(self, *args):
        if getattr(self, "resume_after_settings", False):
            self.resume_after_settings = False
            return super().on_enter(*args)

        # Показуємо номер поточного рівня
        self.ids.level_title.text = f"Рівень {app.LEVEL + 1}"

        # Створюємо анімацію появи заголовка рівня
        label_animation = (

            # Переміщуємо заголовок у центр
                Animation(
                    y=(self.height - self.ids.level_title.height) / 2 + dp(100),
                    duration=1
                )

                # Поступово робимо заголовок видимим
                + Animation(
            opacity=1,
            duration=1
        )

                # Переміщуємо заголовок вгору за межі екрана
                + Animation(
            y=self.height,
            duration=1
        )
        )

        # Додаємо плавне зникнення заголовка
        label_animation &= (
                Animation(
                    opacity=1,
                    duration=2
                )
                + Animation(
            opacity=0,
            duration=1
        )
        )

        # Запускаємо анімацію для заголовка рівня
        label_animation.start(self.ids.level_title)

        # Після завершення анімації запускаємо start_game
        label_animation.bind(
            on_complete=self.start_game
        )

        # Запускаємо фонову музику
        self.back_sound.play()

        # Викликаємо метод батьківського класу
        return super().on_enter(*args)

    # Метод запускає гру після завершення анімації заголовка
    # animation — об'єкт завершеної анімації
    # widget — віджет, на якому була анімація
    def start_game(self, animation, widget):
        self.start_timer()
        self.ids.character.new_character()

    def start_timer(self):
        self.stop_timer()
        self.level_started_at = monotonic()
        self.timer_text = "00:00"
        self.timer_event = Clock.schedule_interval(self.update_timer, 0.1)

    def update_timer(self, dt):
        elapsed = int(monotonic() - self.level_started_at)
        self.timer_text = f"{elapsed // 60:02d}:{elapsed % 60:02d}"

    def stop_timer(self):
        event = getattr(self, "timer_event", None)
        if event is not None:
            event.cancel()
            self.timer_event = None

    def fly_donut(self):
        donut = self.ids.donut_reward
        window = self.ids.game_window
        Animation.cancel_all(donut)
        donut.size = (dp(145), dp(145))
        donut.pos = (window.x + window.width + dp(12), window.center_y - donut.height / 2)
        donut.opacity = 1
        animation = Animation(
            x=window.center_x - donut.width / 2,
            y=window.center_y - donut.height / 2,
            size=(dp(185), dp(185)),
            opacity=1,
            duration=0.7,
            t="out_back"
        ) + Animation(opacity=0, duration=0.45)
        animation.start(donut)

    def open_settings(self):
        self.resume_after_settings = True
        self.manager.get_screen("settings").return_screen = "game"
        self.manager.transition.direction = "up"
        self.manager.current = "settings"

    # Завершуємо рівень і, за швидке проходження, показуємо пончик
    def level_complete(self, *args):
        self.stop_timer()
        elapsed = monotonic() - self.level_started_at
        self.ids.level_complete.opacity = 0

        if elapsed <= app.DONUT_TIME_LIMIT:
            if app.LEVEL not in app.donut_levels:
                app.donut_levels.add(app.LEVEL)
                app.donuts += 1
                app.save_progress()
            self.fly_donut()

        self.ids.next_level_button.text = "Завершити" if app.LEVEL == len(app.LEVELS) - 1 else "Далі"
        self.ids.next_level_button.disabled = False
        self.ids.next_level_button.opacity = 1

        if self.level_complete_sound:
            self.level_complete_sound.play()

    # Переходимо до наступного рівня або завершуємо гру
    def next_level(self):
        if app.LEVEL >= len(app.LEVELS) - 1:
            self.go_home()
            return

        app.LEVEL += 1
        self.ids.level_title.text = f"Рівень {app.LEVEL + 1}"
        self.ids.level_complete.opacity = 0
        self.ids.donut_reward.opacity = 0
        self.ids.next_level_button.opacity = 0
        self.ids.next_level_button.disabled = True
        self.ids.character.character_index = 0
        self.start_timer()
        self.ids.character.new_character()

    # Метод повернення до головного меню
    def go_home(self):
        self.stop_timer()

        # Створюємо коротку анімацію зникнення персонажі
        character_disappear_anim = Animation(
            opacity=0,
            duration=0.1
        )

        # Запускаємо анімацію зникнення персонажі
        character_disappear_anim.start(self.ids.character)

        # Зупиняємо фонову музику
        self.back_sound.stop()

        # Переходимо до головного меню
        self.manager.current = "menu"

        # Встановлюємо напрямок переходу вправо
        self.manager.transition.direction = "right"


# Створюємо основний клас програми
class ClickerApp(App):
    # Спільні налаштування звуку для всіх екранів
    sound_enabled = BooleanProperty(True)
    sound_volume = NumericProperty(0.3)
    donuts = NumericProperty(0)
    donut_levels = set()
    DONUT_TIME_LIMIT = 60

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.donut_levels = set()
        os.makedirs(self.user_data_dir, exist_ok=True)
        self.progress_store = JsonStore(os.path.join(self.user_data_dir, "progress.json"))

    def on_start(self):
        self.load_progress()
        self.apply_sound_settings()

    def load_progress(self):
        if self.progress_store.exists("progress"):
            data = self.progress_store.get("progress")
            self.donuts = int(data.get("donuts", 0))
            self.donut_levels = set(data.get("donut_levels", []))

    def save_progress(self):
        self.progress_store.put(
            "progress",
            donuts=int(self.donuts),
            donut_levels=sorted(self.donut_levels),
        )

    # Застосовуємо гучність до всіх звукових файлів
    def apply_sound_settings(self, *args):
        volume = self.sound_volume if self.sound_enabled else 0
        sounds = (
            Character.click_music,
            Character.defeate_music,
            Game.back_sound,
            Game.level_complete_sound
        )
        for sound in sounds:
            if sound:
                sound.volume = volume

    # Вмикаємо або вимикаємо всі звуки
    def toggle_sound(self):
        self.sound_enabled = not self.sound_enabled
        self.apply_sound_settings()

    # Вибираємо гучність 10%, 20% або 30%
    def set_sound_volume(self, volume):
        # Фіксуємо значення повзунка з точністю до 10 відсотків
        self.sound_volume = round(float(volume) * 10) / 10
        self.apply_sound_settings()

    # Зберігаємо номер поточного рівня
    # Початковий рівень — 0
    LEVEL = 0

    # Створюємо словник із даними про персонажів
    CHARACTERS = {

        # Дані першого персонажа
        'character1':
            {
                # Шлях до зображення першого персонажа
                'source': 'assets/images/homer-simpson.png',

                # Кількість HP першого персонажа
                'hp': 20
            },

        # Дані другого персонажа
        'character2':
            {
                # Шлях до зображення другого персонажа
                'source': 'assets/images/homer-simpson.png',

                # Кількість HP другого персонажа
                'hp': 40
            }
    }

    # Заміни шляхи тут, щоб встановити власне тло для кожного рівня.
    LEVEL_BACKGROUNDS = [
        "assets/images/level1.jpg",
        "assets/images/level2.jpg",
        "assets/images/level3.jpg",
    ]

    # Створюємо список рівнів
    LEVELS = [
        # Перший рівень: три персонажі
        ['character1', 'character1', 'character2'],

        # Другий рівень: чотири персонажі
        ['character2', 'character1', 'character2', 'character1'],

        # Третій рівень: п’ять персонажів
        ['character2', 'character2', 'character1', 'character2', 'character1']
    ]

    # Метод створення основного інтерфейсу програми
    def build(self):

        # Створюємо менеджер екранів
        sm = ScreenManager()

        # Додаємо екран головного меню
        # name="menu" — його унікальне ім'я
        sm.add_widget(
            Menu(name="menu")
        )

        # Додаємо екран вибору рівня
        sm.add_widget(
            LevelSelect(name="level_select")
        )

        # Додаємо екран гри
        # name="game" — його унікальне ім'я
        sm.add_widget(
            Game(name="game")
        )

        # Додаємо екран налаштувань
        # name="settings" — його унікальне ім'я
        sm.add_widget(
            Settings(name="settings")
        )

        # Повертаємо менеджер екранів
        # Він стає головним віджетом програми
        return sm


# Перевіряємо, чи програма запущена не на Android
if platform != 'android':
    # Якщо це ПК, встановлюємо розмір вікна 400×600
    Window.size = (400, 600)

# Створюємо об'єкт програми
app = ClickerApp()

# Запускаємо програму
app.run()