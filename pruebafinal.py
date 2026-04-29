import tkinter as tk
from tkinter import *
from os import path
import random
import json

ventana=tk.Tk()
ventana.title("PokeTec")
ventana.minsize(1200,700)
ventana.resizable(width=NO, height=NO)


vida = 100
vida_op = 100
ataque = 0
defensa = 0
ataque_op = 0
defensa_op = 0
vida_pokemones={}

def mostrar_frame(frame):
    frame.tkraise()
    boton_inicio.config(state="disabled")
    siguiente2.config(state="disabled")


fuente= ('Times New Roman',20)
mensaje="¡Bienvenido a PokeTEC!"

def cargar_img(nombre):
    ruta  = path.join('imagenes', nombre) 
    img = PhotoImage(file=ruta)         
    return img



pagina1=tk.Frame(ventana,bg="gray")
pagina2=tk.Frame(ventana,bg="gray")
pagina3=tk.Frame(ventana,bg="gray")


for frame in (pagina1,pagina2,pagina3):
    frame.grid(row=0, column=0, sticky="nsew")

#Pagina1

canvas1=Canvas(pagina1,width=2000,height=700,bg='pink')
canvas1.place(x=10,y=10)

introduccion=Label(canvas1,text=mensaje, font=('Times New Roman',40), bg='#A8D68B', fg='black')
introduccion.place(x=50,y=100)

nombre1=Label(canvas1,text="Para continuar, ingrese su nombre", font=('Times New Roman',20), bg="#A8D68B", fg='black')
nombre1.place(x=120,y=250)


canvas1.fondo = cargar_img('grookey.png')

Fondo1 = canvas1.create_image(0, 0, anchor=NW,  image=canvas1.fondo)

nombre=Entry(pagina1,width=10,font=fuente)
nombre.place(x=230,y=350)

siguiente=tk.Button(pagina1, text="Siguiente", command=lambda: mostrar_frame(pagina2),width=12, height=2)
siguiente.place(x=260,y=450)
 
def mostrar_nombre():
    global nombre
    info_nombre=nombre.get()
    print(info_nombre)



#Pagina 2
canvas2=Canvas(pagina2,width=2000,height=700,bg='#A8D68B')
canvas2.place(x=10,y=10)

introduccion2=Label(canvas2,text="Elige al entrenador que más te guste", font=('Times New Roman',30), bg='#A8D68B', fg='black')
introduccion2.place(x=50,y=20)

siguiente2=tk.Button(pagina2, text="Siguiente", command=lambda: mostrar_frame(pagina3),width=12, height=2)
siguiente2.place(x=1000,y=620)

canvas2.hood= cargar_img("sprite_0.png")
jason=canvas2.create_image(5,40, anchor=NW, image= canvas2.hood)

canvas2.matt= cargar_img("matt.png")
daredevil=canvas2.create_image(220,100, anchor=NW, image= canvas2.matt)

canvas2.star= cargar_img("prueba.png")
kori=canvas2.create_image(450,130, anchor=NW, image= canvas2.star)

canvas2.dr= cargar_img("senku2.png")
ishi=canvas2.create_image(650,150, anchor=NW, image= canvas2.dr)

canvas2.robin= cargar_img("robin.png")
ro=canvas2.create_image(830,50, anchor=NW, image= canvas2.robin)


entrenador=IntVar()


entrenador1=Radiobutton(pagina2, text="Jasosn", variable=entrenador, value=1)
entrenador2=Radiobutton(pagina2, text="Matt", variable=entrenador, value=2)
entrenador3=Radiobutton(pagina2, text="Starfire", variable=entrenador, value=3)
entrenador4=Radiobutton(pagina2, text="Senku", variable=entrenador, value=4)
entrenador5=Radiobutton(pagina2, text="Robin", variable=entrenador, value=5)


entrenador1.place(x=100,y=480)
entrenador2.place(x=330,y=480)
entrenador3.place(x=570,y=480)
entrenador4.place(x=780,y=480)
entrenador5.place(x=1000,y=480)
opcion_entrenador=None

def elegir_entrenador():
    global opcion_entrenador
    opcion_entrenador=entrenador.get()
    print(opcion_entrenador)
    siguiente2.config(state=("normal"))
    

seleccion=Button(pagina2, text= "seleccionar", command= elegir_entrenador, width=12, height=2)
seleccion.place(x=520,y=550)



#Pagina 3
canvas3=Canvas(pagina3,width=2000,height=700,bg='#A8D68B')
canvas3.place(x=10,y=10)

