import serial, sys;

# check for presence of device port argument
if len(sys.argv) != 2:
    print "Usage: python sensor.py <device port>";
    sys.exit(0);

# initiate serial connection
ser = serial.Serial(port = sys.argv[1], baudrate = 4800);

# keep reading from device
while True:
        line = str(ser.readline());
        sys.stdout.write(line);

ser.close();
