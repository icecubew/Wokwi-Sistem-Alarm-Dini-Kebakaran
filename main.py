import dht
import machine
import time

class DHT22:
    def __init__(self, pin):
        self.d = dht.DHT22(machine.Pin(pin))
        
    def measure(self):
        self.d.measure()
    
    def temperature(self):
        return self.d.temperature()
    
    def humidity(self):
        return self.d.humidity()

class Buzzer:
    def __init__(self, pin):
        self.buzzer = machine.Pin(pin, machine.Pin.OUT)
        
    def on(self):
        self.buzzer.value(1)
        
    def off(self):
        self.buzzer.value(0)

# Inisialisasi DHT22 
sensor = DHT22(4)

# Inisialisasi Buzzer
buzzer = Buzzer(22)

while True:
    sensor.measure()
    temperature = sensor.temperature()
    humidity = sensor.humidity()
    
    if 19 < temperature <= 30 and humidity <= 55:
        status = "Suhu normal, Kelembapan  normal, Situasi Aman Tentram Sentosa"
        buzzer.off()
    elif temperature >= 30 and temperature < 40 and humidity >30 and humidity < 55:
        status = "Suhu tinggi, Kelembapan rendah, Situasi Siaga"
        buzzer.off()
    elif temperature > 40 and humidity < 30:
        status = "SUHU SANGAT TINGGI, Kelembapan sangat rendah, PERINGATAN KEBAKARAN"
        buzzer.on()
    else:
        status = "Invalid condition"
    
    print("============================= PEMBACAAN SENSOR ================================")
    print("Temperature: {}°C".format(temperature))
    print("Humidity: {}%".format(humidity))
    print("Status:", status)
    print("===============================================================================")
    time.sleep(5)
