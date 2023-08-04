import tkinter as tk
from tkinter import ttk
import calendar

def update_calendar():

    try:
        year = int(year_var.get())
        month = int(month_var.get())
        if not (1 <= year <= 9999) or not (1 <= month <= 12):
            raise ValueError("Invalid year or month value.")

        cal_content = calendar.month(year, month)
        cal_label.config(text=cal_content)
    except ValueError as e:
        cal_label.config(text="Please Enter an integer. Error: " + str(e))


window = tk.Tk()
window.title("Digital Calendar")
window.geometry("400x400")

year_var = tk.StringVar()
month_var = tk.StringVar()

year_label = ttk.Label(window, text="Year:")
year_label.pack(pady=10)
year_entry = ttk.Entry(window, textvariable=year_var)
year_entry.pack()

month_label = ttk.Label(window, text="Month:")
month_label.pack(pady=10)
month_entry = ttk.Entry(window, textvariable=month_var)
month_entry.pack()

update_btn = ttk.Button(window, text="Show Calendar", command=update_calendar)
update_btn.pack(pady=10)

cal_label = ttk.Label(window, text="")
cal_label.pack(pady=20)

window.mainloop()
