from flask import Flask, request, jsonify

app = Flask(__name__)
produtos = []

@app.route("/produtos", methods=["GET", "POST"])
def gerenciar_produtos():
 if request.method == "POST":
  produto = request.json
  produtos.append(produto)
  return jsonify(produto), 201
  return jsonify(produtos)
  
if __name__ == "__main__":
 app.run(debug=True)