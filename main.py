from flask import Flask, render_template, request, redirect, url_for
from cliente import Cliente
from registro import RegistroClientesApp

app = Flask(__name__, template_folder=".")

registro_clientes = RegistroClientesApp()

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = None
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        nit = request.form["nit"]
        cliente = Cliente(nombre, correo, nit)
        mensaje = registro_clientes.agregar_cliente(cliente)
    return render_template("index.html", mensaje=mensaje)

@app.route("/getClientes")
def get_clientes():
    clientes = registro_clientes.obtener_clientes()
    return render_template("clientes.html", clientes=clientes)

@app.route("/volver")
def volver():
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
