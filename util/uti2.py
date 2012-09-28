#--------------------------------Imports-----------------------------------

import pygame, time, os
from pygame.locals import *
from sys import exit
from Tkinter import *

#--------------------------------init---------------------------------------
codeDir = os.path.dirname(__file__)


#-------------------------------Function Sets------------------------------
        
#returns the absolute according to the relative path
def absolutePath(directory):
    return os.path.join(codeDir, directory)

def menu_choose():
    pass             
    
def playmusic(filename):    #Format OGG only
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def initialize():
    # playmusic("initmusic.ogg")
    #pygame.time.delay(2000)
    inited = True
    
def user_login():
    def save():
        inp = entry.get()
        print inp
        inpf = open(absolutePath(r"\data\gbuserfile.txt"), "w")
        inpf.write(inp)
        inpf.close()
        return

    win = Tk()
    win.title("Welcom To Global Battle! Please Register:")
    win.geometry("600x200")
    frame = Frame(win)
    frame.pack()
    var = StringVar()
    label = Label(frame, textvariable=var)
    label.pack()
    entry = Entry(frame, textvariable=var)
    entry.pack()
    CN = Button(frame, text="Crate New User", command=save)
    CN.pack()
    note = Label(frame, text='''
Welcome!
1.Type your name in the input box, then click 'Creat New User'
2.After step 1, close this window, and ENJOY!''')
    note.pack()
    win.mainloop()

#--------------------------------Image Path--------------------------------
initscreen = absolutePath(r"\pic\init_scr.png")
bkg1 = absolutePath(r"\pic\under.png")
map1280 = absolutePath(r"\pic\map1280.png")
map800 = absolutePath(r"\pic\map800.png")
sp_home = absolutePath(r"\pic\sp_home.png")

loading = absolutePath(r"\pic\\loading.png")
error = absolutePath(r"\pic\\error.png")
success = absolutePath(r"\pic\\success.png")

sp_e = absolutePath(r"\pic\\sp_e.png")
mp_e = absolutePath(r"\pic\\mp_e.png")
choose = absolutePath(r"\pic\choose.png")

global mar_itm
mar_itm = absolutePath(r"\market\\mar_itmv1v.png")

area1 = absolutePath(r"\pic\marea1.png")

marketdock = absolutePath(r"\pic\market_dock.png")

buymenu = absolutePath(r"\pic\mbuymenu.png")

darken = absolutePath(r"\pic\darken.png")

dbbg = absolutePath(r"\pic\dbbg.png")
orgbg = absolutePath(r"\pic\orgbg.png")
#--------------------------------Image Load--------------------------------

#backgrounds
bkg1 = pygame.image.load(bkg1)
sp_home = pygame.image.load(sp_home)    
map1280 = pygame.image.load(map1280)
map800 = pygame.image.load(map800)
darken = pygame.image.load(darken)
initscreen = pygame.image.load(initscreen)

#Menu item_g

sp_e = pygame.image.load(sp_e)
mp_e = pygame.image.load(mp_e)
choose = pygame.image.load(choose)

#Notify
loading = pygame.image.load(loading)
error = pygame.image.load(error)
success = pygame.image.load(success)

#Market item
maritm_v1 = pygame.image.load(mar_itm)
marketdock = pygame.image.load(marketdock)

#Market Control
buymenu = pygame.image.load(buymenu)

#areas
area1 = pygame.image.load(area1)

#World DataBase
dbbg = pygame.image.load(dbbg)

#Organizer
orgbg = pygame.image.load(orgbg)

#--------------------------------Game Var----------------------------------
#menu items_var

global i_itm1, i_itm2, i_itm3, i_itm4
i_itm1 = None
i_itm2 = None
i_itm3 = None
i_itm4 = None

global started
started = False

loaded = False

inited = False
chy = 200

global mu, md
mu, md = False, True    #determine if choosebar in menu can be moved or no

global itm1_s, itm2_s
itm1_s, itm2_s = True, False    #Menu item, _s for selected



market_type_menu = False

weapon_num = 0

global new_user


    
    

