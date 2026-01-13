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

### `school`
Módulo de gestión escolar (School Management) que permite administrar estudiantes, clases y eventos en una escuela.

**Dependencias:** `base`, `hr`

#### Modelos:
- **school.student** (Estudiantes):
  - Campos: name, last_name, birth_date, id_number (único), active, age (computado), class_id
  - Restricciones: DNI único, campos obligatorios (name, last_name, id_number)
  
- **school.class** (Clases):
  - Campos: name, grade (selection), date_begin, date_end, tutor_id (hr.employee), student_ids, student_number (computado), description
  - Relación: Un tutor (empleado de RRHH) puede tener múltiples clases

- **school.event** (Eventos):
  - Campos: name, date, students_ids (Many2many), type (absence/delay/congratulations/behavior), description
  - Ordenamiento: Por fecha descendente

#### Características:
- Cálculo automático de edad a partir de fecha de nacimiento
- Conteo automático de estudiantes por clase
- Relaciones Many2one, One2many y Many2many entre modelos
- Integración con módulo de Recursos Humanos para tutores

