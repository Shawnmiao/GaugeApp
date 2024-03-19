import tkinter as tk


class GaugeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Gauge Display')
        self.geometry('300x200')

        self.value_var = tk.DoubleVar(value=50.0)  # Set initial value for gauge

        self.create_widgets()

    def create_widgets(self):
        # Add label for the title
        tk.Label(self, text='Sensor Value Display').pack()

        # Create the canvas and a bar to act as the gauge
        self.canvas = tk.Canvas(self, width=200, height=50)
        self.canvas.pack()
        self.gauge = self.canvas.create_rectangle(10, 10, 10 + self.value_var.get(), 40, fill='blue')

        # Add an entry to input the value
        self.entry = tk.Entry(self, textvariable=self.value_var)
        self.entry.pack()

        # Add a button to update the gauge
        tk.Button(self, text='Update Gauge', command=self.update_gauge).pack()

        # Display additional information
        tk.Label(self, text='Unit: °C').pack()
        tk.Label(self, text='Normal range: 18°C - 22°C').pack()

    def update_gauge(self):
        # Get the value from the entry and update the gauge
        try:
            new_value = float(self.entry.get())
            self.canvas.coords(self.gauge, 10, 10, 10 + new_value * 2, 40)  # Update the length of the gauge
        except ValueError:
            tk.messagebox.showerror('Invalid Input', 'Please enter a valid number.')


if __name__ == "__main__":
    app = GaugeApp()
    app.mainloop()

