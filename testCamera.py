from picamera import PiCamera
from time import sleep
import io

class TestCamera:
	def __init__(self):
		print('hi')
		self.camera = PiCamera()

	def capture(self):
		self.camera.capture('./static/capture.jpg')

	def stream(self):
		my_stream = io.BytesIO()
    		self.camera.start_preview()
    		# Camera warm-up time
    		sleep(2)
    		self.capture(my_stream, 'jpeg')

camera = TestCamera()
camera.stream()
