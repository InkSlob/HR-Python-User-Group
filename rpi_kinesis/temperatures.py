import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')
device_files = []
for sensor in device_folder:
  tmp = None
  tmp = sensor + '/w1_slave'
  device_files.append(tmp)

def read_temp_raw(device_file):
  f = open(device_file, 'r')
  lines = f.readlines()
  f.close()
  return lines

def read_temp(device_file):
  lines = read_temp_raw(device_file)
  while lines[0].strip()[-3:] != 'YES':
    time.sleep(0.2)
    lines = read_temp_raw()
  equals_pos = lines[1].find('t=')
  if equals_pos != -1:
    temp_string = lines[1][equals_pos+2:]
    temp_c = float(temp_string) / 1000.0
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    return temp_c, temp_f

while True:
  for device_file in device_files: 
    c, f = read_temp(device_file)
    sensor = device_file[28:35]
    #output = "sensor: %s, C: %f, F: %f" % (sensor, c, f) 
    output = {"sensor":sensor, \
              "c"     :c,      \
              "f"     :f}
    print(output)
    time.sleep(1)
