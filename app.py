#Import OpenAI
from langchain.llms import OpenAI
from flask import Flask, request, render_template


#Set llm temperature
llm = OpenAI(temperature=0.9)



#Webapp code
app = Flask(__name__)

from flask import Flask, render_template

app = Flask(__name__)


#jinja code
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    # Process the form data here
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
### End Webapp Code



greeting = "Hello, there!"

name = input("Enter your name: ")
print("Hello, " + name)


#prompt user for question
question = input("Query: ")
print("Processing...")

#Query llm for prediction
answer = llm.predict(question)

print("\n\n")

#Print prediction
print(name + ", " + answer)

