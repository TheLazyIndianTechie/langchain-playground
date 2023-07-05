#Import OpenAI
from langchain.llms import OpenAI

#Set llm temperature
llm = OpenAI(temperature=0.9)


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

