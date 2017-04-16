import tkinter

HEX_FORMAT = "#%02x%02x%02x"


def display(bitmap):
    master = tkinter.Tk()
    w = tkinter.Canvas(master, width=bitmap.width, height=bitmap.height)
    image = tkinter.PhotoImage(width=bitmap.width, height=bitmap.height)
    image.put(
        " ".join('{' + ' '.join(bitmap.get(x, y).hex() for x in range(bitmap.width)) + '}'
                 for y in range(bitmap.height)))

    w.create_image(0, 0, image=image, anchor=tkinter.NW)
    w.pack()
    tkinter.mainloop()