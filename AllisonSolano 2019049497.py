#Split: convertir las lineas del archivo a listas.      lista=lineaArchivo.split(':')
     
from tkinter import *
import tkinter as dt
from tkinter import ttk
from tkinter import messagebox
from io import open
import tkinter as tk
#-------------------------------------------------------------------------------------ventana
base = Tk()
base.title("Allison Solano Flores 2019049497")
base.geometry('1150x500')
base.configure(background='#a0ed12')
#------------------------------------------------------------------------------------Frames
caja1=Frame(base, bg= '#a0ed12')
caja1.grid()
caja2=Frame(base, bg= '#a0ed12')
caja2.grid()
caja3=Frame(base, bg='#a0ed12')
caja3.grid()
framebotones=Frame(base, bg='#a0ed12')
framebotones.place(x=20, y=400)
#---------------------------------------------------------------------------------Variables
caja1visible=False
caja2visible=False
caja3visible=False

#---------------------------------------------------------------------------------funciones

def informacionestudiante():
      '''
      Allison Solano Flores
      2019049497
      '''
      print ('help(funcion)')
#Treeview
tree =ttk.Treeview(base, selectmode='browse')


def on_selected(a):
      '''
      Retorna un diccionario con los elementos del archivo de texto
      @param a
      @type evento
      @devuelve los elementos del tree view en los entry
      
      '''
      curItem=tree.focus()
      #Retorna un diccionario con valores del treeview
      #La llave 'values' tiene los datos de la fila seleccionada
      valor=tree.item(curItem)
      print(valor)
      print(valor['values'])
      datos=valor['values']
      if caja1visible==True:
            codigo.delete(0,END)                #borra los datos en el entry
            codigo.insert(0,datos[0])           #le inserta lo que se le pongga
            nombrec.delete(0, END)
            nombrec.insert(0,datos[1])
            fecha=datos[2].split('.')           #le asigna a la varible fecha los valores de datos[2] separados por el backslash
            diac.delete(0,END)
            diac.insert(0,fecha[0])
            mesc.delete(0, END)
            mesc.insert(0,fecha[1])
            annoc.delete(0,END)
            annoc.insert(0, fecha[2])
      if caja2visible==True:
            combobox1.delete(0,END)
            combobox.insert(0,dato[0])
            datocarnet=datos[0].split('.')
            carnetanno.delete(0, END)
            carnetanoo.insert(0,datocarnet[1])
            carnet.delete(0,END)
            carnet.insert(0,datocarnet[2])
            datonombre=datos[2].split('.')
            nombre.delete(0,END)
            nombre.insert(0,datonombre[0])
            papellido.delete(0,END)
            papellido.insert(0,datonombre[1])
            sapellido.delete(0,END)
            sapellido.insert(0,datonombre[2])
            datoingreso=dato[3].split('.')
            diaingreso.delete(0, END)
            diaingreso.insert(0, datoingreso[0])
            mesingreso.delete(0, END)
            mesingreso.insert(0,datoingreso[1])
            annoingreso.delete(0,END)
            annoingreso.insert(0, datoingreso[2])
            estatura.delete(0,END)
            estatura.insert(0,datos[4])
            combobox.delete(0,END)
            combobox.insert(0,dato[5])
            
            
'''
      crea los treeviews de las diferentes pestannas
      @son llamados por el boton cargar
'''
            

      
def treeviews():
      '''
      Carga los datos del archivo de texto al treeview en pantalla
      @param archivo carreras
      @type .txt
      '''
      tree.place(x=450, y=50)
      listaCarreras=[]
      f = open ('carreras.txt','r')
      lineas = f.read().split('\n')
      f.close()
      #Toma todas las lineas del archivo como listas individuales
      for linea in lineas:
        #forma una lista con los datos de cada carrera
        #listaCarreras: Matriz (con la forma del treeview) donde están los datos de cada carrera
        #Cada fila de la matriz es [codigo,nombre,fechaCreacion]
        columnas = linea.split(',')
        if (len(columnas) == 3):
            listaCarreras.append(columnas)
            
      #Limpia lo que haya en el Treeview antes de ingresarle datos nuevos
      for item in tree.get_children():
        tree.delete(item)
      tag = 0

      #inserta las filas de la matriz 'listaCarreras' como filas del treeView
      for item in listaCarreras:
        tree.insert("",'end', iid = tag,values=item, tags=( tag % 2 ))        #################333
        tag += 1
      tree.bind('<<TreeviewSelect>>', on_selected) 
      
      tree["columns"] = ("1", "2", "3")
      tree['show'] = 'headings'
      tree.column("1", width=100, anchor='w')
      tree.column("2", width=200, anchor='w')
      tree.column("3", width=100, anchor='w')
      tree.heading("1", text="Código")
      tree.heading("2", text="Nombre")
      tree.heading("3", text="Fecha creación")


