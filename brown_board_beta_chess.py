from kivy.config import Config
Config.set('graphics', 'resizable', False)  # this line must be implemented before the rest is imported
from kivy.app import App
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

my_graphics_settings_width = 700  # THE WIDTH
my_graphics_settings_height = 700  # THE HEIGHT
number_of_stones = 8  # NUMBER OF STONES
number_of_stones = number_of_stones + 1
do_scale_switch = False  # RESIZING STONES
do_rotation_switch = False  # TURNING STONES
stone_size_hint = 0.08  # STONE SIZE
stone_speed = 0.4  # MOV SPEED (sec)
doomsday_trick = 1.5  # fixes the DISPROPORTION between the scatter size and its image, logical value is 2
stones_stack_step = 50  # STACK

Config.set('graphics', 'width', str(my_graphics_settings_width))
Config.set('graphics', 'height', str(my_graphics_settings_width))
Window.size = (my_graphics_settings_width, my_graphics_settings_height)
Window.top = 50
Window.left = 200

stone_size = (stone_size_hint * Window.height, stone_size_hint * Window.height)
# stone_colors=['bl','wh','rd']
stone_colors = ['bl', 'wh']
chess_pieces = ['king', 'queen', 'rook', 'bishop', 'horse', 'pawn', 'stone']

stone_counter = -1
for chess_piece in chess_pieces:
    stone_counter += 1
    exec("""bl_%s_default_pos=(0+stone_counter*stones_stack_step,20)""" % chess_piece)
    exec("""wh_%s_default_pos=(0.9*Window.width-stone_counter*stones_stack_step,20)""" % chess_piece)

for chess_piece in chess_pieces:
    for stone_n in range(number_of_stones):
        exec("""bl_%s_sctr%d=Scatter(
        size_hint=(stone_size_hint,stone_size_hint),
        pos=(bl_%s_default_pos),auto_bring_to_front=True, do_scale=do_scale_switch,
        do_rotation=do_rotation_switch)""" % (chess_piece, stone_n, chess_piece))
        exec("""wh_%s_sctr%d=Scatter(
        size_hint=(stone_size_hint,stone_size_hint),
        pos=(wh_%s_default_pos),auto_bring_to_front=True, do_scale=do_scale_switch,
        do_rotation=do_rotation_switch)""" % (chess_piece, stone_n, chess_piece))

# creating stone labels and images:
for stone_color in stone_colors:
    for stone_n in range(number_of_stones):
        for chess_piece in chess_pieces:
            exec(
                """%s_%s_image%d=Image(size=stone_size,center_x=stone_size[0]/doomsday_trick,center_y=stone_size[
                1]/2,source='%s_%s.png')""" % (
                    stone_color, chess_piece, stone_n, stone_color, chess_piece))


class BrownBoard(App):
    def build(self):
        Window.clearcolor = (0.3, 0.15, 0, 1)
        print('window size: ', Window.size)
        background = Image(
            source='brown_board.png')
        the_layout = FloatLayout()
        the_layout.add_widget(background)

        grab_stone_sound = SoundLoader.load('grab_sound.wav')
        move_stone_sound = SoundLoader.load('move_sound.mp3')

        def play_grab_stone_sound(a, b):
            grab_stone_sound.play()

        def play_move_stone_sound(a, b):
            move_stone_sound.play()

        def stop_move_stone_sound(a, b):
            move_stone_sound.stop()

        for stone_color in stone_colors:
            for stone_n in range(number_of_stones):
                for chess_piece in chess_pieces:
                    # adding images and the sound to the stones:
                    # exec("""%s_%s_sctr%d.bind(on_touch_down=play_grab_stone_sound)""" % (
                    #     stone_color, chess_piece, stone_n))
                    # exec("""%s_%s_sctr%d.bind(on_touch_move=play_move_stone_sound)""" % (
                    #     stone_color, chess_piece, stone_n))
                    # exec("""%s_%s_sctr%d.bind(on_touch_down=stop_move_stone_sound)""" % (
                    #     stone_color, chess_piece, stone_n))
                    exec("""%s_%s_sctr%d.bind(on_touch_up=play_grab_stone_sound)""" % (
                        stone_color, chess_piece, stone_n))
                    exec("""%s_%s_sctr%d.add_widget(%s_%s_image%d)""" % (
                        stone_color, chess_piece, stone_n, stone_color, chess_piece, stone_n))

        def return_stones(a):
            for stone_color in stone_colors:
                for stone_n in range(1, number_of_stones):
                    for chess_piece in chess_pieces:
                        exec("""anim=Animation(pos=%s_%s_default_pos,d=stone_speed)""" % (stone_color, chess_piece))
                        exec("""anim.start(%s_%s_sctr%d)""" % (stone_color, chess_piece, stone_n))

        def update_stone_size(a, b):
            print(Window.size)
            for stone_color in stone_colors:
                for stone_n in range(number_of_stones):
                    for chess_piece in chess_pieces:
                        exec("""%s_%s_sctr%d.size_hint=(stone_size_hint,stone_size_hint)""" % (
                            stone_color, chess_piece, stone_n))
                        exec("""%s_%s_image%d.size=stone_size""" % (stone_color, chess_piece, stone_n))

        refresh_btn = Button(
            size_hint=(0.05, 0.05),
            pos_hint={'top': 0.98, 'right': 0.98},
            background_color=(0, 0, 0, 0),
        )
        refresh_btn_image = Image(
            size_hint=(0.05, 0.05),
            pos_hint={'top': 0.98, 'right': 0.98},
            source='refresh.png'
        )

        refresh_btn.bind(on_press=return_stones)
        # Window.bind(size=update_stone_size)

        the_layout.add_widget(refresh_btn_image)
        the_layout.add_widget(refresh_btn)

        # the_layout.add_widget(label1)

        for stone_color in stone_colors:
            for stone_n in range(1, number_of_stones):
                for chess_piece in chess_pieces:
                    exec("""the_layout.add_widget(%s_%s_sctr%d)""" % (stone_color, chess_piece, stone_n))

        return the_layout


if __name__ == '__main__':
    BrownBoard().run()
