import customkinter 
from tkinter import *
from tkinter import messagebox
import sqlite3

app = customkinter.CTk()
app.title("Products")
app.geometry("400 x 200")
app.config(bg="#24344f")

font1 = ('Arial',15,'bold')

db = sqlite3.connect("items.db")
db.execute("CREATE TABLE IF NOT EXISTS PRODUCTS (Product_ID integer,operating_System TEXT)")
Cursor = db.cursor()

app.mainloop()

def insert():
  row =[int(product_entry.get()),os_entry.get()]
  cursor.execute("INSERT into PRODUCTS values (?,?)",row)
  db.commit()
  messagebox.showinfo(title = "saved",message = "Item is saved")


def delete():
  cursor.execute("DELETE from PRODUCTS WHERE Product_ID =?",[product_entry.get()])
  db.commit()
  messagebox.showinfo(title = "deleted",message = "Item is deleted")

product_label1 = customkinter.CTkLabel(app,text="Product ID:",text_font = font1,text_color="#ffffff")
product_label1.place(x=5,y=10)

product_entry = customtkinter.CTkEntry(app,border_width=1,text_font=font1,text_color="#000000",border_color="#003")
product_entry.place(x=190,y=10)

os_label = customtkinter.CTkEntry("operating System:",text_font=font1,text_color="#ffffff")
os_label.place(x=5,y=70)

os_entry = customtkinter.CTkEntry(app,border_width=1,text_font=font1,text_color="#ffffff",border_color="#003")
os_entry.place(x=190,y=70)

save_button=customkinter.CTkButton(app,command=insert,text="Save",text_font=font1,fg_color="#189614")
save_button.place(x=30,y=150)

delete_button=customkinter.CTkButton(app,command=delete,text="Delete",text_font=font1,fg_color="#c754")
delete_button.place(x=180,y=150)





