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
number_of_stones=8 #NUMBER OF STONES
number_of_stones=number_of_stones+1
do_scale_switch=False #RESIZING STONES
do_rotation_switch=False #TURNING STONES
stone_size_hint=0.08 #STONE SIZE
stone_speed=0.3 #MOV SPEED (sec)
doomsday_trick=1.5 #fixes the DISPROPORTION between the scatter size and its image, logical value is 2
stones_stack_step=50 #STACK

Config.set('graphics', 'width', str(my_graphics_settings_width))
Config.set('graphics', 'height', str(my_graphics_settings_width))
Window.size=(my_graphics_settings_width,my_graphics_settings_height)

stone_size=(stone_size_hint*Window.height, stone_size_hint*Window.height)
#stone_colors=['bl','wh','rd']
stone_colors=['bl','wh']
chess_pieces=['king','queen','rook','bishop','horse','pawn']

stone_counter=-1
for chess_piece in chess_pieces:
    stone_counter+=1
    exec("""bl_%s_default_pos=(0+stone_counter*stones_stack_step,20)""" %(chess_piece))    
    exec("""wh_%s_default_pos=(0.9*Window.width-stone_counter*stones_stack_step,20)""" %(chess_piece))
    

stone_counter=-1
for chess_piece in chess_pieces:
    for stone_n in range(number_of_stones):
        stone_counter+=15
        #stone_counter+=1
        exec("""bl_%s_sctr%d=Scatter(
        size_hint=(stone_size_hint,stone_size_hint),
        pos=(bl_%s_default_pos),auto_bring_to_front=False, do_scale=do_scale_switch,
        do_rotation=do_rotation_switch)""" %(chess_piece,stone_n,chess_piece))
        exec("""wh_%s_sctr%d=Scatter(
        size_hint=(stone_size_hint,stone_size_hint),
        pos=(wh_%s_default_pos),auto_bring_to_front=False, do_scale=do_scale_switch,
        do_rotation=do_rotation_switch)""" %(chess_piece,stone_n,chess_piece))
    

#creating stone labels and images:
for stone_color in stone_colors:
    for stone_n in range(number_of_stones):
        for chess_piece in chess_pieces:
            #exec("""%s_stone_label%d=Label()""" %(stone_color,stone_n))
            exec("""%s_%s_image%d=Image(size=stone_size,center_x=stone_size[0]/doomsday_trick,center_y=stone_size[1]/2,source='%s_%s.png')""" %(stone_color,chess_piece,stone_n,stone_color,chess_piece))
#creating stone labels and images end

def turn_to_pawn(a,b):
    if b[0]>500:
        #bl_stone_sctr1.remove_widget(bl_stone_image1)
        bl_stone_sctr1.add_widget(Image(
            center_x=stone_size[0]/2,
            center_y=stone_size[1]/2,
            size=(stone_size[0]*0.6,stone_size[1]*0.6),
            source='pawn.png'))

class BrownBoard(App):
    def build(self):
        Window.clearcolor=(0.3,0.15,0,1)
        print('window size: ',Window.size)
        background=Image(
            source='brown_board.png')
        the_layout=FloatLayout()
        the_layout.add_widget(background)

    

        
        for stone_color in stone_colors:
            for stone_n in range(number_of_stones):
                for chess_piece in chess_pieces:
                

#adding labels and images to the stones:
                    exec("""%s_%s_sctr%d.add_widget(%s_%s_image%d)""" %(stone_color,chess_piece,stone_n,stone_color,chess_piece,stone_n))
                    #exec("""%s_stone_sctr%d.add_widget(%s_stone_label%d)""" %(stone_color,stone_n,stone_color,stone_n))
                    #exec("""%s_stone_sctr%d.bind(pos= lambda a,b: print(%s_stone_sctr%d.pos))""" %(stone_color,stone_n,stone_color,stone_n))
                    #exec("""%s_stone_sctr%d.bind(pos= lambda a,b: setattr(%s_stone_label%d, 'text', str(%s_stone_sctr%d.pos)))""" %(stone_color,stone_n,stone_color,stone_n,stone_color,stone_n))              
#adding labels and images to the stones end
        #bl_stone_sctr1.bind(pos=turn_to_pawn)


        
        


        

        label1=Label(pos=(25,50))        

        def my_change_mouse_pos(a,b):
            label1.text=str(Window.mouse_pos)
        Window.bind(mouse_pos=my_change_mouse_pos)
          
        def return_bl_stones(a):
            anim=Animation(x=20,y=20,d=stone_speed)
            for chess_piece in chess_pieces:
                for stone_n in range(1,number_of_stones):
                    exec("""anim.start(bl_%s_sctr%d)""" %(chess_piece,stone_n))

        def return_wh_stones(a):
            anim=Animation(x=Window.width-90,y=20,d=stone_speed)
            for chess_piece in chess_pieces:
                for stone_n in range(1,number_of_stones):
                    exec("""anim.start(wh_%s_sctr%d)""" %(chess_piece,stone_n))

        def return_stones(a):
            for stone_color in stone_colors:
                for stone_n in range(1, number_of_stones):
                    for chess_piece in chess_pieces:
                        exec("""anim=Animation(pos=%s_%s_default_pos,d=stone_speed)""" %(stone_color,chess_piece))
                        exec("""anim.start(%s_%s_sctr%d)""" %(stone_color,chess_piece,stone_n))

        def update_stone_size(a,b):
            print(Window.size)
            for stone_color in stone_colors:
                for stone_n in range(number_of_stones):
                    for chess_piece in chess_pieces:
                         exec("""%s_%s_sctr%d.size_hint=(stone_size_hint,stone_size_hint)""" %(stone_color,chess_piece,stone_n))
                         exec("""%s_%s_image%d.size=stone_size""" %(stone_color,chess_piece,stone_n))
                        
            
            

        
        
        refresh_btn=Button(
            size_hint=(0.05,0.05),
            pos_hint={'top':0.98,'right':0.98},
            background_color=(0,0,0,0),
            )
        refresh_btn_image=Image(
            size_hint=(0.05,0.05),
            pos_hint={'top':0.98,'right':0.98},
            source='refresh.png'
            )



        refresh_btn.bind(on_press=return_stones)
        #Window.bind(size=update_stone_size)


        

        the_layout.add_widget(refresh_btn_image)
        the_layout.add_widget(refresh_btn)

        #the_layout.add_widget(label1)
        
        for stone_color in stone_colors:
            for stone_n in range(1, number_of_stones):
                for chess_piece in chess_pieces:                
                    exec("""the_layout.add_widget(%s_%s_sctr%d)""" %(stone_color,chess_piece,stone_n))
        
        
        return the_layout
        
    
#if __name__=='__main__':
BrownBoard().run()
