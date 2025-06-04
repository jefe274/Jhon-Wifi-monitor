from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('<h1>📶 Dashboard de Red en Línea</h1><p>Todos los dispositivos conectados aparecerán aquí.</p>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
