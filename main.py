from tkinter import *


window = Tk()

window.title("Age Calculator")
window.geometry("300x200")

# Create labels and entry fields for day, month, and year
day_label = Label(window, text="Day:")
day_label.grid(row=0, column=0, padx=5, pady=5)
day_entry = Entry(window)
day_entry.grid(row=0, column=1, padx=5, pady=5)

month_label = Label(window, text="Month:")
month_label.grid(row=1, column=0, padx=5, pady=5)
month_entry = Entry(window)
month_entry.grid(row=1, column=1, padx=5, pady=5)

year_label = Label(window, text="Year:")
year_label.grid(row=2, column=0, padx=5, pady=5)
year_entry = Entry(window)
year_entry.grid(row=2, column=1, padx=5, pady=5)


# Create a button to calculate the age
calculate_button = Button(window, text="Calculate Age",)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to show result
result_label = Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

window.mainloop()


