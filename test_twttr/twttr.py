def main():
    user_s = input("Input: ").strip()
    print(f"Output: {shorten(user_s)}")

def shorten(word):
    vowels = "aeiouAEIOU"
    mytwttr = ""
    for char in word:
        if char not in vowels:
            mytwttr += char
    return mytwttr

if __name__ == "__main__":
    main()
