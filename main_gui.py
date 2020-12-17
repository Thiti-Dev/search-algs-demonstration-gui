import tkinter as tk
from tkinter import *
import threading
import config as config
from PIL import Image, ImageTk

# ─── CALLBACK FUNCS ─────────────────────────────────────────────────────────────
class Stimulator:
    currentStimulation = None
    tick_timer = None
    tick_interval = 1.0


    #DFS#
    operation_list = [] # a list contains set of lambda
    operation_list_info = []
    current_operator_cnt = 0 # use for fixing the bugged if the array is popped while doing the iteration
    orderize_string = ""
    # ────────────────────────────────────────────────────────────────────────────────

    @staticmethod
    def start(name):
        print("Starting stimulator with type of %s" % (name))
        Stimulator.currentStimulation = name

        #start the thread time
        if name == "DFS":
            #this only runs once the button has been clicked
            Stimulator.tick_timer = threading.Timer(Stimulator.tick_interval, Stimulator.tick_invoke)

            # All of the DFS logics are below here and all of it will be appening in the operation_list
            def dfs(_visited,graph,node):
                if node not in _visited:
                    print(node)
                    _visited.add(node) # mark node as visited
                    if "Next" in graph[node]: # If having node that can transverse to
                        for neighbour in graph[node]["Next"]:
                            #DfsPage.rootCanvas.itemconfig(graph[node]["Next"][neighbour]["Line"], fill='red')
                            Stimulator.operation_list.append(lambda : (
                                DfsPage.rootCanvas.itemconfig(graph[node]["Next"][neighbour]["Line"], fill='red'),
                                print(f'Invoke from {node} to {neighbour}')
                            ))
                            Stimulator.operation_list_info.append((node,neighbour))
                            dfs(visited, graph, neighbour)

            visited = set()
            dfs(visited,DfsPage.relatedNodeElementsMapping,'A')
            Stimulator.orderize_string='A -> '
            print("Length of operation %d" %(len(Stimulator.operation_list)))
            print(Stimulator.operation_list_info)
            # ─────────────────────────────────────────────────────────────────

            
        Stimulator.tick_timer.start()
    @staticmethod
    def tick_invoke():
        Stimulator.tick_timer = threading.Timer(Stimulator.tick_interval, Stimulator.tick_invoke)
        Stimulator.tick_timer.start() # made continuoys
        if Stimulator.currentStimulation == "DFS":
            Stimulator.dfs_tick()
    @staticmethod
    def dfs_tick():
        print("Tick runs here")

        # This methods is bugged
        # if len(Stimulator.operation_list): #if there is the process remain
        #     #Stimulator.operation_list[0]() # run the lambda exp from the list >Currently Bugged<
        #     print(Stimulator.operation_list_info)
        #     if Stimulator.operation_list_info[0]:

        #         fromNode,toNode = Stimulator.operation_list_info[0]
        #         DfsPage.rootCanvas.itemconfig(DfsPage.relatedNodeElementsMapping[fromNode]["Next"][toNode]["Line"], fill='red')
        #         #Stimulator.operation_list.pop(0) # popped after >Currently bugged<
        #         Stimulator.operation_list_info.pop(0) # popped after
        # else:
        #     print("Finish stimulation operation")

        if len(Stimulator.operation_list) > Stimulator.current_operator_cnt:
            fromNode,toNode = Stimulator.operation_list_info[Stimulator.current_operator_cnt]
            DfsPage.rootCanvas.itemconfig(DfsPage.relatedNodeElementsMapping[fromNode]["Next"][toNode]["Line"], fill='red')
            Stimulator.current_operator_cnt=Stimulator.current_operator_cnt+1

            if Stimulator.current_operator_cnt == len(Stimulator.operation_list):
                Stimulator.orderize_string=Stimulator.orderize_string+toNode
            else:
                Stimulator.orderize_string=Stimulator.orderize_string+toNode + ' -> '
            result_label.config(text=Stimulator.orderize_string)
        else:
             print("Finish stimulation operation")

