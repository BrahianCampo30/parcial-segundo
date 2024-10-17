from rich import print
from rich.console import Console
from rich.table import Table
from hospital import Hospital

from rich import print
from rich.console import Console
from rich.table import Table
from hospital import Hospital
from data import cargar_pacientes, cargar_medicos, cargar_citas

con = Console()
hosp = Hospital()

# Cargar datos
cargar_pacientes('data/pacientes.csv', hosp)
cargar_medicos('data/medicos.json', hosp)
cargar_citas('data/citas.csv', hosp)

def menu():
    con.print("\n[bold cyan]--- Menú ---[/bold cyan]")
    opciones = ["Agregar persona", "Pedir cita", "Cancelar cita", 
                "Asignar médico de preferencia", "Ver citas", "Salir"]
    for i, op in enumerate(opciones, 1):
        con.print(f"{i}. {op}")

while True:
    menu()
    opc = input("Opción: ")

    if opc == "1":
        tipo = input("Tipo (médico/paciente): ").lower()
        id, nom, cel, cor = input("ID: "), input("Nombre: "), input("Celular: "), input("Correo: ")

        if tipo == "medico":
            esp = input("Especialidad: ")
            hosp.agregar_medico(id, nom, cel, cor, esp)
        elif tipo == "paciente":
            hosp.agregar_paciente(id, nom, cel, cor)
        else:
            con.print("[red]Tipo inválido.[/red]")

    elif opc == "2":
        id_pac = input("ID del paciente: ")
        pac = hosp.buscar_paciente(id_pac)
        if pac:
            esp = input("Especialidad: ")
            med_disp = hosp.obtener_medicos_por_especialidad(esp)
            if med_disp:
                con.print("[bold]Médicos disponibles:[/bold]")
                tbl = Table(show_header=True, header_style="bold magenta")
                tbl.add_column("ID"), tbl.add_column("Nombre")
                for m in med_disp:
                    tbl.add_row(m.identificacion, m.nombre)
                con.print(tbl)
                id_med = input("ID del médico: ")
                fecha = input("Fecha (YYYY-MM-DD HH:MM): ")
                motivo = input("Motivo: ")
                hosp.agendar_cita(pac, hosp.buscar_medico(id_med), fecha, motivo)
            else:
                con.print(f"[red]Sin médicos para {esp}.[/red]")
        else:
            con.print("[red]Paciente no encontrado.[/red]")

    elif opc == "3":
        id_pac = input("ID del paciente: ")
        pac = hosp.buscar_paciente(id_pac)
        if pac:
            citas = hosp.obtener_citas_paciente(pac)
            if citas:
                con.print("[bold]Citas:[/bold]")
                tbl = Table(show_header=True, header_style="bold magenta")
                tbl.add_column("No."), tbl.add_column("Fecha"), tbl.add_column("Médico")
                for i, c in enumerate(citas, 1):
                    tbl.add_row(str(i), c.fecha_hora, c.medico.nombre)
                sel = int(input("Cita a cancelar: ")) - 1
                if 0 <= sel < len(citas):
                    hosp.cancelar_cita(citas[sel])
                else:
                    con.print("[red]Opción inválida.[/red]")
            else:
                con.print("[yellow]Sin citas pendientes.[/yellow]")
        else:
            con.print("[red]Paciente no encontrado.[/red]")

    elif opc == "4":
        id_pac = input("ID del paciente: ")
        pac = hosp.buscar_paciente(id_pac)
        if pac:
            id_med = input("ID del médico: ")
            med = hosp.buscar_medico(id_med)
            if med:
                pac.asignar_medico_preferencia(med)
            else:
                con.print("[red]Médico no encontrado.[/red]")
        else:
            con.print("[red]Paciente no encontrado.[/red]")

    elif opc == "5":
        id_pac = input("ID del paciente: ")
        pac = hosp.buscar_paciente(id_pac)
        if pac:
            citas = hosp.obtener_citas_paciente(pac)
            if citas:
                con.print("[bold]Citas:[/bold]")
                tbl = Table(show_header=True, header_style="bold magenta")
                tbl.add_column("Fecha"), tbl.add_column("Médico")
                for c in citas:
                    tbl.add_row(c.fecha_hora, c.medico.nombre)
                con.print(tbl)
            else:
                con.print("[yellow]Sin citas pendientes.[/yellow]")
        else:
            con.print("[red]Paciente no encontrado.[/red]")

    elif opc == "6":
        con.print("[green]Saliendo...[/green]")
        break
    else:
        con.print("[red]Opción inválida.[/red]")
