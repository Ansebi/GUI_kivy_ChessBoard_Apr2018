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

my_graphics_settings_width=700 #THE WIDTH
my_graphics_settings_height=700 #THE HEIGHT
number_of_stones=32 #NUMBER OF STONES
do_scale_switch=False #RESIZE STONES
stone_size_hint=0.067 #STONE SIZE

Config.set('graphics', 'width', str(my_graphics_settings_width))
Config.set('graphics', 'height', str(my_graphics_settings_width))
Window.size=(my_graphics_settings_width,my_graphics_settings_height)

stone_size=(stone_size_hint*Window.height, stone_size_hint*Window.height)

bl_stone_sctr_template = """bl_stone_sctr%d=Scatter(
size_hint=(stone_size_hint,stone_size_hint),
pos=(20,20),auto_bring_to_front=False, do_scale=do_scale_switch)"""
for x in range(1, number_of_stones): exec(bl_stone_sctr_template %(x))
wh_stone_sctr_template = """wh_stone_sctr%d=Scatter(
size_hint=(stone_size_hint,stone_size_hint),
pos=(Window.width-90,20),auto_bring_to_front=False, do_scale=do_scale_switch)"""
for x in range(1, number_of_stones): exec(wh_stone_sctr_template %(x))
rd_stone_sctr_template = """rd_stone_sctr%d=Scatter(
size_hint=(stone_size_hint,stone_size_hint),
pos=(20,Window.height-90),auto_bring_to_front=False, do_scale=do_scale_switch)"""
for x in range(1, number_of_stones): exec(rd_stone_sctr_template %(x))

class BrownBoard(App):
    def build(self):
        Window.clearcolor=(0.3,0.15,0,1)
        print('window size: ',Window.size)
        background=Image(source='brown_board.png')
        layout1=FloatLayout()
        layout1.add_widget(background)


#        def draw_bl_stone(widget_name):
#            with widget_name.canvas:
#                #Color(0,0,0,1)
#                Ellipse(size=stone_size,source='bl_stone.png')
#        def draw_wh_stone(widget_name):
#            with widget_name.canvas:
#                #Color(1,1,1,1)
#                Ellipse(size=stone_size,source='wh_stone.png')
#        def draw_rd_stone(widget_name):
#            with widget_name.canvas:
#                #Color(1,0,0,1)
#                Ellipse(size=stone_size,source='rd_stone.png')


#creating and adding labels to the stones:
        for x in range(1,number_of_stones):
            for stone_color in ['bl','wh','rd']:
                exec("""self.%s_stone_label%d=Label(text="%s Gusi")""" %(stone_color,x,stone_color))
                exec("""%s_stone_sctr%d.add_widget(self.%s_stone_label%d)""" %(stone_color,x,stone_color,x))
                exec("""print(self.%s_stone_label%d.text)""" %(stone_color,x))
#creating and adding labels to the stones end
                
        

        def draw_bl_stone(widget_name):
            exec("""bl_stone_image%d=Image(size=stone_size,source='bl_stone.png')""" %(x))
            exec("""widget_name.add_widget(bl_stone_image%d)""" %(x))
        def draw_wh_stone(widget_name):
            exec("""wh_stone_image%d=Image(size=stone_size,source='wh_stone.png')""" %(x))
            exec("""widget_name.add_widget(wh_stone_image%d)""" %(x))
        def draw_rd_stone(widget_name):
            exec("""rd_stone_image%d=Image(size=stone_size,source='rd_stone.png')""" %(x))
            exec("""widget_name.add_widget(rd_stone_image%d)""" %(x))
        
        draw_bl_stone_template = """draw_bl_stone(bl_stone_sctr%d)"""
        for x in range(1, number_of_stones): exec(draw_bl_stone_template %(x))
        draw_wh_stone_template = """draw_wh_stone(wh_stone_sctr%d)"""
        for x in range(1, number_of_stones): exec(draw_wh_stone_template %(x))
        draw_rd_stone_template = """draw_rd_stone(rd_stone_sctr%d)"""
        for x in range(1, number_of_stones): exec(draw_rd_stone_template %(x))


        bl_stone_sctr31.bl_stone_label31=Label()
        bl_stone_sctr31.add_widget(bl_stone_sctr31.bl_stone_label31)
        bl_stone_sctr31.bind(pos= lambda a,b: print(bl_stone_sctr31.pos))
        bl_stone_sctr31.bind(pos= lambda a,b: setattr(bl_stone_sctr31.bl_stone_label31, 'text', str(bl_stone_sctr31.pos)))


        

        label1=Label(pos=(25,50))        

        def my_change_mouse_pos(a,b):
            label1.text=str(Window.mouse_pos)
        Window.bind(mouse_pos=my_change_mouse_pos)
          
        def return_bl_stones(a):
            anim=Animation(x=20,y=20,d=0.4)
            anim_template="""anim.start(bl_stone_sctr%d)"""
            for x in range(1,number_of_stones): exec(anim_template %(x))

        def return_wh_stones(a):
            anim=Animation(x=Window.width-90,y=20,d=0.4)
            anim_template="""anim.start(wh_stone_sctr%d)"""
            for x in range(1,number_of_stones): exec(anim_template %(x))

        def return_rd_stones(a):
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
        btn1.bind(on_press=return_bl_stones)
        btn1.bind(on_press=return_wh_stones)
        btn1.bind(on_press=return_rd_stones)
        
        

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
