import tkinter as tk

sym_list = ('+', '-', '*', '/')


def btn1_function(txt: tk.Entry):
    print(txt.get())
    txt.insert('end', '1')


def btn2_function(txt: tk.Entry):
    print(txt.get())
    txt.insert('end', '2')


def btn3_function(txt: tk.Entry):
    print(txt.get())
    txt.insert('end', '3')


def btn4_function(txt: tk.Entry):
    print(txt.get())
    txt.insert('end', '4')


def btn5_function(txt: tk.Entry):
    print(txt.get())
    txt.insert('end', '5')


def btn6_function(txt: tk.Entry):
    print(txt.get())
    txt.insert('end', '6')


def btn7_function(txt: tk.Entry):
    print(txt.get())
    txt.insert('end', '7')


def btn8_function(txt: tk.Entry):
    print(txt.get())
    txt.insert('end', '8')


def btn9_function(txt: tk.Entry):
    print(txt.get())
    txt.insert('end', '9')


def btn0_function(txt: tk.Entry):
    print(txt.get())
    txt.insert('end', '0')


def btn_plus_function(txt: tk.Entry):
    print(txt.get())
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print(f"replace '{str_str[len(str_str) - 1]}' -> '+'")
            txt.delete(len(str_str) - 1, 'end')
    except ValueError:
        print("add '+'")
    finally:
        txt.insert('end', '+')


def btn_minus_function(txt: tk.Entry):
    print(txt.get())
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print(f"replace '{str_str[len(str_str) - 1]}' -> '-'")
            txt.delete(len(str_str) - 1, 'end')
    except ValueError:
        print("add '-'")
    finally:
        txt.insert('end', '-')


def btn_multi_function(txt: tk.Entry):
    print(txt.get())
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print(f"replace '{str_str[len(str_str) - 1]}' -> '*'")
            txt.delete(len(str_str) - 1, 'end')
    except ValueError:
        print("add '*'")
    finally:
        txt.insert('end', '*')


def btn_split_function(txt: tk.Entry):
    print(txt.get())
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print(f"replace '{str_str[len(str_str) - 1]}' -> '/'")
            txt.delete(len(str_str) - 1, 'end')
    except ValueError:
        print("add '/'")
    finally:
        txt.insert('end', '/')


def btn_percent_function(txt: tk.Entry):
    print(txt.get())
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print("not number to percentage")
    except ValueError:
        txt.insert('end', '%')
        print("add '%'")


def btn_dot_function(txt: tk.Entry):
    print(txt.get())
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print("not number to percentage")
    except ValueError:
        txt.insert('end', '.')
        print("add '.'")


def btn_result_function(txt: tk.Entry):
    print(txt.get())
    # txt.delete(0, 'end')
    # str_str: str = txt.get()
    for item in txt.get():
        print(len(txt.get()))
    txt.delete(len(txt.get()) - 1, 'end')
    print()
