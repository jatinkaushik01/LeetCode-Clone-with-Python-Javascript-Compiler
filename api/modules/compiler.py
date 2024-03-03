import os
import datetime
import js2py
import io,sys
from io import StringIO
import requests


def execute_py(code):
	try:

		#save original standart output reference
		old_stdout = sys.stdout

		#the output of exec() normally is sent to sys.stdout
		#but here we redirect it to StringIO() to get output in memory object without writing to file(.txt)
		new_stdout = io.StringIO()
		#Redirect python stdout into the builtin io.StringIO() buffer
		sys.stdout = new_stdout

		exec(code)
		result = sys.stdout.getvalue().strip()
		

	except Exception as e:
		result = str(e)
		
	finally:
		sys.stdout.close()
		#put stdout back to normal 
		sys.stdout = old_stdout
		print('res',result)
		return result



def execute_js(code):
	try:

		print("I am Here!")
		#url = 'https://friendly-zebra-x55wrj6qr59gcwjv-8080.app.github.dev/submit_js_code'
		# url = 'http://localhost:8080/submit_js_code'
		url = "http://192.168.49.2/submit_js_code"
		dataToSend = {'js_code': code}
		x = requests.post(url, data = dataToSend)
		print(x.text)

		# context = js2py.EvalJs()

		#save original standart output reference
		# old_stdout = sys.stdout

		#the output of exec() normally is sent to sys.stdout
		#but here we redirect it to StringIO() to get output in memory object without writing to file(.txt)
		# new_stdout = io.StringIO()
		#Redirect python stdout into the builtin io.StringIO() buffer
		# sys.stdout = new_stdout


		# context.execute(code)
		# print(context.output)	
		# result = sys.stdout.getvalue().strip()
		# sys.stdout.close()
		#put stdout back to normal 
		# sys.stdout = old_stdout

	except Exception as e:
		return str(e)
	# return result.replace("'","")
	return x.text
