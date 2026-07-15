
def main():
    text = input("How are you right now: ")
    print(convert(text))

# Converting emotions to emojis
def convert(text):
    # Store pairs in a dictionary
    emo = {":)":"🙂", ":(":"🙁"}
    for emotions, emojis in emo.items():
        text = text.replace(emotions,emojis)
    return text

main()