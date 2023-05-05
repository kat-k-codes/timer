import sys
import tkinter as tk
import ctypes
import win32gui
import win32con
import win32com.client
import winsound

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
        self.work_time_label = tk.Label(self.master, text="Work Time (minutes):")
        self.work_time_label.grid(row=0, column=0)

        self.work_time_value = tk.StringVar(self.master, value=int(self.work_time/60))
        self.work_time_entry = tk.Entry(self.master, textvariable=self.work_time_value)
        self.work_time_entry.grid(row=0, column=1)

        self.break_time_label = tk.Label(self.master, text="Break Time (minutes):")
        self.break_time_label.grid(row=1, column=0)

        self.break_time_value = tk.StringVar(self.master, value=int(self.break_time/60))
        self.break_time_entry = tk.Entry(self.master, textvariable=self.break_time_value)
        self.break_time_entry.grid(row=1, column=1)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.grid(row=2, column=1)

        self.time_remaining_label = tk.Label(self.master, text="Time Remaining:")
        self.time_remaining_label.grid(row=3, column=0)

        self.time_remaining_value = tk.StringVar(self.master, value=self.format_time(self.current_time))
        self.time_remaining_entry = tk.Entry(self.master, textvariable=self.time_remaining_value)
        self.time_remaining_entry.grid(row=3, column=1)

        self.message_label = tk.Label(self.master, text="", font=("Helvetica", 16))
        self.message_label.grid(row=4, column=0, columnspan=2)

    def play_sound(self):
        winsound.Beep(1000, 500)  # Frequency (Hz), Duration (ms)

    def force_foreground(self):
        if sys.platform.startswith('win'):
            hwnd = self.master.winfo_id()
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            ctypes.windll.user32.SetForegroundWindow(hwnd)
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')

    def switch_timer(self):
        self.play_sound()
        
        if self.is_work_time:
            self.message_label.config(text="Time for a break!")
            self.current_time = self.break_time
        else:
            self.message_label.config(text="Time to get back to work!")
            self.current_time = self.work_time

        self.force_foreground()

        self.is_work_time = not self.is_work_time
        self.update_timer()

    def start_timer(self):
        self.work_time = int(self.work_time_value.get()) * 60
        self.break_time = int(self.break_time_value.get()) * 60
        self.current_time = self.work_time
        self.update_timer()

    def update_timer(self):
        self.time_remaining_value.set(self.format_time(self.current_time))
        if self.current_time > 0:
            self.current_time -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.switch_timer()

    def format_time(self, seconds):
        minutes = int(seconds / 60)
        seconds = int(seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"
    
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()