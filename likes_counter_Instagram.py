import json
#import matplotlib.pyplot as plt
import urllib.request
import sys
import os

user = sys.argv[1]

url = 'https://instagram.com/{0}/media'.format(user)

print(url)

response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')
data = json.loads(text)

os.mkdir(sys.argv[1])

likes, i = [], 0
for photo in data['items']:
    likes.append(photo['likes']['count'])
    url_photo = photo['images']['standard_resolution']['url']
    urllib.request.urlretrieve(url_photo, "{0}/".format(user) + str(i) + '.jpg')
    i = i + 1
print(likes)

#plt.plot(list(range(1,len(likes)+1)), likes, 'ro-')
#plt.axis([1, 20, 0, max(likes)])
#plt.title('Evolution of {0} likes on Instagram'.format(user))
#plt.savefig("{0}/likes_{0}.png".format(user))
#plt.show()

