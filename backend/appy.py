from flask import Flask, request, jsonify
app = Flask(__name__)

database = []

dic_erro = {
    "ERRO": "Digite um número válido !"
}


@app.route("/", methods=["GET", "POST"])
def calcula_imc():
    if request.method == "GET":
        return jsonify(database)
    else:
        dados = request.json
        if dados['peso'] <= 0 or dados['altura'] <= 0:
            return jsonify(dic_erro)
        else:
            imc = round(dados['peso'] / dados['altura'] ** 2, 2)
            dados['imc'] = imc
            database.append(dados)
        return jsonify(database)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