introduccion3=Label(canvas3,text="Elige 3 pokemones", font=('Times New Roman',30), bg='#A8D68B', fg='black')
introduccion3.place(x=50,y=20)

siguiente3=tk.Button(pagina3, text="volver", command=lambda: mostrar_frame(pagina1),width=12, height=2)
siguiente3.place(x=900,y=640)

canvas3.perry=cargar_img("123.png")
perry= canvas3.create_image(200,90, anchor=NW, image=canvas3.perry)

canvas3.bicho=cargar_img("pok2.png")
perry= canvas3.create_image(200,190, anchor=NW, image=canvas3.bicho)

canvas3.cangrejo=cargar_img("poke3.png")
perry= canvas3.create_image(200,290, anchor=NW, image=canvas3.cangrejo)

canvas3.chopper=cargar_img("poke4.png")
perry= canvas3.create_image(200,390, anchor=NW, image=canvas3.chopper)

canvas3.cisne=cargar_img("pok5.png")
perry= canvas3.create_image(200,490, anchor=NW, image=canvas3.cisne)

canvas3.drax=cargar_img("pok6.png")
perry= canvas3.create_image(850,90, anchor=NW, image=canvas3.drax)

canvas3.ping=cargar_img("pok7.png")
perry= canvas3.create_image(850,190, anchor=NW, image=canvas3.ping)

canvas3.tig=cargar_img("pok8.png")
perry= canvas3.create_image(850,290, anchor=NW, image=canvas3.tig)

canvas3.tortuga=cargar_img("pok9.png")
perry= canvas3.create_image(850,390, anchor=NW, image=canvas3.tortuga)

canvas3.zorro=cargar_img("pok10.png")
perry= canvas3.create_image(850,490, anchor=NW, image=canvas3.zorro)
Pokemon1 = tk.IntVar()
Pokemon2 = tk.IntVar()
Pokemon3 = tk.IntVar()
Pokemon4 = tk.IntVar()
Pokemon5 = tk.IntVar()
Pokemon6 = tk.IntVar()
Pokemon7 = tk.IntVar()
Pokemon8 = tk.IntVar()
Pokemon9 = tk.IntVar()
Pokemon10 = tk.IntVar()



opcion1 = tk.Checkbutton(pagina3, text="Perry", variable=Pokemon1)
opcion2= tk.Checkbutton(pagina3, text="Kal", variable=Pokemon2)
opcion3 = tk.Checkbutton(pagina3, text="Sebastian", variable=Pokemon3)
opcion4 = tk.Checkbutton(pagina3, text="Chopper", variable=Pokemon4)
opcion5 = tk.Checkbutton(pagina3, text="Odette", variable=Pokemon5)
opcion6 = tk.Checkbutton(pagina3, text="Drax", variable=Pokemon6)
opcion7 = tk.Checkbutton(pagina3, text="Oswald", variable=Pokemon7)
opcion8 = tk.Checkbutton(pagina3, text="Mowgli", variable=Pokemon8)
opcion9 = tk.Checkbutton(pagina3, text="Donatello", variable=Pokemon9)
opcion10 = tk.Checkbutton(pagina3, text="Nick", variable=Pokemon10)

opcion1.place(x=100,y=150)
opcion2.place(x=100,y=250)
opcion3.place(x=100,y=350)
opcion4.place(x=100,y=450)
opcion5.place(x=100,y=550)
opcion6.place(x=700,y=150)
opcion7.place(x=700,y=250)
opcion8.place(x=700,y=350)
opcion9.place(x=700,y=450)
opcion10.place(x=700,y=550)

seleccionadas = []



def guardar():
    global seleccionadas, vida, vida_pokemones
    seleccionadas.clear()
    
    if Pokemon1.get() == 1:
        seleccionadas.append("Perry")
    if Pokemon2.get() == 1:
        seleccionadas.append("Kal")
    if Pokemon3.get() == 1:
        seleccionadas.append("Sebastian")
    if Pokemon4.get()==1:
        seleccionadas.append("Chopper")
    if Pokemon5.get()==1:
        seleccionadas.append("Odette")
    if Pokemon6.get()==1:
        seleccionadas.append("Drax")
    if Pokemon7.get()==1:
        seleccionadas.append("Oswald")
    if Pokemon8.get()==1:
        seleccionadas.append("Mowgli")
    if Pokemon9.get()==1:
        seleccionadas.append("Donatello")
    if Pokemon10.get()==1:
        seleccionadas.append("Nick")
    for pokemon in seleccionadas:
        vida=vida_pokemones[pokemon]=100


    boton_inicio.config(state="normal")

