FROM {{cookiecutter.python_docker_image}}
#If you are using a non-debian distribution you may have to change apt-get
RUN apt-get update
RUN apt-get install openssh-client git -y
RUN apt-get install build-essential
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt



ARG UID
RUN useradd docker -l -u $UID -s /bin/bash -m
USER docker

ENV PATH=$PATH:/home/docker/.local/bin
