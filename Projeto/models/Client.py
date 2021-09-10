from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

from database import db

class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    companyName = db.Column(db.String(50), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    inclusionData = db.Column(db.DateTime, nullable=False)

    def to_json(self):
        return {"id": self.id, "name": self.name, "companyName": self.companyName, "cnpj": self.cnpj, "inclusionData": self.inclusionData.strftime('%d/%m/%Y')}
