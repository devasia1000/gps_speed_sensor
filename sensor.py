import serial, sys;

# check for presence of device port argument
if len(sys.argv) != 2:
    print "Usage: sudo python sensor.py <device port>";
    sys.exit(0);

# initiate serial connection
ser = serial.Serial(port = sys.argv[1], baudrate = 4800);

# keep reading from device
while True:
       
        line = str(ser.readline());
        
        # isolate tag that contains speed information
        if "GPRMC" in line:
            
            #extract speed from line
            temp = line.split(",");

            if not str(temp[7]):
                # if NMEA is empty, print out 'No signal!'
                sys.stdout.write("No signal!\n");

            else:
                speed = float(temp[7]);
                # convert speed from knots to mph and write to STDOUT
                sys.stdout.write(str(speed*1.15078)+"\n");

ser.close();
