pos_img = 0
Frases = []
num_frases = 0
def main():
        from PIL import ImageTk, Image
        import tkinter as tk
        from tkinter import filedialog
        import os
        from tkinter.scrolledtext import ScrolledText
        import subprocess
        import sys
        import tkinter.ttk as ttk
        from os import walk

        ws = tk.Tk()
        ws.title('Whatzapp Bot')
        ws.geometry("400x400")
        img = ImageTk.PhotoImage(Image.open(__file__[:-5] + "logo.ico"))
        ws.tk.call('wm', 'iconphoto', ws._w, img)

        images = []
        ws.configure(background='black')
        frame = tk.LabelFrame(
            ws,
            text='Good vibes',
            bg='white',
            font=(20),
            fg='white',
            background='#3F3F3F'
        )
        '''
        print(1)
        Como odio a Buratti
        '''
        # print(1)
        print(1)
        ws.tk_setPalette("#C8C8C8")
        frame.pack(expand=True, fill=tk.BOTH)
        imagenes = tk.Listbox(frame,width=20, bd=3, height=5)
        def ImageOpen():
                global pos_img
                filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes =[('all files', '.*'),("text files",".txt"),('image files', ('.png', '.jpg'))])
                if filename :
                        images.append(filename)
                        imagenes.insert(pos_img,filename.split('/')[-1])
                        pos_img += 1
        tk.Button(ws, text='Imagenes', command=ImageOpen).place(x=200, y=205)
        imagenes.place(x=200,y=210)
        ncontactos = tk.Label(ws, text = "Numeros de contactos: 0")
        def Contactos():
                filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes =[('all files', '.*'),("text files",".txt"),('image files', ('.png', '.jpg'))])
                if filename:
                        with open(filename,"r") as f:
                                contactos = f.read().splitlines()
                        contactos=set(contactos)
                        try:
                                contactos.remove('')
                        except: pass
                        i = len(contactos)

                        file = open(os.path.join("numeros.txt"), "w")
                        for i,num in enumerate(contactos):
                                file.write(num+'\n')

                        file.close()

                        ncontactos.configure(text = f"Numeros de contactos: {str(i+1)}")
        tk.Button(ws, text='Archivo de los Contactos', command=Contactos).place(x=40, y=30)
        ncontactos.place(x=40,y=55)

        Textfield = ScrolledText(ws,wrap = tk.WORD,width = 20,height = 8,font = ("Times New Roman",10))
        frases = tk.Label(ws, text = "Numero de frases: 0")
        frases.place(x=15,y=270)
        def Frase():
                global num_frases
                num_frases +=1
                text = Textfield.get('1.0', tk.END)
                if text :
                        Textfield.delete('1.0', tk.END)
                        with open(os.path.join("frases.txt"),"a",encoding='utf8')as f:
                                f.write(rf"{text}")
                        frases.configure(text = f"Numeros de frases guardados: {int(num_frases)}")
        tk.Label(ws, text = "Que enviar").place(x=15,y=85)
        Textfield.place(x=15 , y=110)
        tk.Button(ws, text='Confirmar', command=Frase).place(x=40, y=300)
        tk.Label(ws,text="Numero de bots: ").place(x=200,y=85)
        inputb = tk.Entry(ws,width=20)
        inputb.place(x=200,y=110)
        tiempo = tk.Entry(ws,width=10)
        tiempo.place(x=220,y=50)
        tiempo3 = tk.Entry(ws,width=10)
        tiempo3.place(x=300,y=50)
        tk.Label(ws, text="min").place(x=190, y=50)
        tk.Label(ws, text="Tiempo em Minutos por mensaje").place(x=200, y=25)
        tiempo2 = tk.Entry(ws, width=10)
        tiempo2.place(x=200, y=170)
        tk.Label(ws, text="Tiempo de espera em Minutos").place(x=200, y=140)
        def Enpezar():
                filenames = next(walk(__file__[:-5]+"notsend"), (None, None, []))[2]  # [] if no file
                for i in filenames:
                        a=open(".\\notsend\\" + i)
                        b=a.readlines()
                        a.close()

                        c=open("allnotsend.txt","a")
                        for i in b:
                                if b:
                                        c.write(i+'\n')
                        c.close()
                with open(__file__[:-5]+'allnotsend.txt') as f:
                        file_one = f.read().splitlines()

                with open(__file__[:-5]+'numeros.txt') as f:
                        file_two = f.read().splitlines()


                result = list(set(file_one) ^ set(file_two))

                with open("numeros.txt", "w") as f:
                        for line in result:
                                f.write(line + "\n")

                bots = int(inputb.get())
                if images:
                        a = open(os.path.join("imagenes.txt"),"w")
                        for z in images:
                                a.write(z)
                        a.close()

                with open(__file__[:-5]+"numeros.txt", "r") as f:
                        for i, _ in enumerate(f):
                                pass
                n = i //bots
                l = [[0,i-n*(bots-1)]]
                count = bots - 1
                for j in range(count):
                        if j == bots-1:
                                l.append([i-n+1,i])
                                continue
                        l.append([i-n*count+1,i-n*(count-1)])
                        count-=1
                print(f"Numeros de bots {bots}")
                print(f"Cada bot enviara mensaje a cada {int(tiempo.get())} minutos")
                for bot, p in enumerate(l):

                        subprocess.run(['python','./main/main.py', str(p[0]), str(p[1]), str(i), str(bot),str(int(tiempo.get()) * 60 ),str(int(tiempo2.get())),str(int(tiempo3.get()) * 60)])
                sys.exit(0)
        enpezar = tk.Button(ws,text="Empezar",command=Enpezar,width=10,font=("Times New Roman",20))
        enpezar.place(x=200,y=335)
        ws.mainloop()
