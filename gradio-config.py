from hello import hello 

INTERFACE = gradio.Interface(fn=h, inputs='textbox', outputs='textbox')
