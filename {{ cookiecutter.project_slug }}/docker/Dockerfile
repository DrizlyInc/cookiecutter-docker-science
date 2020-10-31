FROM {{cookiecutter.python_docker_image}}

COPY requirements.txt ./
RUN pip install -r /requirements.txt

ARG UID
RUN useradd docker -l -u $UID -s /bin/bash -m
USER docker

ENV PATH=$PATH:/home/docker/.local/bin


