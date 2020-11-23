import os
from pathlib import Path

import yaml
from box import Box

# TODO: Figure out how to pass envirorment variables and possibly still support sagemaker SLA

env = os.environ.get("ENV")
config_dir = "config/"

if env is None:
    env = os.environ.get("DAGSTER_ENVIRONMENT")
# dev, local, or prod

# This gets you the path object for the root of the project and lets you load files from that
def get_project_root() -> Path:
    return Path(__file__).parent.parent

def update_config_immutable(update_dict:dict) -> dict:
    updated_box = Box(cfg, default_box=True)

# TODO: Is the environment variable read necessary?
# You can import cfg from this module ala from config import cfg and access it anywhere
# in the project
with open(
    get_project_root().joinpath(f"{config_dir}{env}_resource.yaml"),
    "r",
) as ymlfile:
    cfg = Box(yaml.safe_load(ymlfile))
    ge_root_directory = cfg.resources.ge_data_context.config.ge_root_dir
    cfg.resources.ge_data_context.config.ge_root_dir = (
        get_project_root().joinpath(f"dagster/{ge_root_directory}").as_posix()
    )
    if env == "test":
        file_path = cfg.resources.snowflake.config.file_path
        cfg.resources.snowflake.config.file_path = (
            get_project_root().joinpath(f"dagster/tests/{file_path}").as_posix()
        )

# Loading the default config
with open(
    get_project_root().joinpath(f"{config_dir}local_resource.yaml"),
    "r",
) as ymlfile:
    local_cfg = Box(yaml.safe_load(ymlfile))
    ge_root_directory = local_cfg.resources.ge_data_context.config.ge_root_dir
    local_cfg.resources.ge_data_context.config.ge_root_dir = (
        get_project_root().joinpath(f"dagster/{ge_root_directory}").as_posix()
    )