def treeviewestudiantes():
      '''
      Carga los datos del archivo de texto al treeview en pantalla
      @param archivo estudiantes
      @type .txt
      '''
      tree.place(x=450, y=50)
      listaCarreras=[]
      f = open ('estudiantes.txt','r')
      lineas = f.read().split('\n')
      f.close()
      #Toma todas las lineas del archivo como listas individuales
      for linea in lineas:
        #forma una lista con los datos de cada carrera
        #listaCarreras: Matriz (con la forma del treeview) donde están los datos de cada carrera
        #Cada fila de la matriz es [codigo,nombre,fechaCreacion]
        columnas = linea.split(',')
        if (len(columnas) == 8):
            listaCarreras.append(columnas)
            
      #Limpia lo que haya en el Treeview antes de ingresarle datos nuevos
      for item in tree.get_children():
        tree.delete(item)
      tag = 0

      #inserta las filas de la matriz 'listaCarreras' como filas del treeView
      for item in listaCarreras:
        tree.insert("",'end', iid = tag,values=item, tags=( tag % 2 ))
        tag += 1
        
      
      tree["columns"] = ("1", "2", "3", "4","5", "6", "7", "8")
      tree['show'] = 'headings'
      tree.column("1", width=50, anchor='w')
      tree.column("2", width=70, anchor='w')
      tree.column("3", width=120, anchor='w')
      tree.column("4", width=80, anchor='w')
      tree.column("5", width=100, anchor='w')
      tree.column("6", width=70, anchor='w')
      tree.column("7", width=90, anchor='w')
      tree.column("8", width=40, anchor='w')

      tree.heading("1", text="Carrera")
      tree.heading("2", text="Carnet")
      tree.heading("3", text="Nombre")
      tree.heading("4", text="Nacimiento")
      tree.heading("5", text="Ingr.carrera")
      tree.heading("6", text="estatura")
      tree.heading("7", text="provincia")
      tree.heading("8", text="Sexo")



def treeviewcursos():
      '''
      Carga los datos del archivo de texto al treeview en pantalla
      @param archivo ursos
      @type .txt
      '''
      tree.place(x=450, y=50)
      listaCarreras=[]
      f = open ('cursos.txt','r')
      lineas = f.read().split('\n')
      f.close()
      #Toma todas las lineas del archivo como listas individuales
      for linea in lineas:
        #forma una lista con los datos de cada carrera
        #listaCarreras: Matriz (con la forma del treeview) donde están los datos de cada carrera
        #Cada fila de la matriz es [carrera, codigo, nombre de curso...]
        columnas = linea.split(',')
        if (len(columnas) == 5):
            listaCarreras.append(columnas)
            
      #Limpia lo que haya en el Treeview antes de ingresarle datos nuevos
      for item in tree.get_children():
        tree.delete(item)
      tag = 0

      #inserta las filas de la matriz 'listaCarreras' como filas del treeView
      for item in listaCarreras:
        tree.insert("",'end', iid = tag,values=item, tags=( tag % 2 ))
        tag += 1
        
      
      tree["columns"] = ("1", "2", "3", "4","5", "6", "7", "8")
      tree['show'] = 'headings'
      tree.column("1", width=50, anchor='w')
      tree.column("2", width=40, anchor='w')
      tree.column("3", width=120, anchor='w')
      tree.column("4", width=40, anchor='w')
      tree.column("5", width=40, anchor='w')


      tree.heading("1", text="Carrera")
      tree.heading("2", text="codigo")
      tree.heading("3", text="Nombre")
      tree.heading("4", text="Semestre")
      tree.heading("5", text="Creditos")      


#-------------------------Funcion de ventana de Carreras
codigo      = Entry(caja1, width=2, font=('Agency FB', 12))
nombrec     = Entry(caja1, font=('Agency FB', 12))
fechaf      = Frame(caja1,bg= 'yellow')
diac        = Entry(fechaf, width=2, font=('Agency FB', 12))
mesc        = Entry(fechaf, width=2,font=('Agency FB', 12))
annoc       = Entry(fechaf, width=4,font=('Agency FB', 12))


