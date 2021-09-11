from flask import Response, request,Blueprint
import json

from models.Client import Clients
from database import db

api = Blueprint('api', __name__)
@api.route("/clients", methods=["GET"])
def selectAllClients():
    clientsList = Clients.query.all()
    clientsJson = [client.to_json() for client in clientsList]

    return generateResponse(200, clientsJson, "ok", "null")

@api.route("/client/create", methods=["POST"])
def createClient():
    body = request.get_json()

    try:
        client = Clients(name=body["name"], companyName=body["companyName"],
                         cnpj=body["cnpj"], inclusionData=body["inclusionData"])
        print(client)
        db.session.add(client)
        db.session.commit()
        return generateResponse(200, client.to_json(), "Criado com sucesso", "null")
    except Exception as e:
        print(e)
        return generateResponse(400, {}, "Erro ao cadastrar", "Error")


@api.route("/client/update/e<id>", methods=["PUT"])
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
        return generateResponse(200, client.to_json(), "Atualizado com sucesso", "null")

    except Exception as e:
        print(e)
        return generateResponse(400, {}, "Erro ao atualzar", "Error")


@api.route("/client/delete/<id>", methods=["DELETE"])
def deleteClient(id):
    client = Clients.query.filter_by(id=id).first()

    try:
        db.session.delete(client)
        db.session.commit()
        return generateResponse(200, {}, "Apagado com sucesso", "null")
    except Exception as e:
        print(e)
        return generateResponse(400, {}, "Erro ao deletar", "Error")


def generateResponse(status, content, mensagem, error):
    body = {}
    body["status"] = status
    body["Clients"] = content
    body["Message"] = mensagem
    body["Error"] = error

    return Response(json.dumps(body), status=status, mimetype="application/json")