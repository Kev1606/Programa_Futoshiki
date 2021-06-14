import os
import tkinter as tk
from functools import partial

from tkinter import messagebox

class Futoshiki(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master =  master
        self.master.title('Futoshiki')
        self.master.geometry('600x600')

        self.inicializar_gui()
        self.nivelJuego = tk.IntVar()
        self.nivelJuego.set('1')
        self.relojConfig = tk.IntVar()
        self.relojConfig.set('1')
        self.PosicionNumeros = tk.IntVar()
        self.PosicionNumeros.set('1')
        

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
        nivelJuego = self.nivelJuego.get()
        if nivelJuego == 1:
            self.lblNivelJuego = tk.Label(self.master,text='NIVEL FÁCIL', font=('System',16)).pack(fill=tk.X)
        elif nivelJuego == 2:
            self.lblNivelJuego = tk.Label(self.master,text='NIVEL INTERMEDIO', font=('System',16)).pack(fill=tk.X)
        elif nivelJuego == 3:
            self.lblNivelJuego = tk.Label(self.master,text='NIVEL DÍFICIL', font=('System',16)).pack(fill=tk.X)
        
        self.lblNombre = tk.Label(self.master,text='Nombre del jugador',font=('System',12)).place(x=10,y=60)
        self.txtNombre = tk.Entry(self.master,width=50,font=('System',12)).place(x=150,y=60)
        self.btnIniciarJuego = tk.Button(self.master,text='INICIAR JUEGO',bg='red',font=('System',10)).place(x=5,y=450)
        self.btnBorrarJugada = tk.Button(self.master,text='BORRAR JUGADA',bg='blue',font=('System',10)).place(x=125,y=450)
        self.btnTerminarJuego = tk.Button(self.master,text='TERMINAR JUEGO',bg='green',font=('System',10)).place(x=265,y=450)
        self.btnBorraJuego = tk.Button(self.master,text='BORRAR JUEGO',bg='white',font=('System',10)).place(x=405,y=450)
        self.btnTopLevel = tk.Button(self.master,text='TOP 10',bg='yellow',font=('System',10)).place(x=535,y=450)

        posicion = self.PosicionNumeros.get()
        if posicion == 1:
            #BOTONES DEL JUEGO
            self.btn1 = tk.Button(self.master,text='1',font=('System',12),activebackground='green').place(x=50,y=120)
            self.btn2 = tk.Button(self.master,text='2',font=('System',12),activebackground='green').place(x=50,y=160)
            self.btn3 = tk.Button(self.master,text='3',font=('System',12),activebackground='green').place(x=50,y=200)
            self.btn4 = tk.Button(self.master,text='4',font=('System',12),activebackground='green').place(x=50,y=240)
            self.btn5 = tk.Button(self.master,text='5',font=('System',12),activebackground='green').place(x=50,y=280)
            #self.btn11.place_forget()
            #self.btn22.place_forget()
            #self.btn33.place_forget()
            #self.btn44.place_forget()
            #self.btn55.place_forget()
        else:
            self.btn11 = tk.Button(self.master,text='1',font=('System',12),activebackground='green').place(x=530,y=120)
            self.btn22= tk.Button(self.master,text='2',font=('System',12),activebackground='green').place(x=530,y=160)
            self.btn33 = tk.Button(self.master,text='3',font=('System',12),activebackground='green').place(x=530,y=200)
            self.btn44 = tk.Button(self.master,text='4',font=('System',12),activebackground='green').place(x=530,y=240)
            self.btn55 = tk.Button(self.master,text='5',font=('System',12),activebackground='green').place(x=530,y=280)
            #self.btn1.place_forget()
            #self.btn2.place_forget()
            #self.btn3.place_forget()
            #self.btn4.place_forget()
            #self.btn5.place_forget()
        self.btnGuardarJuego = tk.Button(self.master,text='GUARDAR JUEGO',font=('System',10)).place(x=305,y=525)
        self.btnCargarJuego = tk.Button(self.master,text='CARGAR JUEGO',font=('System',10)).place(x=445,y=525)



    def configurar(self):
        self.ventanaConfigurar = tk.Tk()
        self.ventanaConfigurar.geometry('500x300')
        self.ventanaConfigurar.title('Configuración')

        self.lblTitulo = tk.Label(self.ventanaConfigurar,text='FUTOSHIKI',fg='white',bg='red',font=('System',20)).pack(fill=tk.X) 
        self.lblNivel = tk.Label(self.ventanaConfigurar,text='Nivel:',font=('System',12)).place(x=10,y=45)

        self.chkFacil = tk.Radiobutton(self.ventanaConfigurar,text="Fácil",font=('System',12),value = 1, variable=self.nivelJuego \
                                                    ,command=self.radioNivelJuego\
                                                    ).place(x=55,y=45)

        self.chkIntermedio = tk.Radiobutton(self.ventanaConfigurar,text="Intermedio",font=('System',12),value = 2, variable=self.nivelJuego \
                                                    ,command=self.radioNivelJuego\
                                                    ).place(x=55,y=65)

        self.chkDificil = tk.Radiobutton(self.ventanaConfigurar,text="Díficil", font=('System',12), value = 3, variable=self.nivelJuego \
                                                    ,command=self.radioNivelJuego\
                                                    ).place(x=55,y=85)


        self.lblReloj = tk.Label(self.ventanaConfigurar,text='Reloj:',font=('System',12)).place(x=10,y=115)

        self.chkConTiempo = tk.Radiobutton(self.ventanaConfigurar,text="Si", font=('System',12), value = 1, variable=self.relojConfig \
                                                    ,command=self.radioTemporizador\
                                                    ).place(x=55,y=115)

        self.chkSinTiempo = tk.Radiobutton(self.ventanaConfigurar,text="No", font=('System',12), value = 2, variable=self.relojConfig \
                                                    ,command=self.radioTemporizador\
                                                    ).place(x=55,y=135)

        self.chkTimer = tk.Radiobutton(self.ventanaConfigurar,text="Timer", font=('System',12), value = 3, variable=self.relojConfig \
                                                    ,command=self.radioTemporizador\
                                                    ).place(x=55,y=155)
        

        self.lblPosicionDigitos = tk.Label(self.ventanaConfigurar,text='Posición en la ventana del panel de dígitos:',font=('System',12)).place(x=10,y=185)

        self.chkDerecha = tk.Radiobutton(self.ventanaConfigurar,text="Derecha", font=('System',12), value = 1, variable=self.PosicionNumeros \
                                                    ,command=self.PosicionamientoNumeros\
                                                    ).place(x=300,y=185)

        self.chkIzquierda = tk.Radiobutton(self.ventanaConfigurar,text="Izquierda", font=('System',12), value = 2, variable=self.PosicionNumeros \
                                                    ,command=self.PosicionamientoNumeros\
                                                    ).place(x=300,y=205)

    #ERROR NO FUNCIONA
    # EL VALOR SIEMPRE DA CERO
    def radioNivelJuego(self):
        nivelJuego = self.nivelJuego.get()
        print(self.nivelJuego.get())
        if nivelJuego == 1:
            self.ventanaConfigurar.configure(bg='green')
        elif nivelJuego == 2:
            self.ventanaConfigurar.configure(bg='yellow')
        elif nivelJuego == 3:
            self.ventanaConfigurar.configure(bg='red')
    def radioTemporizador(self):
        pass
    
    def PosicionamientoNumeros(self):
        pass
    """
        posicion = self.PosicionNumeros.get()
        if posicion == 1:
            #BOTONES DEL JUEGO
            self.btn1 = tk.Button(self.master,text='1',font=('System',12),activebackground='green').place(x=250,y=120)
            self.btn2 = tk.Button(self.master,text='2',font=('System',12),activebackground='green').place(x=250,y=160)
            self.btn3 = tk.Button(self.master,text='3',font=('System',12),activebackground='green').place(x=250,y=200)
            self.btn4 = tk.Button(self.master,text='4',font=('System',12),activebackground='green').place(x=250,y=240)
            self.btn5 = tk.Button(self.master,text='5',font=('System',12),activebackground='green').place(x=250,y=280)
        else:
            self.btn1 = tk.Button(self.master,text='1',font=('System',12),activebackground='green').place(x=50,y=120)
            self.btn2 = tk.Button(self.master,text='2',font=('System',12),activebackground='green').place(x=50,y=160)
            self.btn3 = tk.Button(self.master,text='3',font=('System',12),activebackground='green').place(x=50,y=200)
            self.btn4 = tk.Button(self.master,text='4',font=('System',12),activebackground='green').place(x=50,y=240)
            self.btn5 = tk.Button(self.master,text='5',font=('System',12),activebackground='green').place(x=50,y=280)
    """
    def ayuda(self):
        pass
        #path = ''
        #os.system(path)

    def acercaDe(self):
        self.ventanaInfo = tk.Tk()
        self.ventanaInfo.geometry('800x300')
        self.ventanaInfo.title('Información del Programa')
        self.lblTitulo = tk.Label(self.ventanaInfo,text='FUTOSHIKI',fg='white',bg='red',font=('System',20)).pack(fill=tk.X) 
        Autor = tk.Label(self.ventanaInfo,text='Autor del Programa:',font=('Courier New',16,'bold')).place(x=0,y=60)
        nombreAutor = tk.Label(self.ventanaInfo,text='Kevin Vinicio Núñez Cruz',font=('Courier New',16)).place(x=300,y=60)
        programa = tk.Label(self.ventanaInfo,text='Nombre del Programa:',font=('Courier New',16,'bold')).place(x=0,y=90)
        nombrePrograma = tk.Label(self.ventanaInfo,text='Juego Futoshiki',font=('Courier New',16)).place(x=300,y=90)
        version = tk.Label(self.ventanaInfo,text='Versión:',font=("Courier New",16,'bold')).place(x=0,y=120)
        nombreVersion = tk.Label(self.ventanaInfo,text='Python 3.8.3',font=('Courier New',16)).place(x=300,y=120)
        creacion = tk.Label(self.ventanaInfo,text='Fecha de Creacion:',font=('Courier New',16,'bold')).place(x=0,y=150)
        fechaCreacion = tk.Label(self.ventanaInfo,text='12 de Junio del 2021',font=('Courier New',16)).place(x=300,y=150)

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