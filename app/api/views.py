# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import os
import uuid
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from classifier.utils import download_file, process_genre_detection
from genre_detection.settings import PROCESSING_QUEUE_DIR

log = logging.getLogger()


class ProcessSongsList(APIView):

    def post(self, request, format=None):

        request_data = request.data

        if 'songs' in request_data:
            songs = request_data['songs']
            if isinstance(songs, list):
                songs_processing_data = []
                # define job ID
                job_ID = str(uuid.uuid4())

                # location for song download
                job_dir = os.path.join(PROCESSING_QUEUE_DIR, job_ID)
                if not os.path.exists(job_dir):
                    os.mkdir(job_dir)

                # download songs
                for song_url in songs:
                    song_data = {}
                    song_data['url'] = song_url
                    song_data['name'] = os.path.basename(song_url)
                    song_data['full_path'] = os.path.join(job_dir, song_data['name'])
                    song_data['downloaded'] = download_file(song_url, song_data['full_path'])
                    songs_processing_data.append(song_data)

                # genre detection
                for song in songs_processing_data:
                    if song['downloaded'] is not False:
                        song['genre_detected'] = process_genre_detection(song['full_path'])

                return Response({
                    'msg': 'Automatic genre detection finished, job ID: {}.'.format(
                        job_ID), 'genre_detection_results': songs_processing_data
                }, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'msg': 'No songs list in request.'},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response({'msg': 'No songs in request.'}, status=status.HTTP_400_BAD_REQUEST)
