FROM ubuntu:latest

RUN apt-get update

RUN apt install --no-install-recommends -y \
curl git libffi-dev libjpeg-devlibwebp-dev python3-lxml python3-psycopg2 libpq-dev libcurl4-openssl-dev \
libxml2-dev libxslt1-dev python3-pip python3-sqlalchemy openssl wget postgresql \
python3 python3-dev libreadline-dev libyaml-dev gcc zlib1g ffmpeg libssl-dev postgresql-contrib \
libgconf-2-4 libxi6 unzip libopus0 libopus-dev python3-venv libmagickwand-dev pv tree mediainfo

CMD ["echo Hello World"]
