.. |travis| image:: https://travis-ci.org/docker-science/cookiecutter-docker-science.svg?branch=master
    :target: https://travis-ci.org/docker-science/cookiecutter-docker-science

|travis|

Table of Contents
------------------

.. contents:: This article consists of the following sections.
    :depth: 1

Features
--------

 `Cookiecutter Docker Science <https://docker-science.github.io/>`_ provides the following features.

* **Improve reproducibility** of the results in machine learning projects with **Docker**
* Output optimal directories and file template for machine learning projects
* `Edit codes with favorite editors (Atom, vim, Emacs etc) <https://docker-science.github.io/#edit-codes-with-preferred-editors>`_

* Provide `make` targets useful for data analysis (Jupyter notebook, test, lint, docker etc)

Introduction
------------
This is the Datascience Cookiecutter for use with dagster

Requirements
------------

* Python 3.5 or later
* `Cookiecutter 1.6 or later <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_
* `Docker version 17 or later <https://docs.docker.com/install/#support>`_
* `AWS configuration set up. If you can use boto3 you are all set`

Quick start
-----------

To generate project from the cookiecutter-docker-science template, please run the following command.

``$cookiecutter gh:DrizlyInc/cookiecutter-docker-science``

Then the cookiecutter command ask for several questions on generated project as follows.

You can skip everything except project_name.
If you already have a project you are working simultaneously, it's recommended you specify an different jupyter port
::

    $cookiecutter git@github.com:DrizlyInc/cookiecutter-docker-science.git
    project_name [project_name]: food-image-classification
    project_slug [food_image_classification]:
    jupyter_host_port [8888]:
    description [Please Input a short description]: Classify food images into several categories
    Select data_source_type:
    1 - s3
    2 - nfs
    3 - url
    data_source [Please Input data source]: s3://research-data/food-images

Then you get the generated project directory, ``food-image-classification``.

Initial directories and files
-----------------------------

The following is the initial directory structure generated in the previous section.

::

    ├── Makefile                          <- Makefile contains many targets such as create docker container or
    │                                        get input files.
    ├── config                            <- This directory contains configuration files used in dagster, project source
    │   │                                    or Jupyter Notebook.
    │   └── jupyter_config.py
    ├── dagster                           <- basic dagster setup that uses configuration from config and can read from snowflake out of the box.
    ├── data                              <- data directory contains the input resources. syncs write here
    ├── docker                            <- docker directory contains Dockerfile.
    │   ├── Dockerfile                    <- Base Dockerfile contains the basic settings.
    │   ├── Dockerfile.dev                <- Dockerfile for experiments this Docker image is derived from the base Docker image.
    │   │                                    This Docker image does not copy the files and directory but used mount the top
    │   │                                    directory of the host environments.
    │   └── Dockerfile.release            <- Dockerfile for production this Docker image is derived from the base Docker image.
    │                                        The Docker image copy the files and directory under the project top directory.
    ├── ds_util                           <- contains utility files used across all projects. shouldn't need to be changed
    ├── model                             <- model directory store the model files created in the experiments.
    ├── my_data_science_project           <- cookie-cutter-docker-science creates the directory whose name is same
    │   │                                    as project name. In this directory users puts python files used in scripts
    │   │                                    or Jupyter Notebook.
    │   └── __init__.py
    ├── notebook                          <- This directory stores the ipynb files saved in Jupyter Notebook.
    ├── requirements.txt
    ├── dev-requirements.txt              <- Libraries needed to run experiments. The library listed in this file
    │                                        are installed in the Docker container.
    └── scripts                           <- Users add the script files to generate model files or run evaluation.


Makefile targets
----------------

Cookiecutter Docker Science provides many Makefile targets to supports experiments in a Docker container. Users can run the target with `make [TARGET]` command.

init
~~~~~

After cookiecutter-docker-science generate the directories and files, users first run this command. `init` setups resources for experiments.
Specifically `init` run `init-docker` and `sync-from-source` command.

- init-docker

  `init-docker` command first creates Docker the images based on `docker/Dockerfile`.

- sync-from-source

  `sync-from-source` downloads input files which we specified in the project generation.  If you want to change the input files, please modify this target to download the new data source.

create-container
~~~~~~~~~~~~~~~~~

`create-container` command creates Docker container based on the created image and login the Docker container.

