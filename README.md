## Sistema de Gestión de Citas Médicas

Este proyecto es un sistema de gestión de citas médicas que permite a los pacientes solicitar citas con médicos, gestionar la agenda de los médicos y enviar notificaciones. El sistema está diseñado para facilitar la administración de citas, asegurando que tanto médicos como pacientes tengan una experiencia fluida.

## Funcionalidades

- Verificación de disponibilidad de médicos según especialidad.
- Asignación de un médico de preferencia para los pacientes.
- Visualización de cupos disponibles para citas, mostrando día y hora.
- Notificación a los pacientes dos días antes de la cita a través de llamada telefónica.
- Gestión de la agenda de médicos, incluyendo la adición de citas con fecha y hora.
- Opción para que los pacientes cancelen citas.
- Reorganización de citas cercanas a aquellas que han sido canceladas.
- Almacenamiento de datos de pacientes y médicos.
- Permitir a los usuarios solicitar sus propias citas.
- Envío de confirmaciones de citas por correo electrónico, mensaje de texto o notificación.
- Generación de reportes sobre médicos, especialidades y tendencias de citas.
- Cálculo del porcentaje de ausentismo para evaluar la eficiencia.
- Exportación de reportes a formato Excel.

## Requisitos

Para ejecutar el proyecto, asegúrate de tener instalados los siguientes elementos:

- Python 3.x
- Biblioteca `rich` para impresión formateada
- Biblioteca `csv` y `json` para manipulación de datos

### Puedes instalar las bibliotecas necesarias ejecutando:

```bash
pip install rich
```
1. Clonar el Repositorio: Abre tu terminal y ejecuta el siguiente comando para clonar el repositorio
```
git clone https://github.com/tu_usuario/tu_repositorio.git
```
2. Navegar al Directorio del Proyecto:
```
cd tu_repositorio
```
3. Crear y Activar un Entorno Virtual (Opcional pero recomendado):
```
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
```
4. Instalar Dependencias: Asegúrate de que requirements.txt esté en el directorio raíz y ejecuta:
```
pip install -r requirements.txt
```
5. Ejecutar el Proyecto: Para iniciar el sistema, ejecuta el siguiente comando:
```
python main.py
```
## Uso
- Al iniciar el sistema, se presentará un menú donde los usuarios podrán seleccionar diferentes opciones, como agregar pacientes, pedir citas, cancelar citas, asignar médicos de preferencia y ver citas pendientes.
- Los datos de pacientes y médicos se pueden cargar desde archivos CSV y JSON.
- Las citas se gestionan en la agenda de los médicos y se notifican a los pacientes.