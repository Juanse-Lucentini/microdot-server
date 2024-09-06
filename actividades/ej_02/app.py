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

app.run(port=80)