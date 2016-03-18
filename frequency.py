import sys
import json

def tweetsProcess(df):
    corpus = [] # initialize an empty list
    for line in df:
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            text = tweet['text'].encode('utf-8')
            words = text.strip().split()
            corpus.extend(words)
    df.close()
    return corpus

def main():
    tweet_file = open(sys.argv[1])
    texts = tweetsProcess(tweet_file)
    freq = {}
    for word in texts:
        freq[word] = 0
    for word in texts:
        freq[word] += 1 / float(len(texts))
    for word, distri in sorted(freq.items(), key = lambda x:x[1], reverse=True):
        print word, distri

if __name__ == '__main__':
    main()
