import sys
import json

def tweetsProcess(df):
    hashtags = [] # initialize an empty list
    for line in df:
        tweet = json.loads(line)
        if 'entities' in tweet.keys() and \
        len(tweet['entities']["hashtags"]) != 0:
            for text in tweet['entities']["hashtags"]:
                text = text['text'].encode('utf-8')
                tag = text.strip()
                hashtags.append(tag)
    df.close()
    return hashtags

def main():
    tweet_file = open(sys.argv[1])
    hashtags = tweetsProcess(tweet_file)
    freq = {}
    for tag in hashtags:
        freq[tag] = 0
    for tag in hashtags:
        freq[tag] += 1
    for tag, distri in sorted(freq.items(), key = lambda x:x[1], reverse=True)[:10]:
        print tag, distri

if __name__ == '__main__':
    main()
