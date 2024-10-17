import csv
import json
from .paciente import Paciente
from .medico import Medico
from .cita import Cita
from datetime import datetime

def cargar_pacientes(archivo, hosp):
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            hosp.agregar_paciente(
                row['identificación'],
                row['nombre_completo'],
                row['celular'],
                row['correo']
            )

def cargar_medicos(archivo, hosp):
    with open(archivo, encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        for item in data:
            hosp.agregar_medico(
                item['id'],
                item['nombre'],
                item['correo'],
                item['celular'],
                item['especialidad']
            )

def cargar_citas(archivo, hosp):
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pac = hosp.buscar_paciente(row['paciente'])
            med = hosp.buscar_medico(row['medicos'])
            if pac and med:
                fecha_hora = datetime.strptime(row['fecha_hora'], '%Y-%m-%d %H:%M:%S')
                hosp.agendar_cita(pac, med, fecha_hora.strftime('%Y-%m-%d %H:%M'), "Cita cargada")

