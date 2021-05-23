from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def datos():
	return render_template("datos.html",nombre="CITLALLY HERRERA MENDEZ",datos="DATOS PERSONALES",formacion="FORMACION ACADEMICA"
		,cursos="CERTIFICACIONES",lenguajes="IDIOMAS",interes="DATOS DE INTERES")

@app.route("/pasatiempos")
def pasatiempos():
	return render_template("pasatiempos.html",hobbies="PASATIEMPOS")

if __name__ == "__main__":
	app.run(debug=True)
