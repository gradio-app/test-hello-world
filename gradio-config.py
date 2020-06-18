from hello import hello 
import gradio

io = gradio.Interface(fn=hello, inputs='textbox', outputs='textbox', verbose=True, server_name='0.0.0.0')

io.launch()
