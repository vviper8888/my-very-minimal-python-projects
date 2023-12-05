import tkinter as tk
import requests
from bs4 import BeautifulSoup
window_box = tk.Tk()
window_box.title("Finder by vviper8888")
window_box.geometry("200x200")
select_label1 = tk.Label(text="ZIP code or phone area code?")
select_label1.pack()
area_button = tk.Button(text="Area code")
zip_button = tk.Button(text="ZIP code")
zip_button.pack()
area_button.pack()
window_box.mainloop()