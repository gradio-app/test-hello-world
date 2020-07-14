from hello import hello 
import gradio

io = gradio.Interface(fn=hello, inputs='text', outputs='text', verbose=True, title='Hello Worl
    description='Hello World Description', thumbnail='https://github.com/gradio-app/gradio_static/blob/master/static/img/logo.png?raw=true')

io.launch()
