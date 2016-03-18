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
    places = []
    for line in df:
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            texts.append(tweet['text'].encode('utf-8'))
            if 'place' in tweet.keys() and tweet['place'] is not None:
                if 'country_code' in tweet['place'].keys() and\
                'full_name' in tweet['place'].keys():
                    places.append((tweet['place']['country_code'], tweet['place']['full_name']))
                else:
                    places.append(None)
            else:
                places.append(None)
    df.close()
    return texts, places

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = afinnWords(sent_file)
    texts, places = tweetsProcess(tweet_file)
    senti = []
    usPlaceSenti = []
    result = {}
    for text in texts:
        score = 0
        words = text.strip().split()
        for word in words:
            if word in scores.keys():
                score += scores[word]
        senti.append(score)

    for i in range(len(texts)):
        if places[i] is not None and places[i][0] == u'US':
            usPlaceSenti.append((senti[i], places[i][1].split(", ")[-1]))

    for item in usPlaceSenti:
        if len(item[1]) == 2:
            result[item[1]] = 0
    for item in usPlaceSenti:
        if len(item[1]) == 2:
            result[item[1]] += item[0]

    happiest = sorted(result.items(), key=lambda x: x[1], reverse=True)[0]
    print happiest[0]


if __name__ == '__main__':
    main()
