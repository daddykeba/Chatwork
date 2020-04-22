import requests

sender = input("What is your name?\n")

bot_message = ""
while bot_message!="merci":
    message = input("What is your name?\n")

    print("Sending message now...")

    r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"sender":sender, "message":message})

    print("Bot says, ", end='')
    for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")