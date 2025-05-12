import snap7

# Configuração do cliente
plc = snap7.client.Client()
plc.connect('192.168.0.1', 0, 1)  # IP, rack, slot

# Verificar conexão
if plc.get_connected():
    print("Conectado ao PLC!")
else:
    print("Falha na conexão")

# Ler uma área de memória (ex: DB1, 10 bytes a partir do offset 0)
db_number = 1
start_address = 0
length = 10
data = plc.db_read(db_number, start_address, length)

# Escrever em uma área de memória
new_data = bytearray([1, 2, 3, 4, 5])
plc.db_write(db_number, start_address, new_data)

# Desconectar
plc.disconnect()