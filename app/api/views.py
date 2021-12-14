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
                # define job ID
                job_ID = str(uuid.uuid4())

                # location for song download
                job_dir = os.path.join(PROCESSING_QUEUE_DIR, job_ID)
                if not os.path.exists(job_dir):
                    os.mkdir(job_dir)

                # download songs
                for song in songs:
                    song_name = os.path.basename(song)
                    df = download_file(song, os.path.join(job_dir, song_name))
                    if df is not True:
                        log.info('Error in downloading file: {}'.format(song))

                # Process genre detection
                process_report = process_genre_detection(job_dir)

                # TODO: What to do with processing response

                return Response(
                    {'msg': 'Automatic genre detection finished, job ID: {}.'.format(job_ID)},
                    status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'msg': 'No songs list in request.'},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response({'msg': 'No songs in request.'}, status=status.HTTP_400_BAD_REQUEST)