def carreras():
      '''
      despliega los entry del menu carreras y remueve los que estan presentes
      @param menu que esta presente en la ventana
      @type frame
      @remueve los presentes y despliega carreras
      '''
      global caja1visible,caja2visible,caja3visible
      caja2.grid_remove()
      caja2visible=False
      caja3.grid_remove()
      caja3visible=False
      caja1.grid()
      caja1visible=True
      caja1.place(x=5, y=100)
      dt=Label(caja1, text='Código', bg="#a0ed12", font=('Agency FB', 15)).grid(row=1, column=1)  #está definiendo la etiqueta
      dt=Label(caja1, text='Nombre de la carrera', bg="#a0ed12", font=('Agency FB', 15)).grid(row=3, column=1)
      dt=Label(caja1, text='Fecha de creación', bg="#a0ed12", font=('Agency FB', 15)).grid(row=5, column=1)
      codigo.grid(row=1, column=3)
      nombrec.grid(row=3, column=3)
      #Width: Cambia el ancho del entry
      fechaf.place(x=250, y=60)
      diac.grid(row=1, column=1)
      mesc.grid(row=1, column=3)
      annoc.grid(row=1, column=5)

#--------------------------Funcion de ventana  de estudiantes
carnetframe = Frame(caja2,bg= '#a0ed12')
carnetanno  = Entry(carnetframe, width=4,font=('Agency FB', 12))
carnet      = Entry(carnetframe, width=6,font=('Agency FB', 12))
combobox1   = ttk.Combobox(caja2,values=('IC', 'AE'))
nombre      = Entry(caja2, font=('Agency FB', 12))
papellido   = Entry(caja2, font=('Agency FB', 12))
sapellido   = Entry(caja2, font=('Agency FB', 12))
ingreso     = Frame(caja2, bg= '#a0ed12')
diaingreso  = Entry(ingreso,width=2, font=('Agency FB', 12))
mesingreso  = Entry(ingreso,width=2, font=('Agency FB', 12))
annoingreso = Entry(ingreso,width=4, font=('Agency FB', 12))
estatura    = Entry(caja2, font=('Agency FB', 12))
fechae      = Frame(caja2,bg= 'yellow')
diae        = Entry(fechae, width=2, font=('Agency FB', 12))
mese        = Entry(fechae, width=2,font=('Agency FB', 12))
annoe       = Entry(fechae, width=4,font=('Agency FB', 12))
combobox    = ttk.Combobox(caja2,values=('San José','Alajuela', 'Cartago', 'Heredia', 'Puntarenas', 'Guanacaste', 'Limón'))
m           = IntVar()
f           = IntVar()


def estudiantes():
    '''
            despliega los entry del menu estudiantes y remueve los que estan presentes
            @param menu que esta presente en la ventana
            @type frame
            @remueve los presentes y despliega estudiantes
    '''
    global caja1visible,caja2visible,caja3visible
    caja1.grid_remove()
    caja1visible=False
    caja3.grid_remove()
    caja3visible=False
    caja2.grid()
    caja2visible=True
    dt=Label(caja2, text='Carrera', bg='#a0ed12', font=('Agency FB', 15)).grid(row=1, column=1)
    combobox1.grid(row=1, column=2)
    dt=Label(caja2, text='Carnet:', bg='#a0ed12', font=('Agency FB', 15)).grid(row=3, column=1)
    carnetframe.grid(row=3, column=2)
    carnetanno.grid(row=0, column=0)
    carnet.grid(row=0, column=1)
    dt=Label(caja2, text='Nombre:', bg='#a0ed12', font=('Agency FB', 15)).grid(row=4, column=1)
    nombre.grid(row=4,column=2)
    dt=Label(caja2, text='Primer apellido:', bg='#a0ed12', font=('Agency FB', 15)).grid(row=7, column=1)
    papellido.grid(row=7, column=2)
    dt=Label(caja2, text='Segundo apellido:', bg='#a0ed12', font=('Agency FB', 15)).grid(row=9, column=1)
    sapellido.grid(row=9, column=2)
    dt=Label(caja2, text='Fecha de nacimiento:', bg='#a0ed12', font=('Agency FB', 15)).grid(row=11, column=1)
    fechae.place(x=250, y=150)
    diae.grid(row=1, column=1)
    mese.grid(row=1, column=3)
    annoe.grid(row=1, column=5)
    dt=Label(caja2, text=' Ingreso a la carrera:', bg='#a0ed12', font=('Agency FB', 15)).grid(row=13, column=1)
    ingreso.grid(row=13, column=2)
    diaingreso.grid(row=1, column=1)
    mesingreso.grid(row=1, column=2)
    annoingreso.grid(row=1,column=3)
    dt=Label(caja2, text='Estatura:', bg='#a0ed12', font=('Agency FB', 15)).grid(row=14, column=1)
    estatura.grid(row=14, column=2)
    dt=Label(caja2, text='Provincia', bg='#a0ed12', font=('Agency FB', 15)).grid(row=15, column=1)
    combobox.grid(row=15, column=2)
    rb1 = Radiobutton(caja2, text='F', variable=f,  value=1, bg='#a0ed12', font=('Agency FB', 15)).grid(row=15, column=7)
    rb2 =Radiobutton(caja2, text='M', variable=m, value=2, bg='#a0ed12', font=('Agency FB', 15)).grid(row=14, column=7)

