from flask import Flask, render_template, request
import subtitle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods =['POST', 'GET'])
def result():
    if request.method == 'POST':
        req = request.form
        res = subtitle.subTitle(req['Url'], int(req['Zip']))
        return render_template("result.html", result = res)

if __name__ == '__main__':
    app.run(debug=True)