import tkinter as tk

sym_list = ('+', '-', '*', '/', '=')
sym_str = "+-*/="
sym2_str = "+-"
sym3_str = "*/"
calc_list = []


def append(string: str, add_chars: str):
    string = string + add_chars
    return string


def calc_function(a, b, c):
    if c == '+':
        if float(float(a) + float(b)) != int(float(a) + float(b)):
            return str(float(float(a) + float(b)))
        else:
            return str(int(float(a) + float(b)))
    elif c == '-':
        if float(float(a) - float(b)) != int(float(a) - float(b)):
            return str(float(float(a) - float(b)))
        else:
            return str(int(float(a) - float(b)))
    elif c == '*':
        if float(float(a) * float(b)) != int(float(a) * float(b)):
            return str(float(float(a) * float(b)))
        else:
            return str(int(float(a) * float(b)))
    elif c == '/':
        if float(float(a) / float(b)) != int(float(a) / float(b)):
            return str(float(float(a) / float(b)))
        else:
            return str(int(float(a) / float(b)))
    else:
        print(f"! ERROR ! calc_function: c = '{c}'")
        return a


def btn_clear_function(txt: tk.Entry):
    txt.delete(0, 'end')
    calc_list.clear()


def btn1_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    txt.insert('end', '1')
    # print("add '1'")
    # print("end text: '", txt.get(), "'\n")


def btn2_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    txt.insert('end', '2')
    # print("add '2'")
    # print("end text: '", txt.get(), "'\n")


def btn3_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    txt.insert('end', '3')
    # print("add '3'")
    # print("end text: '", txt.get(), "'\n")


def btn4_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    txt.insert('end', '4')
    # print("add '4'")
    # print("end text: '", txt.get(), "'\n")


def btn5_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    txt.insert('end', '5')
    # print("add '5'")
    # print("end text: '", txt.get(), "'\n")


def btn6_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    txt.insert('end', '6')
    # print("add '6'")
    # print("end text: '", txt.get(), "'\n")


def btn7_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    txt.insert('end', '7')
    # print("add '7'")
    # print("end text: '", txt.get(), "'\n")


def btn8_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    txt.insert('end', '8')
    # print("add '8'")
    # print("end text: '", txt.get(), "'\n")


def btn9_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    txt.insert('end', '9')
    # print("add '9'")
    # print("end text: '", txt.get(), "'\n")


def btn0_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    txt.insert('end', '0')
    # print("add '0'")
    # print("end text: '", txt.get(), "'\n")


def btn_plus_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            # print(f"replace '{str_str[len(str_str) - 1]}' -> '+'")
            txt.delete(len(str_str) - 1, 'end')
            txt.insert('end', '+')
    except ValueError:
        # print("add '+'")
        txt.insert('end', '+')
    except IndexError:
        print("not number for '+'")
    # finally:
        # print("end text: '", txt.get(), "'\n")


def btn_minus_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            # print(f"replace '{str_str[len(str_str) - 1]}' -> '-'")
            txt.delete(len(str_str) - 1, 'end')
            txt.insert('end', '-')
    except ValueError:
        # print("add '-'")
        txt.insert('end', '-')
    except IndexError:
        print("not number for '-'")
    # finally:
        # print("end text: '", txt.get(), "'\n")


def btn_multi_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            # print(f"replace '{str_str[len(str_str) - 1]}' -> '*'")
            txt.delete(len(str_str) - 1, 'end')
            txt.insert('end', '*')
    except ValueError:
        # print("add '*'")
        txt.insert('end', '*')
    except IndexError:
        print("not number for '*'")
    # finally:
    #     print("end text: '", txt.get(), "'\n")


def btn_split_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            # print(f"replace '{str_str[len(str_str) - 1]}' -> '/'")
            txt.delete(len(str_str) - 1, 'end')
            txt.insert('end', '/')
    except ValueError:
        # print("add '/'")
        txt.insert('end', '/')
    except IndexError:
        print("not number for '/'")
    # finally:
    #     print("end text: '", txt.get(), "'\n")


