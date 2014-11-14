import json

def tweetdata(val):
    if val == None or val == []:
        val = 'empty'
    elif type(val) is dict:
        val = 'ddd'
    elif type(val) is list:
        val = 'lll'
    return val

bb = dict()
cc = dict()
dd = dict()

def tweetdict(dictionary, elem):
	if elem not in dictionary:
	    dictionary[elem] = 1
	else:
	    dictionary[elem] += 1
	return dictionary

i = 0
tweet_file = open('out_skin_' + str(i) + '.txt')
data = json.load(tweet_file)
for tweet in data:
    b = tweet['favorite_count']
    c = tweet['source']
    d = tweet['coordinates']
    val_b = tweetdata(b)
    val_c = tweetdata(c)
    val_d = tweetdata(d)
    tweetdict(bb, val_b)
    tweetdict(cc, val_c)
    tweetdict(dd, val_d)
print bb
print cc
print dd



"""
    a = tweet['text']
    b = tweet['favorite_count']
    c = tweet['source']
    d = tweet['coordinates']
    e = tweet['entities']['symbols']
    f = tweet['entities']['user_mentions']
    g = tweet['entities']['hashtags']
    h = tweet['entities']['urls']
    i = tweet['geo']
    j = tweet['lang'].encode('utf-8')
    k = tweet['created_at'][:13].encode('utf-8') #hourly [:10] = daily
    l = tweet['place'] # unhashable
    m = tweet['retweet_count']
    n = [a, b, c, d, e, f, g, h, i, j, k, l]
    return n
"""
