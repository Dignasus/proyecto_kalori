import mysql.connector

class KaloriModel:
    def __init__(self):
        self.config_servidor = {
            'host': 'localhost',
            'user': 'root',
            'password': ''
        }
        self.nombre_bd = 'kalori_db'
        self.verificar_e_iniciar_db()

    def verificar_e_iniciar_db(self):
        try:
            conexion = mysql.connector.connect(**self.config_servidor)
            cursor = conexion.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.nombre_bd}")
            cursor.execute(f"USE {self.nombre_bd}")

            sql_tabla = """
            CREATE TABLE IF NOT EXISTS historial_simulaciones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                peso_inicial FLOAT,
                altura INT,
                edad INT,
                genero VARCHAR(10),
                actividad VARCHAR(20),
                calorias_diarias FLOAT,
                peso_proyectado FLOAT,
                fecha_simulacion DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
            cursor.execute(sql_tabla)
            cursor.close()
            conexion.close()
        except mysql.connector.Error as err:
            print(f"Error BD: {err}")

    def calcular_geb(self, peso, altura, edad, genero='hombre'):
        if genero == 'hombre':
            return 66.5 + (13.75 * peso) + (5.003 * altura) - (6.755 * edad)
        else:
            return 655.1 + (9.563 * peso) + (1.850 * altura) - (4.676 * edad)

    def proyectar_peso(self, peso_actual, geb, ingesta_diaria, factor_actividad):
        # Multiplicamos el GEB por el factor seleccionado por el usuario
        gasto_total_real = geb * factor_actividad
        
        balance_diario = ingesta_diaria - gasto_total_real
        
        datos_x = []
        datos_y = []
        peso_temp = peso_actual
        
        for semana in range(5):
            datos_x.append(semana)
            datos_y.append(peso_temp)
            # 7700 kcal = 1 kg
            peso_temp += (balance_diario * 7) / 7700
            
        return datos_x, datos_y, peso_temp, gasto_total_real

    def guardar_en_bd(self, peso, altura, edad, ingesta, peso_final, genero, actividad):
        try:
            config_db = self.config_servidor.copy()
            config_db['database'] = self.nombre_bd
            conexion = mysql.connector.connect(**config_db)
            cursor = conexion.cursor()
            
            sql = """INSERT INTO historial_simulaciones 
                     (peso_inicial, altura, edad, calorias_diarias, peso_proyectado, genero, actividad) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            valores = (peso, altura, edad, ingesta, peso_final, genero, actividad)
            
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error al guardar: {err}")
            return False