start-container
~~~~~~~~~~~~~~~~

Users can start and login the Docker container with `start container` created by the `create-container`.

jupyter
~~~~~~~

`jupyter-host-no-referrer` from within the container (post create) to launch Jupyter Notebook server.

profile
~~~~~~~

`profile` target shows the misc information of the project such as port number or container name.


clean
~~~~~

`clean` target removes the artifacts such as models and *.pyc files.

- clean-model

  `clean-model` command removes model files in `model` directory.

- clean-pyc

  `clean-pyc` command removes model files of *.pyc, *.pyo and __pycache__.

- clean-docker

  `clean-docker` command removes the Docker images and container generated with `make init-docker` and `make create-container`.
  When we update Python libraries in `requirements.txt` or system tools in `Dockerfile`, we need to clean Docker the image and container with this target and create the updated image and container with `make init-docker` and `make create-container`.

distclean
~~~~~~~~~

`distclean` target removes all reproducible objects. Specifically this target run `clean` target and remove all files in data directory.

- clean-data

  `clean-data` command removes all datasets in `data` directory.

lint
~~~~~

`lint` target check if coding style meets the coding standard.

test
~~~~~

`test` target executes tests.


sync-to-source
~~~~~~~~~~~~~~

`sync-to-remote` target uploads the local files stored in `data` to specified data sources in such as S3 or NFS directories.

Working with Docker container
------------------------------

With Cookiecutter Docker Science, data scientists or software engineers do their developments in host environment.
They open Jupyter notebook in the browsers in the host machine connecting the Jupyter server launched in Docker container.
They also writes the ML scripts or library classes in the host machine. The code modification in host environment are
reflected in the container environment. In the containers, they just launch Jupyter server or start ML scripts
with make command.

Files and directories
~~~~~~~~~~~~~~~~~~~~~

When you log in a Docker container by ``make create-container`` or ``make start-container`` command, the log in directory is ``/work``.
The directory contains the project top directories in host computer such as ``data`` or ``model``. Actually the Docker container mounts
the project directory to ``/work`` of the container and therefore when you can edit the files in the host environment with your favorite editor
such as Vim, Emacs, Atom or PyCharm. The changes in host environment are reflected in container environment.

Jupyter Notebook
~~~~~~~~~~~~~~~~~

We can run a Jupyter Notebook in the Docker container. The Jupyter Notebook uses the default port ``8888`` in **Docker container (NOT host machine)** and
the port is forwarded to the one you specify with ``JUPYTER_HOST_PORT``  in the cookiecutter command. You can see the Jupyter Notebook UI accessing
"http://localhost:JUPYTER_HOST_PORT". When you save notebooks the files are saved in the ``notebook`` directory.

Tips
-----


Override port number for Jupyter Notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the generation of project with cookiecutter, the default port of Jupyter Notebook in host is ``8888``. The number is common and could
have a collision to another server processes.

If we already have the container, we first need to remove the current container with ``make clean-container``. And then
we create the Docker container changing the port number with ``make create-container`` command adding the Jupyter port parameter (JUPYTER_HOST_PORT).
For example the following command creates Docker container forwarding Jupyter default port ``8888`` to ``9900`` in host.

::

    make create-container JUPYTER_HOST_PORT=9900

Then you launch Jupyter Notebook in the Docker container, you can see the Jupyter Notebook in http://localhost:9900

Specify suitable Dockerfile in stages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some projects can have multiple Dockerfiles. ``Dockerfile.gpu`` contains the settings for GPU machines. ``Dockerfile.cpu`` contains settings to be that can be used in production for non-GPU machines.

To use one of these specific Dockerfile, override the settings by adding parameters to the make command. For example, when we want to create a container from ``docker/Dockerfile.cpu``, we run ``make create-container DOCKERFILE=docker/Dockerfile.cpu``.


Show target specific help
~~~~~~~~~~~~~~~~~~~~~~~~~

`help` target flushes the details of specified target. For example, to get the details of `clean` target.

:: 

    $make help TARGET=clean
    target: clean
    dependencies: clean-model clean-pyc clean-docker
    description: remove all artifacts

As we can see, the dependencies and description of the specified target (`clean`) are shown.

License
-------

Apache version 2.0

Contribution
-------------

See `CONTRIBUTING.md <CONTRIBUTING.md>`_.