boton_guardar = Button(pagina3, text="Guardar Pokemon", command=guardar,width=12, height=2)
boton_guardar.place(x=550, y=620)
    
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)
pokemon_inicial=None
def abrir_ventana():
    global opcion_entrenador,vida, vida_op, ataque, defensa, ataque_op, defensa_op, disponibles, pokemon_inicial,pokemon_op_inicial,pokemones_oponente, puntaje1, vida_pokemones, puntaje2, vida_pokemones_oponente
    ventana2=tk.Toplevel(ventana)
    ventana2.minsize(1200,700)
    ventana2.resizable(width=NO,height=NO)

    pantalla1 = tk.Frame(ventana2, bg="gray")
    pantalla2 = tk.Frame(ventana2, bg="gray")
    pantalla3=tk.Frame(ventana2, bg="#A8D68B")
    fin=Label(pantalla3, text="Mejores Puntajes", font=("Times New Roman",30), bg="gray", fg="black")
    fin.place(x=470,y=0)
    

    for frame2 in (pantalla1, pantalla2, pantalla3):
        frame2.grid(row=0, column=0, sticky="nsew")
    ventana2.grid_rowconfigure(0, weight=1)
    ventana2.grid_columnconfigure(0, weight=1)
    def mostrar_pantalla(frame):
        frame.tkraise()
        if frame==pantalla3:
            mostrar_puntaje()

    

    def siguiente(frame):
        frame.tkraise()
        ataque1.config(state="normal")
        defensa1.config(state="normal")
        continuar3.config(state="disabled")
        cambiar_label2("Inicia combate")

    ARCHIVO="puntajes.json"

    def cargar_puntos():
        if path.exists(ARCHIVO):
            with open(ARCHIVO, "r") as puntos_finales:
                return json.load(puntos_finales)
        return []

    def guardar_puntos(datos):
        with open(ARCHIVO, "w") as puntaje:
            json.dump(datos, puntaje, indent=4)

    fotos_entrenadores = {1: cargar_img("jason.png"),
        2: cargar_img("icono.png"),
        3: cargar_img("star.png"),
        4: cargar_img("iconos.png"),
        5: cargar_img("icono2.png")}
    
    def guardar_resultado(nombre_jugador, puntos, entrenador_id):
            datos = cargar_puntos()

            datos.append({
                "nombre": nombre_jugador,
                "puntos": puntos,
                "entrenador": entrenador_id
            })

            datos = sorted(datos, key=lambda x: x["puntos"], reverse=True)

            guardar_puntos(datos)
    
    
    tabla = Frame(pantalla3, bg="white", width=500, height=600)
    tabla.place(x=500, y=100)

    def mostrar_puntaje():
        for widget in tabla.winfo_children():
            widget.destroy()

        datos = cargar_puntos()

        for i, jugador in enumerate(datos[:10]):
            img = fotos_entrenadores.get(jugador["entrenador"])

            linea = Label(tabla,
                image=img,
                compound="left",
                text=f"  {i+1}. {jugador['nombre']} - {jugador['puntos']}",
                bg="white",
                font=("Times New Roman", 14),
                anchor="w")
            linea.image = img
            linea.pack(anchor="w", pady=5)
            

    mostrar_pantalla(pantalla1)
    puntaje1=0
    puntaje2=0


    personajes=["entrenador1","entrenador2","entrenador3","entrenador4","entrenador5"]
    pokemones=["Perry","Kal","Sebastian","Chopper","Odette","Drax","Oswald","Mowgli","Donatello","Nick"]

    oponente=random.choice(personajes)
    print(oponente)
    
    pokemones_oponente=random.sample(pokemones,3)
    pokemon_op_inicial=pokemones_oponente[0]
    print(pokemones_oponente)

    disponibles = Listbox(pantalla1,width=50,height=100)
    disponibles.place(x=1000, y=0)
    disponibles.delete(0, END)

    for elemento in seleccionadas:
        disponibles.insert(END, elemento)

    inicio=Canvas(pantalla1,width=1000, height=700, bg="#ADD395")
    inicio.place(x=0,y=0)
    combate=Canvas(pantalla2,width=1200, height=700, bg="#ADD395")
    combate.place(x=0,y=0)

    def elegir():
        global pokemon_inicial,elemento, defensa, ataque, vida, vida_op, defensa_op, ataque_op
        seleccion = disponibles.curselection()
        elemento = disponibles.get(seleccion[0])
        pokemon_inicial=elemento
        print("Elegiste: ",elemento)
        valores()
            

    valores_pokemones = {"Perry": (20, 10),
    "Kal": (10, 35),
    "Sebastian": (11, 25),
    "Chopper": (5, 30),
    "Odette": (30, 5),
    "Drax": (2, 40),
    "Oswald": (25, 18),
    "Mowgli": (7, 30),
    "Donatello": (9, 25),
    "Nick": (12, 27)}

    def valores():
        global defensa, ataque, vida

        defensa, ataque = valores_pokemones[pokemon_inicial]
        vida = vida_pokemones[pokemon_inicial]
                

    defensa_op, ataque_op = valores_pokemones[pokemon_op_inicial]
    imagenes_pokemones = {
            "Perry": "perry.png",
            "Kal": "bicho.png",
            "Sebastian": "cangrejo.png",
            "Chopper": "chopper.png",
            "Odette": "cisne.png",
            "Drax": "dragon.png",
            "Oswald": "pinguino.png",
            "Mowgli": "tigre.png",
            "Donatello": "tortuga.png",
            "Nick": "zorro.png"}

    entrenadores_img = {
            1: "sprite_0.png",
            2: "matt.png",
            3: "prueba.png",
            4: "senku2.png",
            5: "robin.png"}
    
    mapa_entrenadores = {"entrenador1": 1,
        "entrenador2": 2,
        "entrenador3": 3,
        "entrenador4": 4,
        "entrenador5": 5}
    

    def escena():
            combate.delete("all")
           
            avatar= cargar_img(entrenadores_img[opcion_entrenador])
            combate.create_image(0, 300, anchor=NW, image=avatar)
            combate.imagen2 = avatar
            avatar2 = cargar_img(entrenadores_img[mapa_entrenadores[oponente]])
            combate.create_image(900,5, anchor=NW, image=avatar2)
            combate.imagen4 = avatar2

            imagen = cargar_img(imagenes_pokemones[pokemon_inicial])
            inicio.create_image(390,220, anchor=NW, image=imagen)
            inicio.imagen = imagen
            imagen1 = cargar_img(imagenes_pokemones[pokemon_inicial])
            combate.create_image(200,300, anchor=NW, image=imagen1)
            combate.imagen = imagen1
            imagen_op = cargar_img(imagenes_pokemones[pokemon_op_inicial])
            combate.create_image(800,200, anchor=NW, image=imagen_op)
            combate.imagen3 = imagen_op

            


    def actualizar_lista():
        disponibles.delete(0, END)
        for elemento in seleccionadas:
            disponibles.insert(END, elemento)



    def atacar():
        global vida, vida_op, ataque, defensa_op

        if vida > 0 and vida_op > 0:

            impacto = max(1, ataque - defensa_op)
            vida_op = max(0, vida_op-impacto)
            vida_pokemones[pokemon_inicial] = vida
            if vida>0:
                turno_oponente()
            cambiar_label(f"Tu vida: {vida} - Vida oponente: {vida_op}")

            final()

    def defenderse():
        global  vida,vida_op, defensa, ataque, vida_pokemones
        if vida>0 and vida_op>0:
            impacto=max(0, (ataque_op-defensa)-10)
            vida = max(0, vida-impacto )
            vida_pokemones[pokemon_inicial] = vida
        
            if vida>0:
                turno_oponente()
            final()
            cambiar_label(f"Tu vida: {vida} - Vida oponente: {vida_op}")


    def turno_oponente():
        accion = random.choice(["atacar", "defender"])

        if accion == "atacar":
            contraataque()

        elif accion == "defender":
            defender_oponente()

        

    def defender_oponente():
        global vida_op,vida, ataque, defensa_op
        if vida>0 and vida_op>0:
            daño=max(0, (ataque-defensa_op)//2)
            vida_op= max(0, vida_op-daño )
            mensaje= f"Tu oponente se ha defendido "
            cambiar_label2(mensaje)
        
            
        
    def contraataque():
        global vida,vida_op, ataque_op, defensa
        daño=max(1,(ataque_op-defensa))
        vida = max(0,(vida - daño))
        vida_pokemones[pokemon_inicial] = vida
        mensaje2=f"Tu oponente decide contraatacar, has recibido un daño de {daño}"
        cambiar_label2(mensaje2)

        

    continuar=tk.Button(pantalla1, text="Inicio Combate", command=lambda: siguiente(pantalla2),width=12, height=2)
    continuar.place(x=1050,y=500)

    texto_label=Label(pantalla2, text="Inicio del juego", font=("Times New Roman",20), bg="gray", fg="black")
    texto_label.place(x=0,y=0)

    texto1=Label(pantalla2, text="", font=("Times New Roman",20), bg="gray", fg="black")
    texto1.place(x=0,y=50)

    texto2=Label(pantalla2, text="Puntos: 0", font=("Times New Roman",20), bg="gray", fg="black")
    texto2.place(x=15,y=300)

    texto3=Label(pantalla2, text="Puntos: 0", font=("Times New Roman",20), bg="gray", fg="black")
    texto3.place(x=900,y=10)

    texto4=Label(pantalla1, text="Elige al pokemon que quieras mandar a batalla", font=("Times New Roman",30), bg="gray", fg="black")
    texto4.place(x=0,y=0)


    def cambiar_label(texto):
        texto_label.config(text=texto)

    def cambiar_label2(texto):
        texto1.config(text=texto)

    def cambiar_label3(texto):
        texto2.config(text=texto)
    def cambiar_label4(texto):
        texto3.config(text=texto)

    def cambiar_pokemon():
        global pokemon_inicial, vida

        seleccion = disponibles.curselection()

        nuevo = disponibles.get(seleccion[0])

        vida_pokemones[pokemon_inicial] = vida
        pokemon_inicial = nuevo
        vida = vida_pokemones[pokemon_inicial]
        valores()
        escena()
        cambiar_label(f"Cambiaste a {pokemon_inicial} Vida: {vida}")


    def reinicio():
        global vida, vida_op, pokemon_inicial, pokemon_op_inicial

        if len(pokemones_oponente) > 0 and len(seleccionadas) >0:
            vida=100
            vida_op=100
            
        
        
    def botones():
            defensa1.config(state="disabled")
            ataque1.config(state="disabled")
            continuar2.config(state="normal")

    def puntos():
        global puntaje1
        puntaje1=puntaje1 +1
        cambiar_label3(f"Puntos: {puntaje1}")

    def puntos_oponente():
        global puntaje2
        puntaje2=puntaje2 +1
        cambiar_label4(f"Puntos: {puntaje2}")




    def final():
        global vida_op, vida,pokemon_inicial,pokemon_op_inicial
        fin=False
        if vida <=0:
            pokemones_oponente.append(pokemon_inicial)
            seleccionadas.remove(pokemon_inicial)
            if len(seleccionadas)>0:
                actualizar_lista()
                pokemon_inicial=elemento
                valores()
                fin=True
                botones()
                puntos_oponente()
            else:
                cambiar_label("Te quedaste sin pokemones, has perdido el combate")
                cambiar_label2("Fin del combate")
                puntos_oponente()
                ataque1.config(state="disabled")
                defensa1.config(state="disabled")
                continuar2.config(state="disabled")
                continuar3.config(state="normal")
                guardar_resultado(nombre.get(), puntaje1, opcion_entrenador)
                
            
        if vida_op <= 0:
            seleccionadas.append(pokemon_op_inicial)
            pokemones_oponente.remove(pokemon_op_inicial)
            if len(pokemones_oponente)>0:
                actualizar_lista()
                pokemon_op_inicial=pokemones_oponente[0]
                botones() 
                puntos()          
                fin=True
            else:
                cambiar_label("Tu oponente se quedó sin pokemones, has ganado el combate")
                cambiar_label2("Fin del combate")
                puntos()
                ataque1.config(state="disabled")
                defensa1.config(state="disabled")
                continuar2.config(state="disabled")
                continuar3.config(state="normal")
                guardar_resultado(nombre.get(), puntaje1, opcion_entrenador)


        if fin:
            reinicio()
        
        print(seleccionadas)
        print (pokemones_oponente)


    ataque1=Button(pantalla2, text="Atacar", command= atacar, width=10, height=2)
    ataque1.place(x=300, y=600)

    defensa1=Button(pantalla2, text="Defender", command= defenderse, width=10, height=2)
    defensa1.place(x=400, y=600)
    
    elecciion = Button(pantalla1, text="Elegir", command=cambiar_pokemon, width=12, height=2)
    elecciion.place(x=1050, y=400)
    
    continuar2=tk.Button(pantalla2, text="Cambiar de Pokemon", command=lambda: mostrar_pantalla(pantalla1),width=20, height=2)
    continuar2.place(x=500,y=600)
    continuar3=tk.Button(pantalla2, text="Mejores puntajes", command=lambda: mostrar_pantalla(pantalla3),width=12, height=2)
    continuar3.place(x=900,y=600)
    

boton_inicio=Button(pagina3, text= 'inicio', command=abrir_ventana,width=12, height=2)
boton_inicio.place(x=1000,y=640)

mostrar_frame(pagina1)
ventana.mainloop()