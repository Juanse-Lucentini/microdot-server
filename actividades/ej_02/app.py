# Aplicacion del servidor
from microdot import Microdot, send_file
from boot import led1, led2, led3

app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html')

@app.route('/<dir>/<file>')
async def index(request, dir, file):
    return send_file("/{}/{}". format(dir, file))

@app.route('/led/toggle/<led>')
async def led_toggle(request, led):
    
    if led == "led1":
        led1.value(not led1.value())
        
    elif led == "led2":
        led2.value(not led2.value())
        
    elif led == "led3":
        led3.value(not led3.value())
        

app.run(port=80)