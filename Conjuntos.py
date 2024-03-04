import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib_venn import venn2_unweighted


def mostrar_venn():
    conjunto1 = set(map(int, entry_conjunto1.get().replace(" ", "").split(',')))
    conjunto2 = set(map(int, entry_conjunto2.get().replace(" ", "").split(',')))

    # Calcular la intersección de los conjuntos
    interseccion = conjunto1.intersection(conjunto2)

    # Limpiar el eje antes de dibujar el nuevo diagrama
    ax.clear()

    # Crear el diagrama de Venn con áreas proporcionales
    venn = venn2_unweighted([conjunto1, conjunto2], ('Conjunto 1', 'Conjunto 2'), ax=ax)

    # Mostrar los elementos dentro del diagrama
    for area, label in zip(venn.subset_labels, ['A', 'B', 'AB']):
        if label == 'AB':
            area.set_text(f'{label}\n{", ".join(map(str, interseccion))}')
        else:
            area.set_text(f'{label}\n{", ".join(map(str, conjunto1 if label == "A" else conjunto2))}')

    # Actualizar el lienzo de Matplotlib
    canvas.draw()


# Configuración de la interfaz
root = tk.Tk()
root.title("Diagrama de Venn")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_conjunto1 = tk.Label(frame, text="Conjunto 1:")
label_conjunto1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_conjunto1 = tk.Entry(frame)
entry_conjunto1.grid(row=0, column=1, padx=5, pady=5)

label_conjunto2 = tk.Label(frame, text="Conjunto 2:")
label_conjunto2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_conjunto2 = tk.Entry(frame)
entry_conjunto2.grid(row=1, column=1, padx=5, pady=5)

boton_mostrar = tk.Button(frame, text="Mostrar Venn", command=mostrar_venn)
boton_mostrar.grid(row=2, columnspan=2, pady=10)

# Configuración de Matplotlib
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# Agregar el lienzo de Matplotlib a la interfaz de Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()



