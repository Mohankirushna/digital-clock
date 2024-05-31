"""import tkinter as tk
from datetime import datetime

def update_time():
    # Get the current date and time
    current_time = datetime.now()

    # Format the time as a string
    formatted_time = current_time.strftime("%H:%M:%S")

    # Update the label text
    time_label.config(text="Current Time: " + formatted_time)

    # Schedule the update function to run again after 1000 milliseconds (1 second)
    root.after(1000, update_time)

# Create the main Tkinter window
root = tk.Tk()
root.title("Current Time Display")

# Create a label to display the time
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
time_label.pack(anchor='center')

# Call the update_time function to display the initial time and start updating
update_time()

# Run the Tkinter event loop
root.mainloop()"""
"""import tkinter as tk
from datetime import datetime

def update_time():
    # Get the current date and time
    current_time = datetime.now()

    # Format the time as a string
    formatted_time = current_time.strftime("%H:%M:%S %p")  # Added %p for AM/PM

    # Update the label text
    time_label.config(text=formatted_time)

    # Schedule the update function to run again after 1000 milliseconds (1 second)
    root.after(1000, update_time)

# Create the main Tkinter window
root = tk.Tk()
root.title("Digital Clock")

# Customize the window size and appearance
root.geometry("300x120")
root.configure(bg='black')

# Create a label to display the time
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
time_label.pack(pady=20)

# Call the update_time function to display the initial time and start updating
update_time()

# Run the Tkinter event loop
root.mainloop()
"""
"""import tkinter as tk
from datetime import datetime

def update_time():
    # Get the current date and time
    current_time = datetime.now()

    # Format the time in 12-hour and 24-hour formats
    formatted_time_12h = current_time.strftime("%I:%M:%S %p")  # 12-hour format
    formatted_time_24h = current_time.strftime("%H:%M:%S")  # 24-hour format

    # Update the label texts
    time_label_12h.config(text="12-Hour Format: " + formatted_time_12h)
    time_label_24h.config(text="24-Hour Format: " + formatted_time_24h)

    # Schedule the update function to run again after 1000 milliseconds (1 second)
    root.after(1000, update_time)

# Create the main Tkinter window
root = tk.Tk()
root.title("Digital Clock")

# Customize the window size and appearance
root.geometry("400x120")
root.configure(bg='black')

# Create labels to display the time in 12-hour and 24-hour formats
time_label_12h = tk.Label(root, font=('calibri', 20, 'bold'), background='black', foreground='white')
time_label_12h.pack(pady=10)

time_label_24h = tk.Label(root, font=('calibri', 20, 'bold'), background='black', foreground='white')
time_label_24h.pack(pady=10)

# Call the update_time function to display the initial time and start updating
update_time()

# Run the Tkinter event loop
root.mainloop()


"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime

def update_time():
    
    current_time = datetime.now()

    
    formatted_time_12h = current_time.strftime("%I:%M:%S %p")  
    formatted_time_24h = current_time.strftime("%H:%M:%S")

    
    time_label_12h.config(text="12-Hour Format: " + formatted_time_12h)
    time_label_24h.config(text="24-Hour Format: " + formatted_time_24h)

    
    root.after(1000, update_time)


root = tk.Tk()
root.title("Digital Clock")


root.geometry("500x180")
root.configure(bg='#282828')  


style = ttk.Style()
style.configure("TLabel", background='#282828', foreground='white', font=('calibri', 20, 'bold'))

time_label_12h = ttk.Label(root, text="12-Hour Format: ", style="TLabel")
time_label_12h.pack(pady=10)

time_label_24h = ttk.Label(root, text="24-Hour Format: ", style="TLabel")
time_label_24h.pack(pady=10)

update_time()

root.mainloop()
