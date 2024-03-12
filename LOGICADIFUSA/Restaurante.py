#Sistema de recomendacion de restaurantes 
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


distancia = ctrl.Antecedent(np.arange(0, 16, 1), 'distancia')
distancia['cerca'] = fuzz.trimf(distancia.universe, [0, 0, 3])
distancia['medio'] = fuzz.trimf(distancia.universe, [2, 4, 6])
distancia['lejos'] = fuzz.trimf(distancia.universe, [5, 10, 15])


precio = ctrl.Antecedent(np.arange(0, 31, 1), 'precio')
precio['barato'] = fuzz.trimf(precio.universe, [0, 0, 12])
precio['moderado'] = fuzz.trimf(precio.universe, [10, 15, 20])
precio['caro'] = fuzz.trimf(precio.universe, [18, 25, 30])


calificacion = ctrl.Antecedent(np.arange(0, 6, 1), 'calificacion')
calificacion['baja'] = fuzz.gaussmf(calificacion.universe, 1, 0.3)
calificacion['media'] = fuzz.gaussmf(calificacion.universe, 2.5, 0.3)
calificacion['alta'] = fuzz.gaussmf(calificacion.universe, 4.5, 0.5)

recomendacion = ctrl.Consequent(np.arange(0, 11, 1), 'recomendacion')
recomendacion['no_recomendado'] = fuzz.trimf(recomendacion.universe, [0, 0, 3])
recomendacion['quizas_recomendado'] = fuzz.trimf(recomendacion.universe, [2, 5, 8])
recomendacion['altamente_recomendado'] = fuzz.trimf(recomendacion.universe, [7, 10, 10])


rule1 = ctrl.Rule(distancia['cerca'] & precio['moderado'] & calificacion['alta'], recomendacion['altamente_recomendado'])
rule2 = ctrl.Rule(distancia['cerca'] & precio['barato'] & calificacion['alta'], recomendacion['altamente_recomendado'])
rule3 = ctrl.Rule(distancia['lejos'] | precio['caro'], recomendacion['no_recomendado'])
rule4 = ctrl.Rule(calificacion['baja'], recomendacion['no_recomendado'])
rule5 = ctrl.Rule(distancia['cerca'] & calificacion['alta'], recomendacion['altamente_recomendado'])
rule6 = ctrl.Rule(precio['moderado'] & calificacion['media'], recomendacion['quizas_recomendado'])
rule7 = ctrl.Rule(distancia['medio'] & precio['barato'] & calificacion['media'], recomendacion['quizas_recomendado'])
rule8 = ctrl.Rule(distancia['lejos'] & calificacion['media'], recomendacion['quizas_recomendado'])
rule9 = ctrl.Rule(precio['caro'] | calificacion['baja'], recomendacion['no_recomendado'])
rule10 = ctrl.Rule(distancia['medio'] & calificacion['baja'], recomendacion['no_recomendado'])


# Crear el sistema de control y la simulación
recomendacion_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10])
recomendacion_sim = ctrl.ControlSystemSimulation(recomendacion_ctrl)

import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def evaluar_recomendacion():
    distancia_input = float(distancia_slider.get())
    precio_input = float(precio_slider.get())
    calificacion_input = float(calificacion_slider.get())

    recomendacion_sim.input['distancia'] = distancia_input
    recomendacion_sim.input['precio'] = precio_input
    recomendacion_sim.input['calificacion'] = calificacion_input


    recomendacion_sim.compute()

    recomendacion_result = recomendacion_sim.output['recomendacion']
    resultado = ""
    if recomendacion_result >= 7:  # Asumiendo que 7-10 es "Altamente Recomendado"
        resultado = "Altamente Recomendado"
    elif recomendacion_result >= 4:  # Asumiendo que 4-6 es "Quizás Recomendado"
        resultado = "Quizás Recomendado"
    else:  # Asumiendo que 0-3 es "No Recomendado"
        resultado = "No Recomendado"


    recomendacion_label.config(text=f'Resultado de la Recomendación: {resultado}')
    

    plt.close('all')

    # Generar y mostrar la gráfica de resultados difusos
    recomendacion.view(sim=recomendacion_sim)
    plt.show()



root = tk.Tk()
root.title("Sistema de Recomendación de Restaurantes")

# Creación de sliders para las entradas
distancia_slider = tk.Scale(root, from_=0, to=15, orient='horizontal', label="Distancia (km)", length=400)
distancia_slider.pack()

precio_slider = tk.Scale(root, from_=0, to=30, orient='horizontal', label="Precio", length=400)
precio_slider.pack()

calificacion_slider = tk.Scale(root, from_=0, to=5, orient='horizontal', label="Calificación", length=400)
calificacion_slider.pack()

# Botón para evaluar la recomendación
evaluar_btn = ttk.Button(root, text="Evaluar Recomendación", command=evaluar_recomendacion)
evaluar_btn.pack()

# Etiqueta para mostrar el resultado
recomendacion_label = ttk.Label(root, text="Resultado de la Recomendación: ")
recomendacion_label.pack()

root.mainloop()
