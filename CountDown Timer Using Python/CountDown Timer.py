import tkinter as tk
from threading import Thread
import time

class CountdownTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Countdown Timer")
        self.label = tk.Label(self.root, text="Enter time in seconds:", font=('Helvetica', 24))
        self.label.pack()
        self.entry = tk.Entry(self.root, width=10, font=('Helvetica', 24))
        self.entry.pack()
        self.time_label = tk.Label(self.root, text="", font=('Helvetica', 48))
        self.time_label.pack()
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer, font=('Helvetica', 24))
        self.start_button.pack()
        self.root.mainloop()

    def countdown(self, count):
        while count > 0:
            mins, secs = divmod(count, 60)
            self.time_label.config(text=f"{mins:02d}:{secs:02d}")
            self.root.update()
            time.sleep(1)
            count -= 1
        self.time_label.config(text="Time's up!")
        self.start_button.config(state="normal")

    def start_timer(self):
        self.start_button.config(state="disabled")
        try:
            count = int(self.entry.get())
            if count < 0:
                self.time_label.config(text="Invalid input!")
            else:
                thread = Thread(target=self.countdown, args=(count,))
                thread.start()
        except ValueError:
            self.time_label.config(text="Invalid input!")


if __name__ == "__main__":
    CountdownTimer()