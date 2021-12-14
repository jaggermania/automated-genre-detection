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

SQLlite DB by Django default initialisation. Any ideas to add processing results there? If not DB will be reomved from code.