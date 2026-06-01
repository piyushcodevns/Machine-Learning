from nltk.corpus import wordnet

def chatbot():
    print("Chatbot: How can I help, Piyush?")
    while True:
        user_input=input("You :")
        if user_input == "exit":
            print("Chatbot: Bye Piyush")
            break
        words=user_input.split()
        for word in words:
            syns=wordnet.synsets(word)
            if syns:
                meaning=syns[0].definition()
                print(f"chatbot: '{word}' = '{meaning}'")
            else:
                print(f"chatbot: '{word}' Not Found")
chatbot()