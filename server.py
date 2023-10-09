from flask import Flask, request, jsonify
import datetime
import json
import csv
from flask_cors import CORS
import mysql.connector

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mbnewsletter"
)

mycursor = mydb.cursor()

app = Flask(__name__)
CORS(app)

@app.route('/newsletter', methods=['POST'])
def submitNewsletter():
    if request.method == 'POST':

        name = request.form.get("name")
        email = request.form.get("email")

        response_data = {"message": "Newsletter submission successful", "name": name}
        sql = "INSERT INTO clients (name, email) VALUES (%s, %s)"

        val = (name, email)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
