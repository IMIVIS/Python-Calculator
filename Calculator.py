from customtkinter import *

#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#ABOVE CODE FOR EXE CONVERSION(IGNORE)

def calc():
    equation=entry.get()
    try:
        ans = eval(equation)
    except ZeroDivisionError:
        ans = "Division by Zero is not possible."
    label.configure(text=ans)
    

app = CTk()
app.geometry("500x400")
set_appearance_mode("system")

frame = CTkFrame(master=app, fg_color="#D9D9D9", border_width=0, corner_radius=20, width=500, height=400, border_color="#54C392")

entry = CTkEntry(master=frame, placeholder_text="Enter Yor Equation", fg_color="black", width=466, height=106, font=("Aptos", 32), text_color="white", placeholder_text_color="white", border_width=0, corner_radius=20)
label = CTkLabel(master=frame, text="Your Answer Here", text_color="black", font=("Aptos", 30), width=318, height=248, fg_color="white", corner_radius=20)
s_button = CTkButton(master=frame, text="=", corner_radius=16, fg_color="red", hover_color="#FF7700", text_color="black", width=136, height=248, font=("Aptos", 72),command=calc)

frame.place(relx=0.5, rely=0.5, anchor="center")
entry.place(x=17, y=14)
label.place(x=17, y=130)
s_button.place(x=347, y=130)

app.title("Calculator")
app.mainloop()