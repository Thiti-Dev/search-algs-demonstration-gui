import tkinter as tk
from tkinter import *
import threading
import config as config
from PIL import Image, ImageTk
import algorithm as algos
from operator import itemgetter

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

    #BFS#
    bfs_operation_list = []
    bfs_operation_list_info = []
    bfs_current_operator_cnt = 0
    bfs_orderize_string = ""   
    # ────────────────────────────────────────────────────────────────────────────────


    #KRUSKAL#
    kruskal_operation_list = []
    kruskal_operation_list_info = []
    kruskal_current_operator_cnt = 0
    kruskal_orderize_string = ""
    kruskal_mst_value = 0
    # ────────────────────────────────────────────────────────────────────────────────

    #DIJKSTRA#
    dijkstra_operation_list = []
    dijkstra_operation_list_info = []
    dijkstra_current_operator_cnt = 0
    dijkstra_orderize_string = ""
    dijkstra_orderized_path = []
    dijstra_total_distance = 0.0
    # ────────────────────────────────────────────────────────────────────────────────


    @staticmethod
    def resetStaticValuesToInitial():
        #DFS#
        Stimulator.operation_list = [] # a list contains set of lambda
        Stimulator.operation_list_info = []
        Stimulator.current_operator_cnt = 0 # use for fixing the bugged if the array is popped while doing the iteration
        Stimulator.orderize_string = ""
        # ────────────────────────────────────────────────────────────────────────────────

        #BFS#
        Stimulator.bfs_operation_list = []
        Stimulator.bfs_operation_list_info = []
        Stimulator.bfs_current_operator_cnt = 0
        Stimulator.bfs_orderize_string = ""   
        # ────────────────────────────────────────────────────────────────────────────────


        #KRUSKAL#
        Stimulator.kruskal_operation_list = []
        Stimulator.kruskal_operation_list_info = []
        Stimulator.kruskal_current_operator_cnt = 0
        Stimulator.kruskal_orderize_string = ""
        Stimulator.kruskal_mst_value = 0
        # ────────────────────────────────────────────────────────────────────────────────

        #DIJKSTRA#
        Stimulator.dijkstra_operation_list = []
        Stimulator.dijkstra_operation_list_info = []
        Stimulator.dijkstra_current_operator_cnt = 0
        Stimulator.dijkstra_orderize_string = ""
        Stimulator.dijkstra_orderized_path = []
        Stimulator.dijstra_total_distance = 0.0
        # ────────────────────────────────────────────────────────────────────────────────        

    @staticmethod
    def start(name):

        if Stimulator.tick_timer is not None: return # return if tick_timer is in progress

        Stimulator.resetStaticValuesToInitial() # reset -> made available for clicking the start again
        print("Starting stimulator with type of %s" % (name))
        Stimulator.currentStimulation = name
        isStimulatorTickBeenSettle = False
        #start the thread time
        if name == "DFS":
            #this only runs once the button has been clicked
            Stimulator.tick_timer = threading.Timer(Stimulator.tick_interval, Stimulator.tick_invoke)
            isStimulatorTickBeenSettle = True
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
            Stimulator.orderize_string='A'
            print("Length of operation %d" %(len(Stimulator.operation_list)))
            print(Stimulator.operation_list_info)
            # ─────────────────────────────────────────────────────────────────

            
        elif name == "BFS":
            print("BFS STARTING")
            Stimulator.tick_timer = threading.Timer(Stimulator.tick_interval, Stimulator.tick_invoke)
            isStimulatorTickBeenSettle = True





            #BFS LOGICS ARE BELOW HERE
            queue = []     #Initialize a queue
            def bfs(visited, graph, node):
                visited.append(node)
                queue.append(node)

                while queue:
                    s = queue.pop(0) 
                    print (s, end = " ") 

                    if "Next" in graph[s]:
                        for neighbour in graph[s]["Next"]:
                            if neighbour not in visited:
                                visited.append(neighbour)
                                queue.append(neighbour)
                                Stimulator.bfs_operation_list_info.append((s,neighbour))

            visited = [] # List to keep track of visited nodes.
            bfs(visited, DfsPage.relatedNodeElementsMapping, 'A')
            Stimulator.bfs_orderize_string='A'
            # ─────────────────────────────────────────────────────────────────





        elif name == "KRUSKAL":
            print("KRUSKAL STARTING")
            Stimulator.tick_timer = threading.Timer(Stimulator.tick_interval, Stimulator.tick_invoke)
            isStimulatorTickBeenSettle = True

            #KRUSKAL LOGICS ARE BELOW HERE

            g = algos.Kruskal(5)
            g.add_edge(0, 1, 10)
            g.add_edge(0, 2, 6)
            g.add_edge(0, 3, 5)
            g.add_edge(1, 3, 15)
            g.add_edge(2, 3, 4)
            g.add_edge(3, 4, 7)
            g.kruskal_algo()

            Stimulator.kruskal_operation_list,Stimulator.kruskal_mst_value = g.kruskal_algo_custom()

            # ─────────────────────────────────────────────────────────────────


        elif name == "DIJKSTRA":
            print("DIJKSTRA STARTING")
            Stimulator.tick_timer = threading.Timer(Stimulator.tick_interval, Stimulator.tick_invoke)
            isStimulatorTickBeenSettle = True



            #DIJKSTRA LOGICS ARE BELOW HERE
            input_vertices = ("A", "B", "C", "D", "E")
            input_graph = {
                "A": {"B": 10, "C": 3},
                "B": {"D": 2},
                "C": {"B": 4, "D": 8, "E": 2},
                "D": {"E": 7},
                "E": {"D": 7}
            }
            start_vertex = "A"
            end_vertex= "B"
            dijkstra = algos.Dijkstra(input_vertices, input_graph)
            p, v = dijkstra.find_route(start_vertex, end_vertex)
            Stimulator.dijkstra_operation_list = dijkstra.find_route_custom(start_vertex, end_vertex)
            Stimulator.dijstra_total_distance = v[end_vertex]
            print("Distance from %s to %s is: %.2f" % (start_vertex, end_vertex, v[end_vertex]))
            Stimulator.dijkstra_orderized_path = dijkstra.generate_path(p, start_vertex, end_vertex)
            print("Path from %s to %s is: %s" % (start_vertex, end_vertex, " -> ".join(Stimulator.dijkstra_orderized_path)))

            # ─────────────────────────────────────────────────────────────────


        #just to ensure that the tick was set -> before starting it
        if isStimulatorTickBeenSettle:
            Stimulator.tick_timer.start() # start any tick thread created from above
    @staticmethod
    def tick_invoke():
        Stimulator.tick_timer = threading.Timer(Stimulator.tick_interval, Stimulator.tick_invoke)
        Stimulator.tick_timer.start() # made continuoys
        if Stimulator.currentStimulation == "DFS":
            Stimulator.dfs_tick()
        elif Stimulator.currentStimulation == "BFS":
            Stimulator.bfs_tick()
        elif Stimulator.currentStimulation == "KRUSKAL":
            Stimulator.kruskal_tick()
        elif Stimulator.currentStimulation == "DIJKSTRA":
            Stimulator.dijkstra_tick()

    @staticmethod
    def dijkstra_tick():

        def reverseNodeBgToDefault():
            for node in DijkstraPage.relatedNodeElementsMapping:
                DijkstraPage.rootCanvas.itemconfig(DijkstraPage.relatedNodeElementsMapping[node]["Oval"], fill='white')

        print("Dijkstra tick runs here")
        print(Stimulator.dijkstra_operation_list)
        reverseNodeBgToDefault() # clean the color

        if len(Stimulator.dijkstra_operation_list) > Stimulator.dijkstra_current_operator_cnt:
            fromNode, toNode = Stimulator.dijkstra_operation_list[Stimulator.dijkstra_current_operator_cnt]
            DijkstraPage.rootCanvas.itemconfig(DijkstraPage.relatedNodeElementsMapping[fromNode]["Oval"], fill='blue')
            DijkstraPage.rootCanvas.itemconfig(DijkstraPage.relatedNodeElementsMapping[toNode]["Oval"], fill='red')

            Stimulator.dijkstra_orderize_string = Stimulator.dijkstra_orderize_string + f'Considering {fromNode} -> {toNode}\n'
            dijkstra_result_label.config(text=Stimulator.dijkstra_orderize_string)

            Stimulator.dijkstra_current_operator_cnt=Stimulator.dijkstra_current_operator_cnt+1
        else:
            print('Finished to operation')
            print(Stimulator.dijkstra_orderized_path)

            for node in Stimulator.dijkstra_orderized_path:
                DijkstraPage.rootCanvas.itemconfig(DijkstraPage.relatedNodeElementsMapping[node]["Oval"], fill='green')

            Stimulator.dijkstra_orderize_string = Stimulator.dijkstra_orderize_string + 'Shortest path from A -> B is: ' + "->".join(Stimulator.dijkstra_orderized_path) + '\nWith total distance: ' + str(Stimulator.dijstra_total_distance)
            dijkstra_result_label.config(text=Stimulator.dijkstra_orderize_string)

            Stimulator.tick_timer.cancel()
            Stimulator.tick_timer = None

    @staticmethod
    def kruskal_tick():


        def reverseNodeBgToDefault():
            for node in KruskalPage.relatedNodeElementsMapping:
                if "Next" in KruskalPage.relatedNodeElementsMapping[node]:
                    for nextNode in KruskalPage.relatedNodeElementsMapping[node]["Next"]:
                        if "Line" in KruskalPage.relatedNodeElementsMapping[node]["Next"][nextNode]:
                            KruskalPage.rootCanvas.itemconfig(KruskalPage.relatedNodeElementsMapping[node]["Next"][nextNode]['Line'], fill='black')

        print("Kruskal tick runs here")
        print(Stimulator.kruskal_operation_list)
        if Stimulator.kruskal_current_operator_cnt == 0: reverseNodeBgToDefault() # reverse = clean the line color

        if len(Stimulator.kruskal_operation_list) > Stimulator.kruskal_current_operator_cnt:
            fromNode, toNode, weight = itemgetter('from', 'to','weight')(Stimulator.kruskal_operation_list[Stimulator.kruskal_current_operator_cnt])
            print(f'From {fromNode} to {toNode}')
            Stimulator.kruskal_orderize_string = Stimulator.kruskal_orderize_string + f'FROM {fromNode} -> {toNode} : WEIGHT({weight})\n'
            kruskal_result_label.config(text=Stimulator.kruskal_orderize_string)
            KruskalPage.rootCanvas.itemconfig(KruskalPage.relatedNodeElementsMapping[str(fromNode)]["Next"][str(toNode)]["Line"], fill='red')
            Stimulator.kruskal_current_operator_cnt=Stimulator.kruskal_current_operator_cnt+1
        else:
             print("Finish stimulation operation")
             Stimulator.kruskal_orderize_string = Stimulator.kruskal_orderize_string + '\nTotal weight of MST: ' + str(Stimulator.kruskal_mst_value)
             kruskal_result_label.config(text=Stimulator.kruskal_orderize_string)
             Stimulator.tick_timer.cancel()
             Stimulator.tick_timer = None

    @staticmethod
    def dfs_tick():
        print("Tick runs here")

        def reverseNodeBgToDefault():
            for node in DfsPage.relatedNodeElementsMapping:
                if "Next" in DfsPage.relatedNodeElementsMapping[node]:
                    for nextNode in DfsPage.relatedNodeElementsMapping[node]["Next"]:
                        if "Line" in DfsPage.relatedNodeElementsMapping[node]["Next"][nextNode]:
                            DfsPage.rootCanvas.itemconfig(DfsPage.relatedNodeElementsMapping[node]["Next"][nextNode]['Line'], fill='black')
        if Stimulator.current_operator_cnt == 0: reverseNodeBgToDefault() # reverse = clean the line color

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

            Stimulator.orderize_string=Stimulator.orderize_string+' -> '+toNode
            result_label.config(text=Stimulator.orderize_string)
        else:
             print("Finish stimulation operation")
             Stimulator.tick_timer.cancel()
             Stimulator.tick_timer = None

    @staticmethod
    def bfs_tick():
        print("BFS TICK'S RUNNING")

        def reverseNodeBgToDefault():
            for node in BfsPage.relatedNodeElementsMapping:
                if "Next" in BfsPage.relatedNodeElementsMapping[node]:
                    for nextNode in BfsPage.relatedNodeElementsMapping[node]["Next"]:
                        if "Line" in BfsPage.relatedNodeElementsMapping[node]["Next"][nextNode]:
                            BfsPage.rootCanvas.itemconfig(BfsPage.relatedNodeElementsMapping[node]["Next"][nextNode]['Line'], fill='black')

        if Stimulator.bfs_current_operator_cnt == 0: reverseNodeBgToDefault() # reverse = clean the line color

        if len(Stimulator.bfs_operation_list_info) > Stimulator.bfs_current_operator_cnt:
            fromNode,toNode = Stimulator.bfs_operation_list_info[Stimulator.bfs_current_operator_cnt]
            BfsPage.rootCanvas.itemconfig(BfsPage.relatedNodeElementsMapping[fromNode]["Next"][toNode]["Line"], fill='red')
            Stimulator.bfs_current_operator_cnt=Stimulator.bfs_current_operator_cnt+1

            Stimulator.bfs_orderize_string=Stimulator.bfs_orderize_string+' -> '+toNode
            result_label_bfs.config(text=Stimulator.bfs_orderize_string)
        else:
             print("Finish stimulation operation")
             Stimulator.tick_timer.cancel()
             Stimulator.tick_timer = None

