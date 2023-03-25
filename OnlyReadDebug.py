import serial
import keyboard
port_name = "COM5"
ser = serial.Serial(port_name, 115200)


while True:
    try:
        if keyboard.is_pressed('q'):
            value = input("Enter the value of Freq: ")
            value = ''.join(e for e in value if e.isdigit())  # keeps only digits
            value = value + "\r\n"
            ser.write(str(value).encode('utf-8'))

        line = ser.readline().decode('utf-8').strip()
        line = ''.join(e for e in line if e.isalnum() or e.isspace())
        print(line)
    except KeyboardInterrupt:
        break