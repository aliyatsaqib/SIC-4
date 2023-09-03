import time
import random
from rpi_lcd import LCD
from actuator import *
from sensor import *
from send_data import * 
from time import sleep


lcd = LCD()

def cleanup():
	# Membersihkan pin GPIO pada Raspberry Pi
	GPIO.cleanup()
	
	
try:
	while True:
		print("Silahkan Tap Kartu Anda")
		lcd.text("Silahkan", 1)
		lcd.text("Tap Kartu Yaaaaa", 2)
		status=rfid_read()
		print(status)
		#status=["berhasil","gagal"]
		#random_status=random.choice(status)
		if  status=="berhasil":
			lcd.clear()
			#run(status)
			ledgreenon()
			#buzzeron()
			bip_benar()
			#time.sleep(0.1)
			lcd.text("Berhasil", 1)
			sleep(1)
			
		else:
			lcd.clear()
			#run(status)
			ledredon()
			#buzzeron()
			bip_salah()
			#time.sleep(0.5)
			lcd.text("Gagal", 1)
			sleep(1)
		buzzeroff()
		ledredoff()
		ledgreenoff()
		lcd.clear()
		# buzzeron()
		# ledredoff()
		# ledgreenon()
		# time.sleep(1)  # Memberi jeda sebelum membaca data berikutnya
		# buzzeroff()
		# ledredon()
		# ledgreenoff()
		# time.sleep(1)  # Memberi jeda sebelum membaca data berikutnya

except KeyboardInterrupt:
	# Memberhentikan program dengan menekan Ctrl + C
	cleanup()
