from azure.iot.device import IoTHubDeviceClient, Message
import random
import time

# Substitua pela sua string de conexão do IoT Hub
CONNECTION_STRING = "HostName=MeuHubIoTAzure.azure-devices.net;DeviceId=MeuDispositivoIoT1;SharedAccessKey=DFCGlXc0/tEYnvjkO6YpOLp5FRwMPRtk44NP208OtTc="

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

try:
    while True:
        temperature = random.randint(20, 30)  # Simula a leitura da temperatura
        msg = Message(f'{{"temperature": {temperature}}}')
        client.send_message(msg)
        print(f'Sent: {msg}')
        time.sleep(10)  # Envia dados a cada 10 segundos
except KeyboardInterrupt:
    print("Sending stopped")
finally:
    client.shutdown()



