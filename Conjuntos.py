import tkinter as tk
from tkinter import messagebox, ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib_venn import venn2, venn3


def mostrar_venn():
    global canvas

    # Obtener los elementos de los conjuntos desde las entradas de texto
    conjunto1 = obtener_conjunto(entry_conjunto1)
    conjunto2 = obtener_conjunto(entry_conjunto2)
    conjunto3 = obtener_conjunto(entry_conjunto3)

    # Eliminar el widget del lienzo de Matplotlib si ya existe
    if canvas:
        canvas.get_tk_widget().destroy()

    # Crear un nuevo lienzo de Matplotlib
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    if len(entries) == 2:  # Si hay dos conjuntos
        # Crear el diagrama de Venn con dos conjuntos
        venn = venn2(subsets=(len(conjunto1 - conjunto2), len(conjunto2 - conjunto1), len(conjunto1 & conjunto2)),
                     set_labels=('Conjunto 1', 'Conjunto 2'), ax=ax)

        # Etiquetar las intersecciones
        venn.get_label_by_id('10').set_text(f"A\n{', '.join(map(str, conjunto1 - conjunto2))}")
        venn.get_label_by_id('01').set_text(f"B\n{', '.join(map(str, conjunto2 - conjunto1))}")
        venn.get_label_by_id('11').set_text(f"AB\n{', '.join(map(str, conjunto1 & conjunto2))}")

    elif len(entries) == 3:  # Si hay tres conjuntos
        # Crear el diagrama de Venn con tres conjuntos
        venn = venn3(subsets=(len(conjunto1 - conjunto2 - conjunto3), len(conjunto2 - conjunto1 - conjunto3),
                       len(conjunto1 & conjunto2 - conjunto3),
                       len(conjunto3 - conjunto1 - conjunto2), len(conjunto1 & conjunto3 - conjunto2),
                       len(conjunto2 & conjunto3 - conjunto1),
                       len(conjunto1 & conjunto2 & conjunto3)), set_labels=('Conjunto 1', 'Conjunto 2', 'Conjunto 3'), ax=ax)

        # Etiquetar las intersecciones
        venn.get_label_by_id('100').set_text(f"A\n{', '.join(map(str, conjunto1 - conjunto2 - conjunto3))}")
        venn.get_label_by_id('010').set_text(f"B\n{', '.join(map(str, conjunto2 - conjunto1 - conjunto3))}")
        venn.get_label_by_id('001').set_text(f"C\n{', '.join(map(str, conjunto3 - conjunto1 - conjunto2))}")
        venn.get_label_by_id('110').set_text(f"AB\n{', '.join(map(str, conjunto1 & conjunto2 - conjunto3))}")
        venn.get_label_by_id('101').set_text(f"AC\n{', '.join(map(str, conjunto1 & conjunto3 - conjunto2))}")
        venn.get_label_by_id('011').set_text(f"BC\n{', '.join(map(str, conjunto2 & conjunto3 - conjunto1))}")
        venn.get_label_by_id('111').set_text(f"ABC\n{', '.join(map(str, conjunto1 & conjunto2 & conjunto3))}")

    # Agregar el lienzo de Matplotlib a la interfaz de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def obtener_conjunto(entry):
    if entry and entry.winfo_exists():
        return set(map(int, entry.get().replace(" ", "").split(',')))
    else:
        return set()

def agregar_conjunto():
    global entry_conjunto3, boton_agregar, num_conjuntos,label_conjunto3

    if num_conjuntos < 3:
        num_conjuntos += 1
        label = f"Conjunto {num_conjuntos}:"
        row = num_conjuntos
        entry = tk.Entry(frame)
        entry.grid(row=2, column=1, padx=5, pady=5)
        label_conjunto3 = tk.Label(frame, text="Conjunto 3:")
        label_conjunto3.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entry_conjunto3 = tk.Entry(frame)
        entry_conjunto3.grid(row=2, column=1, padx=5, pady=5)
        entries.append(entry)
        if num_conjuntos == 3:

            boton_agregar.config(state=tk.DISABLED)

def eliminar_conjunto():
    global entry_conjunto3, boton_agregar, num_conjuntos,label_conjunto3

    if num_conjuntos > 2:
        entries[-1].destroy()
        entries.pop()
        label_conjunto3.grid_remove()
        num_conjuntos -= 1
        boton_agregar.config(state=tk.NORMAL)

# Función para la unión de dos conjuntos
def union(conjunto1, conjunto2):
    resultado = set()

    for elemento in conjunto1:
        resultado.add(elemento)

    for elemento in conjunto2:
        if elemento not in resultado:
            resultado.add(elemento)

    return resultado

# Función para la intersección de dos conjuntos
def interseccion(conjunto1, conjunto2):
    resultado = set()

    for elemento in conjunto1:
        if elemento in conjunto2:
            resultado.add(elemento)

    return resultado

# Función para la diferencia entre dos conjuntos (conjunto1 - conjunto2)
def diferencia(conjunto1, conjunto2):
    resultado = set()

    for elemento in conjunto1:
        if elemento not in conjunto2:
            resultado.add(elemento)

    return resultado

# Función para la complemento de un conjunto con respecto a otro (conjunto_universo - conjunto)
def complemento(conjunto, conjunto_universo):
    resultado = set()

    for elemento in conjunto_universo:
        if elemento not in conjunto:
            resultado.add(elemento)

    return resultado

