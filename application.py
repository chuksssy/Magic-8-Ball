#import flask package

from flask import Flask, request, render_template
import random

#specifyng flask instance and assigning it to app. We can now reference the application using "app"
app = Flask(__name__)

@app.route("/", methods= ['GET', 'POST'])

#define the function | capture the name
def welcome():

    possibleResponses = ["You can count on it","Yes","Only time will tell","My reply is No","Not Sure, Ask me again Later","Its doubtful","I would not advise it"]
    response = None
    question = ''

    if request.method == 'POST' and 'questionIn' in request.form:
        question = (request.form.get('questionIn')).lower()

    if question == '':
        response = ""

    elif question == "quit":
        response = "Bye-Bye! Have a wonderful day!"

    else:
        if request.method == 'POST':
            response = random.choice(possibleResponses)

    return render_template("index.html", printedResponse=response)

app.run(host='0.0.0.0', port='5000')