#-----------------------------------------funcion de ventana de cursos
combobox2   = ttk.Combobox(caja3,values=('IC. Ingeniería en Computación', 'AE'))
codigoc     = Entry(caja3, width=2, font=('Agency FB', 12))
nombrecurso = Entry(caja3, font=('Agency FB', 12))
combobox3   = ttk.Combobox(caja3,values=('1','2','3','4','5','6','7','8','9','10'))
uno         = IntVar()
dos         = IntVar()
tres        = IntVar()
cuatro      = IntVar()
ninguno     = IntVar()



def cursos():
    '''
      despliega los entry del menu cursos y remueve los que estan presentes
            @param menu que esta presente en la ventana
            @type frame
            @remueve los presentes y despliega cursos
    '''    
    global caja1visible,caja2visible,caja3visible
    caja1.grid_remove()
    caja1visible=False
    caja2.grid_remove()
    caja2visible=False
    caja3.grid()
    caja3visible=True
    dt=Label(caja3, text='Carrera', bg='#a0ed12', font=('Agency FB', 15)).grid(row=1, column=1)
    combobox2.grid(row=1, column=2)
    dt=Label(caja3, text='Código:', bg='#a0ed12', font=('Agency FB', 15)).grid(row=2, column=1)
    codigoc.grid(row=2, column=2)
    dt=Label(caja3, text='Nombre curso:', bg='#a0ed12', font=('Agency FB', 15)).grid(row=3, column=1)
    nombrecurso.grid(row=3, column=2)
    dt=Label(caja3, text='Semestre', bg='#a0ed12', font=('Agency FB', 15)).grid(row=4, column=1)
    combobox3.grid(row=4, column=2)
    dt=Label(caja3, text='Créditos', bg='#a0ed12', font=('Agency FB', 15)).grid(row=5, column=1)
    rb1 = Radiobutton(caja3, text='1', variable=uno,  value=1, bg='#a0ed12', font=('Agency FB', 15))
    rb1.grid(row=5, column=2)
    rb2 =Radiobutton(caja3, text='2', variable=dos, value=2, bg='#a0ed12', font=('Agency FB', 15)) 
    rb2.grid(row=6, column=2)
    rb3 =Radiobutton(caja3, text='3', variable=tres, value=3, bg='#a0ed12', font=('Agency FB', 15)) 
    rb3.grid(row=7, column=2)
    rb4 =Radiobutton(caja3, text='4', variable=cuatro, value=4, bg='#a0ed12', font=('Agency FB', 15)) 
    rb4.grid(row=8, column=2)
    rbn =Radiobutton(caja3, text='ninguno', variable=ninguno, value=5, bg='#a0ed12', font=('Agency FB', 15))
    rbn.grid(row=9, column=2)

#------------------------------------------------------------Validaciones
#validacion de entry codigo de carreras

'''
            Valida los codigos de los entry 
            @param codigo
            @type string
            @param nombre
            @type string
            return valid true or false
'''

def validaCodigo(codigo, nombre):
      valid = (codigo.isalpha() and codigo.isupper()and nombre.isalpha())
      if (valid):
            valid=True
      else:
            valid=False
            print('codigo o nombre invalido')
            labelinformativo('codigo o nombre invalido')
      return valid

#validacion de fechas

'''
            Valida la fecha de los entry 
            @param mes
            @type int
            @param dia
            @type int
            return valid true or false
'''

diasPorMes=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def validaMes(mes,entryDia):
    """
    Valida el mes de la fecha de creacion de la carrera.
    @param mes mes del anno
    @type mes 0 .. 12
    @return valid True si el mes digitado es Ok.
    @rtype valid boolean
    """
    valid = ((len(mes) == 1) and mes.isdigit() and entryDia.isdigit()) or \
    ((len(mes) == 2) and mes.isdigit() and (int(mes) > 0) and (int(mes) <= 12)and entryDia.isdigit())

    if (valid and (diasPorMes[ int(mes) ] >= int(entryDia))):
        valid=True;
    else:
        valid = False 
        print("Dia invalido.")
        labelinformativo('dia invalido')
    return valid


'''
            Valida los annos de los entry mayores a 1970 
            @param anno
            @type int
            return valid true or false
'''

def validaAnno(anno):
    """
    Valida el anno de la fecha de creacion de la carrera
    @param anno
    @type anno > 1970
    @return valid True si el anno digitado es Ok
    @rtype valid boolean
    """
    valid = ((len(anno) == 4) and (int(anno)) > 1970)
    if (valid and((len(anno) == 4) and (int(anno)) > 1970)):
        valid=True
    if(valid == False):
          print("anno invalido.")
          labelinformativo('anno invalido')
    return valid



