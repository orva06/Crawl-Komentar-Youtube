import pandas as pd
from googleapiclient.discovery import build

"""Crawl data"""

def video_comments(video_id):
	# empty list for storing reply
	replies = []

	# creating youtube resource object
	youtube = build('youtube', 'v3', developerKey=api_key)

	# retrieve youtube video results
	video_response = youtube.commentThreads().list(part='snippet,replies', videoId=video_id).execute()

	# iterate video response
	while video_response:

		# extracting required info
		# from each result object
		for item in video_response['items']:

			# Extracting comments ()
			published = item['snippet']['topLevelComment']['snippet']['publishedAt']
			user = item['snippet']['topLevelComment']['snippet']['authorDisplayName']

			# Extracting comments
			comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
			likeCount = item['snippet']['topLevelComment']['snippet']['likeCount']

			replies.append([published, user, comment, likeCount])

			# counting number of reply of comment
			replycount = item['snippet']['totalReplyCount']

			# if reply is there
			if replycount>0:
				# iterate through all reply
				for reply in item['replies']['comments']:

					# Extract reply
					published = reply['snippet']['publishedAt']
					user = reply['snippet']['authorDisplayName']
					repl = reply['snippet']['textDisplay']
					likeCount = reply['snippet']['likeCount']

					# Store reply is list
					#replies.append(reply)
					replies.append([published, user, repl, likeCount])

			# print comment with list of reply
			#print(comment, replies, end = '\n\n')

			# empty reply list
			#replies = []

		# Again repeat
		if 'nextPageToken' in video_response:
			video_response = youtube.commentThreads().list(
					part = 'snippet,replies',
					pageToken = video_response['nextPageToken'],
					videoId = video_id
				).execute()
		else:
			break
	#endwhile
	return replies

"""Run Crawl"""

# isikan dengan api key
api_key = 'AIzaSyAKenCf09wcI1cBGhqwoVC9dlmct_4NBwM'

# Enter video id
video_id = "Ip3JDIWypB4" #isikan dengan kode / ID video

# Call function
comments = video_comments(video_id)


"""Ubah ke dataframe"""

df = pd.DataFrame(comments, columns=['publishedAt', 'authorDisplayName', 'textDisplay', 'likeCount'])


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://rayhankrnwn:atlas789@cluster0.hws32xd.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Pilih database dan koleksi
db = client.get_database("Tugas1")
collection = db.get_collection("Tugasbigdata")

# Ubah DataFrame menjadi bentuk dokumen BSON (Python dictionary)
data_to_insert = df.to_dict(orient='records')

# Masukkan data ke koleksi MongoDB Atlas
# collection.insert_many(data_to_insert)
for data in data_to_insert:
    # Tentukan kriteria pencarian berdasarkan field tertentu yang unik (misalnya 'publishedAt')
    filter_criteria = {"publishedAt": data["publishedAt"],
                       "authorDisplayName": data["authorDisplayName"],
                       "textDisplay": data["textDisplay"]}
    
    # Perbarui dokumen yang cocok atau buat dokumen baru jika tidak ada yang cocok
    collection.update_one(filter_criteria, {"$set": data}, upsert=True)
print("Impor data selesai")