# ────────────────────────────────────────────────────────────────────────────────


class MenuPage(tk.Frame):
    pagePointer = "Menu"
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        #Passing self as root_window
        message = tk.Label(self, text="Search algorithms gui demonstration", bg="blue2", fg="snow",font=('times', 20, ' bold '))
        message.place(x=getCenteredAxis()["x"], y=30,anchor="center")

        credit = tk.Label(self, text="Created by Thiti Mahawannakit 60090500410 and uses for CSS121", bg="gray", fg="black",font=('times', 8, ' bold '))
        credit.place(x=185, y=455,anchor="center")

        dijkstra_btn = tk.Button(self,command=lambda: controller.show_frame(DijkstraPage), text="Dijkstra search algorithm",bg="orange",fg="white",activebackground="gray",font=('times', 15, ' bold '))
        dijkstra_btn.place(x=getCenteredAxis()["x"],y=150,anchor="center",width=300)

        bfs_btn = tk.Button(self,command=lambda: controller.show_frame(BfsPage), text="Breadth first search algorithm",bg="orange",fg="white",activebackground="gray",font=('times', 15, ' bold '))
        bfs_btn.place(x=getCenteredAxis()["x"],y=200,anchor="center",width=300)

        dfs_btn = tk.Button(self,command=lambda: controller.show_frame(DfsPage), text="Depth first search algorithm",bg="orange",fg="white",activebackground="gray",font=('times', 15, ' bold '))
        dfs_btn.place(x=getCenteredAxis()["x"],y=250,anchor="center",width=300)

        dijkstra_btn = tk.Button(self,command=lambda: controller.show_frame(KruskalPage), text="Kruskal’s MST Algorithm",bg="orange",fg="white",activebackground="gray",font=('times', 15, ' bold '))
        dijkstra_btn.place(x=getCenteredAxis()["x"],y=300,anchor="center",width=300)

        exit_btn = tk.Button(self,command=exitProgram, text="Exit",bg="red",fg="white",activebackground="gray",font=('times', 15, ' bold '))
        exit_btn.place(x=600,y=450,anchor="center")

