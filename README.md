# Sistemas de Gestión Empresarial

## Módulos Odoo

### `gestion_tareas`
Módulo de gestión de tareas pendientes que permite:
- Crear y administrar tareas con diferentes niveles de prioridad
- Marcar tareas como realizadas
- Sistema automático de clasificación de urgencia (tareas con prioridad > 10 se marcan como urgentes)
- Vista de lista para visualizar todas las tareas
#### Campos:
  - `tarea` (text): Descripción de la tarea
  - `prioridad` (int): Nivel de prioridad de la tarea
  - `urgente` (bool): Indica si la tarea es urgente
  - `realizada` (bool): Indica si la tarea ha sido completada
