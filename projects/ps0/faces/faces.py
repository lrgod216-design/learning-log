
def main():
    print(convert())

# Converting emotions to emojis
def convert():
    prompt = input("How are you right now: ")
    prompt = prompt.replace(":)", "🙂")
    prompt = prompt.replace(":(", "🙁")
    return prompt

main()