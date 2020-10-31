FROM {{cookiecutter.python_docker_image}}

RUN apt-get update
# Needed for drizly_dagster_utils install
RUN apt-get install openssh-client git -y
RUN apt-get install build-essential -y
RUN apt-get install -yqq cron

ARG UID
RUN useradd docker -l -u $UID -s /bin/bash -m
USER docker

ENV PATH=$PATH:/home/docker/.local/bin

COPY requirements.txt ./
RUN pip install -r /requirements.txt

