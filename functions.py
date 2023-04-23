import tkinter as tk

sym_list = ('+', '-', '*', '/', '=')

sym_str = "+-*/="


# print(sym_str.find('7'))

def append(string: str, add_chars: str):
    string = string + add_chars
    return string


def calc_function(a, b, c):
    if c == '+':
        return str(float(a) + float(b))
    elif c == '-':
        return str(float(a) - float(b))
    elif c == '*':
        return str(float(a) * float(b))
    elif c == '/':
        return str(float(a) / float(b))
    else:
        print(f"! ERRPR ! : c = '{c}'")


def btn_clear_function(txt: tk.Entry):
    txt.delete(0, 'end')


def btn1_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    txt.insert('end', '1')
    print("add '1'")
    print("end text: '", txt.get(), "'\n")


def btn2_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    txt.insert('end', '2')
    print("add '2'")
    print("end text: '", txt.get(), "'\n")


def btn3_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    txt.insert('end', '3')
    print("add '3'")
    print("end text: '", txt.get(), "'\n")


def btn4_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    txt.insert('end', '4')
    print("add '4'")
    print("end text: '", txt.get(), "'\n")


def btn5_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    txt.insert('end', '5')
    print("add '5'")
    print("end text: '", txt.get(), "'\n")


def btn6_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    txt.insert('end', '6')
    print("add '6'")
    print("end text: '", txt.get(), "'\n")


def btn7_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    txt.insert('end', '7')
    print("add '7'")
    print("end text: '", txt.get(), "'\n")


def btn8_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    txt.insert('end', '8')
    print("add '8'")
    print("end text: '", txt.get(), "'\n")


def btn9_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    txt.insert('end', '9')
    print("add '9'")
    print("end text: '", txt.get(), "'\n")


def btn0_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    txt.insert('end', '0')
    print("add '0'")
    print("end text: '", txt.get(), "'\n")


def btn_plus_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print(f"replace '{str_str[len(str_str) - 1]}' -> '+'")
            txt.delete(len(str_str) - 1, 'end')
            txt.insert('end', '+')
    except ValueError:
        print("add '+'")
        txt.insert('end', '+')
    except IndexError:
        print("not number for '+'")
    finally:
        print("end text: '", txt.get(), "'\n")


def btn_minus_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print(f"replace '{str_str[len(str_str) - 1]}' -> '-'")
            txt.delete(len(str_str) - 1, 'end')
            txt.insert('end', '-')
    except ValueError:
        print("add '-'")
        txt.insert('end', '-')
    except IndexError:
        print("not number for '-'")
    finally:
        print("end text: '", txt.get(), "'\n")


def btn_multi_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print(f"replace '{str_str[len(str_str) - 1]}' -> '*'")
            txt.delete(len(str_str) - 1, 'end')
            txt.insert('end', '*')
    except ValueError:
        print("add '*'")
        txt.insert('end', '*')
    except IndexError:
        print("not number for '*'")
    finally:
        print("end text: '", txt.get(), "'\n")


def btn_split_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print(f"replace '{str_str[len(str_str) - 1]}' -> '/'")
            txt.delete(len(str_str) - 1, 'end')
            txt.insert('end', '/')
    except ValueError:
        print("add '/'")
        txt.insert('end', '/')
    except IndexError:
        print("not number for '/'")
    finally:
        print("end text: '", txt.get(), "'\n")


def btn_percent_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print("not number to percentage")
    except ValueError:
        txt.insert('end', '%')
        print("add '%'")
    except IndexError:
        print("not number to percentage")
    finally:
        print("end text: '", txt.get(), "'\n")


def btn_dot_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print("not number for dot")
    except ValueError:
        txt.insert('end', '.')
        print("add '.'")
    except IndexError:
        print("not number for dot")
    finally:
        print("end text: '", txt.get(), "'\n")


def btn_result_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")

    str_str: str = txt.get()

    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print(f"replace '{str_str[len(str_str) - 1]}' -> '='")
            txt.delete(len(str_str) - 1, 'end')
            txt.insert('end', '=')
    except ValueError:
        print("add '='")
        txt.insert('end', '=')
    except IndexError:
        print("not number for '='")
    finally:
        result_function(txt)

    print("end text: '", txt.get(), "'\n")


def result_function(txt: tk.Entry):
    str_str: str = txt.get()
    a: str = ''
    b: str = ''
    c: str = ''

    for item in str_str:
        # print(item)
        if sym_str.find(item) < 0 and item != '%':
            if len(c) <= 0:
                a = append(a, item)
            else:
                b = append(b, item)

        elif sym_str.find(item) >= 0:
            if len(c) <= 0:
                c = item
            else:
                a = calc_function(a, b, c)
                print(f"result ({c}): {a}")
                b = ''
                c = item

        elif sym_str.find(item) < 0 and item == '%':
            if len(c) > 0:
                a = str((float(a) / 100) * float(b))
                b = ''
                c = ''
            else:
                print(f"! ERROR ! : c = '{c}'")

    txt.insert('end', a)