#validacion de fecha de nacimiento e ingreso a la carrera en estudiantes
def validaMese(mes,entryDia):
    """
    Valida el mes de la fecha de creacion de la carrera.
    @param mes mes del anno
    @type mes 0 .. 12
    @return valid True si el mes digitado es Ok.
    @rtype valid boolean
    """
    valid = ((len(mes) == 1) and mes.isdigit() and entryDia.isdigit()) or \
    ((len(mes) == 2) and mes.isdigit() and (int(mes) > 0) and (int(mes) <= 12)and entryDia.isdigit())

    if (valid and (diasPorMes[ int(mes) ] >= int(entryDia))):
        valid=True;
    else:
        valid = False 
        print("fechas invalidas.")
        labelinformativo('fechas invalidas')
    return valid

def validaAnnoe(anno):
    """
    Valida el anno de la fecha de nacimiento e ingreso a la carrera
    @param anno
    @type anno > 2000
    @return valid True si el anno digitado es Ok
    @rtype valid boolean
    """
    valid = ((len(anno) == 4) and (int(anno)) > 2000)
    if (valid and((len(anno) == 4) and (int(anno)) > 2000)):
        valid=True
    if(valid == False):
          print("fechas invalidas.")
          labelinformativo('fechas invalidas')
    return valid

#validacion de carnet en estudiantes

def validaCarnet(anno, resto):
      valid=(len(anno)== 4 and (int(anno)>2000)and anno.isdigit()and len(resto)== 6 and resto.isdigit())
      if valid:
            valid= True
      else:
            valid= False
            print('carnet invalido')
            labelinformativo('Carnet invalido')
      return valid


#--------------------Funciones de botones
#entra a carreras pero no a las otras. con estudiantes suele guardar lo de carreras

def insertar():
      global caja1visible, caja2visible, caja3visible
      if (caja1visible==True):      #frame de carreras visible
            if(validaCodigo(codigo.get(), nombrec.get()) and validaAnno(annoc.get()) and validaMes(mesc.get(),diac.get())): 
                  archivo=open('carreras.txt', 'a')
                  archivocarrera=codigo.get()+","+ nombrec.get()+","+diac.get()+"/"+ mesc.get()+"/"+annoc.get()
                  #Hacer que no lo guarde si valid = False
                  archivo.write(str(archivocarrera))
                  archivo.write('\n')
                  archivo.close()
                  labelinformativo('informacion guardada')
                  treeviews()
            
      if (caja2visible==True):
            if validaCarnet(carnetanno.get(), carnet.get()) and validaAnnoe(annoe.get()) and validaMese(mese.get(),diae.get()):
                  archivo=open('estudiantes.txt', 'a')
                  if m.get()==1:
                        archivoestudiantes=combobox1.get()+','+carnetanno.get() +'.'+ carnet.get()+','+nombre.get()+'.'+\
                                            papellido.get()+'.'+sapellido.get()+','+ diaingreso.get()\
                                            +'.'+mesingreso.get()+'.'+anooingreso.get()+','+\
                                            diae.get()+ mese.get()+ annoe.get()+','+estatura.get()+','\
                                            +combobox.get()+',M'
                  else:
                        archivoestudiantes=combobox1.get()+','+carnetanno.get() +'.'+ carnet.get()+','+nombre.get()+'.'\
                                      + papellido.get()+'.'+sapellido.get()+','+ diaingreso.get()\
                                      +'.'+mesingreso.get()+'.'+annoingreso.get()+','+\
                                      diae.get()+ mese.get()+ annoe.get()+','+estatura.get()+','\
                                      +combobox.get()+','+'F'                
                  archivo.write(str(archivoestudiantes))
                  archivo.write('\n')
                  archivo.close()
                  labelinformativo('informacion guardada')
                  treeviewestudiantes()
            
      if(caja3visible==True):
            if validaCodigo(codigoc.get(),nombrecurso.get()):
                  archivo=open('cursos.txt', 'a')
                  if uno.get()==1:
                        archivocursos=combobox2.get()+','+codigoc.get()+','+nombrecurso.get()\
                                       +','+combobox3.get()+','+ ',1'
                  if dos.get() == 1:
                        archivocursos=combobox2.get()+','+codigoc.get()+','+nombrecurso.get()\
                                       +','+combobox3.get()+','+ ',2'
                  if tres.get() == 1:
                        archivocursos=combobox2.get()+','+codigoc.get()+','+nombrecurso.get()\
                                       +','+combobox3.get()+','+ ',3'
                  if cuatro.get() == 1:
                        archivocursos=combobox2.get()+','+codigoc.get()+','+nombrecurso.get()\
                                       +','+combobox3.get()+','+ ',4'
                  else:
                        archivocursos=combobox2.get()+','+codigoc.get()+','+nombrecurso.get()\
                                       +','+combobox3.get()+','+"ninguno"
            archivo.write(str(archivocursos))
            archivo.write('\n')
            archivo.close()
            labelinformativo('informacion guardada')
