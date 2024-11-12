#including files
import functionDictionary as fd
import noteDictionary as nd

# Including system libraries
import pyvisa
from time import sleep

# Connecting the device
rm = pyvisa.ResourceManager()
device = rm.open_resource("USB0::0x0957::0x2607::MY59003077::0::INSTR")  #-----> add the usb address
device.write("OUTP1:LOAD 33")
device.write("OUTP2:LOAD 33")
#device.write("UNIT:ANGL:DEG")
device.write("SOUR2:TRAC ON")
# Setting device timeout to 1 sec
device.timeout = 1000


# playNote function
# param : note, noteDuration, pieceSpeed(100), function
def playNote(note, noteDuration, pieceSpeed = 100, function = "sine"):
    durationDictionary = {
        "full": 4*(60/pieceSpeed),
        "half": 2*(60/pieceSpeed),
        "half_pointed": 3*(60/pieceSpeed),
        "quarter": 1*(60/pieceSpeed),
        "quarter_pointed": 1.5*(60/pieceSpeed),
        "eighth": 0.5*(60/pieceSpeed),
        "eighth_pointed": 0.75*(60/pieceSpeed),
        "sixteenth": 0.25*(60/pieceSpeed)
        }

    device.write("SOUR1"+fd.funcDict[function] + nd.noteDict[note] + ", 30mVpp, 0V")  # --->Writing magnitude and offset
    #device.write("SOUR2"+fd.funcDict[function] + nd.noteDict[note] + ", 30mVpp, 0V")  # --->Writing magnitude and offset
    print("SOUR1"+fd.funcDict[function] + nd.noteDict[note] + ", 30mVpp, 0V") # ----->Writing magnitude and offset
    print("SOUR2"+fd.funcDict[function] + nd.noteDict[note] + ", 30mVpp, 0V") # ----->Writing magnitude and offset
    # Usually, magnitude = 30mVpp and offset = 0V
    # Turning the outputs on
    device.write("OUTP1 ON")
    device.write("OUTP2 ON")

    # Calculating duration of the note:
    # duration = pieceSpeed*60

    sleep(durationDictionary[noteDuration])

    # Turning off the outputs
    device.write("OUTP1 OFF")
    device.write("OUTP2 OFF")

    sleep(0.05)