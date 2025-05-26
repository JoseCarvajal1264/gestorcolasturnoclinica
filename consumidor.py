import pika
import json

# Conexión a RabbitMQ
conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()

# Declarar la cola (igual que en productor)
canal.queue_declare(queue='cola_ejemplo', durable=True)

# Función que se ejecuta al recibir un mensaje
def callback(ch, method, properties, body):
    turno = json.loads(body)
    print("\n📋 Turno recibido:")
    print("Nombre:", turno["nombre"])
    print("Especialidad:", turno["especialidad"])
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Consumir mensajes
canal.basic_qos(prefetch_count=1)
canal.basic_consume(queue='cola_ejemplo', on_message_callback=callback)

print("🟢 Esperando turnos. Presiona CTRL+C para salir.")
canal.start_consuming()
