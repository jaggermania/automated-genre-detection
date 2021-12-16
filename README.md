## MOP/Beatport Hackaton 2021 - Automated genre detection

#### 1. Clone project from GitHub:

```sh
TODO ...
```

#### 2. Build services

```sh
docker-compose build
```

#### 3. Environment variables

Are in .env.dev file.

#### 4. To run services

```sh
docker-compose up
```

#### 5. To ....

TODO ...

#### 6. To ....

TODO ...


#### DEV notes:

api - location of REST logic

classifier - location of genre classification logic

https://github.com/Caparrini/pyGenreClf

logs - django log rotation file (if needed?)

https://docs.djangoproject.com/en/4.0/topics/logging/


SQLlite DB by Django default initialisation. 
Any ideas to add processing results there? If not DB will be reomved from code.

curl example:

curl --location --request POST 'http://localhost:8000/api/process-songs/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "songs": [
        "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_700KB.mp3",
        "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_1MG.mp3",
        "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_2MG.mp3",
        "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_5MG.mp3"
    ]
}'

Files will be downloaded to processing_queue dir. Every request create new unique dir for song download.

Example songs for download:

https://file-examples.com/index.php/sample-audio-files/sample-mp3-download/
https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_700KB.mp3
https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_1MG.mp3
https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_2MG.mp3
https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_5MG.mp3

Response:

{
    "msg": "Automatic genre detection finished, job ID: 068951cd-139d-4235-9859-999489342fb3.",
    "genre_detection_results": [
        {
            "url": "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_700KB.mp3",
            "downloaded": true,
            "genre_detected": "PsyTrance",
            "name": "file_example_MP3_700KB.mp3",
            "full_path": "/opt/project/app/processing_queue/068951cd-139d-4235-9859-999489342fb3/file_example_MP3_700KB.mp3"
        },
        {
            "url": "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_1MG.mp3",
            "downloaded": true,
            "genre_detected": "PsyTrance",
            "name": "file_example_MP3_1MG.mp3",
            "full_path": "/opt/project/app/processing_queue/068951cd-139d-4235-9859-999489342fb3/file_example_MP3_1MG.mp3"
        },
        {
            "url": "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_2MG.mp3",
            "downloaded": true,
            "genre_detected": "PsyTrance",
            "name": "file_example_MP3_2MG.mp3",
            "full_path": "/opt/project/app/processing_queue/068951cd-139d-4235-9859-999489342fb3/file_example_MP3_2MG.mp3"
        },
        {
            "url": "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_5MG.mp3",
            "downloaded": true,
            "genre_detected": "ElectronicaDowntempo",
            "name": "file_example_MP3_5MG.mp3",
            "full_path": "/opt/project/app/processing_queue/068951cd-139d-4235-9859-999489342fb3/file_example_MP3_5MG.mp3"
        }
    ]
}