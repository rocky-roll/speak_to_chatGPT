import os
import threading
import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import messagebox

from chatGPT_ import *
from encrypt import key_cript
from recognize_google_ import *


def start():
    global t0
    t0 = threading.Thread(target=main, daemon=True)
    t0.start()
    ChatGPT.login_openai()


def close():
    os._exit(0)


def position(window, width_window, tall_window):
    x_window = window.winfo_screenwidth() // 2 - width_window // 2
    y_window = window.winfo_screenheight() // 2 - tall_window // 2
    position_ = str(width_window) + "x" + str(tall_window) + \
        "+" + str(x_window) + "+" + str(y_window)
    return position_


root = tk.Tk()
root.option_add('*Dialog.msg.font', 'Roboto 10')
root.title("Haba con chatGPT")
p1 = tk.PhotoImage(file='logo32.png')
root.iconphoto(True, p1)
root.resizable(0, 0)
root.geometry(position(root, 250, 270))


class Application():

    def __init__(self, root):
        f1 = tk.Frame(root)
        f1.pack()
        menu = tk.Menu()
        menu_file = tk.Menu(menu, tearoff=0)
        menu_help = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Archivo", menu=menu_file)
        menu.add_cascade(label="Ayuda", menu=menu_help, command='')
        menu_file.add_command(label="ChatGPT API key", command=self.window_API)
        menu_help.add_command(label="Acerca de..", command=self.about)
        root.config(menu=menu)
        self.image = tk.PhotoImage(file="chatGPT_b.png")
        self.image2 = tk.PhotoImage(file="chatGPT_c.png")
        self.label1 = tk.Label(root, image=self.image)
        self.label1.pack(pady=2, padx=1, ipadx=4, ipady=4)
        btn_boton = tk.Button(root, text="Salir", command=close,
                              activebackground="red", activeforeground="#D3D7CF")
        btn_boton.pack(pady=7, padx=4, ipadx=4, ipady=4)
        root.after(100, self.actualizar_etiqueta, q)

    def actualizar_etiqueta(self, q):
        try:
            cont = q.get_nowait()
            if cont == True:
                self.label1.configure(image=self.image2)
            if cont == False:
                self.label1.configure(image=self.image)
        except queue.Empty:
            pass
        root.after(10, self.actualizar_etiqueta, q)

    def callback(self, url):
        webbrowser.open_new_tab(url)

    def about(self):
        toplevel = tk.Toplevel(root)
        f2 = tk.Frame(toplevel)
        f2.grid()
        toplevel.title("Acerca de..")
        toplevel.geometry(position(toplevel, 420, 135))
        toplevel.grid()
        toplevel.focus()
        toplevel.grab_set()
        l1 = tk.Label(toplevel, image="::tk::icons::information")
        l1.grid(row=0, column=0)
        l2 = tk.Label(toplevel, justify="left",
                      text="Utilice este programa bajo su propia responsabilidad. \nNo se ofrece ningún tipo de garantía. \nVersión beta 0.01v. \nLicencia GPL3.\nAño 2023")
        l2.grid(row=0, column=1, padx=11, ipady=10)
        lbl = tk.Label(toplevel, justify="left",
                       text=r"github.com", fg="blue", cursor="hand2")
        lbl.grid(row=1, column=1, sticky='W')
        lbl.bind("<Button-1>", lambda e: self.callback("https://github.com/rocky-roll/speak_to_the_chatGPT"))
        lbl2 = tk.Label(toplevel, justify="left",
                        text=r"sourceforge.net", fg="blue", cursor="hand2")
        lbl2.grid(row=1, column=1, sticky='E')
        lbl2.bind("<Button-1>", lambda e: self.callback(
            "https://sourceforge.net/projects/habla-con-chatgpt/"))

    def window_API(self):
        self.new_window = tk.Toplevel()
        self.new_window.title("API key de chatGPT")
        self.new_window.geometry(position(self.new_window, 300, 135))
        texto = tk.Label(
            self.new_window, text="Ingrese la API key de openai", font=('Roboto', 12))
        texto.pack(pady=4, padx=1)
        self.lbl = tk.Label(
            self.new_window, text=r"https://platform.openai.com", fg="blue", cursor="hand2")
        self.lbl.pack()
        self.lbl.bind(
            "<Button-1>", lambda e: self.callback("https://platform.openai.com/account/api-keys"))
        self.e1 = tk.Entry(self.new_window, state="normal",
                           show=None, font=('Roboto', 12))
        self.e1.pack(pady=4, padx=1)
        self.btn_22 = tk.Button(
            self.new_window, state="normal", text="Enviar", command=self.write_API)
        self.btn_22.pack(pady=4, padx=4, ipadx=4, ipady=4)
        self.new_window.focus()
        self.new_window.grab_set()

    def write_API(self):
        key_ = key_cript(self.e1.get())
        self.e1["state"] = "disabled"
        self.btn_22["state"] = "disabled"
        self.new_window.destroy()
        response = messagebox.askquestion(
            "Configuración", "¿Cerrar el programa y aplicar los cambios?")
        if response == 'yes':
            f = open("api_key.txt", "w", encoding='utf-8')
            f.write(f"{key_.decode('utf-8')}")
            f.close
            root.destroy()


start()
obj1 = Application(root)
root.mainloop()
