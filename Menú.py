import tkinter as tk
from functools import partial

from tkinter import messagebox

class Futoshiki:
    def __init__(self,master):
        self.master =  master
        self.master.title('Futoshiki')
        self.master.geometry('500x500')

        self.inicializar_gui()

    def inicializar_gui(self):
        self.lblTitulo = tk.Label(self.master,text='FUTOSHIKI',fg='white',bg='red',font=('System',20)).pack(fill=tk.X) 
        self.barMenu = tk.Menu(self.master)
        self.barMenu.add_command(label='Jugar',command=self.juego)
        self.barMenu.add_command(label='Configuracion',command=self.configurar)
        self.barMenu.add_command(label='Ayuda',command=self.ayuda)
        self.barMenu.add_command(label='Acerca De',command=self.acercaDe)
        self.barMenu.add_command(label='Salir',command=self.salir)
        self.master.config(menu=self.barMenu)
    
    def juego(self):
        self.btnIniciarJuego = tk.Button(self.master,text='Iniciar Juego',bg='red',font=('System',12)).place(x=20,y=45)

    def configurar(self):
        self.ventanaConfigurar = tk.Tk()
        self.ventanaConfigurar.geometry('500x300')
        self.ventanaConfigurar.title('Configuración')

        self.lblTitulo = tk.Label(self.ventanaConfigurar,text='FUTOSHIKI',fg='white',bg='red',font=('System',20)).pack(fill=tk.X) 
        self.lblNivel = tk.Label(self.ventanaConfigurar,text='Nivel:',font=('System',12)).place(x=10,y=45)
        self.c1 = tk.IntVar()
        self.c2 = tk.IntVar()
        self.c3 = tk.IntVar()

        check1 = tk.Radiobutton(self.ventanaConfigurar,text="Fácil",variable=self.c1 \
                                                    ,value=1 \
                                                    ).place(x=35,y=45)

        check2 = tk.Radiobutton(self.ventanaConfigurar,text="Intermedio",variable=self.c2 \
                                                    , value=2 \
                                                    ).place(x=35,y=65)

        check3 = tk.Radiobutton(self.ventanaConfigurar,text="Díficil",variable=self.c3 \
                                                    ,value=3 \
                                                    ).place(x=35,y=85)

        self.lblReloj = tk.Label(self.ventanaConfigurar,text='Reloj:',font=('System',12)).place(x=10,y=115)
        self.lblPosicionDigitos = tk.Label(self.ventanaConfigurar,text='Posición en la ventana del panel de dígitos:',font=('System',12)).place(x=10,y=135)

    def showOption(self,opcion):
        pass

    def ayuda(self):
        pass

    def acercaDe(self):
        pass

    def salir(self):
        respuesta= messagebox.askyesno("Cuidado", "¿Quiere salir del programa?")
        if respuesta==True:
            self.master.destroy()

def main():
    app = tk.Tk()
    ventanaPrincipal = Futoshiki(app)
    app.mainloop()

if __name__ == "__main__":
    main()