class BfsPage(tk.Frame):
    pagePointer = "Bfs"
    rootCanvas = None
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

        sim_start_btn = tk.Button(self,command=lambda: Stimulator.start("BFS"), text="Start",bg="orange",fg="white",activebackground="gray",font=('times', 8, ' bold '))
        sim_start_btn.place(x=300,y=80,anchor="center",width=60)

        sim_start_label = tk.Label(self,text="To start the breadth first search algorithm")
        sim_start_label.place(x=350,y=70)

        code_peek_btn = tk.Button(self,command=lambda: codeViewing("BFS"), text="Code",bg="orange2",fg="white",activebackground="gray",font=('times', 8, ' bold '))
        code_peek_btn.place(x=300,y=120,anchor="center",width=60)

        code_peek_btn_label = tk.Label(self,text="To see how this algorithm written in python")
        code_peek_btn_label.place(x=350,y=110)

        result_label_info = tk.Label(self,text="Visited node in order:")
        result_label_info.place(x=220,y=220)

        global result_label_bfs
        result_label_bfs = tk.Label(self,text="")
        result_label_bfs.place(x=220,y=270)

        #Logic will be belonging here

        BfsPage.rootCanvas = Canvas(self,width=400,height=480,bg="gray")
        BfsPage.rootCanvas.place(x=-200,y=0)
        BfsPage.relatedNodeElementsMapping["A"]["Oval"] = BfsPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        BfsPage.rootCanvas.move(BfsPage.relatedNodeElementsMapping["A"]["Oval"], 220,100)
        BfsPage.relatedNodeElementsMapping["A"]["Label"] = BfsPage.rootCanvas.create_text(220+35,100+35,text="A") # Add 35 to fix the position
        BfsPage.relatedNodeElementsMapping["A"]["Next"]["B"]["Line"] = BfsPage.rootCanvas.create_line(220+25, 100+55, 225, 200, arrow=tk.LAST)
        BfsPage.relatedNodeElementsMapping["A"]["Next"]["C"]["Line"] = BfsPage.rootCanvas.create_line(230+25, 100+55, 290, 200, arrow=tk.LAST)
        BfsPage.relatedNodeElementsMapping["A"]["Next"]["D"]["Line"] = BfsPage.rootCanvas.create_line(240+25, 100+55, 290+65, 200, arrow=tk.LAST)

        BfsPage.relatedNodeElementsMapping["B"]["Oval"] = BfsPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        BfsPage.rootCanvas.move(BfsPage.relatedNodeElementsMapping["B"]["Oval"], 180,100+85)
        BfsPage.relatedNodeElementsMapping["B"]["Label"] = BfsPage.rootCanvas.create_text(180+35,100+85+35,text="B") # Add 35 to fix the position

        BfsPage.relatedNodeElementsMapping["C"]["Oval"] = BfsPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        BfsPage.rootCanvas.move(BfsPage.relatedNodeElementsMapping["C"]["Oval"], 260,100+85)
        BfsPage.relatedNodeElementsMapping["C"]["Label"] = BfsPage.rootCanvas.create_text(260+35,100+85+35,text="C") # Add 35 to fix the position
        BfsPage.relatedNodeElementsMapping["C"]["Next"]["E"]["Line"] = BfsPage.rootCanvas.create_line(260+25, 180+55, 260 , 265, arrow=tk.LAST)

        BfsPage.relatedNodeElementsMapping["D"]["Oval"] = BfsPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        BfsPage.rootCanvas.move(BfsPage.relatedNodeElementsMapping["D"]["Oval"], 340,100+85)
        BfsPage.relatedNodeElementsMapping["D"]["Label"] = BfsPage.rootCanvas.create_text(340+35,100+85+35,text="D") # Add 35 to fix the position
        BfsPage.relatedNodeElementsMapping["D"]["Next"]["F"]["Line"] = BfsPage.rootCanvas.create_line(340+25, 180+55, 340 , 265, arrow=tk.LAST)

        BfsPage.relatedNodeElementsMapping["E"]["Oval"] = BfsPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        BfsPage.rootCanvas.move(BfsPage.relatedNodeElementsMapping["E"]["Oval"], 220,160+85)
        BfsPage.relatedNodeElementsMapping["E"]["Label"] = BfsPage.rootCanvas.create_text(220+35,160+85+35,text="E") # Add 35 to fix the position

        BfsPage.relatedNodeElementsMapping["F"]["Oval"] = BfsPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        BfsPage.rootCanvas.move(BfsPage.relatedNodeElementsMapping["F"]["Oval"], 300,160+85)
        BfsPage.relatedNodeElementsMapping["F"]["Label"] = BfsPage.rootCanvas.create_text(300+35,160+85+35,text="F") # Add 35 to fix the position

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
    rootCanvas = None
    pagePointer = "Dijkstra"
    relatedNodeElementsMapping =  {
        "A": {
            "Next": {
                "B": {},
                "C": {},
                "D": {}
            }
        },
        "B": {
            "Next":{
                "D":{}
            }
        },
        "C": {
            "Next":{
                "E":{},
                "B":{},
                "D":{}
            }
        },
        "D": {
            "Next":{
                "F":{}
            }
        },
        "E": {
            "Next":{
                "D":{}
            }
        }
    }    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        exit_btn = tk.Button(self,command=lambda: controller.show_frame(MenuPage), text="Home",bg="gray",fg="blue2",activebackground="red",font=('times', 15, ' bold '))
        exit_btn.place(x=600,y=450,anchor="center")       


        result_label_info = tk.Label(self,text="Dijkstra operations in order:")
        result_label_info.place(x=280,y=220)

        global dijkstra_result_label
        dijkstra_result_label = tk.Label(self,text="")
        dijkstra_result_label.place(x=380,y=320,anchor="center")

        greeting = tk.Label(self,text="Stimulation Panel")
        greeting.place(x=400,y=20)


        sim_start_btn = tk.Button(self,command=lambda: Stimulator.start("DIJKSTRA"), text="Start",bg="orange",fg="white",activebackground="gray",font=('times', 8, ' bold '))
        sim_start_btn.place(x=300+15,y=80,anchor="center",width=60)

        sim_start_label = tk.Label(self,text="To start the search algorithm")
        sim_start_label.place(x=350,y=70)

        code_peek_btn = tk.Button(self,command=lambda: codeViewing("DIJKSTRA"), text="Code",bg="orange2",fg="white",activebackground="gray",font=('times', 8, ' bold '))
        code_peek_btn.place(x=300+15,y=120,anchor="center",width=60)

        code_peek_btn_label = tk.Label(self,text="To see how this algorithm written in python")
        code_peek_btn_label.place(x=350,y=110)


        #Logic will be belonging here

        DijkstraPage.rootCanvas = Canvas(self,width=400,height=480,bg="gray")    
        DijkstraPage.rootCanvas.place(x=-150,y=0)

        weight_label_a_b = Label(DijkstraPage.rootCanvas,text = "10",fg="blue",bg="yellow")
        weight_label_a_b.place(x = 210,y = 150)


        weight_label_a_c = Label(DijkstraPage.rootCanvas,text = "3",fg="blue",bg="yellow")
        weight_label_a_c.place(x = 280,y = 150)

        weight_label_b_d = Label(DijkstraPage.rootCanvas,text = "2",fg="blue",bg="yellow")
        weight_label_b_d.place(x = 215,y = 250)

        weight_label_c_b = Label(DijkstraPage.rootCanvas,text = "4",fg="blue",bg="yellow")
        weight_label_c_b.place(x = 252,y = 190)

        weight_label_c_d = Label(DijkstraPage.rootCanvas,text = "8",fg="blue",bg="yellow")
        weight_label_c_d.place(x = 255,y = 230)

        weight_label_c_e = Label(DijkstraPage.rootCanvas,text = "2",fg="blue",bg="yellow")
        weight_label_c_e.place(x = 320,y = 230)

        weight_label_ed_de = Label(DijkstraPage.rootCanvas,text = "7",fg="blue",bg="yellow")
        weight_label_ed_de.place(x = 290,y = 285)


        DijkstraPage.relatedNodeElementsMapping["A"]["Oval"] = DijkstraPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        DijkstraPage.rootCanvas.move(DijkstraPage.relatedNodeElementsMapping["A"]["Oval"], 220,100)
        DijkstraPage.relatedNodeElementsMapping["A"]["Label"] = DijkstraPage.rootCanvas.create_text(220+35,100+35,text="A") # Add 35 to fix the position
        DijkstraPage.relatedNodeElementsMapping["A"]["Next"]["B"]["Line"] = DijkstraPage.rootCanvas.create_line(220+25, 100+55, 225, 200, arrow=tk.LAST)
        DijkstraPage.relatedNodeElementsMapping["A"]["Next"]["C"]["Line"] = DijkstraPage.rootCanvas.create_line(230+25, 100+55, 290, 200, arrow=tk.LAST)

        DijkstraPage.relatedNodeElementsMapping["B"]["Oval"] = DijkstraPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        DijkstraPage.rootCanvas.move(DijkstraPage.relatedNodeElementsMapping["B"]["Oval"], 180,100+85)
        DijkstraPage.relatedNodeElementsMapping["B"]["Label"] = DijkstraPage.rootCanvas.create_text(180+35,100+85+35,text="B") # Add 35 to fix the position
        DijkstraPage.relatedNodeElementsMapping["B"]["Next"]["D"]["Line"] = DijkstraPage.rootCanvas.create_line(190+25, 180+55, 250 , 270, arrow=tk.LAST)

        DijkstraPage.relatedNodeElementsMapping["C"]["Oval"] = DijkstraPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        DijkstraPage.rootCanvas.move(DijkstraPage.relatedNodeElementsMapping["C"]["Oval"], 260,100+85)
        DijkstraPage.relatedNodeElementsMapping["C"]["Label"] = DijkstraPage.rootCanvas.create_text(260+35,100+85+35,text="C") # Add 35 to fix the position
        DijkstraPage.relatedNodeElementsMapping["C"]["Next"]["B"]["Line"] = DijkstraPage.rootCanvas.create_line(260+20, 100+120, 180+50 , 100+120,arrow=tk.LAST)
        DijkstraPage.relatedNodeElementsMapping["C"]["Next"]["D"]["Line"] = DijkstraPage.rootCanvas.create_line(260+25, 180+55, 260 , 265, arrow=tk.LAST)
        DijkstraPage.relatedNodeElementsMapping["C"]["Next"]["E"]["Line"] = DijkstraPage.rootCanvas.create_line(280+25, 180+55, 330 , 270, arrow=tk.LAST)

        DijkstraPage.relatedNodeElementsMapping["D"]["Oval"] = DijkstraPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        DijkstraPage.rootCanvas.move(DijkstraPage.relatedNodeElementsMapping["D"]["Oval"], 220,160+85)
        DijkstraPage.relatedNodeElementsMapping["D"]["Label"] = DijkstraPage.rootCanvas.create_text(220+35,160+85+35,text="D") # Add 35 to fix the position

        DijkstraPage.relatedNodeElementsMapping["E"]["Oval"] = DijkstraPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        DijkstraPage.rootCanvas.move(DijkstraPage.relatedNodeElementsMapping["E"]["Oval"], 300,160+85)
        DijkstraPage.relatedNodeElementsMapping["E"]["Label"] = DijkstraPage.rootCanvas.create_text(300+35,160+85+35,text="E") # Add 35 to fix the position
        DijkstraPage.relatedNodeElementsMapping["E"]["Next"]["D"]["Line"] = DijkstraPage.rootCanvas.create_line(300+20, 160+120, 220+50 , 160+120)


        # ─────────────────────────────────────────────────────────────────

