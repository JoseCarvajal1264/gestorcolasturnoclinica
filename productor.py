import pika
import json

# Conexión a RabbitMQ
conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()

# Declarar la cola
canal.queue_declare(queue='cola_ejemplo', durable=True)

# Mensaje simulado (puedes cambiar los datos)
turno = {
    "nombre": "José Carvajal",
    "especialidad": "Fisioterapia"
}

mensaje = json.dumps(turno)

# Enviar mensaje a la cola
canal.basic_publish(
    exchange='',
    routing_key='cola_ejemplo',
    body=mensaje,
    properties=pika.BasicProperties(delivery_mode=2)  # Persistente
)

print("✅ Turno enviado:", mensaje)

conexion.close()
