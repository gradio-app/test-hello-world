from hello import hello 
import gradio

INTERFACE = gradio.Interface(fn=hello, inputs='textbox', outputs='textbox')
