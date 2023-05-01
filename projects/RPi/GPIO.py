#class GPIO:
BOARD = 0
BCM = 1
IN = 0
OUT = 1
io = [None, #zero index not used for pin #
    False,False,False,False,False,
    False,False,False,False,False,
    False,False,False,False,False,
    False,False,False,False,False,
    False,False,False,False,False,
    False,False,False,False,False,
    False,False,False,False,False,
    False,False,False,False,False]

def setmode(mode):
    pass

def setwarnings(state):
    pass

def setup(pin, in_out, initial=False):
    pass    

def input(pin):

    return io[pin]

def output(pin, state):
    io[pin] = state

def cleanup():
    pass


class PWM:
    # initialise PWM channel
    def __init__(self, channel, frequency):
        self.chanel = channel
        self.frequency = frequency
    def start(self, dutycycle):
        self.dutycycle = dutycycle
    
    # where freq is the new frequency in Hz
    def ChangeFrequency(self, frequency):
        self.frequency = frequency

    # where 0.0 <= dc <= 100.0
    def ChangeDutyCycle(self, dutycycle):
        if dutycycle < 0 or dutycycle > 100:
            raise ValueError("Invalid duty cycle value.")
        self.dutycycle = dutycycle

    # stop PWM generation
    def stop(self):
        pass        