import logging
import time

import requests

log = logging.getLogger()


def download_file(file_url, file_loc):
    try:
        beg_ts = time.time()
        r = requests.get(file_url, stream=True)

        with open(file_loc, "wb") as file:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        end_ts = time.time()
        log.debug(
            'File downloaded in {} , from: {} , to: {}'.format(end_ts - beg_ts, file_url, file_loc))
        return True
    except Exception as e:
        log.exception(e)
        return False


def process_genre_detection(song_dir):
    # TODO: Processing logic, function will return dict with processing report?

    return {}
