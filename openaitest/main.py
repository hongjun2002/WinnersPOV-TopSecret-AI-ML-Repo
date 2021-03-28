# Takes in a text file full of processed reviews and extracts an array of sentiments

import os
import openai

os.environ["OPENAI_API_KEY"] = "sk-x7wPkzm7kRacZPOWZhbOT727pPAY65xRFiDSYCUQ"

openai.api_key = os.environ["OPENAI_API_KEY"]

with open('data.txt', 'r') as file:
  data = file.read().replace('\n', '')

f = open("output.txt", "r")
data = "Summarize what needs to be improved in the hospital based on the reviews below(ignore sentiment and quality of care):\n"
data += f.read()
data += "\nsummary:\n In general, the hospital should \n"

response = openai.Completion.create(
 engine = "davinci-instruct-beta",
 prompt = data,
 temperature = 0.7,
 max_tokens = 64,
 top_p = 1,
 frequency_penalty = 0,
 presence_penalty = 0
)
print(response.choices[0].text)

sentiments = []
quality = []
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
    currentLine1 = (line.strip().split("Quality of Care: "))
    QualityVal = 0
    for i in currentLine:
        try:
            QualityVal = float(i)
            if(QualityVal > 0):
                quality.append(QualityVal)
        except ValueError:
            pass
          
print(sentiments)
print(quality)
file1.close()
