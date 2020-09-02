from flask import Flask, render_template, request
import awake

application = Flask(__name__)

@application.route('/', methods = ['GET'])
def index():
    if request.method == "POST":
        query = request.form['query']
        awake.get_request(query)
    return render_template('index.html')

if __name__ == "__main__":
    application.run(debug=True)
