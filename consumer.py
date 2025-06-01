import json
from azure.servicebus import ServiceBusClient

with open('../config/config.json') as f:
    config = json.load(f)

conn_str = config["CONNECTION_STR"]
queue_name = config["QUEUE_NAME"]

with ServiceBusClient.from_connection_string(conn_str) as client:
    receiver = client.get_queue_receiver(queue_name=queue_name)
    with receiver:
        for msg in receiver:
            cita = json.loads(str(msg))
            print("\n📅 Cita recibida:")
            print(f"🧑 Paciente: {cita['paciente']}")
            print(f"🩺 Especialidad: {cita['especialidad']}")
            print(f"📆 Fecha: {cita['fecha']} a las {cita['hora']}")
            print(f"👩‍⚕️ Doctor(a): {cita['doctor']}")
            receiver.complete_message(msg)
