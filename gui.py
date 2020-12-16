import tkinter as tk
from tkinter import *
import config as config

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
    root.destroy()
# ────────────────────────────────────────────────────────────────────────────────


def createMainApplicationWindowAndContinueEventLooping():
    global root
    root = tk.Tk()
    root.title("Search algorithm demonstration gui")
    root.minsize(config.configs["application"]["width"],config.configs["application"]["height"])
    root.geometry(f'{config.configs["application"]["width"]}x{config.configs["application"]["height"]}')
    root.configure(bg='snow')
    createLandedElement()
    root.mainloop()

def createLandedElement():
    #greeting = tk.Label(text="Development mode: True")
    #greeting.pack()

    message = tk.Label(root, text="Search algorithms gui demonstration", bg="blue2", fg="snow",font=('times', 20, ' bold '))
    message.place(x=getCenteredAxis()["x"], y=30,anchor="center")

    dijkstra_btn = tk.Button(root, text="Dijkstra search algorithm",bg="orange",fg="white",activebackground="gray",font=('times', 15, ' bold '))
    dijkstra_btn.place(x=getCenteredAxis()["x"],y=150,anchor="center",width=300)

    bfs_btn = tk.Button(root, text="Breadth first search algorithm",bg="orange",fg="white",activebackground="gray",font=('times', 15, ' bold '))
    bfs_btn.place(x=getCenteredAxis()["x"],y=200,anchor="center",width=300)

    dfs_btn = tk.Button(root, text="Depth first search algorithm",bg="orange",fg="white",activebackground="gray",font=('times', 15, ' bold '))
    dfs_btn.place(x=getCenteredAxis()["x"],y=250,anchor="center",width=300)

    exit_btn = tk.Button(root,command=exitProgram, text="Exit",bg="red",fg="white",activebackground="gray",font=('times', 15, ' bold '))
    exit_btn.place(x=600,y=450,anchor="center")

createMainApplicationWindowAndContinueEventLooping()