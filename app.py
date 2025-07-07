from flask import Flask, render_template, request

app = Flask(__name__)

# Diccionario con equivalencias
meses = {
    "enero": ["1", "01", "enero", "ene"],
    "febrero": ["2", "02", "febrero", "feb"],
    "marzo": ["3", "03", "marzo", "mar"],
    "abril": ["4", "04", "abril", "abr"],
    "mayo": ["5", "05", "mayo", "may"],
    "junio": ["6", "06", "junio", "jun"],
    "julio": ["7", "07", "julio", "jul"],
    "agosto": ["8", "08", "agosto", "ago"],
    "septiembre": ["9", "09", "septiembre", "sep"],
    "octubre": ["10", "octubre", "oct"],
    "noviembre": ["11", "noviembre", "nov"],
    "diciembre": ["12", "diciembre", "dic"]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    entrada = request.form["mes"].strip().lower()
    for mes, variantes in meses.items():
        if entrada in variantes:
            mensaje = f"Naciste en {mes.upper()}... qué sorpresa 😏"
            if mes == "noviembre":
                mensaje += " ¡POBRE CRIATURA!"
            break
    else:
        mensaje = "¿Ese mes existe? ¿Vienes de otro plano?"

    return render_template("resultado.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