#---------------------------------------------------Boton que carga la lista
def cargalista():
      if caja1visible==True:
            treeviews()
      if caja2visible==True:
            treeviewestudiantes()
      if caja3visible == True:
            treeviewcursos()
      
def acerca():
    messagebox.showinfo('Acerca de', 'Allison Solano Flores 2019049497')


    


#-----------------------------------------------------------------------------------Simulacion
matrizmama=[]


def juegobotones():
      ##Genera la matriz de números
      global matrizmama
      x=10
      y=10
      matrizfilas=[]
      simulacion = Tk()
      for i in range(30):
            matriznumeros=[]
            for j in range(30):
                  if ((matrizmama[i][j])==1):
                        viva = Button(simulacion,text='  ',bg='#a0ed12').place(x=x,y=y)
                        x+=35
                        matriznumeros.append(viva)
                  else:
                        viva = Button(simulacion, text='  ',bg='#c40d03').place(x=x,y=y)
                        matriznumeros.append(viva)
                        x+=35
            matrizfilas.append(matriznumeros)
            y+=35
            x=8
def juego():
      ##Genera la matriz de números
      for i in range(30):
            matriznumeros=[]
            for j in range(30):
                  matriznumeros.append(0)
            matrizmama.append(matriznumeros)
      
      archivovivas= open ('celulasvivas.txt','r')
      vivas =archivovivas.read().split('\n')
      archivovivas.close()

      for i in vivas:
            linea= i.split(':')
            for j in linea:
                  punto =j.split(',')
                  x =int(punto[0])
                  y =int(punto[1])
                  matrizmama[x][y] = 1
      juegobotones()


'''
            determina cuantas celulas vivas tiene alrededor
            @param matrizmama
            con el contador se determina si la celula muere o vive
            @return celula viva o muerta
'''

