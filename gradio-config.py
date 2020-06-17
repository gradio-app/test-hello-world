from hello import hello 
import gradio
import sys
import time


io = gradio.Interface(fn=hello, inputs='textbox', outputs='textbox', server_name='0.0.0.0')

io.launch()

try:
    print("Entering infinite loop...")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit(0)

