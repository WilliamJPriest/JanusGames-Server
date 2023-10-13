import json
import mysql.connector

mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database="newsletters"
)

mycursor = mydb.cursor()


def lambda_handler(event, context):
    print(event)
    
    email = event["email"]
    print(email)
    response_data = {"message": "Unsubscribed", "email": email}
    sql = "delete from clients where email = (email) VALUES (%s)"
    val = (email)
    print(val)
    mycursor.execute(sql, val)
    mydb.commit()
    # return jsonify(response_data)
    
    return {
        'statusCode': 200,
        'body': json.dumps(response_data)
    }

if __name__ == '__main__':
    lambda_handler.run(debug=True)

