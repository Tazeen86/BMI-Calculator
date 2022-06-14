from tkinter import *

window =  Tk()
window.title("Body Mass Index (BMI) Calculator")
window.config(height=300,width=500, padx=20,pady=20)

weight_label=Label(text="Weight/kg", padx=20,pady=20)
weight_label.grid(column=1 , row = 1)

weight_entry= Entry()
weight_entry.grid(column= 2 , row= 1)
height_label = Label(text="Height/m", padx=20,pady=20)
height_label.grid(column=1 , row = 2)

height_entry= Entry()
height_entry.grid(column= 2 , row= 2)

bmi_label = Label(text="BMI", padx=20,pady=20)
bmi_label.grid(column = 1  , row = 3)

bmi_result_label = Label(text="0", padx=20,pady=20)
bmi_result_label.grid(column=2,row=3)
def calculate_bmi():
    weight= weight_entry.get()
    height= height_entry.get()
    bmi= float(weight)/float(height)**2
    bmi_result_label["text"] = round(bmi,2)
calculate_button = Button(text="Calculate" ,command = calculate_bmi)
calculate_button.grid(column=2 , row=4)

window.mainloop()