def preguntas():
      global matrizmama
      for i in range(30):
            for j in range (30):
                  if matrizmama[i][j] == 0:
                        if i==0 and j==0:
                              cont=0
                              if matrizmama[i][j+1]==1:
                                    cont+=1
                              if matrizmama[i+1][j+1]==1:
                                    cont+=1
                              if matrizmama[i+1][j]:
                                    cont+=1
                              if cont == 3:
                                    matrizmama[i][j]=1
                                    
                        elif i==29 and j==0:      #Esquina inferior izquierda
                              cont=0
                              if matrizmama[i-1][j]==1:
                                    cont +=1

                              if matrizmama[i-1][j+1]==1:
                                    cont+=1

                              if matrizmama[i][j+1]==1:
                                    cont+=1
                              if cont==3:
                                    matrizmama[i][j]=1

                        
                        elif i==0 and j==29:          #esquina superior derecha
                              cont=0
                              if matrizmama[i][j-1]==1:
                                    cont +=1

                              if matrizmama[i+1][j-1]==1:
                                    cont+=1

                              if matrizmama[i+1][j]==1:
                                    cont+=1
                                    
                              if cont==3:
                                    matrizmama[i][j]=1



                        elif i==29 and j==29:         #esquina inferior derecha
                              cont=0
                              if matrizmama[i-1][j]==1:
                                    cont +=1

                              if matrizmama[i-1][j-1]==1:
                                    cont+=1

                              if matrizmama[i][j-1]==1:
                                    cont+=1
                              if cont==3:
                                    matrizmama[i][j]=1

                        elif i==0 :                   #borde superior
                              cont=0
                              if matrizmama[i][j-1]==1:
                                    cont +=1

                              if matrizmama[i+1][j-1]==1:
                                    cont+=1

                              if matrizmama[i+1][j]==1:
                                    cont+=1

                              if matrizmama[i+1][j+1]==1:
                                    cont+=1
                              if matrizmama[i][j+1]==1:
                                    cont+=1
                              if cont >=3:
                                    matrizmama[i][j]=1
                              



                        elif i==29:                   #borde inferior
                              cont=0
                              if matrizmama[i][j-1]==1:
                                    cont +=1

                              if matrizmama[i-1][j-1]==1:
                                    cont+=1

                              if matrizmama[i-1][j]==1:
                                    cont+=1

                              if matrizmama[i-1][j+1]==1:
                                    cont+=1
                                    
                              if matrizmama[i][j+1]==1:
                                    cont+=1
                                    
                              if cont >=3:
                                    matrizmama[i][j]=1


                        elif j==29:                    #borde derecho
                              cont=0
                              if matrizmama[i+1][j]==1:
                                    cont +=1

                              if matrizmama[i+1][j-1]==1:
                                    cont+=1

                              if matrizmama[i][j-1]==1:
                                    cont+=1

                              if matrizmama[i-1][j-1]==1:
                                    cont+=1
                              if matrizmama[i-1][j]==1:
                                    cont+=1
                              if cont >=3:
                                    matrizmama[i][j]=1

                        elif j==0:                   #borde izquierdo
                              cont=0
                              if matrizmama[i-1][j]==1:
                                    cont +=1

                              if matrizmama[i-1][j+1]==1:
                                    cont+=1

                              if matrizmama[i][j+1]==1:
                                    cont+=1

                              if matrizmama[i+1][j+1]==1:
                                    cont+=1
                              if matrizmama[i+1][j]==1:
                                    cont+=1
                              if cont >=3:
                                    matrizmama[i][j]=1
                        else:
                              cont=0
                              if matrizmama[i-1][j-1]==1:
                                    cont +=1

                              if matrizmama[i-1][j]==1:
                                    cont+=1

                              if matrizmama[i-1][j+1]==1:
                                    cont+=1

                              if matrizmama[i][j-1]==1:
                                    cont+=1
                              if matrizmama[i][j+1]==1:
                                    cont+=1
                              if matrizmama[i+1][j-1]==1:
                                    cont+=1
                              if matrizmama[i+1][j]==1:
                                    cont+=1
                              if matrizmama[i+1][j+1]==1:
                                    cont+=1
                              if cont >=3:
                                    matrizmama[i][j]=1
                                    
                  else: #celulas vivitas y coleando
                        if i==0 and j==0:
                              cont=0
                              if matrizmama[i][j+1]==1:
                                    cont+=1
                              if matrizmama[i+1][j+1]==1:
                                    cont+=1
                              if matrizmama[i+1][j]:
                                    cont+=1
                              if cont == 0 or cont ==1:
                                    matrizmama[i][j]=0
                              if cont>=4:
                                    matrizmama[i][j]=0
                                    
                        elif i==29 and j==0:      #Esquina inferior izquierda
                              cont=0
                              if matrizmama[i-1][j]==1:
                                    cont +=1

                              if matrizmama[i-1][j+1]==1:
                                    cont+=1

                              if matrizmama[i][j+1]==1:
                                    cont+=1
      
                              if cont == 0 or cont ==1:
                                    matrizmama[i][j]=0
                              if cont>=4:
                                    matrizmama[i][j]=0
                              
                        elif i==0 and j==29:          #esquina superior derecha
                              cont=0
                              if matrizmama[i][j-1]==1:
                                    cont +=1

                              if matrizmama[i+1][j-1]==1:
                                    cont+=1

                              if matrizmama[i+1][j]==1:
                                    cont+=1
                                    
                              if cont == 0 or cont ==1:
                                    matrizmama[i][j]=0
                              if cont>=4:
                                    matrizmama[i][j]=0

                        elif i==29 and j==29:         #esquina inferior derecha
                              cont=0
                              if matrizmama[i-1][j]==1:
                                    cont +=1

                              if matrizmama[i-1][j-1]==1:
                                    cont+=1

                              if matrizmama[i][j-1]==1:
                                    cont+=1
                              if cont == 0 or cont ==1:
                                    matrizmama[i][j]=0
                              if cont>=4:
                                    matrizmama[i][j]=0

                        elif i==0 :                   #borde superior
                              cont=0
                              if matrizmama[i][j-1]==1:
                                    cont +=1

                              if matrizmama[i+1][j-1]==1:
                                    cont+=1

                              if matrizmama[i+1][j]==1:
                                    cont+=1

                              if matrizmama[i+1][j+1]==1:
                                    cont+=1
                              if matrizmama[i][j+1]==1:
                                    cont+=1
                              if cont == 0 or cont ==1:
                                    matrizmama[i][j]=0
                              if cont>=4:
                                    matrizmama[i][j]=0
                              

                        elif i==29:                   #borde inferior
                              cont=0
                              if matrizmama[i][j-1]==1:
                                    cont +=1

                              if matrizmama[i-1][j-1]==1:
                                    cont+=1

                              if matrizmama[i-1][j]==1:
                                    cont+=1

                              if matrizmama[i-1][j+1]==1:
                                    cont+=1
                                    
                              if matrizmama[i][j+1]==1:
                                    cont+=1
                                    
                              if cont == 0 or cont ==1:
                                    matrizmama[i][j]=0
                              if cont>=4:
                                    matrizmama[i][j]=0
                              

                        elif j==29:                    #borde derecho
                              cont=0
                              if matrizmama[i+1][j]==1:
                                    cont +=1

                              if matrizmama[i+1][j-1]==1:
                                    cont+=1

                              if matrizmama[i][j-1]==1:
                                    cont+=1

                              if matrizmama[i-1][j-1]==1:
                                    cont+=1
                              if matrizmama[i-1][j]==1:
                                    cont+=1
                              if cont == 0 or cont ==1:
                                    matrizmama[i][j]=0
                              if cont>=4:
                                    matrizmama[i][j]=0

                        elif j==0:                   #borde izquierdo
                              cont=0
                              if matrizmama[i-1][j]==1:
                                    cont +=1

                              if matrizmama[i-1][j+1]==1:
                                    cont+=1

                              if matrizmama[i][j+1]==1:
                                    cont+=1

                              if matrizmama[i+1][j+1]==1:
                                    cont+=1
                              if matrizmama[i+1][j]==1:
                                    cont+=1
                              if cont == 0 or cont ==1:
                                    matrizmama[i][j]=0
                              if cont>=4:
                                    matrizmama[i][j]=0
                        else:
                              cont=0
                              if matrizmama[i-1][j-1]==1:
                                    cont +=1

                              if matrizmama[i-1][j]==1:
                                    cont+=1

                              if matrizmama[i-1][j+1]==1:
                                    cont+=1

                              if matrizmama[i][j-1]==1:
                                    cont+=1
                              if matrizmama[i][j+1]==1:
                                    cont+=1
                              if matrizmama[i+1][j-1]==1:
                                    cont+=1
                              if matrizmama[i+1][j]==1:
                                    cont+=1
                              if matrizmama[i+1][j+1]==1:
                                    cont+=1
                              if cont == 0 or cont ==1:
                                    matrizmama[i][j]=0
                              if cont>=4:
                                    matrizmama[i][j]=0
      juegobotones()

