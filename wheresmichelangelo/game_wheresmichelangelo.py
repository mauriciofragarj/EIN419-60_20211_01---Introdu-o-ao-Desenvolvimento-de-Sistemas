from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Onde Está Michelangelo?')
root.iconbitmap('C:/Z_SANDBOX/wheresmichelangelo/media/art.ico')
#___________________________________________________________________________________________
img_title = ImageTk.PhotoImage(Image.open('C:/Z_SANDBOX/wheresmichelangelo/media/Slide_01.png'))
objeto1 = Label(root, image=img_title).grid(row=0, column=0, columnspan=3)
#____________________________________________________________________________________________
def iniciarjogo():
    global img_01
    top = Toplevel()
    top.title('Onde Está Michelangelo?')
    top.iconbitmap('C:/Z_SANDBOX/wheresmichelangelo/media/art.ico')

    img_01 = ImageTk.PhotoImage(Image.open('C:/Z_SANDBOX/wheresmichelangelo/media/Slide_02.png'))
    objeto2 = Label(top, image=img_01).grid(row=0, column=0, columnspan=3)
    proximo2 = Button(top, text="Continuar", command=fase1).grid(row=1, column=0, columnspan=3)

def fase1():
    global img_02
    top2 = Toplevel()
    top2.title('Onde Está Michelangelo?')
    top2.iconbitmap('C:/Z_SANDBOX/wheresmichelangelo/media/art.ico')

    img_02 = ImageTk.PhotoImage(Image.open('C:/Z_SANDBOX/wheresmichelangelo/media/Slide3.png'))
    objeto3 = Label(top2, image=img_02).grid(row=0, column=0, columnspan=3)
    proximo3 = Button(top2, text="Continuar", command=fase2).grid(row=1, column=0, columnspan=3)

def fase2():
    global img_03
    top3 = Toplevel()
    top3.title('Onde Está Michelangelo?')
    top3.iconbitmap('C:/Z_SANDBOX/wheresmichelangelo/media/art.ico')

    img_03 = ImageTk.PhotoImage(Image.open('C:/Z_SANDBOX/wheresmichelangelo/media/Slide4.png'))
    objeto3 = Label(top3, image=img_03).grid(row=0, column=0, columnspan=3)
    proximo3 = Button(top3, text="Continuar", command=fase3).grid(row=1, column=0, columnspan=3)

def fase3():
    global img_04
    top4 = Toplevel()
    top4.title('Onde Está Michelangelo?')
    top4.iconbitmap('C:/Z_SANDBOX/wheresmichelangelo/media/art.ico')


    img_04 = ImageTk.PhotoImage(Image.open('C:/Z_SANDBOX/wheresmichelangelo/media/Slide5.png'))
    objeto4 = Label(top4, image=img_04).grid(row=0, column=0, columnspan=3)

    r1 = IntVar()


    Radiobutton(top4, text="a) O Rapto das Sabinas", variable=r1, value=1, command=lambda: clicked(r1.get())).grid(row=1, column=0)
    Radiobutton(top4, text="b) Davi", variable=r1, value=2, command=lambda: clicked(r1.get())).grid(row=1, column=1)
    Radiobutton(top4, text="c) Baco", variable=r1, value=3, command=lambda: clicked(r1.get())).grid(row=1, column=2)
    proximo4 = Button(top4, text="Responder e Continuar", command=fase4).grid(row=3, column=1)

def fase4():
    return

#____________________________________________________________________________________________
proximo = Button(root, text="Iniciar Jogo", command=iniciarjogo).grid(row=1, column=0, columnspan=3)


root.mainloop()
