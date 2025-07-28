from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        inventory_response = requests.get("https://inventory-service-m53o.onrender.com/")
        return f"Order Service Active<br>Response from Inventory: {inventory_response.text}"
    except Exception as e:
        return f"Order Service Active<br>Failed to connect to Inventory Service: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