'''
            Creacion del menu principal y los submenud
'''
#-------------------------------------------------------------------------------------Menú
barramenu = Menu(base )        #Barras de menu
base.config(menu = barramenu)     #Indicamos que la barra de menú estará en la ventana
#-------------------------------------------------------------------------------------Menus y comandos
catalogoMenu= Menu(barramenu)       #menu catalogos
catalogoMenu.add_command(label= "Carreras", command=carreras)     #Comandos de menu
catalogoMenu.add_command(label="Estudiantes", command=estudiantes)
catalogoMenu.add_command(label="Cursos", command=cursos)
simulacionM=Menu(barramenu)     #menu simulacion
simulacionM.add_command(label="Abrir", command=juego)
simulacionM.add_command(label="Generacion",command=preguntas)
mas=Menu(barramenu)
mas.add_command(label="Salir", command=base.destroy)
mas.add_command(label="Acerca de", command=acerca)
#--------------------------------------------------------------------------------Agregar menus a la barra
barramenu.add_cascade(label= "Catálogos", menu= catalogoMenu)
barramenu.add_cascade(label="Simulación", menu=simulacionM)
barramenu.add_cascade(label="Más", menu=mas)
#----------------------------------------------------------------------------------Campo de texto informativo
def labelinformativo(informacion):
    info=Label(base, text=informacion, font=('Agency FB', 15), bg='#a0ed12').place(x=130, y=450)
#-----------------------------------------------------------------------------Botones
for i in range(0,200):
    base.columnconfigure(i, weight=1)
    base.rowconfigure(i, weight=1)
imgBoton=PhotoImage(file='insertar.gif')
insertar=Button(framebotones, image=imgBoton, command=insertar, bg='#a0ed12', relief='flat').grid(row=0, column=0)
imgBoton2=PhotoImage(file='modificar.gif')
insertar=Button(framebotones, image=imgBoton2,bg='#a0ed12', relief='flat').grid(row=0, column=1)
imgBoton3=PhotoImage(file='borrar.gif')
insertar=Button(framebotones, image=imgBoton3, bg='#a0ed12', relief='flat').grid(row=0, column=2)
imgBoton4=PhotoImage(file='cargar.gif')
insertar=Button(framebotones, image=imgBoton4, command=cargalista, bg='#a0ed12', relief='flat').grid(row=0, column=3)
imgBoton5=PhotoImage(file='primero.gif')
insertar=Button(framebotones, image=imgBoton5, bg='#a0ed12', relief='flat').grid(row=0, column=4)
imgBoton6=PhotoImage(file='anterior.gif')
insertar=Button(framebotones, image=imgBoton6, bg='#a0ed12', relief='flat').grid(row=0, column=5)
imgBoton7=PhotoImage(file='siguiente.gif')
insertar=Button(framebotones, image=imgBoton7, bg='#a0ed12', relief='flat').grid(row=0, column=6)
imgBoton8=PhotoImage(file='ultimo.gif')
insertar=Button(framebotones, image=imgBoton8, bg='#a0ed12', relief='flat').grid(row=0, column=7)
base.mainloop()
