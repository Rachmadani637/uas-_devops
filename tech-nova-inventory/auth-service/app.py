from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Auth Service Active"

@app.route("/check-inventory")
def check_inventory():
    try:
        # Ganti dengan URL Render dari inventory-service kamu
        inventory_url = "https://auth-service-ibv8.onrender.com"
        response = requests.get(inventory_url)
        return f"Response from Inventory Service: {response.text}"
    except Exception as e:
        return f"Error contacting Inventory Service: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
