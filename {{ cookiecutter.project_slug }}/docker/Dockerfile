FROM {{cookiecutter.python_docker_image}}

COPY requirements.txt ./
RUN pip install --use-feature=2020-resolver -r  /requirements.txt

RUN echo "root:root" | chpasswd
RUN apt-get update
# Needed for drizly_dagster_utils install
RUN apt-get install openssh-client git -y
RUN apt-get install build-essential -y
RUN apt-get install -yqq cron
RUN apt-get install sudo
RUN echo "docker:docker" | chpasswd && adduser docker sudo

#This exists in order to do a pip install of drizly_dagster_utils wherever needed
RUN mkdir -p -m 0700 ~/.ssh
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts
RUN --mount=type=ssh,mode=0666  pip install git+ssh://git@github.com/DrizlyInc/drizly-dagster.git@ds_js/margin-optimized-sort-skeleton"#egg=integrations&subdirectory=drizly_dagster_utils"

RUN chmod +x /usr/local/etc/jupyter/nbconfig/

ARG UID
RUN useradd docker -l -u $UID -s /bin/bash -m
USER docker

ENV PATH=$PATH:/home/docker/.local/bin


