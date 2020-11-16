# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Requirements

* [Docker version 17 or later](https://docs.docker.com/install/#support)
* Setup your ssh agent to connect to github: https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh
* Setup aws credentials locally via aws configure. (You should have credentials in ~/.aws . Talk to dev ops if you haven't gotten these yet)

## Setup development environment for dagster (and other flows)

We setup the development environment in a Docker container with the following command.

- `make init`

This command prepares the Docker image for development work.

After creating the Docker image, you run the following command.

- `make create-container`

The above command creates a Docker container from the Docker image which we create with `make init`, and then
login to the Docker container. Now we made the development environment. 

## Development with Docker container

This section shows how we develop with the created Docker container.

### Drizly specific

#### Jupyter
You should have run the command and entered the project directory with `cd project name`:

![Alt text](docs/images/cookiecutter_creation.png?raw=true "Cookiecutter Creation")

Then you need to build the image with `make init`:
![Alt text](docs/images/build docker image.png?raw=true "Create docker image")

Then create the container with `make create-container`
![Alt text](docs/images/create the container.png?raw=true "Create docker image")

Then launch the server within the container with `make jupyter-host-no-referrer`
and navigate to the url (127.0.0.1) with the token output 
![Alt text](docs/images/Notebook Server Setup.png?raw=true "Create docker image")

Then navigate to the notebook directory to get started with EDA 
![Alt text](docs/images/Notebook Server Setup.png?raw=true "Create docker image")

It's suggested that you do most of your development in the notebooks, and as you
finalize your project, migrate your code from notebook form into the {{cookiecutter.project_slug}}
directory and separate it into the appropriate modules. If you still want to use
a notebook as a solid in dagster, you can import the modules and run them. 

From there you should begin development in dagster, translating what you have
written into solid form.

#### Dagster

When you have finalized your data processing outside of dagster, to get it
to run properly right away you need to do the following:
 
You will have made changes to the queries from the base template and so you 
need to modify custom_types.py to accommodate your new column names:
![Alt text](docs/images/custom types.png?raw=true "Setup custom types")

Following that, if this is a dagster flow you can (if you haven't already) add your 
code to the repo.py file in the drizly-dagster repo you are in:
![Alt text](docs/images/dagster setup.png?raw=true "Setup dagster repo")

Then you can run `dagit -w workspace.yml` from the drizly-dagster project root
and it should load everything you need to run your first dagster flow.

From there, refer to the drizly-dagster documentation and you should be able to 
develop from there

Dependencies: If you have dependencies that are not captured in your dagster repo
you will need to add lines within the dagster repo to install your dependencies with pip.

### Edit source code

Most of the source code of this project, `{{ cookiecutter.project_name }}` are stored in the `{{ cookiecutter.project_slug }}` directory.
Generated Docker container mounts the project directory to ``/work`` of the container and therefore
when you can edit the files in the host environment with your favorite editor
such as Vim, Emacs, Atom or PyCharm. The changes in host environment are reflected in the Docker container environment.

If you want to test out a new package or figure out how to configure things. Run them within the container following a `make create-container` or `make start-container` Any of these installs will be deleted if you delete the container, so if you want them to persist you should add them to the requirements file. 

### Update dependencies

When we need to add libraries in `Dockerfile` or `requirements.txt`
which are added to working environment in the Docker container, we need to drop the current Docker container and
image, and then create them again with the latest setting. To remove the Docker the container and image, run `make clean-docker`
and then `make init-docker` command to create the Docker container with the latest setting.

### Login Docker container

Only the first time you need to create a Docker container, from the image created in `make init` command.
`make create-container` creates and launch the {{ cookiecutter.project_slug }} container.
After creating the container, you just need run `make start-container`.

### Logout from Docker container

When you logout from shell in Docker container, please run `exit` in the console.

### Run linter

When you check the code quality, please run `make lint`

### Run test

When you run test in `tests` directory, please run `make test`

### Sync data source to local data directory

When you want to download data in remote data sources such as Amazon S3 or NFS, `sync-from-remote` target downloads them.

### Sync local data to remote source

When you modify the data in local environment, `sync-to-remote` target uploads the local files stored in `data` to specified data sources such as S3 or NFS directories.

### Show profile of Docker container

When you see the status of Docker container, please run `make profile` in host machine.

### Use Jupyter Notebook

To launch Jupyter Notebook, please run `make jupyter-start` in the Docker container. After launch the Jupyter Notebook, you can
access the Jupyter Notebook service in http://localhost:{{ cookiecutter.jupyter_host_port }}.

You will need to put in the token the first time the server is run each container start up (following a make start or make create).
After that, you can set a password on the prompt page and login with that while the container is running.

### Run formatter
When you format project's codes, please run `make format`.
More details of black in https://github.com/psf/black 


# Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [cookiecutter-docker-science](https://docker-science.github.io/) project template.
