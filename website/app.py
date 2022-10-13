from flask import Flask, render_template,  request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        one = request.form['one']
        two = request.form['two']
        three = request.form['three']
        four = request.form['four']
        five = request.form['five']
        six = request.form['six']
        seven = request.form['seven']
        eight = request.form['eight']
        nine = request.form['nine']
        ten = request.form['ten']

        print(one, two, three, four, five, six, seven, eight, nine, ten)
        
    return render_template("index.html")


if __name__== '__main__':
    app.run(debug=True)