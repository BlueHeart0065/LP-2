response = {
    
}

def chatbort(user_input):
    user_input = user_input.lower()
    if user_input in response:
        return response[user_input]
    else:
        return response["defualt"]
    
print("welcome to the chatbot ! you can start chating and type 'bye' to exit ")
while True:
    user_input = input("you: ")
    if user_input.lower() == 'bye':
        print(chatbort(user_input))
        break
    else:
        print("chatbot: ", chatbort(user_input))