import time
from gpiozero import Buzzer
import RPi.GPIO as GPIO

buzzer = Buzzer(17)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

def bip_benar():
	buzzer.on()
	#print("Buzzer On")
	time.sleep(0.1)  # Buzzer menyala selama 2 detik
			
	buzzer.off()
	#print("Buzzer Off")
	time.sleep(0.1)  # Jeda selama 2 detik sebelum mengulang
	
	buzzer.on()
	#print("Buzzer On")
	time.sleep(0.1)  # Buzzer menyala selama 2 detik
			
	buzzer.off()
	#print("Buzzer Off")
	time.sleep(0.1)  # Jeda selama 2 detik sebelum mengulang
	
def bip_salah():
	buzzer.on()
	#print("Buzzer On")
	time.sleep(0.1)  # Buzzer menyala selama 2 detik
			
	buzzer.off()
	#print("Buzzer Off")
	time.sleep(0.1)  # Jeda selama 2 detik sebelum mengulang
	
	buzzer.on()
	#print("Buzzer On")
	time.sleep(0.1)  # Buzzer menyala selama 2 detik
			
	buzzer.off()
	#print("Buzzer Off")
	time.sleep(0.1)  # Jeda selama 2 detik sebelum mengulang
	
	buzzer.on()
	#print("Buzzer On")
	time.sleep(0.1)  # Buzzer menyala selama 2 detik
			
	buzzer.off()
	#print("Buzzer Off")
	time.sleep(0.1)  # Jeda selama 2 detik sebelum mengulang
	
	buzzer.on()
	#print("Buzzer On")
	time.sleep(0.1)  # Buzzer menyala selama 2 detik
			
	buzzer.off()
	#print("Buzzer Off")
	time.sleep(0.1)  # Jeda selama 2 detik sebelum mengulang
	
	buzzer.on()
	#print("Buzzer On")
	time.sleep(0.1)  # Buzzer menyala selama 2 detik
			
	buzzer.off()
	#print("Buzzer Off")
	time.sleep(0.1)  # Jeda selama 2 detik sebelum mengulang
	
	buzzer.on()
	#print("Buzzer On")
	time.sleep(0.1)  # Buzzer menyala selama 2 detik
			
	buzzer.off()
	#print("Buzzer Off")
	time.sleep(0.1)  # Jeda selama 2 detik sebelum mengulang
	
	buzzer.on()
	#print("Buzzer On")
	time.sleep(0.1)  # Buzzer menyala selama 2 detik
			
	buzzer.off()
	#print("Buzzer Off")
	time.sleep(0.1)  # Jeda selama 2 detik sebelum mengulang
	
	buzzer.on()
	#print("Buzzer On")
	time.sleep(0.1)  # Buzzer menyala selama 2 detik
			
	buzzer.off()
	#print("Buzzer Off")
	time.sleep(0.1)  # Jeda selama 2 detik sebelum mengulang	

def buzzeron():
	buzzer.on()
	#print("buzzer menyala")
	
def buzzeroff():
	buzzer.off()
	#print("buzzer mati")

def ledredon():
	GPIO.output(14,GPIO.HIGH)
	#print("led merah nyala")
	
def ledredoff():
	GPIO.output(14,GPIO.LOW)
	#print("led merah mati")
	
def ledgreenon():
	GPIO.output(15,GPIO.HIGH)
	#print("led hijau nyala")
	
def ledgreenoff():
	GPIO.output(15,GPIO.LOW)
	#print("led hijau mati")
