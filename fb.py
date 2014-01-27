import urllib2
import urllib,requests,json
# Function to get relevant posts from your news feed
def get_posts():
    # Making an FQL query to filter out posts directed to the user after a given timestamp
    query = ("SELECT post_id, actor_id, message, created_time FROM stream WHERE filter_key = 'others' AND source_id = me() AND created_time > 1390575329  LIMIT 400")
    # Adding parameters
    payload = {'q': query, 'access_token': TOKEN}
    # Sending the request to get the feed
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']

# Enter your OAuth token here
TOKEN = '<Put your token here>'
params = {'access_token' : TOKEN}
if(TOKEN=='<Put your token here>'):
    print "Please add the token key in the source code"
    exit(1)
res = get_posts()
for item in res:
    # For each item in the feed write a comment
	params = {'access_token':TOKEN, 'message' : 'pppclub'}
	url = 'https://graph.facebook.com/%s/comments' % item['post_id']
	requests.post(url, data=params)
	print "Posted a comment"