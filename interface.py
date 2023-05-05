import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        self.master.geometry("1920x1080")

        self.left_pane = tk.Frame(self.master, width=960, height=1080, bg="white")
        self.left_pane.pack(side=tk.LEFT, fill=tk.BOTH)

        self.right_pane = tk.Frame(self.master, width=960, height=1080, bg="white")
        self.right_pane.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.add_timer_elements()

        # Temporary message for testing
        self.message_label = tk.Label(self.right_pane, text="This is a test message!", font=("Helvetica", 16))
        self.message_label.pack()

    def create_widgets(self):
        # Create paned window
        self.paned_window = ttk.PanedWindow(self.master, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

        # Left pane
        self.left_pane = ttk.Frame(self.paned_window)
        self.paned_window.add(self.left_pane, weight=1)

        # Right pane
        self.right_pane = ttk.Frame(self.paned_window)
        self.paned_window.add(self.right_pane, weight=1)

        # Add timer elements to the left pane
        self.add_timer_elements()

        # Add message elements to the right pane
        self.add_message_elements()

    def add_timer_elements(self):
        # Focus Time label
        self.focus_time_label = tk.Label(self.left_pane, text="Focus Time", font=("Helvetica", 16))
        self.focus_time_label.pack(pady=(20, 0))

        # Focus Time display
        self.focus_time = 24 * 60
        self.focus_time_text = tk.StringVar()
        self.focus_time_text.set(self.format_time(self.focus_time))
        self.focus_time_display = tk.Label(self.left_pane, textvariable=self.focus_time_text, font=("Helvetica", 24))
        self.focus_time_display.pack(pady=(0, 20))

        # Focus Time adjustment buttons
        self.focus_time_increase_button = tk.Button(self.left_pane, text="+", command=self.increase_focus_time)
        self.focus_time_increase_button.pack(side=tk.LEFT, padx=(20, 10))

        self.focus_time_decrease_button = tk.Button(self.left_pane, text="-", command=self.decrease_focus_time)
        self.focus_time_decrease_button.pack(side=tk.LEFT)

        # Break Time label
        self.break_time_label = tk.Label(self.left_pane, text="Break Time", font=("Helvetica", 16))
        self.break_time_label.pack(pady=(40, 0))

        # Break Time display
        self.break_time = 12 * 60
        self.break_time_text = tk.StringVar()
        self.break_time_text.set(self.format_time(self.break_time))
        self.break_time_display = tk.Label(self.left_pane, textvariable=self.break_time_text, font=("Helvetica", 24))
        self.break_time_display.pack(pady=(0, 20))

        # Break Time adjustment buttons
        self.break_time_increase_button = tk.Button(self.left_pane, text="+", command=self.increase_break_time)
        self.break_time_increase_button.pack(side=tk.LEFT, padx=(20, 10))

        self.break_time_decrease_button = tk.Button(self.left_pane, text="-", command=self.decrease_break_time)
        self.break_time_decrease_button.pack(side=tk.LEFT)

        # Start Pomodoro button
        self.start_pomodoro_button = tk.Button(self.left_pane, text="Start Pomodoro", command=self.start_pomodoro)
        self.start_pomodoro_button.pack(pady=(40, 0))

    def increase_focus_time(self):
        self.focus_time += 60
        self.focus_time_text.set(self.format_time(self.focus_time))

    def decrease_focus_time(self):
        self.focus_time = max(60, self.focus_time - 60)
        self.focus_time_text.set(self.format_time(self.focus_time))

    def increase_break_time(self):
        self.break_time += 60
        self.break_time_text.set(self.format_time(self.break_time))

    def decrease_break_time(self):
        self.break_time = max(60, self.break_time - 60)
        self.break_time_text.set(self.format_time(self.break_time))

    def start_pomodoro(self):
        # Logic for starting the Pomodoro timers
        pass

    def format_time(self, seconds):
        minutes = int(seconds / 60)
        seconds = int(seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def add_message_elements(self):
        self.message_label = tk.Label(self.right_pane, textvariable=self.message_text, font=("Helvetica", 16))
        self.message_label.pack(padx=20, pady=20)