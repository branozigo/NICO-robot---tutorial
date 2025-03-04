#COM ports  list and test
import serial
import serial.tools.list_ports

def check_serial_port(port_name):
    try:
        # Try to open the port
        ser = serial.Serial(port_name)
        ser.close()  # Close immediately after opening
        print(f"{port_name} is available and not in use.")
    except serial.SerialException as e:
        print(f"{port_name} is not available or is in use. Error: {e}")

# List all available serial ports
print("List of all available serial ports")
ports = serial.tools.list_ports.comports()
for port in ports:
    print("Port:")
    check_serial_port(port.device)
