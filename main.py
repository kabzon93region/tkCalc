import tkinter as tk

import functions as f

window = tk.Tk()  # создание окна программы

bgcolor = '#1E1F22'
actbgcolor = '#575A63'
txtcolor = '#B8BAC0'
acttxtcolod = '#15161A'
title_str = "Кукуляторъ"
icon_str = "main.ico"
xw = 250  # задаем ширину окна
yw = 175  # задаем высоту окна
xspos = (window.winfo_screenwidth() - xw) / 2  # рассчитываем отступ по ширине для создания окна на экране по центру
yspos = (window.winfo_screenheight() - yw) / 2  # рассчитываем отступ по высоте для создания окна на экране по центру

window.title(title_str)  # задаем название окна
window.geometry(
    "%dx%d+%d+%d" % (xw, yw, xspos, yspos))  # задаем ширину, высоту окна и отступы по ширине и высоте для создания окна
window.resizable(False, False)  # задаем возможность изменять размер окна по ширине, высоте
window.iconbitmap(icon_str)  # задаем иконку окна
window.config(bg=bgcolor)  # задаем цвет фона в хекс формате
fontvar = ('Arial', 10)
fontbvar = ('Arial', 11, 'bold')
fontevar = ('Arial', 12)

for i in range(5):
    window.grid_rowconfigure(i, minsize=30)
    window.grid_columnconfigure(i, minsize=50)

txt = tk.Entry(window, bg=bgcolor, fg=txtcolor, relief='solid', justify='right', font=fontevar)
txt.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky='nwes')

btn1 = tk.Button(window, text='1', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor, activeforeground=acttxtcolod,
                 relief='solid', font=fontvar, command=lambda: f.btn1_function(txt))
btn1.grid(row=3, column=0, padx=2, pady=2, sticky='nwes')

btn2 = tk.Button(window, text='2', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor, activeforeground=acttxtcolod,
                 relief='solid', font=fontvar, command=lambda: f.btn2_function(txt))
btn2.grid(row=3, column=1, padx=2, pady=2, sticky='nwes')

btn3 = tk.Button(window, text='3', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor, activeforeground=acttxtcolod,
                 relief='solid', font=fontvar, command=lambda: f.btn3_function(txt))
btn3.grid(row=3, column=2, padx=2, pady=2, sticky='nwes')

btn4 = tk.Button(window, text='4', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor, activeforeground=acttxtcolod,
                 relief='solid', font=fontvar, command=lambda: f.btn4_function(txt))
btn4.grid(row=2, column=0, padx=2, pady=2, sticky='nwes')

btn5 = tk.Button(window, text='5', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor, activeforeground=acttxtcolod,
                 relief='solid', font=fontvar, command=lambda: f.btn5_function(txt))
btn5.grid(row=2, column=1, padx=2, pady=2, sticky='nwes')

btn6 = tk.Button(window, text='6', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor, activeforeground=acttxtcolod,
                 relief='solid', font=fontvar, command=lambda: f.btn6_function(txt))
btn6.grid(row=2, column=2, padx=2, pady=2, sticky='nwes')

btn7 = tk.Button(window, text='7', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor, activeforeground=acttxtcolod,
                 relief='solid', font=fontvar, command=lambda: f.btn7_function(txt))
btn7.grid(row=1, column=0, padx=2, pady=2, sticky='nwes')

btn8 = tk.Button(window, text='8', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor, activeforeground=acttxtcolod,
                 relief='solid', font=fontvar, command=lambda: f.btn8_function(txt))
btn8.grid(row=1, column=1, padx=2, pady=2, sticky='nwes')

btn9 = tk.Button(window, text='9', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor, activeforeground=acttxtcolod,
                 relief='solid', font=fontvar, command=lambda: f.btn9_function(txt))
btn9.grid(row=1, column=2, padx=2, pady=2, sticky='nwes')

btn0 = tk.Button(window, text='0', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor, activeforeground=acttxtcolod,
                 relief='solid', font=fontvar, command=lambda: f.btn0_function(txt))
btn0.grid(row=4, column=0, columnspan=2, sticky='nwes', padx=2, pady=2)

btn_dot = tk.Button(window, text='.', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor,
                    activeforeground=acttxtcolod, relief='solid', font=fontbvar,
                    command=lambda: f.btn_dot_function(txt))
btn_dot.grid(row=4, column=2, padx=2, pady=2, sticky='nwes')

btn_plus = tk.Button(window, text='+', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor,
                     activeforeground=acttxtcolod, relief='solid', font=fontbvar,
                     command=lambda: f.btn_plus_function(txt))
btn_plus.grid(row=1, column=3, padx=2, pady=2, sticky='nwes')

btn_minus = tk.Button(window, text='-', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor,
                      activeforeground=acttxtcolod, relief='solid', font=fontbvar,
                      command=lambda: f.btn_minus_function(txt))
btn_minus.grid(row=2, column=3, padx=2, pady=2, sticky='nwes')

btn_multi = tk.Button(window, text='*', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor,
                      activeforeground=acttxtcolod, relief='solid', font=fontbvar,
                      command=lambda: f.btn_multi_function(txt))
btn_multi.grid(row=3, column=3, padx=2, pady=2, sticky='nwes')

btn_split = tk.Button(window, text='/', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor,
                      activeforeground=acttxtcolod, relief='solid', font=fontbvar,
                      command=lambda: f.btn_split_function(txt))
btn_split.grid(row=4, column=3, padx=2, pady=2, sticky='nwes')

btn_percent = tk.Button(window, text='%', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor,
                        activeforeground=acttxtcolod, relief='solid', font=fontbvar,
                        command=lambda: f.btn_percent_function(txt))
btn_percent.grid(row=1, column=4, padx=2, pady=2, sticky='nwes')

btn_result = tk.Button(window, text='=', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor,
                       activeforeground=acttxtcolod, relief='solid', font=fontbvar,
                       command=lambda: f.btn_result_function(txt))
btn_result.grid(row=2, column=4, rowspan=3, sticky='nwes', padx=2, pady=2)

btn_clear = tk.Button(window, text='C', bg=bgcolor, fg=txtcolor, activebackground=actbgcolor,
                       activeforeground=acttxtcolod, relief='solid', font=fontbvar,
                       command=lambda: f.btn_clear_function(txt))
btn_clear.grid(row=0, column=4, sticky='nwes', padx=2, pady=2)



# ent1 = tk.Entry(window)  # создаем поле ввода, можно добавить параметр show=и указать символ который отображается вместо введенных
# ent1.grid(row=0, column=3, sticky='we')
# btn1.config(command=lambda: ent1.delete(0, 'end'))
# btn2.config(command=lambda: label1.config(text=ent1.get()))


window.mainloop()
