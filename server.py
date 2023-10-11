import json
from typing import Self
import mysql.connector

mydb = mysql.connector.connect(
#   host="database",
#   user="user",
#   password="password",
  database="newsletters"
)

mycursor = mydb.cursor()


def lambda_handler(event, context):
    
    name = event["name"]
    email = event["email"]
    
    response_data = {"message": "Newsletter submission successful", "name": name}
    sql = "INSERT INTO clients (name, email) VALUES (%s, %s)"
    val = (name, email)
    mycursor.execute(sql, val)
    mydb.commit()
    
    print(mycursor.rowcount, "record inserted.")
    
    return {
        'statusCode': 200,
        'body': json.dumps(response_data)
    }

      

# def lambda_handler(event, context):
#   return awsgi.response(app, event, context, base64_content_types={"image/png"})

if __name__ == '__main__':
    Self.run(debug=True)


