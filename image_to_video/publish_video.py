# -*- coding: utf-8 -*-

import os

from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build

def upload_video(youtube, file, title, description, tags):
    try:
        # Create a request to upload a video to YouTube.
        request = youtube.videos().insert(
            part='id,snippet,status',
            body={
                'snippet': {
                    'title': title,
                    'description': description,
                    'tags': tags,
                    'categoryId': '22'
                },
                'status': {
                    'privacyStatus': 'public'
                }
            },
            media_body=MediaFileUpload(file, chunksize=-1, resumable=True)
        )

        # Execute the request and print the response.
        response = request.execute()
        print(f'Video "{title}" was uploaded to YouTube with ID: {response["id"]}')
    except HttpError as error:
        print(f'An error occurred while uploading the video: {error}')

def main():
    # Set up the YouTube API client.
    youtube = build('youtube', 'v3', credentials=Credentials.from_authorized_user_info())

    # Set the file path, title, description, and tags for the video.
    file = 'video.mp4'
    title = 'My video'
    description = 'This is my video.'
    tags = ['cool', 'video']

    # Call the YouTube API's videos().insert() method to upload the video.
    upload_video(youtube, file, title, description, tags)

if __name__ == '__main__':
    main()