def btn_percent_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print("not number to percentage")
    except ValueError:
        txt.insert('end', '%')
        # print("add '%'")
    except IndexError:
        print("not number to percentage")
    # finally:
    #     print("end text: '", txt.get(), "'\n")


def btn_dot_function(txt: tk.Entry):
    # print("start text: '", txt.get(), "'")
    try:
        str_str: str = txt.get()
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print("not number for dot")
    except ValueError:
        txt.insert('end', '.')
        # print("add '.'")
    except IndexError:
        print("not number for dot")
    # finally:
    #     print("end text: '", txt.get(), "'\n")


def btn_result_function(txt: tk.Entry):
    print("start text: '", txt.get(), "'")

    str_str: str = txt.get()

    try:
        if sym_list.index(str_str[len(str_str) - 1]) >= 0:
            print(f"replace '{str_str[len(str_str) - 1]}' -> '='")
            txt.delete(len(str_str) - 1, 'end')
            txt.insert('end', '=')
    except ValueError:
        # print("add '='")
        txt.insert('end', '=')
    except IndexError:
        print("not number for '='")
    finally:
        result_function(txt)

    print("end text: '", txt.get(), "'\n")


def result_function(txt: tk.Entry):

    result2_function(txt)

    str_str: str = txt.get()
    a: str = ''
    b: str = ''
    c: str = ''

    for item in str_str:
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
                b = ''
                c = item

        elif sym_str.find(item) < 0 and item == '%':
            if len(c) > 0:
                if float((float(a) / 100) * float(b)) != int((float(a) / 100) * float(b)):
                    b = str(float((float(a) / 100) * float(b)))
                else:
                    b = str(int((float(a) / 100) * float(b)))
                a = calc_function(a, b, c)
                b = ''
                c = ''
            else:
                print(f"! ERROR ! result_function: c = '{c}'")
        # if
    # for
    txt.insert('end', a)
# def result_function


def result2_function(txt: tk.Entry):
    str_str: str = txt.get()

    for item in str_str:
        calc_list.append(item)

    for i in range(len(calc_list)):
        a: str = ''
        b: str = ''
        c: str = ''
        if i < len(calc_list) - 1:  # если не закончился текст
            index = i
            item = calc_list[index]

            if sym3_str.find(item) >= 0:  # если вообще есть умножение или деление

                for i2 in range(len(calc_list)):
                    index2 = i2
                    item2 = calc_list[index2]
                    if sym2_str.find(item2) < 0 and sym3_str.find(item2) < 0 and item2 != '=':
                        if len(c) <= 0:
                            a = append(a, item2)
                        else:
                            b = append(b, item2)
                    elif sym2_str.find(item2) >= 0 > sym3_str.find(item2) and item2 != '=':
                        if len(c) <= 0:
                            a = ''
                        else:
                            break
                    elif sym2_str.find(item2) < 0 <= sym3_str.find(item2):
                        c = item2
                    # if
                # for

                tmp = calc_function(a, b, c)

                del_index = len(b)
                for i3 in range(len(a) + len(b) + len(c)):
                    calc_list.pop(index + del_index)
                    del_index -= 1

                str_str = ''
                for i4 in range(len(calc_list)):
                    if i4 < index - len(a):
                        str_str = append(str_str, calc_list[i4])
                    elif i4 == index - len(a):
                        str_str = append(str_str, tmp)
                        str_str = append(str_str, calc_list[i4])
                    elif i4 > index - len(a):
                        str_str = append(str_str, calc_list[i4])
                txt.delete(0, 'end')
                txt.insert(index - len(a), str_str)

                calc_list.clear()
                for item in str_str:
                    calc_list.append(item)
            # if
        # if
    # for
# def result2_function
