import tkinter as tk

def on_click(button_text):
    current_text = result_var.get()

    if button_text == "=":
        try:
            result = eval(current_text)
            result_var.set(result)
        except Exception as e:
            result_var.set("Erreur")

    elif button_text == "C":
        result_var.set("")

    else:
        result_var.set(current_text + button_text)

window = tk.Tk()
window.title("Calculatrice")

result_var = tk.StringVar()
result_var.set("")

display = tk.Entry(window, textvar=result_var, font="Helvetica 16", justify="right")
display.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1


window.mainloop()