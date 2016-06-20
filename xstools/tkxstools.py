from tkinter import messagebox, Menu, Tk, TOP, SUNKEN, W, X, BOTTOM, Image, LEFT, \
    NW, StringVar
from tkinter.ttk import *

_BLUE = '#2c4484'
_YELLOW = '#fadd67'
_GOLDEN_YELLOW = '#c09853'


def do_nothing():
    print('do nothing called')


def about_dialog():
    title = 'About GXSTOOLs'
    msg = 'Graphical XSTOOLs Utilities Version 0.1.31'
    msg_box = messagebox.showinfo(title, msg)
    return msg_box


def port_frame(master):
    frame = Frame(master=master)
    var = StringVar(master=master)
    usb0 = 'USB0'
    var.set(usb0)
    port_optmenu = OptionMenu(frame, var, usb0)
    port_optmenu.pack(side=LEFT)
    blink_button = Button(master=frame, text='Blink', command=do_nothing)
    blink_button.pack(side=LEFT)
    return frame


if __name__ == '__main__':
    root = Tk()

    root.title('XESS Board Tools')

    menu = Menu(master=root)
    root.config(menu=menu)

    children = menu.children

    sub_menu = Menu()
    menu.add_cascade(label='XSTools', menu=sub_menu)
    sub_menu.add_command(label='About', command=about_dialog)

    tab_texts = [
        ('Ports', port_frame),
        ('FPGA', None),  # {'image': ImageTk.PhotoImage(Image.open('icons/fpga.png'))}),
        ('SDRAM', None),
        ('Flash', None),
        ('Test', None),
        ('Flags', None),
        ('uC', None),
    ]

    nb = Notebook(master=root, width=100, height=100)  # , activefg=_YELLOW
    for tab_text, fn in tab_texts:
        if fn is None:
            tab = Frame(master=root)
        else:
            tab = fn(master=root)
        nb.add(tab, text=tab_text)
    nb.pack(side=TOP)

    status_kwargs = dict(relief=SUNKEN, anchor=W)  # bg=_BLUE, bd=1, fg='white',
    txt = 'Port: USB0 Board: XuLA2-LX25'
    status = Label(master=root, text=txt, **status_kwargs)
    status.pack(side=BOTTOM, fill=X)

    root.mainloop()
