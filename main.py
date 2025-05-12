import snap7
from snap7.util import *
from snap7.types import Areas

# Cria o cliente
client = snap7.client.Client()

# Conecta ao CLP - substitua pelo IP e Rack/Slot corretos
client.connect('192.168.0.1', 0, 1)  # IP, Rack, Slot

# Verifica se está conectado
if client.get_connected():
    print("Conectado ao CLP!")

    # Lê 4 bytes do DB 1, começando no byte 0
    db_number = 1
    start = 0
    size = 4
    data = client.read_area(Areas.DB, db_number, start, size)

    # Interpreta os 4 bytes como um inteiro (int32)
    value = get_int(data, 0)
    print(f"Valor lido do DB{db_number}: {value}")

    # Desconecta
    client.disconnect()
else:
    print("Falha na conexão com o CLP.")
