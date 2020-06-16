from hello import hello 

INTERFACE = gradio.Interface(fn=hello, inputs='textbox', outputs='textbox')
