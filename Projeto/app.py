from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:drb49f@localhost/prova'

db = SQLAlchemy(app)


class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    companyName = db.Column(db.String(50), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    inclusionData = db.Column(db.DateTime, nullable=False)

    def to_json(self):
        return {"id": self.id, "name": self.name, "companyName": self.companyName, "cnpj": self.cnpj, "inclusionData": self.inclusionData.strftime('%d/%m/%Y')}


@app.route("/clients", methods=["GET"])
def seleciona_usuarios():
    clientsList = Clients.query.all()
    clientsJson = [client.to_json() for client in clientsList]

    return gera_response(200, clientsJson, "ok", "null")


@app.route("/client/<id>", methods=["GET"])
def seleciona_usuario(id):
    client = Clients.query.filter_by(id=id).first()
    clientJson = client.to_json()

    return gera_response(200, clientJson, "ok", "null")


@app.route("/client", methods=["POST"])
def cria_usuario():
    body = request.get_json()

    try:
        client = Clients(name=body["name"], companyName=body["companyName"],
                         cnpj=body["cnpj"], inclusionData=body["inclusionData"])
        print(client)
        db.session.add(client)
        db.session.commit()
        return gera_response(201, client.to_json(), "Criado com sucesso", "null")
    except Exception as e:
        print(e)
        return gera_response(400, {}, "Erro ao cadastrar", "Error")


@app.route("/client/<id>", methods=["PUT"])
def atualiza_usuario(id):
    client = Clients.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if('name' in body):
            client.name = body['name']
        if('companyName' in body):
            client.companyName = body['companyName']
        if('cnpj' in body):
            client.cnpj = body['cnpj']
        if('inclusionData' in body):
            client.inclusionData = body['inclusionData']

        db.session.add(client)
        db.session.commit()
        return gera_response(201, client.to_json(), "Atualizado com sucesso", "null")

    except Exception as e:
        print(e)
        return gera_response(400, {}, "Erro ao atualzar", "Error")


@app.route("/client/<id>", methods=["DELETE"])
def deleta_usuario(id):
    client = Clients.query.filter_by(id=id).first()

    try:
        db.session.delete(client)
        db.session.commit()
        return gera_response(201, {}, "Apagado com sucesso", "null")
    except Exception as e:
        print(e)
        return gera_response(400, {}, "Erro ao deletar", "Error")


def gera_response(status, content, mensagem, error):
    body = {}
    body["status"] = status
    body["Clients"] = content
    body["Message"] = mensagem
    body["Error"] = error

    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run()
