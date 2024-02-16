import tkinter as tk


def calculate():
    weight_str = weight_entry.get()
    height_str = height_entry.get()

    if not weight_str:
        status_label.config(text="Error! Please enter your weight!")
        return
    if not height_str:
        status_label.config(text="Error! Please enter your height!")
        return

    try:
        weight = float(weight_str)
        height = float(height_str)
    except ValueError:
        status_label.config(text="Error! Please enter valid numbers for weight and height!")
        return

    bmi = weight / ((height / 100)**2)
    if bmi < 18.5:
        bmi_label.config(text=f"Your BMI is: {bmi:.2f}", bg="gray")
        status_label.config(text="Underweight", bg="gray")
    elif 18.5 < bmi < 26:
        bmi_label.config(text=f"Your BMI is: {bmi:.2f}", bg="green")
        status_label.config(text="Normal Weight", bg="green")
    elif 25 < bmi < 31:
        bmi_label.config(text=f"Your BMI is: {bmi:.2f}", bg="yellow")
        status_label.config(text="Overweight", bg="yellow")
    else:
        bmi_label.config(text=f"Your BMI is: {bmi:.2f}", bg="red")
        status_label.config(text="Obese" , bg="red")


window = tk.Tk()
window.title("BMI Calculator")

weight_label = tk.Label(window, text="Please enter your weight in kilograms:", padx=10, pady=10)
height_label = tk.Label(window, text="Please enter your height in centimeters:", padx=10, pady=10)
weight_entry = tk.Entry(window)
height_entry = tk.Entry(window)
bmi_label = tk.Label(window, padx=10, pady=10)
status_label = tk.Label(window, padx=10, pady=1)

button = tk.Button(
    window,
    text="Calculate",
    bg="gray",
    fg="black",
    activebackground="white",
    activeforeground="black",
    font=("Arial", 12),
    height=2,
    width=10,
    cursor="hand2",
    command=calculate
)

weight_label.pack()
weight_entry.pack()
height_label.pack()
height_entry.pack()
button.pack()
bmi_label.pack()
status_label.pack()

window.mainloop()
