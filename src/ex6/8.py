# Write a program that parses through a YouTube link, extracts and outputs the YouTube video ID.
# The input to your program is a string representing the URL to a YouTube video. The format can be
# in “https://www.youtube.com/watch?v=VIDEO_ID” or the shorter “https://youtu.be/VIDEO_ID”
# format. The output is a string containing the extracted YouTube video ID. Your code has to work
# with both input formats!
# Example:
#   Input: https://www.youtube.com/watch?v=1vewOUInGv8
#   Output: 1vewOUInGv8

def extract_yt_id(s: str):
    return s[17 if s.startswith("https://youtu.be/") else 32:]


print(extract_yt_id("https://youtu.be/VIDEO_ID"))
print(extract_yt_id("https://www.youtube.com/watch?v=1vewOUInGv8"))