# ────────────────────────────────────────────────────────────────────────────────


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
    rootCanvas = None
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

        exit_btn = tk.Button(self,command=lambda: controller.show_frame(MenuPage), text="Home",bg="gray",fg="blue2",activebackground="red",font=('times', 15, ' bold '))
        exit_btn.place(x=600,y=450,anchor="center")
        
        greeting = tk.Label(self,text="Stimulation Panel")
        greeting.place(x=370,y=20)

        sim_start_btn = tk.Button(self,command=lambda: Stimulator.start("DFS"), text="Start",bg="orange",fg="white",activebackground="gray",font=('times', 8, ' bold '))
        sim_start_btn.place(x=300,y=80,anchor="center",width=60)

        sim_start_label = tk.Label(self,text="To start the search algorithm")
        sim_start_label.place(x=350,y=70)

        code_peek_btn = tk.Button(self,command=lambda: codeViewing("DFS"), text="Code",bg="orange2",fg="white",activebackground="gray",font=('times', 8, ' bold '))
        code_peek_btn.place(x=300,y=120,anchor="center",width=60)

        code_peek_btn_label = tk.Label(self,text="To see how this algorithm written in python")
        code_peek_btn_label.place(x=350,y=110)

        result_label_info = tk.Label(self,text="Visited node in order:")
        result_label_info.place(x=220,y=220)

        global result_label
        result_label = tk.Label(self,text="")
        result_label.place(x=220,y=270)

        #ELEMENT CREATION -> CANVAS
        DfsPage.rootCanvas = Canvas(self,width=400,height=480,bg="gray")
        DfsPage.rootCanvas.place(x=-200,y=0)
        self.relatedNodeElementsMapping["A"]["Oval"] = DfsPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        DfsPage.rootCanvas.move(self.relatedNodeElementsMapping["A"]["Oval"], 220,100)
        self.relatedNodeElementsMapping["A"]["Label"] = DfsPage.rootCanvas.create_text(220+35,100+35,text="A") # Add 35 to fix the position
        self.relatedNodeElementsMapping["A"]["Next"]["B"]["Line"] = DfsPage.rootCanvas.create_line(220+25, 100+55, 225, 200, arrow=tk.LAST)
        self.relatedNodeElementsMapping["A"]["Next"]["C"]["Line"] = DfsPage.rootCanvas.create_line(230+25, 100+55, 290, 200, arrow=tk.LAST)
        self.relatedNodeElementsMapping["A"]["Next"]["D"]["Line"] = DfsPage.rootCanvas.create_line(240+25, 100+55, 290+65, 200, arrow=tk.LAST)

        self.relatedNodeElementsMapping["B"]["Oval"] = DfsPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        DfsPage.rootCanvas.move(self.relatedNodeElementsMapping["B"]["Oval"], 180,100+85)
        self.relatedNodeElementsMapping["B"]["Label"] = DfsPage.rootCanvas.create_text(180+35,100+85+35,text="B") # Add 35 to fix the position

        self.relatedNodeElementsMapping["C"]["Oval"] = DfsPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        DfsPage.rootCanvas.move(self.relatedNodeElementsMapping["C"]["Oval"], 260,100+85)
        self.relatedNodeElementsMapping["C"]["Label"] = DfsPage.rootCanvas.create_text(260+35,100+85+35,text="C") # Add 35 to fix the position
        self.relatedNodeElementsMapping["C"]["Next"]["E"]["Line"] = DfsPage.rootCanvas.create_line(260+25, 180+55, 260 , 265, arrow=tk.LAST)

        self.relatedNodeElementsMapping["D"]["Oval"] = DfsPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        DfsPage.rootCanvas.move(self.relatedNodeElementsMapping["D"]["Oval"], 340,100+85)
        self.relatedNodeElementsMapping["D"]["Label"] = DfsPage.rootCanvas.create_text(340+35,100+85+35,text="D") # Add 35 to fix the position
        self.relatedNodeElementsMapping["D"]["Next"]["F"]["Line"] = DfsPage.rootCanvas.create_line(340+25, 180+55, 340 , 265, arrow=tk.LAST)

        self.relatedNodeElementsMapping["E"]["Oval"] = DfsPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        DfsPage.rootCanvas.move(self.relatedNodeElementsMapping["E"]["Oval"], 220,160+85)
        self.relatedNodeElementsMapping["E"]["Label"] = DfsPage.rootCanvas.create_text(220+35,160+85+35,text="E") # Add 35 to fix the position

        self.relatedNodeElementsMapping["F"]["Oval"] = DfsPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        DfsPage.rootCanvas.move(self.relatedNodeElementsMapping["F"]["Oval"], 300,160+85)
        self.relatedNodeElementsMapping["F"]["Label"] = DfsPage.rootCanvas.create_text(300+35,160+85+35,text="F") # Add 35 to fix the position
        #canvas.update()
        # ─────────────────────────────────────────────────────────────────


    #Deprecated -> unused
    def createPanelWindow(self):
        self.panel = tk.Tk()
        self.panel.title("Panel")
        self.panel.geometry('200x200')
        self.panel.configure(background='snow')
        self.panel.mainloop()

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
        
        if FrameController.currentPage == "Dfs":
            print("Nothing")
            #self.frames[cont].createPanelWindow()
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


def codeViewing(algs_name):
    if algs_name == "DFS":
        code_window = tk.Tk()
        code_window.title("Depth first search in python")
        #code_window.geometry('533x411')
        code_window.configure(background='snow')

        load = Image.open("dfs_code.PNG")
        code_window.geometry(f'{load.size[0]}x{load.size[1]}')
        render = ImageTk.PhotoImage(load,master=code_window)
        img = Label(code_window, image=render)
        img.image = render
        img.place(x=0, y=0)
        
        code_window.mainloop()
# ────────────────────────────────────────────────────────────────────────────────

#Interval checker&logic driven
def tick():
    global tickTimer
    tickTimer = threading.Timer(1.0, tick)
    tickTimer.start()
    print("Current viewing frame page :  %s" % (FrameController.currentPage))
# ────────────────────────────────────────────────────────────────────────────────


global app
app = FrameController()
app.title("Search Algorithm Demonstration GUI-APPLICATION")
tick()
app.mainloop()

tickTimer.cancel()#defer
Stimulator.tick_timer.cancel()#defer