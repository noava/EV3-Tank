from flask import Flask, render_template, send_from_directory
import requests
import logging

class Count():
    count = 0
count = Count()

try:
    with open('count.txt', 'r') as f:
        count.count = int(f.read())
except:
    with open('count.txt', 'w') as f:
        f.write("0")
        count.count = 0

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/godtatt")
def godtatt():
    count.count += 1
    resp = requests.post("https://discordapp.com/api/webhooks/624587543857332243/VrPdiWg0Y6E4blFmAHsD7nQ7FoxsBHfopkoT7SjrYxJR9eNE2D8pL_zxi47SkmBoVN9O", data={"content": "Smørbukk nummer {} sendt!".format(count.count)})
    with open('count.txt', 'w') as f:
        f.write(str(count.count))
    return render_template('index2.html')

@app.route("/favicon.ico")
def icon():
    return send_from_directory("D:\\Mine dokumenter\\Skole\\Python\\EV3-Tank\\Smørbukk", "b.bmp")

 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
