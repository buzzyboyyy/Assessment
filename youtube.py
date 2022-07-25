from googleapiclient.discovery import build

api_key='AIzaSyD82VZrhz6QKIGBksOvGYyplvx42mD5v-s'

youtube=build('youtube', 'v3', developerKey=api_key)



request=youtube.videos().list(
        part='snippet',
        chart='mostPopular'
    )
response=request.execute()

info=response['items'][0]['snippet']['title']

print("Title: " + info)
