from flask import Flask
from waitress import serve

DESARROLLO=True
PUERTO_ACCESO=5000

app = Flask(__name__)

@app.route("/health")
def health_ok():
	return "ok McKay"

@app.route("/")
def hello():
	return "¡Hola mundo!"

@app.route("/echo/<texto>")
def echo(texto):
	return(texto)

if __name__ == '__main__':
	if DESARROLLO == True:
		app.run(debug=True)								#Entorno de desarrollo
	else:
		serve(app,host='0.0.0.0', port=PUERTO_ACCESO)	#Entorno de producción
