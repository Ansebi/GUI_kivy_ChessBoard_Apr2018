from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import *
from kivy.animation import *
from kivy.config import Config
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '700')
#zerg=input()
#Window.size=(zerg.split(',')[0],zerg.split(',')[1])
Window.size=(700,700)
number_of_stones=32
do_scale_switch=False


bl_stone_sctr_template = """bl_stone_sctr%d=Scatter(size_hint=(0.067,0.067),pos=(20,20),auto_bring_to_front=False, do_scale=do_scale_switch)"""
for x in range(1, number_of_stones): exec(bl_stone_sctr_template %(x))
wh_stone_sctr_template = """wh_stone_sctr%d=Scatter(size_hint=(0.067,0.067),pos=(Window.width-90,20),auto_bring_to_front=False, do_scale=do_scale_switch)"""
for x in range(1, number_of_stones): exec(wh_stone_sctr_template %(x))
rd_stone_sctr_template = """rd_stone_sctr%d=Scatter(size_hint=(0.067,0.067),pos=(20,Window.height-90),auto_bring_to_front=False, do_scale=do_scale_switch)"""
for x in range(1, number_of_stones): exec(rd_stone_sctr_template %(x))

class BrownBoard(App):
    def build(self):
        Window.clearcolor=(0.3,0.15,0,1)
        print('window size: ',Window.size)
        background=Image(source='brown_board.png')
        layout1=FloatLayout()
        layout1.add_widget(background)


        def draw_black_stone(widget_name):
            with widget_name.canvas:
                #Color(0,0,0,1)
                Ellipse(size=(60,60),source='black_stone.png')
        def draw_white_stone(widget_name):
            with widget_name.canvas:
                #Color(1,1,1,1)
                Ellipse(size=(60,60),source='white_stone.png')
        def draw_red_stone(widget_name):
            with widget_name.canvas:
                #Color(1,0,0,1)
                Ellipse(size=(60,60),source='red_stone.png')
        draw_black_stone_template = """draw_black_stone(bl_stone_sctr%d)"""
        for x in range(1, number_of_stones): exec(draw_black_stone_template %(x))
        draw_white_stone_template = """draw_white_stone(wh_stone_sctr%d)"""
        for x in range(1, number_of_stones): exec(draw_white_stone_template %(x))
        draw_red_stone_template = """draw_red_stone(rd_stone_sctr%d)"""
        for x in range(1, number_of_stones): exec(draw_red_stone_template %(x))

        label1=Label(pos=(25,50))        

        def my_change_mouse_pos(a,b):
            label1.text=str(Window.mouse_pos)
        Window.bind(mouse_pos=my_change_mouse_pos)
          
        def return_black_stones(a):
            anim=Animation(x=20,y=20,d=0.4)
            anim_template="""anim.start(bl_stone_sctr%d)"""
            for x in range(1,number_of_stones): exec(anim_template %(x))

        def return_white_stones(a):
            anim=Animation(x=Window.width-90,y=20,d=0.4)
            anim_template="""anim.start(wh_stone_sctr%d)"""
            for x in range(1,number_of_stones): exec(anim_template %(x))

        def return_red_stones(a):
            anim=Animation(x=20,y=Window.height-90,d=0.4)
            anim_template="""anim.start(rd_stone_sctr%d)"""
            for x in range(1,number_of_stones): exec(anim_template %(x))
        
        btn1=Button(
            size_hint=(0.05,0.05),
            pos_hint={'top':0.98,'right':0.98},
            background_color=(0,0,0,0),
            #text='очистить доску'
            )
        btn1_image=Image(
            size_hint=(0.05,0.05),
            pos_hint={'top':0.98,'right':0.98},
            source='refresh.png'
            )
        btn1.bind(on_press=return_black_stones)
        btn1.bind(on_press=return_white_stones)
        btn1.bind(on_press=return_red_stones)
        
        

        layout1.add_widget(btn1_image)
        layout1.add_widget(btn1)
        #layout1.add_widget(label1)
        add_bl_stone_template = """layout1.add_widget(bl_stone_sctr%d)"""
        for x in range(1, number_of_stones): exec(add_bl_stone_template %(x))
        add_wh_stone_template = """layout1.add_widget(wh_stone_sctr%d)"""
        for x in range(1, number_of_stones): exec(add_wh_stone_template %(x))
        add_rd_stone_template = """layout1.add_widget(rd_stone_sctr%d)"""
        for x in range(1, number_of_stones): exec(add_rd_stone_template %(x))
        
        return layout1
        
    
#if __name__=='__main__':
BrownBoard().run()
