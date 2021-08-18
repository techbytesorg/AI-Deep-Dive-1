from flask import Flask, render_template, jsonify, request
import requests

# import all of these modules





# We need to convert 3 input features into the 20 polynomial features
# that the model can accept



app = Flask(__name__)


@app.route('/')
def main():

    return render_template("index.html")

@app.route('/call', methods=["GET"])
def get_weather():

    gender = request.args.get("gender")
    age = request.args.get("age")
    salary = request.args.get("salary")

    # Convert gender to lower case, and handle invalid inputs



    # Age must be integer


    
    # Salary must be integer



    # form input variables into a 1x20 torch.tensor


    # make prediction


 

   
    return jsonify({"code": 200, "msg": None})


if __name__ == "__main__":
    app.run(debug=True)