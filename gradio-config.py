from hello import hello 
import gradio
import time

io = gradio.Interface(fn=hello, inputs='textbox', outputs='textbox', verbose=True)

io.launch()

time.sleep(60)
