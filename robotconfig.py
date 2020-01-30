{
    # DONT CHANGE ANYTHING ON THE LEFTSIDE OF COLONS, THOSE ARE HARD-CODED!
    # TRUE AND FALSE MUST BE CAPITALIZED
    # String values should be in quotes and correspond exactly (string values- controller names, unit types, etc.)
    # Class names of motor controllers used.
    # Note: The first motor on each side should always be a Talon SRX/FX, as the
    # VictorSPX does not support encoder connections
    "rightControllerTypes": ("WPI_TalonSRX", "WPI_TalonSRX"),
    "leftControllerTypes": ("WPI_TalonSRX", "WPI_TalonSRX"),
    # Note: The first id in the list of ports should be the one with an encoder
    # Ports for the left-side motors - pwm
    "leftMotorPorts": (0),
    # Ports for the right-side motors - pwm
    "rightMotorPorts": (1),
    # Inversions for the left-side motors
    "leftMotorsInverted": (False, False),
    # Inversions for the right side motors
    "rightMotorsInverted": (False, False),
    # Wheel diameter (in units of choice(inch)- will dictate units of analysis)
    "wheelDiameter": 6,
    # If your robot has only one encoder, set all right encoder fields to `None`
    # Encoder edges-per-revolution (*NOT* cycles per revolution!)
    # This value should be the edges per revolution *of the wheels*, and so
    # should take into account gearing between the encoder and the wheels
    "encoderEPR": 512,
    # Whether the left encoder is inverted
    "leftEncoderInverted": (False),
    # Whether the right encoder is inverted:
    "rightEncoderInverted": (False),
    # Your gyro type
    "gyroType": "NavX",
    # Whatever you put into the constructor of your gyro
    # Could be:
    # "SPI.Port.kMXP" (MXP SPI port for NavX or ADXRS450),
    # "SerialPort.Port.kMXP" (MXP Serial port for NavX),
    # "I2C.Port.kOnboard" (Onboard I2C port for NavX),
    # "0" (Pigeon CAN ID or AnalogGyro channel),
    # "new WPI_TalonSRX(3)" (Pigeon on a Talon SRX),
    # "leftSlave" (Pigeon on the left slave Talon SRX/FX),
    # "" (NavX using default SPI, ADXRS450 using onboard CS0, or no gyro)
    "gyroPort": "",
}

