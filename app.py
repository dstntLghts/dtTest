from flask import Flask,render_template,json
import re
import atkinsieve

app = Flask(__name__)

@app.route('/')
def hello():
    x = "Hey! This web service has the purpose of extracting the prime numbers up to a given integer (2-100000).\nPlease go to the path /primes for more information."
    return render_template("welcome.html", title="Hello", content=x)

@app.route('/primes')
def primeinfo():
    x = "Use the path /primes/atkin/key, to get a JSON of the primes until up to the key integer by using the Sieve of Atkin\nor use the path primes/xml/atkin/key, to get a xml output of the same function.\n"
    return render_template("usage.html", title="How to use this service", content=x)   

@app.route('/primes/atkin/<key>')
def makejsonat(key):
    if re.match('^[0-9]*$',key) and int(key) in range(2, 100000):
        data = {"initial": key}
        data['primes'] = atkinsieve.atkin(int(key))
        json_data = json.dumps(data) 
        return json_data 
    else:
        return failure()

@app.route('/primes/xml/atkin/<key>')
def makexmlat(key):
    if re.match('^[0-9]*$',key) and int(key) in range(2, 100000): 
        xml=()
        xml = atkinsieve.atkin(int(key))
        return render_template("primes.xml", number=key, title="Sieve of Atkin", content=xml)
    else:
        return failure()     

@app.route('/failure')
def failure():
    x = "Something went wrong!!\n The services /primes/atkin/key and /primes/xml/atkin/key are usable, only for integers between 2 - 100000. Thank you!\n"
    return render_template("fail.html", title="How to use this service", content=x)