### MAIN ###
import signal
import sys
import RPi.GPIO as GPIO
from WebServer import WebServer
def shutdownServer(sig, unused):
    """
    Shutsdown server from a SIGINT recieved signal
    """
    server.shutdown()
    GPIO.cleanup()
    sys.exit(1)

signal.signal(signal.SIGINT, shutdownServer)
server = WebServer(8080)
server.start()
print("Press Ctrl+C to shut down server.")
