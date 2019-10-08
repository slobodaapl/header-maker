from tkinter import *
from PIL import ImageDraw
from PIL import Image

width = 500
height = 175
blue = (0, 56, 200)
lim = 4
v_draw = 0

pointer = [50, 50]

window = Canvas(width=width, height=height, background='white')
window.pack()

image1 = Image.new("RGB", (width, height+300), (255, 255, 255))
draw = ImageDraw.Draw(image1)

for i in range(5):
    string = str(i) + "B"
    window.create_text(pointer[0] + i*100-3, pointer[1] - 35, text=string, anchor="center")
    draw.text([pointer[0] + i*100-i*1, pointer[1] - 35], text=string, fill='black', anchor="center")
    window.create_line(pointer[0] + i*100, pointer[1], pointer[0] + i*100, pointer[1] - 28, width=3)
    draw.line([pointer[0] + i*100-i*1, pointer[1], pointer[0] + i*100-i*1, pointer[1] - 20], width=3, fill='black')



def newblock():
    global pointer, height, width, image1, v_draw
    pointer[1] += 75
    pointer[0] = 50
    v_draw += 1
    height += 75
    window.config(height=height)

def newpart(size):
    global pointer
    pointer[0] += 100*size


def inserttext(text, size):
    global pointer, window, draw
    window.create_text(pointer[0] + size*50, pointer[1] + 75/2, text=text, anchor="center")
    w, h = draw.textsize(text)
    draw.text([pointer[0] + size * 50 - w/2, pointer[1] + 75 / 2 - h/2], text=text, fill='black', align="center")


def drawblock(size, text):
    global pointer, window, draw, lim, v_draw
    window.create_rectangle(pointer[0], pointer[1], pointer[0] + size*100, pointer[1] + 75, width=3,  fill='white', outline='cyan')
    draw.rectangle([pointer[0]-3, pointer[1]-v_draw*3, pointer[0] + size*100, pointer[1] + 75 - v_draw*3], fill='white', width=3, outline='cyan')
    inserttext(text, size)
    newpart(size)


def drawheader():
    global lim
    stra = input()
    if(stra == "end"):
        name = input()
        filename = name + '.png'
        image1.save(filename)
        return
    else:
        strb = input()
        stra = int(stra)
        drawblock(stra, strb)
        lim -= stra
        if lim == 0:
            newblock()
            lim = 4
        window.after(10, drawheader)

drawheader()
window.mainloop()
