import time
import sys
import tkinter as tk
from threading import Thread
from Mastermind import *

# ---- Animation du texte ----
def delay_print(label, s: str):
    text = ""
    for c in s:
        text += c
        label.config(text=text)
        time.sleep(0.005)

# ---- Actions des boutons ----
def solo():
    print("Solo clicked")
    jeu(premier=True)

def online():
    print("Online clicked")

def plugins():
    print("Plugins clicked")

def settings():
    print("Settings clicked")

# ---- Page principale ----
def MainPage(root):
    title_label = tk.Label(
        root,
        text="",
        font=("Consolas", 12),
        justify="left"
    )
    title_label.pack(pady=20)

    Thread(
        target=delay_print,
        args=(title_label, "welcome to MasterMod the Mastermind NSI projet plugin loader."),
        daemon=True
    ).start()

    button_frame = tk.Frame(root)
    button_frame.pack(pady=30)

    # Ordre : Solo | Online
    tk.Button(button_frame, text="Solo", width=15, command=solo)\
        .grid(row=0, column=0, padx=10, pady=5)
    tk.Button(button_frame, text="Online", width=15, command=online)\
        .grid(row=0, column=1, padx=10, pady=5)

    # Ordre : Plugins | Settings
    tk.Button(button_frame, text="Plugins", width=15, command=plugins)\
        .grid(row=1, column=0, padx=10, pady=5)
    tk.Button(button_frame, text="Settings", width=15, command=settings)\
        .grid(row=1, column=1, padx=10, pady=5)

# ---- Programme principal ----
def main():
    root = tk.Tk()
    root.title("MasterMod")
    root.geometry("600x300")
    root.resizable(False, False)

    MainPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
