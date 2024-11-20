import emoji
#asking emojiName from user
emojName= input("Input: ")

print(f"Output:",emoji.emojize(emojName,language='alias'))
