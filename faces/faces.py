def convert_emoticons_to_emoji(text):
        text = text.replace(":)", "🙂").replace(":(", "🙁")
        return text

user_input = input()
converted_text = convert_emoticons_to_emoji(user_input)
print(converted_text)
