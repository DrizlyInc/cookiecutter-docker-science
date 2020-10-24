FROM {{cookiecutter.python_docker_image}}

RUN pip3 install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ARG UID
RUN useradd docker -l -u $UID -s /bin/bash -m
USER docker

ENV PATH=$PATH:/home/docker/.local/bin
