import tkinter as tk
from tkinter import *
import threading
import config as config

class MenuPage(tk.Frame):
    pagePointer = "Menu"
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
    pagePointer = "Bfs"
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        greeting = tk.Label(self,text="Breadth first search visualization page goes here")
        greeting.pack()

        #Logic will be belonging here

        # ─────────────────────────────────────────────────────────────────

class DfsPage(tk.Frame):
    pagePointer = "Dfs"
    relatedNodeElementsMapping =  {
        "A": {
            "Next": {
                "B": {},
                "C": {},
                "D": {}
            }
        },
        "B": {},
        "C": {
            "Next":{
                "E":{}
            }
        },
        "D": {
            "Next":{
                "F":{}
            }
        },
        "E": {},
        "F": {}
    }
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        greeting = tk.Label(self,text="Depth first search visualization page goes here")
        greeting.pack()

        #ELEMENT CREATION
        self.rootCanvas = Canvas(self,width=640,height=480)
        self.rootCanvas.pack()
        self.relatedNodeElementsMapping["A"]["Oval"] = self.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        self.rootCanvas.move(self.relatedNodeElementsMapping["A"]["Oval"], 220,100)
        self.relatedNodeElementsMapping["A"]["Label"] = self.rootCanvas.create_text(220+35,100+35,text="A") # Add 35 to fix the position
        self.relatedNodeElementsMapping["A"]["Next"]["B"]["Line"] = self.rootCanvas.create_line(220+25, 100+55, 225, 200, arrow=tk.LAST)
        self.relatedNodeElementsMapping["A"]["Next"]["C"]["Line"] = self.rootCanvas.create_line(230+25, 100+55, 290, 200, arrow=tk.LAST)
        self.relatedNodeElementsMapping["A"]["Next"]["D"]["Line"] = self.rootCanvas.create_line(240+25, 100+55, 290+65, 200, arrow=tk.LAST)

        self.relatedNodeElementsMapping["B"]["Oval"] = self.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        self.rootCanvas.move(self.relatedNodeElementsMapping["B"]["Oval"], 180,100+85)
        self.relatedNodeElementsMapping["B"]["Label"] = self.rootCanvas.create_text(180+35,100+85+35,text="B") # Add 35 to fix the position

        self.relatedNodeElementsMapping["C"]["Oval"] = self.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        self.rootCanvas.move(self.relatedNodeElementsMapping["C"]["Oval"], 260,100+85)
        self.relatedNodeElementsMapping["C"]["Label"] = self.rootCanvas.create_text(260+35,100+85+35,text="C") # Add 35 to fix the position
        self.relatedNodeElementsMapping["C"]["Next"]["E"]["Line"] = self.rootCanvas.create_line(260+25, 180+55, 260 , 265, arrow=tk.LAST)

        self.relatedNodeElementsMapping["D"]["Oval"] = self.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        self.rootCanvas.move(self.relatedNodeElementsMapping["D"]["Oval"], 340,100+85)
        self.relatedNodeElementsMapping["D"]["Label"] = self.rootCanvas.create_text(340+35,100+85+35,text="D") # Add 35 to fix the position
        self.relatedNodeElementsMapping["D"]["Next"]["F"]["Line"] = self.rootCanvas.create_line(340+25, 180+55, 340 , 265, arrow=tk.LAST)

        self.relatedNodeElementsMapping["E"]["Oval"] = self.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        self.rootCanvas.move(self.relatedNodeElementsMapping["E"]["Oval"], 220,160+85)
        self.relatedNodeElementsMapping["E"]["Label"] = self.rootCanvas.create_text(220+35,160+85+35,text="E") # Add 35 to fix the position

        self.relatedNodeElementsMapping["F"]["Oval"] = self.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        self.rootCanvas.move(self.relatedNodeElementsMapping["F"]["Oval"], 300,160+85)
        self.relatedNodeElementsMapping["F"]["Label"] = self.rootCanvas.create_text(300+35,160+85+35,text="F") # Add 35 to fix the position
        #canvas.update()
        # ─────────────────────────────────────────────────────────────────

class DijkstraPage(tk.Frame):
    pagePointer = "Dijkstra"
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        greeting = tk.Label(self,text="Dijkstra search visualization page goes here")
        greeting.pack()

        #Logic will be belonging here

        # ─────────────────────────────────────────────────────────────────

# ─── CONTROLLER ─────────────────────────────────────────────────────────────────
class FrameController(tk.Tk):
    currentPage = NONE
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
        FrameController.currentPage = self.frames[cont].pagePointer
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
    tickTimer.cancel()

     
# ────────────────────────────────────────────────────────────────────────────────

#Interval checker&logic driven
def tick():
    global tickTimer
    tickTimer = threading.Timer(1.0, tick)
    tickTimer.start()
    print("Ticking %s" % (FrameController.currentPage))
# ────────────────────────────────────────────────────────────────────────────────


global app
app = FrameController()
app.title("Search Algorithm Demonstration GUI-APPLICATION")
tick()
app.mainloop()

tickTimer.cancel()#defer