import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        
        self.work_time = 25*60
        self.break_time = 5*60
        self.current_time = self.work_time
        self.is_work_time = True
        
        self.create_widgets()

    def create_widgets(self):
        self.timer_label = tk.Label(self.master, text=self.format_time(self.current_time), font=("Arial", 24))
        self.timer_label.pack(pady=20)

        self.work_time_label = tk.Label(self.master, text="Work time (mins):", font=("Arial", 14))
        self.work_time_label.pack()
        self.work_time_spinbox = tk.Spinbox(self.master, from_=1, to=180, width=5, font=("Arial", 14))
        self.work_time_spinbox.pack()
        self.work_time_spinbox.delete(0, "end")
        self.work_time_spinbox.insert(0, self.work_time // 60)

        self.break_time_label = tk.Label(self.master, text="Break time (mins):", font=("Arial", 14))
        self.break_time_label.pack()
        self.break_time_spinbox = tk.Spinbox(self.master, from_=1, to=180, width=5, font=("Arial", 14))
        self.break_time_spinbox.pack()
        self.break_time_spinbox.delete(0, "end")
        self.break_time_spinbox.insert(0, self.break_time // 60)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer, font=("Arial", 14))
        self.start_button.pack(pady=10)

    def format_time(self, seconds):
        return f'{seconds // 60:02d}:{seconds % 60:02d}'

    def start_timer(self):
        self.work_time = int(self.work_time_spinbox.get()) * 60
        self.break_time = int(self.break_time_spinbox.get()) * 60
        self.current_time = self.work_time
        self.is_work_time = True
        self.master.after(1000, self.update_timer)

    def update_timer(self):
        if self.current_time > 0:
            self.current_time -= 1
            self.timer_label.config(text=self.format_time(self.current_time))
            self.master.after(1000, self.update_timer)
        else:
            if self.is_work_time:
                messagebox.showinfo("Pomodoro Timer", "Time for a break!")
                self.current_time = self.break_time
            else:
                messagebox.showinfo("Pomodoro Timer", "Time to get back to work!")
                self.current_time = self.work_time
            
            self.is_work_time = not self.is_work_time
            self.update_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
