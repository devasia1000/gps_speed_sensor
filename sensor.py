import serial, sys;
from Tkinter import *
import time

# check for presence of device port argument
if len(sys.argv) != 2:
    print "Usage: sudo python sensor.py <device port>";
    sys.exit(0);

root=Tk()

# initiate serial connection
ser = serial.Serial(port = sys.argv[1], baudrate = 4800);

# variable used to manage updated to GUI
speed_str = StringVar()

# keep reading from device
def update_label():

    while True:
        line = str(ser.readline());
        
        # isolate tag that contains speed information
        if "GPRMC" in line:
            
            #extract speed from line
            temp = line.split(",");

            if not str(temp[7]):
                # if NMEA is empty, print out 'No signal!'
                sys.stdout.write("No signal!\n");
                speed_str.set("No signal!\n");

            else:
                speed = float(temp[7]);
                # convert speed from knots to mph and write to STDOUT
                sys.stdout.write(str(speed*1.15078)+"\n");
                speed_str.set("{0:.2f}".format(speed*1.15078)+" mph");

            # update GUI
            root.update();


speed_label=Label(root, textvariable=speed_str, font=("Helvetica", 50))
speed_label.pack()
start_button=Button(root, text="start", command=update_label)
start_button.pack()
root.mainloop()
