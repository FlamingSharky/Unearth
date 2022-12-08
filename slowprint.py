import sys
from time import sleep
def slowprint(text, speed):
	for c in text + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		sleep(speed/10)

