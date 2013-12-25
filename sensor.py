import serial, sys;
from Tkinter import *
import time

# check for presence of argument
if len(sys.argv) != 2:
    print "Usage: sudo python sensor.py <device port>";
    sys.exit(0);

root=Tk()

# initiate serial connection
ser = serial.Serial(port = sys.argv[1], baudrate = 4800);

# synchronize updates to our GUI
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
                # convert speed from knots to mph
                speed = float(temp[7])*1.15078;

                # format speed to 2 decimal places
                sys.stdout.write(str(speed)+"\n");
                speed_str.set("{0:.2f}".format(speed)+" mph");

            # update GUI
            root.update();

# create label
speed_label=Label(root, textvariable=speed_str, font=("Helvetica", 100))
speed_label.pack()

# create start button
start_button=Button(root, text="start", command=update_label)
start_button.pack()

# start GUI thread
root.mainloop()
