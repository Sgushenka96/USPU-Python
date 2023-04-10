import subprocess
import tkinter as tk
from PIL import Image, ImageTk
from sql_connect import *

# Параметры стартового окна
window = tk.Tk()
window.title("Start Flappy Bird")
window.geometry('400x600')
window.resizable(False,False)

# Уствновка фона
img = Image.open("fon.png")
image = ImageTk.PhotoImage(img)
panel = tk.Label(window, image = image)
panel.grid(column=0,row=0)
panel.pack(side="top", fill="both", expand="no")

#window.mainloop()

# Функции
def start_game():
    if txt.get=="":
        lbl.configure(text="БЕЗ ИМЕНИ НЕ ПУЩУ")
    else:
        res="{}".format(txt.get())
        mysql_in("INSERT INTO 'game'.'user' ('user') VALUES ('"+res+"') \
        ON DUPLICATE KEY UPDATE 'user'='"+res+"', 'record'=0;")
        subprocess.Popen('python game.py '+"{}".format(txt.get()))

def records_output():
    text = ""
    database = mysql_out("SELECT * FROM 'game'.'user' \
    ORDER by 'record' DESC LIMIT 10;")

    try:
        if len(database)>1:
            for elements in database:
                text = text+"\n"+str(elements[0])+" -> "+str(elements[1])
        else:
            text = text + "\n" + str(database[0])
    except Exception:
        text="Пока никто не играл ("
        rectxt.configure(text="Top-10:\n"+text)

# Установка кнопок
btnstrt = tk.Button(text="Начать", command=start_game)
btnstrt.place(x=175,y=125)

btnrcrd = tk.Button(text="Обновить рекорды", command=records_output)
btnrcrd.place(x=200, y=300)

# Установка полей ввода и вывода
lbl=tk.Label(window, text="Введите никнейм",
             bg="#00bfff",
             justify=tk.LEFT)
lbl.place(x=175, y=75)
txt=tk.Entry(window, width=25)
txt.place(x=175, y=100)
txt.focus()
rectxt=tk.Label(window)