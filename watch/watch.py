import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Corrected regular expression pattern to match the YouTube embed URL
    pattern = r'<iframe[^>]+src=["\']https?://(?:www\.)?youtube\.com/embed/([\w-]+)["\']'

    # Using re.search to extract the video ID directly
    match = re.search(pattern, s)

    # If a match is found, construct the shorter URL using the video ID, otherwise return None
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