class KruskalPage(tk.Frame):
    pagePointer = "Kruskal"
    rootCanvas = None
    relatedNodeElementsMapping =  {
        "0": {
            "Next": {
                "1": {},
                "2": {},
                "3": {}
            }
        },
        "1": {
            "Next": {
                "0": {},
                "3": {}
            }
        },
        "2": {
            "Next":{
                "0":{},
                "3":{}
            }
        },
        "3": {
            "Next":{
                "4":{}
            }
        },
        "4": {}
    }
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        
        exit_btn = tk.Button(self,command=lambda: controller.show_frame(MenuPage), text="Home",bg="gray",fg="blue2",activebackground="red",font=('times', 15, ' bold '))
        exit_btn.place(x=600,y=450,anchor="center")

        result_label_info = tk.Label(self,text="Spanning operations in order:")
        result_label_info.place(x=280,y=220)

        global kruskal_result_label
        kruskal_result_label = tk.Label(self,text="")
        kruskal_result_label.place(x=380,y=320,anchor="center")


        greeting = tk.Label(self,text="Stimulation Panel")
        greeting.place(x=420,y=20)


        sim_start_btn = tk.Button(self,command=lambda: Stimulator.start("KRUSKAL"), text="Start",bg="orange",fg="white",activebackground="gray",font=('times', 8, ' bold '))
        sim_start_btn.place(x=300+15,y=80,anchor="center",width=60)

        sim_start_label = tk.Label(self,text="To start the search algorithm")
        sim_start_label.place(x=350,y=70)

        code_peek_btn = tk.Button(self,command=lambda: codeViewing("KRUSKAL"), text="Code",bg="orange2",fg="white",activebackground="gray",font=('times', 8, ' bold '))
        code_peek_btn.place(x=300+15,y=120,anchor="center",width=60)

        code_peek_btn_label = tk.Label(self,text="To see how this algorithm written in python")
        code_peek_btn_label.place(x=350,y=110)

        #Logic will be belonging here

        KruskalPage.rootCanvas = Canvas(self,width=400,height=480,bg="gray")
        KruskalPage.rootCanvas.place(x=-120,y=0)

        weight_label_0_1 = Label(KruskalPage.rootCanvas,text = "10",fg="blue",bg="yellow")
        weight_label_0_1.place(x = 190,y = 140)

        
        weight_label_0_3 = Label(KruskalPage.rootCanvas,text = "5",fg="blue",bg="yellow")
        weight_label_0_3.place(x = 300,y = 140)

        weight_label_0_2 = Label(KruskalPage.rootCanvas,text = "6",fg="blue",bg="yellow")
        weight_label_0_2.place(x = 240,y = 165)

        weight_label_1_3 = Label(KruskalPage.rootCanvas,text = "15",fg="blue",bg="yellow")
        weight_label_1_3.place(x = 220,y = 350)


        weight_label_2_3 = Label(KruskalPage.rootCanvas,text = "4",fg="blue",bg="yellow")
        weight_label_2_3.place(x = 285,y = 180)


        weight_label_3_4 = Label(KruskalPage.rootCanvas,text = "7",fg="blue",bg="yellow")
        weight_label_3_4.place(x = 260,y = 230)

        KruskalPage.relatedNodeElementsMapping["0"]["Oval"] = KruskalPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        KruskalPage.rootCanvas.move(KruskalPage.relatedNodeElementsMapping["0"]["Oval"], 220,100)
        KruskalPage.relatedNodeElementsMapping["0"]["Label"] = KruskalPage.rootCanvas.create_text(220+35,100+35,text="0") # Add 35 to fix the position
        KruskalPage.relatedNodeElementsMapping["0"]["Next"]["1"]["Line"] = KruskalPage.rootCanvas.create_line(220+25, 100+45, 150+35, 170+20)
        KruskalPage.relatedNodeElementsMapping["0"]["Next"]["2"]["Line"] = KruskalPage.rootCanvas.create_line(220+35, 100+50, 230+35, 170+20)
        KruskalPage.relatedNodeElementsMapping["0"]["Next"]["3"]["Line"] = KruskalPage.rootCanvas.create_line(225+35, 100+50, 300+35, 170+20)

        KruskalPage.relatedNodeElementsMapping["1"]["Oval"] = KruskalPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        KruskalPage.rootCanvas.move(KruskalPage.relatedNodeElementsMapping["1"]["Oval"], 150,170)
        KruskalPage.relatedNodeElementsMapping["1"]["Label"] = KruskalPage.rootCanvas.create_text(150+35,170+35,text="1") # Add 35 to fix the position
        KruskalPage.relatedNodeElementsMapping["1"]["Next"]["3"]["Line"] = KruskalPage.rootCanvas.create_line(160+25, 175+45, 200+35, 200+20,200,400,350,200,smooth=1)

        
        KruskalPage.relatedNodeElementsMapping["2"]["Oval"] = KruskalPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        KruskalPage.rootCanvas.move(KruskalPage.relatedNodeElementsMapping["2"]["Oval"], 230,170)
        KruskalPage.relatedNodeElementsMapping["2"]["Label"] = KruskalPage.rootCanvas.create_text(230+35,170+35,text="2") # Add 35 to fix the position
        KruskalPage.relatedNodeElementsMapping["2"]["Next"]["3"]["Line"] = KruskalPage.rootCanvas.create_line(245+35, 155+50, 290+35, 185+20)


        KruskalPage.relatedNodeElementsMapping["3"]["Oval"] = KruskalPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        KruskalPage.rootCanvas.move(KruskalPage.relatedNodeElementsMapping["3"]["Oval"], 300,170)
        KruskalPage.relatedNodeElementsMapping["3"]["Label"] = KruskalPage.rootCanvas.create_text(300+35,170+35,text="3") # Add 35 to fix the position
        KruskalPage.relatedNodeElementsMapping["3"]["Next"]["4"]["Line"] = KruskalPage.rootCanvas.create_line(300+25, 170+45, 230+35, 240+20)

        KruskalPage.relatedNodeElementsMapping["4"]["Oval"] = KruskalPage.rootCanvas.create_oval(20, 20, 50, 50, outline="black",
            fill="white", width=2)
        KruskalPage.rootCanvas.move(KruskalPage.relatedNodeElementsMapping["4"]["Oval"], 230,240)
        KruskalPage.relatedNodeElementsMapping["4"]["Label"] = KruskalPage.rootCanvas.create_text(230+35,240+35,text="4") # Add 35 to fix the position          
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

        for F in (MenuPage,BfsPage,DfsPage,DijkstraPage,KruskalPage):

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
    code_window = tk.Tk()
    if algs_name == "DFS":
        code_window.title("Depth first search in python")
        #code_window.geometry('533x411')
        code_window.configure(background='snow')

        load = Image.open("dfs_code.PNG")
        code_window.geometry(f'{load.size[0]}x{load.size[1]}')
        render = ImageTk.PhotoImage(load,master=code_window)
        img = Label(code_window, image=render)
        img.image = render
        img.place(x=0, y=0)
    elif algs_name == "BFS":
        code_window.title("Bredth first search in python")
        #code_window.geometry('533x411')
        code_window.configure(background='snow')

        load = Image.open("bfs_code.PNG")
        code_window.geometry(f'{load.size[0]}x{load.size[1]}')
        render = ImageTk.PhotoImage(load,master=code_window)
        img = Label(code_window, image=render)
        img.image = render
        img.place(x=0, y=0)
    elif algs_name == "KRUSKAL":
        code_window.title("Kruskal MST in python")
        #code_window.geometry('533x411')
        code_window.configure(background='snow')

        load = Image.open("kruskal_code.PNG")
        code_window.geometry(f'{load.size[0]}x{load.size[1]}')
        render = ImageTk.PhotoImage(load,master=code_window)
        img = Label(code_window, image=render)
        img.image = render
        img.place(x=0, y=0)
    elif algs_name == "DIJKSTRA":
        code_window.title("Dijkstra's algorithm in python")
        #code_window.geometry('533x411')
        code_window.configure(background='snow')

        load = Image.open("dijkstra_code.PNG")
        code_window.geometry(f'{load.size[0]}x{load.size[1]}')
        render = ImageTk.PhotoImage(load,master=code_window)
        img = Label(code_window, image=render)
        img.image = render
        img.place(x=0, y=0)        
    code_window.mainloop()
# ────────────────────────────────────────────────────────────────────────────────


global app
app = FrameController()
app.title("Search Algorithm Demonstration GUI-APPLICATION")
app.mainloop()

if Stimulator.tick_timer is not None : Stimulator.tick_timer.cancel()#defer