import random
import json
import torch
import webbrowser
import datetime
from Brain import NeuralNet
from NeturalNetwork import bag_of_words,tokenize
from Task import NonInputExecution
from Listen import Listen
from Speak import Say

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Say("Good Morning!")

    elif hour >= 12 and hour < 18:
        Say("Good Afternoon!")

    else:
        Say("Good Evening!")

    Say("I am baiust guide assistant. How can I help you sir?")



def Main():

    sentence = Listen()


    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:

        for intent in intents['intents']:

            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])

                if "time" in reply:
                    NonInputExecution(reply)

                elif "date" in reply:
                    NonInputExecution(reply)

                elif "day" in reply:
                    NonInputExecution(reply)

                elif tag == "cse_faculty":
                    Say(reply)
                    webbrowser.open("https://cse.baiust.edu.bd/academic_personnel")

                elif tag == "triple_e_faculty":
                    Say(reply)
                    webbrowser.open("https://ce.baiust.edu.bd/academic_personnel")

                elif tag == "ce_faculty":
                    Say(reply)
                    webbrowser.open("https://ce.baiust.edu.bd/academic_personnel")

                elif tag == "bba_faculty":
                    Say(reply)
                    webbrowser.open("https://dba.baiust.edu.bd/academic_personnel")

                elif tag == "english_faculty":
                    Say(reply)
                    webbrowser.open("https://eng.baiust.edu.bd/academic_personnel")

                elif tag == "law_faculty":
                    Say(reply)
                    webbrowser.open("https://law.baiust.edu.bd/academic_personnel")

                elif tag == "portal":
                    Say(reply)
                    webbrowser.open("https://iumss.baiust.edu.bd/")

                elif tag == "location":
                    Say(reply)
                    webbrowser.open("https://www.google.com/maps/place/Bangladesh+Army+International+University+of+Science+and+Technology+(BAIUST)/@23.4773671,91.1112492,17z/data=!4m5!3m4!1s0x37547b8b07235dcd:0x1f168ba787f7f6d2!8m2!3d23.4770929!4d91.1136854")

                elif tag == "ragister_officer":
                    Say(reply)
                    webbrowser.open("https://www.baiust.edu.bd/organization-member/colonel-suman-kumar-barua-retd")

                elif tag == "vc":
                    Say(reply)
                    webbrowser.open("https://www.baiust.edu.bd/organization-member/k-m-salzar-hossain")

                elif tag == "eee_head":
                    Say(reply)
                    webbrowser.open("https://eee.baiust.edu.bd/faculty/profile/shah-md.-salimullah")

                elif tag == "cse_head":
                    Say(reply)
                    webbrowser.open("https://cse.baiust.edu.bd/faculty/profile/mohammad-asaduzzaman-khan")

                elif tag == "ce_head":
                    Say(reply)
                    webbrowser.open("https://www.baiust.edu.bd/organization-member/k-m-salzar-hossain")

                elif tag == "bba_head":
                    Say(reply)
                    webbrowser.open("https://dba.baiust.edu.bd/faculty/profile/dr-fatema-johara")

                elif tag == "english_head":
                    Say(reply)
                    webbrowser.open("https://eng.baiust.edu.bd/faculty/profile/6")

                elif tag == "law_head":
                    Say(reply)
                    webbrowser.open("https://law.baiust.edu.bd/faculty/profile/shakhawat-hossain")

                elif tag == "bye":
                    Say(reply)
                    exit()

                elif tag == "admission":
                    Say(reply)
                    webbrowser.open("https://admission.baiust.edu.bd/admission/apply-online/start")

                elif tag =="website":
                    Say(reply)
                    webbrowser.open("https://www.baiust.edu.bd/")

                elif tag =="facebook":
                    Say(reply)
                    webbrowser.open("https://www.facebook.com/baiust/")

                elif tag =="notice":
                    Say(reply)
                    webbrowser.open("https://www.baiust.edu.bd/notice-panel")

                elif tag =="library":
                    Say(reply)
                    webbrowser.open("http://opac.baiust.edu.bd/")

                elif tag =="baiust":
                    Say(reply)
                    webbrowser.open("https://www.baiust.edu.bd/")

                else:
                    Say(reply)
    else:
        print("Sorry! I do't get it.")


wishMe()
while True:
    Main()