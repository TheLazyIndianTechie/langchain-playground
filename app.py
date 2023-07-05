#Import OpenAI
from langchain.llms import OpenAI
from flask import Flask, request, render_template

#Set llm temperature
llm = OpenAI(temperature=0.9)



### WEBAPP CODE ###

# Create an app
app = Flask(__name__)


## Create route handlers

# Landing root route handler ;)
@app.route('/')
def index():
    return render_template('index.html')


# Form route handler
@app.route('/submit', methods=['POST'])
def submit():
    greeting = "Hello, there!"
    name = request.form.get('name')
    question = request.form.get('question')

    answer = llm.predict(question)

    return render_template('result.html', name=name, answer=answer)

# Main app
if __name__ == '__main__':
    app.run()




###### BACKUP SOURCE CODE #####
###### DO NOT DELETE #####

### Source Code ###

# greeting = "Hello, there!"

# name = input("Enter your name: ")
# print("Hello, " + name)


# #prompt user for question
# question = input("Query: ")
# print("Processing...")

# #Query llm for prediction
# answer = llm.predict(question)

# print("\n\n")

# #Print prediction
# print(name + ", " + answer)


###### END BACKUP SOURCE CODE #####
