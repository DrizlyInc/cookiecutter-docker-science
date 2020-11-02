# syntax=docker/dockerfile:experimental
FROM {{cookiecutter.python_docker_image}}

COPY requirements.txt ./
RUN pip install --use-feature=2020-resolver -r  /requirements.txt
# make a root password
RUN echo "root:root" | chpasswd

#This exists in order to do a pip install of drizly_dagster_utils wherever needed
RUN apt-get update  \
    && apt-get install openssh-client git -y  \
    && apt-get install build-essential -y  \
    && mkdir -p -m 0700 ~/.ssh \
    && ssh-keyscan github.com >> ~/.ssh/known_hosts  \
    && --mount=type=ssh,mode=0666  pip install git+ssh://git@github.com/DrizlyInc/drizly-dagster.git@ds_js/margin-optimized-sort-skeleton"#egg=integrations&subdirectory=drizly_dagster_utils"

# Allowing configuration changes in nbconfig for extensions
RUN chmod +x /usr/local/etc/jupyter/nbconfig/

# Create a docker user and grant it sudo
ARG UID
RUN useradd docker -l -u $UID -s /bin/bash -m  \
    && echo "docker:docker" | chpasswd  \
    && apt-get install sudo  \
    && adduser docker sudo
USER docker

ENV PATH=$PATH:/home/docker/.local/bin


