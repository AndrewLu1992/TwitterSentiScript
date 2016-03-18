import sys
import json
def afinnWords(df):
    afinnfile = df
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    df.close()
    return scores # Print every (term, score) pair in the dictionary

def tweetsProcess(df):
    texts = [] # initialize an empty list
    for line in df:
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            text = tweet['text'].encode('utf-8')
            words = text.strip().split()
            texts.append(words)
        else:
            texts.append([""])
    df.close()
    return texts

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = afinnWords(sent_file)
    texts = tweetsProcess(tweet_file)
    senti = {}
    for text in texts:
        score = 0
        for word in text:
            if word in scores.keys():
                score += scores[word]
            else:
                if word not in senti.keys():
                    senti[word] = 0
        for word in text:
            if (score >= 1 or score <= -1) and \
            (word not in scores.keys()):
                senti[word] += score
    for word, num in senti.items():
        print word, num

if __name__ == '__main__':
    main()
