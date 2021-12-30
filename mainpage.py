import tkinter as tk
from tkinter import *
from checkerBoard1 import CheckerBoard1
from checkerBoard2 import CheckerBoard2

def Options():
    def CGame():
        OptionScreen.destroy()
        newCheckerBoard = CheckerBoard1()
    def SpecGame():
        OptionScreen.destroy()
        newCheckerBoard = CheckerBoard2()
    def BackHome():
        OptionScreen.destroy()
        HomePage()
    OptionScreen=tk.Tk()
    OptionScreen.title("Select Game")
    c = tk.Canvas(OptionScreen,bg="#8ED8DD",width=610,height=400)

    
    CGameB = Button(OptionScreen,text="Classic Mode",command=CGame)
    CGameB.configure(width=15,activebackground="#33B5E5")
    CGameB_window = c.create_window(300,50,window=CGameB)

    CGameB = Button(OptionScreen,text="Challenge Mode",command=SpecGame)
    CGameB.configure(width=15,activebackground="#33B5E5")
    CGameB_window = c.create_window(300,150,window=CGameB)

    CGameB = Button(OptionScreen,text="Player vs AI")
    CGameB.configure(width=15,activebackground="#33B5E5")
    CGameB_window = c.create_window(300,250,window=CGameB)
    
    BackB = Button(OptionScreen,text="BACK",command=BackHome)
    BackB.configure(width=10,activebackground="#33B5E5")
    BackB_window = c.create_window(300,350,window=BackB)
    
    c.pack()

def HomePage():
    def StartGame():
        HomeScreen.destroy()
        Options()
        
    HomeScreen=tk.Tk()
    HomeScreen.title("Home Screen")
    w = tk.Canvas(HomeScreen,bg="#8ED8DD",width=610,height=400)
    w.create_text(305,25,text="WELCOME",font=('Times','24','bold'))
    w.create_text(305,80,text="RULES",font=('Times','18','bold'))
    w.create_text(300,120,text="There needs to be 12 pieces for each side")
    w.create_text(300,140,text="Each piece can move diagonally only")
    w.create_text(300,160,text="They cannot skip over pieces of same color")
    w.create_text(300,180,text="Opponent pieces are taken only when the player moves over the opponent man")
    w.create_text(300,200,text="The subsequent space must be free when taking an opponent")
    w.create_text(300,220,text="Each player can have multiple kings if and only if each man reaches the opponent side end")
    w.create_text(300,240,text="Only The king can move backwards")
    w.create_text(300,260,text="To win the player needs to take all of opponent's pieces")
    StartB = Button(HomeScreen,text="START",command= StartGame)
    StartB.configure(width=10,activebackground="#33B5E5",bg="#234EAF")
    StartB_window = w.create_window(220,350,window=StartB)

    QuitB = Button(HomeScreen,text="QUIT",command=exit)
    QuitB.configure(width=10,activebackground="#33B5E5",bg="#F54848")
    QuitB_window = w.create_window(400,350,window=QuitB)
                                                        
    w.pack()

#HomePage()
Options()

