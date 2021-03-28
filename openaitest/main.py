# Takes in a text file full of processed reviews and extracts an array of sentiments

import os
import openai

os.environ["OPENAI_API_KEY"] = "keey"

openai.api_key = os.environ["OPENAI_API_KEY"]

with open('data.txt', 'r') as file:
  data = file.read().replace('\n', '')

#below code will summarize what needs to be improved  
 
#f = open("reviews.txt", "r")
#data = "Summarize what needs to be improved in the hospital based on the reviews below(ignore sentiment and quality of care):\n"
#data += f.read()
#data += "\nsummary:\n In general, the hospital should \n"

#response = openai.Completion.create(
# engine = "davinci-instruct-beta",
# prompt = data,
# temperature = 0.7,
# max_tokens = 64,
# top_p = 1,
# frequency_penalty = 0,
# presence_penalty = 0
#)

# Parse sentiments from file
sentiments = []
file1 = open("output.txt")
for line in file1.readlines():
    currentLine = (line.strip().split("Sentiment: "))
    sentimentVal = 0
    for i in currentLine:
        try:
            sentimentVal = float(i)
            if(sentimentVal > 0):
                sentiments.append(sentimentVal)
        except ValueError:
            pass
file1.close()
print(len(sentiments))

# Parse reviews from file
reviews = []
file1 = open("output.txt")
chunks = (file1.read().split("###"))
for index, item in enumerate(chunks):
    if (index % 2) != 0: # if index is odd (1, 3, 5, etc.)
        reviews.append(chunks[index])
file1.close()
print(len(reviews))

