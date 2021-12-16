# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import os
import time
import requests
from classifier.py_genre_clf.classifier import predictGenre

log = logging.getLogger()


def download_file(file_url, file_loc):
    try:
        beg_ts = time.time()
        r = requests.get(file_url, stream=True)

        with open(file_loc, "wb") as file:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        log.debug(
            'File downloaded in {} sec, from: {} , to: {}'.format(time.time() - beg_ts, file_url,
                                                                  file_loc))
        return True
    except Exception as e:
        log.exception(e)
        return False


def process_genre_detection(song_url):
    # 1. extrakcija:
    # python main.py featureExtraction -f DATA_FOLDER -o midataset.csv

    # 2. klasifikacija BT:
    # python main.py bestTreeClassifier -df midataset.csv -o myclassifier.pkl -f REPORT_FOLDER

    # 3. klasifikacija BF:
    # python main.py predictClass -i AUDIO_FILE -clf myclassifier.pkl

    # 4. predikcija:
    # python main.py bestForestClassifier -df midataset.csv -o miclasificador.pkl -f CARPETA_INFORME

    binary_classifier_route = os.path.join(os.path.dirname(__file__), 'py_genre_clf', 'Examples',
                                           'beats23classifier.pkl')

    try:
        beg_ts = time.time()
        pd = predictGenre(song_url, binary_classifier_route)
        log.debug(
            'Song genre detection finished in {} sec'.format(time.time() - beg_ts))
        return pd
    except Exception as e:
        log.exception(e)
        return False
