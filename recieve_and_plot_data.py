import serial

arduinoComPort = "/dev/ttyACM0"

baudRate = 9600

serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)


# main loop to read data from the Arduino, then display it
while True:
  lineOfData = serialPort.readline().decode(encoding = "ascii")
  print(lineOfData)

  if len(lineOfData) > 0:
      pass

    #convert data into 3 integers
    # a, b, c = (int(x) for x in lineOfData.split(','))



    # print("a = " + str(a), end="")
    # print(", b = " + str(b), end="")
    # print(", c = " + str(c), end="")
