from flask import Flask, render_template,  request
import pickle

app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    pred = 0
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

        # print(one, two, three, four, five, six, seven, eight, nine, ten)

        feature_list =[]
        feature_list.append(int(one))
        feature_list.append(int(two))
        feature_list.append(int(three))
        feature_list.append(int(four))
        feature_list.append(int(five))
        feature_list.append(int(six))
        feature_list.append(int(seven))
        feature_list.append(int(eight))
        feature_list.append(int(nine))
        feature_list.append(int(ten))
 
        # print(feature_list) // to print feature list values

        pred = prediction(feature_list)
        # print(pred) // // to print predicted value


    return render_template("index.html", pred = pred)


if __name__== '__main__':
    app.run(debug=True)