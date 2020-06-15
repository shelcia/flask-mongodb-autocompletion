from flask import Flask, render_template
import json
import pymongo
app = Flask(__name__)

# get the access of your database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["country"]  # Use your database name
mycol = mydb["myCollection"]  # Use your Collection name

# this stores country names in a array
data = mycol.distinct("Country")


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
