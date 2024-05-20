import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

conn = sqlite3.connect('veterinaria.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                especie TEXT,
                raza TEXT,
                edad INTEGER,
                propietario TEXT
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS citas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER,
                fecha TEXT,
                hora TEXT,
                FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS consultas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER,
                diagnostico TEXT,
                tratamiento TEXT,
                medicamentos TEXT,
                fecha TEXT,
                FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS inventario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                cantidad INTEGER,
                precio REAL
            )''')

conn.commit()

class VetClinicSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Clínica Veterinaria")
        self.geometry("800x600")
        
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        pacientes_menu = tk.Menu(menubar, tearoff=0)
        pacientes_menu.add_command(label="Registrar", command=self.registrar_paciente)
        pacientes_menu.add_command(label="Actualizar", command=self.actualizar_paciente)
        pacientes_menu.add_command(label="Consultar historial", command=self.consultar_historial)
        menubar.add_cascade(label="Pacientes", menu=pacientes_menu)

        citas_menu = tk.Menu(menubar, tearoff=0)
        citas_menu.add_command(label="Programar", command=self.programar_cita)
        menubar.add_cascade(label="Citas", menu=citas_menu)

        consultas_menu = tk.Menu(menubar, tearoff=0)
        consultas_menu.add_command(label="Registrar", command=self.registrar_consulta)
        menubar.add_cascade(label="Consultas", menu=consultas_menu)

        inventario_menu = tk.Menu(menubar, tearoff=0)
        inventario_menu.add_command(label="Registrar", command=self.registrar_medicamento)
        inventario_menu.add_command(label="Actualizar existencias", command=self.actualizar_existencias)
        inventario_menu.add_command(label="Alertas de inventario", command=self.alertas_inventario)
        menubar.add_cascade(label="Inventario", menu=inventario_menu)

        reportes_menu = tk.Menu(menubar, tearoff=0)
        reportes_menu.add_command(label="Generar reportes", command=self.generar_reportes)
        menubar.add_cascade(label="Reportes", menu=reportes_menu)

    def registrar_paciente(self):
        def submit():
            nombre = nombre_entry.get()
            especie = especie_entry.get()
            raza = raza_entry.get()
            edad = int(edad_entry.get())
            propietario = propietario_entry.get()
            
            c.execute("INSERT INTO pacientes (nombre, especie, raza, edad, propietario) VALUES (?, ?, ?, ?, ?)", 
                      (nombre, especie, raza, edad, propietario))
            conn.commit()
            messagebox.showinfo("Éxito", "Paciente registrado correctamente")
            ventana.destroy()

        ventana = tk.Toplevel(self)
        ventana.title("Registrar Paciente")

        tk.Label(ventana, text="Nombre").grid(row=0, column=0)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=0, column=1)

        tk.Label(ventana, text="Especie").grid(row=1, column=0)
        especie_entry = tk.Entry(ventana)
        especie_entry.grid(row=1, column=1)

        tk.Label(ventana, text="Raza").grid(row=2, column=0)
        raza_entry = tk.Entry(ventana)
        raza_entry.grid(row=2, column=1)

        tk.Label(ventana, text="Edad").grid(row=3, column=0)
        edad_entry = tk.Entry(ventana)
        edad_entry.grid(row=3, column=1)

        tk.Label(ventana, text="Propietario").grid(row=4, column=0)
        propietario_entry = tk.Entry(ventana)
        propietario_entry.grid(row=4, column=1)

        tk.Button(ventana, text="Registrar", command=submit).grid(row=5, column=0, columnspan=2)

    def actualizar_paciente(self):
        def buscar():
            paciente_id = int(id_entry.get())
            c.execute("SELECT * FROM pacientes WHERE id=?", (paciente_id,))
            paciente = c.fetchone()
            if paciente:
                nombre_entry.insert(0, paciente[1])
                especie_entry.insert(0, paciente[2])
                raza_entry.insert(0, paciente[3])
                edad_entry.insert(0, paciente[4])
                propietario_entry.insert(0, paciente[5])
            else:
                messagebox.showerror("Error", "Paciente no encontrado")

        def actualizar():
            paciente_id = int(id_entry.get())
            nombre = nombre_entry.get()
            especie = especie_entry.get()
            raza = raza_entry.get()
            edad = int(edad_entry.get())
            propietario = propietario_entry.get()

            c.execute("UPDATE pacientes SET nombre=?, especie=?, raza=?, edad=?, propietario=? WHERE id=?", 
                      (nombre, especie, raza, edad, propietario, paciente_id))
            conn.commit()
            messagebox.showinfo("Éxito", "Paciente actualizado correctamente")
            ventana.destroy()

        ventana = tk.Toplevel(self)
        ventana.title("Actualizar Paciente")

        tk.Label(ventana, text="ID Paciente").grid(row=0, column=0)
        id_entry = tk.Entry(ventana)
        id_entry.grid(row=0, column=1)
        tk.Button(ventana, text="Buscar", command=buscar).grid(row=0, column=2)

        tk.Label(ventana, text="Nombre").grid(row=1, column=0)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=1, column=1)

        tk.Label(ventana, text="Especie").grid(row=2, column=0)
        especie_entry = tk.Entry(ventana)
        especie_entry.grid(row=2, column=1)

        tk.Label(ventana, text="Raza").grid(row=3, column=0)
        raza_entry = tk.Entry(ventana)
        raza_entry.grid(row=3, column=1)

        tk.Label(ventana, text="Edad").grid(row=4, column=0)
        edad_entry = tk.Entry(ventana)
        edad_entry.grid(row=4, column=1)

        tk.Label(ventana, text="Propietario").grid(row=5, column=0)
        propietario_entry = tk.Entry(ventana)
        propietario_entry.grid(row=5, column=1)

        tk.Button(ventana, text="Actualizar", command=actualizar).grid(row=6, column=0, columnspan=2)

    def consultar_historial(self):
        def buscar():
            paciente_id = int(id_entry.get())
            c.execute("SELECT * FROM consultas WHERE paciente_id=?", (paciente_id,))
            consultas = c.fetchall()
            for consulta in consultas:
                tree.insert("", "end", values=(consulta[0], consulta[2], consulta[3], consulta[4], consulta[5]))

        ventana = tk.Toplevel(self)
        ventana.title("Consultar Historial Médico")

        tk.Label(ventana, text="ID Paciente").grid(row=0, column=0)
        id_entry = tk.Entry(ventana)
        id_entry.grid(row=0, column=1)
        tk.Button(ventana, text="Buscar", command=buscar).grid(row=0, column=2)

        columns = ("ID Consulta", "Diagnóstico", "Tratamiento", "Medicamentos", "Fecha")
        tree = ttk.Treeview(ventana, columns=columns, show="headings")
        tree.heading("ID Consulta", text="ID Consulta")
        tree.heading("Diagnóstico", text="Diagnóstico")
        tree.heading("Tratamiento", text="Tratamiento")
        tree.heading("Medicamentos", text="Medicamentos")
        tree.heading("Fecha", text="Fecha")
        tree.grid(row=1, column=0, columnspan=3)

    def programar_cita(self):
        def submit():
            paciente_id = int(paciente_id_entry.get())
            fecha = fecha_entry.get()
            hora = hora_entry.get()
            
            c.execute("INSERT INTO citas (paciente_id, fecha, hora) VALUES (?, ?, ?)", 
                      (paciente_id, fecha, hora))
            conn.commit()
            messagebox.showinfo("Éxito", "Cita programada correctamente")
            ventana.destroy()

        ventana = tk.Toplevel(self)
        ventana.title("Programar Cita")

        tk.Label(ventana, text="ID Paciente").grid(row=0, column=0)
        paciente_id_entry = tk.Entry(ventana)
        paciente_id_entry.grid(row=0, column=1)

        tk.Label(ventana, text="Fecha").grid(row=1, column=0)
        fecha_entry = tk.Entry(ventana)
        fecha_entry.grid(row=1, column=1)

        tk.Label(ventana, text="Hora").grid(row=2, column=0)
        hora_entry = tk.Entry(ventana)
        hora_entry.grid(row=2, column=1)

        tk.Button(ventana, text="Programar", command=submit).grid(row=3, column=0, columnspan=2)

    def registrar_consulta(self):
        def submit():
            paciente_id = int(paciente_id_entry.get())
            diagnostico = diagnostico_entry.get()
            tratamiento = tratamiento_entry.get()
            medicamentos = medicamentos_entry.get()
            fecha = fecha_entry.get()
            
            c.execute("INSERT INTO consultas (paciente_id, diagnostico, tratamiento, medicamentos, fecha) VALUES (?, ?, ?, ?, ?)", 
                      (paciente_id, diagnostico, tratamiento, medicamentos, fecha))
            conn.commit()
            messagebox.showinfo("Éxito", "Consulta registrada correctamente")
            ventana.destroy()

        ventana = tk.Toplevel(self)
        ventana.title("Registrar Consulta")

        tk.Label(ventana, text="ID Paciente").grid(row=0, column=0)
        paciente_id_entry = tk.Entry(ventana)
        paciente_id_entry.grid(row=0, column=1)

        tk.Label(ventana, text="Diagnóstico").grid(row=1, column=0)
        diagnostico_entry = tk.Entry(ventana)
        diagnostico_entry.grid(row=1, column=1)

        tk.Label(ventana, text="Tratamiento").grid(row=2, column=0)
        tratamiento_entry = tk.Entry(ventana)
        tratamiento_entry.grid(row=2, column=1)

        tk.Label(ventana, text="Medicamentos").grid(row=3, column=0)
        medicamentos_entry = tk.Entry(ventana)
        medicamentos_entry.grid(row=3, column=1)

        tk.Label(ventana, text="Fecha").grid(row=4, column=0)
        fecha_entry = tk.Entry(ventana)
        fecha_entry.grid(row=4, column=1)

        tk.Button(ventana, text="Registrar", command=submit).grid(row=5, column=0, columnspan=2)

    def registrar_medicamento(self):
        def submit():
            nombre = nombre_entry.get()
            cantidad = int(cantidad_entry.get())
            precio = float(precio_entry.get())
            
            c.execute("INSERT INTO inventario (nombre, cantidad, precio) VALUES (?, ?, ?)", 
                      (nombre, cantidad, precio))
            conn.commit()
            messagebox.showinfo("Éxito", "Medicamento registrado correctamente")
            ventana.destroy()

        ventana = tk.Toplevel(self)
        ventana.title("Registrar Medicamento")

        tk.Label(ventana, text="Nombre").grid(row=0, column=0)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=0, column=1)

        tk.Label(ventana, text="Cantidad").grid(row=1, column=0)
        cantidad_entry = tk.Entry(ventana)
        cantidad_entry.grid(row=1, column=1)

        tk.Label(ventana, text="Precio").grid(row=2, column=0)
        precio_entry = tk.Entry(ventana)
        precio_entry.grid(row=2, column=1)

        tk.Button(ventana, text="Registrar", command=submit).grid(row=3, column=0, columnspan=2)

    def actualizar_existencias(self):
        def buscar():
            medicamento_id = int(id_entry.get())
            c.execute("SELECT * FROM inventario WHERE id=?", (medicamento_id,))
            medicamento = c.fetchone()
            if medicamento:
                nombre_entry.insert(0, medicamento[1])
                cantidad_entry.insert(0, medicamento[2])
                precio_entry.insert(0, medicamento[3])
            else:
                messagebox.showerror("Error", "Medicamento no encontrado")

        def actualizar():
            medicamento_id = int(id_entry.get())
            nombre = nombre_entry.get()
            cantidad = int(cantidad_entry.get())
            precio = float(precio_entry.get())

            c.execute("UPDATE inventario SET nombre=?, cantidad=?, precio=? WHERE id=?", 
                      (nombre, cantidad, precio, medicamento_id))
            conn.commit()
            messagebox.showinfo("Éxito", "Medicamento actualizado correctamente")
            ventana.destroy()

        ventana = tk.Toplevel(self)
        ventana.title("Actualizar Existencias")

        tk.Label(ventana, text="ID Medicamento").grid(row=0, column=0)
        id_entry = tk.Entry(ventana)
        id_entry.grid(row=0, column=1)
        tk.Button(ventana, text="Buscar", command=buscar).grid(row=0, column=2)

        tk.Label(ventana, text="Nombre").grid(row=1, column=0)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=1, column=1)

        tk.Label(ventana, text="Cantidad").grid(row=2, column=0)
        cantidad_entry = tk.Entry(ventana)
        cantidad_entry.grid(row=2, column=1)

        tk.Label(ventana, text="Precio").grid(row=3, column=0)
        precio_entry = tk.Entry(ventana)
        precio_entry.grid(row=3, column=1)

        tk.Button(ventana, text="Actualizar", command=actualizar).grid(row=4, column=0, columnspan=2)

    def alertas_inventario(self):
        ventana = tk.Toplevel(self)
        ventana.title("Alertas de Inventario")

        tree = ttk.Treeview(ventana, columns=("ID", "Nombre", "Cantidad"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Cantidad", text="Cantidad")
        tree.grid(row=0, column=0, columnspan=3)

        c.execute("SELECT * FROM inventario WHERE cantidad < 10")
        medicamentos_bajos = c.fetchall()
        for medicamento in medicamentos_bajos:
            tree.insert("", "end", values=(medicamento[0], medicamento[1], medicamento[2]))

    def generar_reportes(self):
        ventana = tk.Toplevel(self)
        ventana.title("Generar Reportes")

        tk.Label(ventana, text="Seleccionar reporte").grid(row=0, column=0)

        reporte_opciones = ["Pacientes atendidos", "Citas programadas", "Ventas de medicamentos"]
        reporte_var = tk.StringVar(value=reporte_opciones[0])
        reporte_menu = tk.OptionMenu(ventana, reporte_var, *reporte_opciones)
        reporte_menu.grid(row=0, column=1)

        tree = ttk.Treeview(ventana, columns=("ID", "Detalle", "Fecha"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Detalle", text="Detalle")
        tree.heading("Fecha", text="Fecha")
        tree.grid(row=1, column=0, columnspan=2)

        def generar():
            reporte = reporte_var.get()
            tree.delete(*tree.get_children())

            if reporte == "Pacientes atendidos":
                c.execute("SELECT * FROM pacientes")
                pacientes = c.fetchall()
                for paciente in pacientes:
                    tree.insert("", "end", values=(paciente[0], paciente[1], "N/A"))

            elif reporte == "Citas programadas":
                c.execute("SELECT * FROM citas")
                citas = c.fetchall()
                for cita in citas:
                    tree.insert("", "end", values=(cita[0], cita[1], cita[2]))

            elif reporte == "Ventas de medicamentos":
                c.execute("SELECT * FROM inventario")
                inventario = c.fetchall()
                for item in inventario:
                    tree.insert("", "end", values=(item[0], item[1], item[2]))

        tk.Button(ventana, text="Generar", command=generar).grid(row=2, column=0, columnspan=2)

if __name__ == "__main__":
    app = VetClinicSystem()
    app.mainloop()
    conn.close()
