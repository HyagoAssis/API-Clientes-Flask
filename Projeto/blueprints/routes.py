from flask import Response, request,Blueprint
import json

from models.Client import Clients
from database import db

api = Blueprint('api', __name__)
@api.route("/clients", methods=["GET"])
def selectAllClients():
    clientsList = Clients.query.all()
    clientsJson = [client.to_json() for client in clientsList]

    return gera_response(200, clientsJson, "ok", "null")


@api.route("/client/<id>", methods=["GET"])
def selectClient(id):
    client = Clients.query.filter_by(id=id).first()
    clientJson = client.to_json()

    return gera_response(200, clientJson, "ok", "null")


@api.route("/client", methods=["POST"])
def createClient():
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


@api.route("/client/<id>", methods=["PUT"])
def updateClient(id):
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


@api.route("/client/<id>", methods=["DELETE"])
def deleteClient(id):
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