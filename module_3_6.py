import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()
window.title('калькулятор')
window.geometry('350x350')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=2, height=2, command=add)
button_add.place(x=300, y=300)
button_sub = tk.Button(window, text='-', width=2, height=2, command=sub)
button_sub.place(x=300, y=255)
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul)
button_mul.place(x=300, y=210)
button_div = tk.Button(window, text='/', width=2, height=2, command=div)
button_div.place(x=300, y=165)
number1_entry = tk.Entry(window, width=25)
number1_entry.place(x=100, y=100)
number2_entry = tk.Entry(window, width=25)
number2_entry.place(x=100, y=130)
answer_entry = tk.Entry(window, width=25)
answer_entry.place(x=100, y=260)
number1 = tk.Label(window, text='1 число')
number1.place(x=100, y=75)
number2 = tk.Label(window, text='2 число')
number2.place(x=100, y=150)
answer = tk.Label(window, text='Ответ')
answer.place(x=100, y=235)
window.mainloop()