# Sistema de Agendamiento de Citas Médicas con Azure Service Bus

Este proyecto simula el agendamiento y procesamiento de citas médicas utilizando Azure Service Bus como sistema de mensajería (ESB).

## ¿Cómo funciona?
- `producer.py`: agenda una cita y la envía a una cola.
- `consumer.py`: recibe la cita y muestra la información.

## Requisitos
- Python 3.9+
- Azure Service Bus con una cola llamada `citas-medicas`

## Instalación
```bash
pip install -r requirements.txt
