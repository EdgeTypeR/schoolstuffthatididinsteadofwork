import tkinter as tk
from tkinter import messagebox

# Az ASCII pálcika ember
stick_figure = """
 sanyika
  
 ▄████▄▄░
▄▀█▀▐└─┐░░
█▄▐▌▄█▄┘██
└▄▄▄▄▄┘███
██▒█▒███▀

"""

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def meters_to_cm_mm(meters):
    cm = meters * 100
    mm = meters * 1000
    return cm, mm

def time_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_time(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hours, minutes, seconds

def show_error():
    messagebox.showerror("Hiba", "Te balfasz, azzal nem lehet számolni!")

def convert_temperature():
    try:
        celsius = float(entry_celsius.get())
        kelvin = celsius_to_kelvin(celsius)
        messagebox.showinfo("Eredmény", f"{celsius} °C = {kelvin:.2f} K")
    except ValueError:
        show_error()

def convert_length():
    try:
        meters = float(entry_meters.get())
        cm, mm = meters_to_cm_mm(meters)
        messagebox.showinfo("Eredmény", f"{meters} m = {cm:.2f} cm\n{meters} m = {mm:.2f} mm")
    except ValueError:
        show_error()

def convert_time_to_seconds():
    try:
        hours = int(entry_hours.get())
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
        total_seconds = time_to_seconds(hours, minutes, seconds)
        messagebox.showinfo("Eredmény", f"{hours} óra, {minutes} perc, {seconds} mp = {total_seconds} mp")
    except ValueError:
        show_error()

def convert_seconds_to_time():
    try:
        seconds = int(entry_total_seconds.get())
        hours, minutes, seconds = seconds_to_time(seconds)
        messagebox.showinfo("Eredmény", f"{seconds} mp = {hours} óra, {minutes} perc, {seconds} mp")
    except ValueError:
        show_error()

# A fő ablak
root = tk.Tk()
root.title("Ezörmester")
root.geometry("300x400")

# Szövegek és ASCII pálcika ember
label_stick_figure = tk.Label(root, text=stick_figure, font=("Century Gothic", 14), justify="center")
label_stick_figure.pack()

label_prompt = tk.Label(root, text="Milyen átváltást szeretnél végezni?", font=("Century Gothic", 12))
label_prompt.pack(pady=10)

# Celsius-Kelvin átváltás
frame_celsius = tk.Frame(root)
frame_celsius.pack(pady=5)

entry_celsius = tk.Entry(frame_celsius, width=5)
entry_celsius.pack(side=tk.LEFT)
btn_celsius = tk.Button(frame_celsius, text="Celsius -> Kelvin", font=("Century Gothic", 10), command=convert_temperature)
btn_celsius.pack(side=tk.LEFT)

# Mértékegység átváltás
frame_meters = tk.Frame(root)
frame_meters.pack(pady=5)

entry_meters = tk.Entry(frame_meters, width=5)
entry_meters.pack(side=tk.LEFT)
btn_meters = tk.Button(frame_meters, text="Méter -> cm/mm",font=("Century Gothic", 10), command=convert_length)
btn_meters.pack(side=tk.LEFT)

# Időmpont mp-be átváltás
frame_time_to_seconds = tk.Frame(root)
frame_time_to_seconds.pack(pady=5)

entry_hours = tk.Entry(frame_time_to_seconds, width=3)
entry_hours.pack(side=tk.LEFT)
entry_minutes = tk.Entry(frame_time_to_seconds, width=3)
entry_minutes.pack(side=tk.LEFT)
entry_seconds = tk.Entry(frame_time_to_seconds, width=3)
entry_seconds.pack(side=tk.LEFT)

btn_time_to_seconds = tk.Button(frame_time_to_seconds, text="Óra:Perc:mp -> mp",font=("Century Gothic", 10), command=convert_time_to_seconds)
btn_time_to_seconds.pack(side=tk.LEFT)

# mp-ból időpont átváltás
frame_seconds_to_time = tk.Frame(root)
frame_seconds_to_time.pack(pady=5)

entry_total_seconds = tk.Entry(frame_seconds_to_time, width=5)
entry_total_seconds.pack(side=tk.LEFT)
btn_seconds_to_time = tk.Button(frame_seconds_to_time, text="mp -> Óra:Perc:mp",font=("Century Gothic", 10), command=convert_seconds_to_time)
btn_seconds_to_time.pack(side=tk.LEFT)

# A program futtatása
root.mainloop()
