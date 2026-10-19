from generator import repondre 

def main():

    print("Chatbot démarches administratives (tape 'quit' pour quitter)")

    while True:

        question = input("\nTa question : ").strip()

        if question.lower() in ("quit" , "exit" , "q"):

            print("Au revoir !")

            break

        if not question:

            continue
        print("\n" + repondre(question))


if __name__ == "__main__":

    main()

    