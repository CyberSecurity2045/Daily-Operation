import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    time_label.configure(text=current_time, fg='blue')
    root.after(1000, update_time)

root = tk.Tk()
root.title('Current Time')
root.attributes('-topmost', True)

time_label = tk.Label(root, font=('Arial', 30))
time_label.pack(padx=20, pady=20)

update_time()

root.mainloop()
