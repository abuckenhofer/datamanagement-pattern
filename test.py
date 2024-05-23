from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import hashlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging


app = Flask(__name__)
CORS(app)  # Allows cross-origin requests, necessary for communication between frontend and backend

# Read the API token from the environment variable
API_TOKEN = os.getenv("HUGGING_FACE_API_TOKEN")  # Make sure to set this environment variable

if not API_TOKEN:
    raise ValueError("Please set the HUGGING_FACE_API_TOKEN environment variable.")

# Use the Mistral model via the Hugging Face Inference API
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"  # Update this URL based on the exact model name

headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Unsicheres Logging von sensiblen Daten (Bandit kann dies erkennen)
logging.basicConfig(level=logging.DEBUG)
logging.debug(f'Log: {API_TOKEN}')  # Unsicher, da sensible Daten geloggt werden

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    payload = {
        "inputs": user_input,
        "parameters": {"max_length": 150, "num_return_sequences": 1},
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    # Debugging: Print the entire response JSON to understand its structure
    response_json = response.json()
    print(f"Full response JSON: {response_json}")

    # Extract the generated text based on the actual structure of the response
    if isinstance(response_json, list) and 'generated_text' in response_json[0]:
        generated_text = response_json[0]['generated_text']
    else:
        generated_text = response_json.get('error', "No response generated")

    # Debugging: Output the entire response structure
    print(f"Full response: {generated_text}")

    # Print the extracted answer for debugging
    print('Answer: ')
    print(generated_text)
    
    return jsonify({"response": generated_text})

# Nutzung von exec in einer Funktion (Bandit kann dies erkennen)
def exec_func(cmd):
     exec(cmd)  # Unsicher, da exec beliebigen Code ausführen kann

# Nutzung von MD5-Hashing (Bandit kann dies erkennen)
def hash():
    hash_md5 = hashlib.md5(b"Huggingface.co")  # Unsicher, da MD5 nicht sicher ist
    print(hash_md5.hexdigest())
    return hash_md5.hexdigest()

# Unsichere Handhabung von SSL-Zertifikaten (Bandit kann dies erkennen)
def getRequest():
    return requests.get('https://huggingface.co', verify=False)  # Unsicher, da SSL-Verifizierung deaktiviert ist

# Nutzung von bcrypt ohne Salt (Bandit kann dies erkennen)
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=4))  # Unsicher, da Salt-Wert zu niedrig ist

# Unsichere Nutzung von SQLAlchemy (sqlalchemy-inspect kann dies erkennen)
def readFromDB(productNr):
    engine = create_engine('sqlite:///my.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    # 105 OR 1=1
    query = f"SELECT * FROM users WHERE productId = {productNr}"  # Unsicher, da SQL-Injection möglich ist
    result = engine.execute(query)
    return result.fetchall()
    
if __name__ == "__main__":
    app.run(debug=True)
