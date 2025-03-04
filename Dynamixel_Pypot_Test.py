import pypot.dynamixel

# Step 1: Find the available ports
available_ports = pypot.dynamixel.get_available_ports()
if not available_ports:
    raise IOError("No ports found! Connect your Dynamixel motor to your computer.")

# Step 2: Create a DxlIO object to interface with the motors
dxl_io = pypot.dynamixel.DxlIO(available_ports[0])  # Use the first available port

# Step 3: Scan for motors connected to the port
motor_ids = dxl_io.scan(range(40))  # Scan IDs from 0 to 40
if not motor_ids:
    raise IOError("No Dynamixel motors found!")
    
print(f"Motors found: {motor_ids}")

# Step 4: Enable torque and control motor position
motor_id = motor_ids[7]  # Nico head up-down

# Enable torque (required for movement)
torque=dxl_io.enable_torque([motor_id])
print("Torque: ", torque)

# Set the goal position of the motor
target_position = 20 * (4095/360)  # 30 - converts Dynamixel units into degrees
result = dxl_io.set_goal_position({motor_id: target_position})
print("Result ", result)

# Read the current position of the motor
current_position = dxl_io.get_present_position([motor_id])
print("Motor ID:", motor_id)
print(f"Current position:",current_position," degrees")

# Optional: Disable torque if you want to stop controlling the motor
dxl_io.disable_torque([motor_id])

# Step 5: Close the connection to the motor
dxl_io.close()
