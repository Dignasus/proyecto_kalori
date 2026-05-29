from modelo import KaloriModel
from vista import KaloriView

class KaloriController:
    def __init__(self):
        self.modelo = KaloriModel()
        self.vista = KaloriView(self)

    def realizar_simulacion(self):
        try:
            # DATOS
            peso = float(self.vista.entry_peso.get())
            altura = float(self.vista.entry_altura.get())
            edad = int(self.vista.entry_edad.get())
            ingesta = float(self.vista.entry_calorias.get())
            sexo = self.vista.combo_sexo.get()
            
            # Obtenemos el texto de la actividad
            actividad_texto = self.vista.combo_actividad.get()

            # Diccionario de factores de actividad
            mapa_actividad = {
                "Nulo (Sedentario)": 1.2,
                "Bajo (Ligero)": 1.375,
                "Medio (Moderado)": 1.55,
                "Alto (Intenso)": 1.725,
                "Muy Alto (Atleta)": 1.9
            }
            
            # Buscamos el número correspondiente. Si falla, usamos 1.2 por defecto.
            factor = mapa_actividad.get(actividad_texto, 1.2)

            # CÁLCULOS
            geb = self.modelo.calcular_geb(peso, altura, edad, genero=sexo.lower())
            
            # Ahora pasamos el FACTOR REAL a la proyección
            datos_x, datos_y, peso_final, gasto_total = self.modelo.proyectar_peso(peso, geb, ingesta, factor)

            # MOSTRAR RESULTADOS
            diferencia = peso_final - peso
            signo = "+" if diferencia > 0 else ""
            
            texto_resultado = (
                f"Paciente: {sexo} | Actividad: {actividad_texto.split(' ')[0]}\n"
                f"Gasto Total (TDEE): {gasto_total:.0f} kcal/día\n"
                f"(GEB: {geb:.0f} x Factor {factor})\n"
                f"Peso en 4 semanas: {peso_final:.2f} kg\n"
                f"Variación: {signo}{diferencia:.2f} kg"
            )
            
            self.vista.lbl_resultado_texto.config(text=texto_resultado, fg="#004d40")
            self.vista.mostrar_grafico(datos_x, datos_y)

            # GUARDAR EN BD
            if self.modelo.guardar_en_bd(peso, altura, edad, ingesta, peso_final, sexo, actividad_texto):
                print(f"Registro guardado: {actividad_texto} (Factor {factor})")
                self.vista.mostrar_exito("Simulación calculada y guardada.")
            else:
                self.vista.mostrar_error("Error de conexión BD.")

        except ValueError:
            self.vista.mostrar_error("Error: Ingresa solo números en peso, altura y edad.")
        except Exception as e:
            print(f"Error: {e}")
            self.vista.mostrar_error(f"Error inesperado: {e}")

if __name__ == "__main__":
    app = KaloriController()
    app.vista.mainloop()