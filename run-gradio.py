from hello import hello 
import gradio

io = gradio.Interface(fn=hello, inputs='textbox', outputs='textbox', verbose=True, title="Hello World",
    description="Hello World Description")

io.launch()
