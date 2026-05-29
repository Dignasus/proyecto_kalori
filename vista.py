import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class KaloriView(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Kalori - Prototipo v1.1")
        self.geometry("900x700")
        self.config(bg="#e1f5fe") 

        # --- Encabezado ---
        tk.Label(self, text="Kalori: Visualizador de Impacto", 
                 font=("Segoe UI", 18, "bold"), bg="#0288d1", fg="white").pack(fill="x", pady=0)

        # --- Panel Principal ---
        main_frame = tk.Frame(self, bg="#e1f5fe")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # -- Columna Izquierda: Entradas --
        left_frame = tk.LabelFrame(main_frame, text="Datos del Paciente", bg="white", font=("Arial", 10, "bold"))
        left_frame.pack(side="left", fill="y", padx=10, ipadx=10)

        # 1. Peso
        self.crear_input(left_frame, "Peso (kg):", 0)
        self.entry_peso = self.crear_entry(left_frame, 0)

        # 2. Altura
        self.crear_input(left_frame, "Altura (cm):", 1)
        self.entry_altura = self.crear_entry(left_frame, 1)

        # 3. Edad
        self.crear_input(left_frame, "Edad:", 2)
        self.entry_edad = self.crear_entry(left_frame, 2)

        # 4. Sexo
        tk.Label(left_frame, text="Sexo:", bg="white").grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.combo_sexo = ttk.Combobox(left_frame, values=["Hombre", "Mujer"], state="readonly")
        self.combo_sexo.grid(row=3, column=1, padx=10, pady=10)
        self.combo_sexo.current(0)

        # 5. Actividad Fisica
        tk.Label(left_frame, text="Actividad Física:", bg="white").grid(row=4, column=0, sticky="w", padx=10, pady=10)
        opciones_actividad = ["Nulo (Sedentario)", "Bajo (Ligero)", "Medio (Moderado)", "Alto (Intenso)", "Muy Alto (Atleta)"]
        self.combo_actividad = ttk.Combobox(left_frame, values=opciones_actividad, state="readonly", width=25)
        self.combo_actividad.grid(row=4, column=1, padx=10, pady=10)
        self.combo_actividad.current(0)

        # 6. Ingesta
        self.crear_input(left_frame, "Ingesta Diaria (kcal):", 5)
        self.entry_calorias = self.crear_entry(left_frame, 5)

        # Botón
        btn_calc = tk.Button(left_frame, text="Simular Proyección", command=self.controlador.realizar_simulacion,
                             bg="#0288d1", fg="white", font=("Arial", 11, "bold"), cursor="hand2")
        btn_calc.grid(row=6, column=0, columnspan=2, pady=20, sticky="ew", padx=10)

        # Resultado Texto
        self.lbl_resultado_texto = tk.Label(left_frame, text="...", bg="white", wraplength=200, justify="left")
        self.lbl_resultado_texto.grid(row=7, column=0, columnspan=2, pady=10)

        # Grafico
        right_frame = tk.Frame(main_frame, bg="white", bd=2, relief="sunken")
        right_frame.pack(side="right", fill="both", expand=True)

        self.frame_grafico = tk.Frame(right_frame, bg="white")
        self.frame_grafico.pack(fill="both", expand=True, padx=5, pady=5)

    def crear_input(self, parent, texto, fila):
        tk.Label(parent, text=texto, bg="white").grid(row=fila, column=0, sticky="w", padx=10, pady=10)

    def crear_entry(self, parent, fila):
        entry = ttk.Entry(parent)
        entry.grid(row=fila, column=1, padx=10, pady=10)
        return entry

    def mostrar_grafico(self, x, y):
        for widget in self.frame_grafico.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
        ax.plot(x, y, marker='o', color='#ff5722', linewidth=2, label='Proyección')
        ax.set_title("Tendencia de Peso (4 Semanas)")
        ax.set_xlabel("Semanas")
        ax.set_ylabel("Peso (kg)")
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def mostrar_error(self, msg):
        messagebox.showerror("Error", msg)
        
    def mostrar_exito(self, msg):
        messagebox.showinfo("Guardado", msg)