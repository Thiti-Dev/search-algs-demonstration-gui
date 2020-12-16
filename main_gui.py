import tkinter as tk
from tkinter import *
import config as config

class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        #Passing self as root_window
        message = tk.Label(self, text="Search algorithms gui demonstration", bg="blue2", fg="snow",font=('times', 20, ' bold '))
        message.place(x=getCenteredAxis()["x"], y=30,anchor="center")

        dijkstra_btn = tk.Button(self,command=lambda: controller.show_frame(DijkstraPage), text="Dijkstra search algorithm",bg="orange",fg="white",activebackground="gray",font=('times', 15, ' bold '))
        dijkstra_btn.place(x=getCenteredAxis()["x"],y=150,anchor="center",width=300)

        bfs_btn = tk.Button(self,command=lambda: controller.show_frame(BfsPage), text="Breadth first search algorithm",bg="orange",fg="white",activebackground="gray",font=('times', 15, ' bold '))
        bfs_btn.place(x=getCenteredAxis()["x"],y=200,anchor="center",width=300)

        dfs_btn = tk.Button(self,command=lambda: controller.show_frame(DfsPage), text="Depth first search algorithm",bg="orange",fg="white",activebackground="gray",font=('times', 15, ' bold '))
        dfs_btn.place(x=getCenteredAxis()["x"],y=250,anchor="center",width=300)

        exit_btn = tk.Button(self,command=exitProgram, text="Exit",bg="red",fg="white",activebackground="gray",font=('times', 15, ' bold '))
        exit_btn.place(x=600,y=450,anchor="center")

class BfsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        greeting = tk.Label(self,text="Breadth first search visualization page goes here")
        greeting.pack()

        #Logic will be belonging here

        # ─────────────────────────────────────────────────────────────────

class DfsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        greeting = tk.Label(self,text="Depth first search visualization page goes here")
        greeting.pack()

        #Logic will be belonging here

        # ─────────────────────────────────────────────────────────────────

class DijkstraPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        greeting = tk.Label(self,text="Dijkstra search visualization page goes here")
        greeting.pack()

        #Logic will be belonging here

        # ─────────────────────────────────────────────────────────────────

# ─── CONTROLLER ─────────────────────────────────────────────────────────────────
class FrameController(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self,width=640,height=480)

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0,minsize=480, weight=1)
        container.grid_columnconfigure(0,minsize=640, weight=1)
        self.frames = {}

        for F in (MenuPage,BfsPage,DfsPage,DijkstraPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MenuPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
# ────────────────────────────────────────────────────────────────────────────────



# ─── UTILS FUNCTION ─────────────────────────────────────────────────────────────
def getCenteredAxis():
    x=config.configs["application"]["width"]/2
    y=config.configs["application"]["height"]/2
    return {
        "x": x,
        "y": y
    }
# ────────────────────────────────────────────────────────────────────────────────


# ─── INTERACTIONS CALLBACK ──────────────────────────────────────────────────────
def exitProgram():
     app.destroy()
# ────────────────────────────────────────────────────────────────────────────────

global app
app = FrameController()
app.title("Search Algorithm Demonstration GUI-APPLICATION")
app.mainloop()