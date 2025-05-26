
# Sistema de Gestión de Turnos con RabbitMQ

Escenario
Una clínica que atiende clientes mediante turnos.
El productor genera números de turno (por ejemplo, Turno 1, Turno 2, etc.) y los coloca en la cola de RabbitMQ.
El consumidor escucha esa cola y, a medida que llegan los mensajes, los procesa simulando que atiende a los clientes.


## Archivos

- `productor.py`: Envía un mensaje a la cola con el turno de un paciente.
- `consumidor.py`: Recibe el turno y lo procesa.

## Requisitos

- RabbitMQ ejecutándose en localhost (puede ser instalado vía Docker).
- Python 3
- Librería `pika` (instalación: `pip install pika`)

## Ejecución

1. Ejecutar RabbitMQ en Docker:
```bash
docker run -d --hostname rabbit-host --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

2. Ejecutar primero `consumidor.py` y luego `productor.py`.

---`


