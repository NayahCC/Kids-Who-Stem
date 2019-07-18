import json

tweetFile = open("tweet_data.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()

print("Tweet id: ", tweetData[0]["id"])

print("Tweet text: ", tweetData[0]["text"])

for idx in range(len(tweetData)):
    print("Tweet text: " + tweetData[idx]["text"])