# Función para la combinación de dos conjuntos
def combinacion(conjunto1, conjunto2):
    resultado = set()

    for elemento1 in conjunto1:
        for elemento2 in conjunto2:
            resultado.add((elemento1, elemento2))

    return resultado

# Función para la cardinalidad de un conjunto
def cardinalidad(conjunto):
    return len(conjunto)

# Función para verificar si un conjunto es subconjunto de otro
def es_subconjunto(conjunto1, conjunto2):
    for elemento in conjunto1:
        if elemento not in conjunto2:
            return False
    return True

# Función para verificar si dos conjuntos son disjuntos
def son_disjuntos(conjunto1, conjunto2):
    for elemento in conjunto1:
        if elemento in conjunto2:
            return False
    return True

# Función para la unión de tres conjuntos
def union_tres(conjunto1, conjunto2, conjunto3):
    resultado = union(union(conjunto1, conjunto2), conjunto3)
    return resultado

# Función para la intersección de tres conjuntos
def interseccion_tres(conjunto1, conjunto2, conjunto3):
    resultado = interseccion(interseccion(conjunto1, conjunto2), conjunto3)
    return resultado

# Función para la diferencia entre tres conjuntos (conjunto1 - conjunto2 - conjunto3)
def diferencia_tres(conjunto1, conjunto2, conjunto3):
    resultado = diferencia(diferencia(conjunto1, conjunto2), conjunto3)
    return resultado

# Función para verificar si un conjunto es subconjunto de otro
def es_subconjunto_tres(conjunto1, conjunto2, conjunto3):
    return es_subconjunto(conjunto1, union(union(conjunto2, conjunto3)))

# Función para verificar si dos conjuntos son disjuntos
def son_disjuntos_tres(conjunto1, conjunto2, conjunto3):
    return son_disjuntos(interseccion(interseccion(conjunto1, conjunto2), conjunto3), set())
# defino el evento
def on_select(event):
    global num_conjuntos
    conjunto1 = obtener_conjunto(entry_conjunto1)
    conjunto2 = obtener_conjunto(entry_conjunto2)
    conjunto3 = obtener_conjunto(entry_conjunto3)
    selected_value = combo_box.get()
    print("Selected:", selected_value)
    if (num_conjuntos==2):
        if (selected_value == "Union"):
            mostrar_mensaje("La union entre los dos conjuntos es:"+str(union(conjunto1,conjunto2)))
        if (selected_value == "Intersection"):
            mostrar_mensaje("La interseccion entre los dos conjuntos es:"+str(interseccion(conjunto1,conjunto2)))
        if (selected_value == "Diferencia"):
            mostrar_mensaje("La diferencia entre los dos conjuntos es:"+str(diferencia(conjunto1,conjunto2)))
        if (selected_value == "complemento"):
            mostrar_mensaje("El complemento entre los dos conjuntos es:"+str(complemento(conjunto1,conjunto2)))
        if (selected_value == "combinacion entre ellos"):
            mostrar_mensaje("La combinación entre los dos conjuntos es:"+str(combinacion(conjunto1,conjunto2)))

def mostrar_alerta(mensaje):
    messagebox.showwarning("Alerta", mensaje)

def mostrar_mensaje(mensaje):
    messagebox.showinfo("Mensaje", mensaje)
# Configuración de la interfaz
root = tk.Tk()
root.title("Diagrama de Venn")

frame = tk.Frame(root)
frame.pack(padx=200, pady=60)

label_conjunto1 = tk.Label(frame, text="Conjunto 1:")
label_conjunto1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_conjunto1 = tk.Entry(frame)
entry_conjunto1.grid(row=0, column=1, padx=5, pady=5)

label_conjunto2 = tk.Label(frame, text="Conjunto 2:")
label_conjunto2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_conjunto2 = tk.Entry(frame)
entry_conjunto2.grid(row=1, column=1, padx=5, pady=5)

label_conjunto3 = tk.Label(frame, text="Conjunto 3:")
label_conjunto3.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_conjunto3 = tk.Entry(frame)
entry_conjunto3.grid(row=2, column=1, padx=5, pady=5)

boton_agregar = tk.Button(frame, text="Agregar Conjunto", command=agregar_conjunto)
boton_agregar.grid(row=3, columnspan=2, pady=5)

boton_eliminar = tk.Button(frame, text="Eliminar Conjunto", command=eliminar_conjunto)
boton_eliminar.grid(row=4, columnspan=2, pady=5)

boton_mostrar = tk.Button(frame, text="Mostrar Venn", command=mostrar_venn)
boton_mostrar.grid(row=5, columnspan=2, pady=5)

# Crear un ComboBox
options = ["Union", "Interseccion", "Diferencia","complemento","combinacion entre ellos"]
combo_box = ttk.Combobox(root, values=options)
combo_box.pack (padx =0 , pady=10)

# Asignar una función al evento de selección
combo_box.bind("<<ComboboxSelected>>", on_select)



# Variable global para el lienzo de Matplotlib
canvas = None

# Inicializar el contador de conjuntos y la lista de entradas de texto
num_conjuntos = 3
entries = [entry_conjunto1, entry_conjunto2, entry_conjunto3]
# iniciar
root.mainloop()


