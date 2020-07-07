from hello import hello 
import gradio

io = gradio.Interface(fn=hello, inputs='textbox', outputs='textbox', verbose=True, title='Hello World',
    description='Hello World Description', thumbnail='https://github.com/gradio-app/gradio_static/blob/master/static/img/logo.png?raw=true')

io.launch()
