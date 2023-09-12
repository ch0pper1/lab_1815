from flask import Flask,jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/test', methods=['GET', 'POST'])
def test():
    print("inside function")
    return jsonify({ "response": "yes, this worked." })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)