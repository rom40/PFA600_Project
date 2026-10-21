from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException

client = ModbusTcpClient("127.0.0.1", port=502)

def write_output(address, value):
 result = client.write_register(address, value)
 print(f"Successfully wrote {value} to address {address}")


def read_input(address):
 result = client.read_holding_registers(address=address, count=1)
 return result.registers[0]