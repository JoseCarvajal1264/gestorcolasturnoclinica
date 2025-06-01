import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage

with open("config.json") as f:
    config = json.load(f)

conn_str = config["CONNECTION_STR"]
queue_name = config["QUEUE_NAME"]

with ServiceBusClient.from_connection_string(conn_str) as client:
    sender = client.get_queue_sender(queue_name=queue_name)
    with sender:
        cita = {
            "cita_id": 101,
            "paciente": "Juan Pérez",
            "especialidad": "Cardiología",
            "fecha": "2025-06-15",
            "hora": "09:30",
            "doctor": "Dra. Ana Torres"
        }
        mensaje = ServiceBusMessage(json.dumps(cita))
        sender.send_messages(mensaje)
        print("Cita médica enviada correctamente.")
