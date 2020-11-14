import os
from pathlib import Path

import yaml
from box import Box

# TODO: Figure out how to pass envirorment variables and possibly still support sagemaker SLA

env = os.environ.get("ENV")
if env is None:
    env = os.environ.get("DAGSTER_ENVIRONMENT")
# dev, local, or prod

# This gets you the path object for the root of the project and lets you load files from that
def get_project_root() -> Path:
    return Path(__file__).parent.parent


# TODO: Is the environment variable read necessary?
# You can import cfg from this module ala from config import cfg and access it anywhere
# in the project
with open(
    get_project_root().joinpath(f"environments/config/{env}_resource.yaml"),
    "r",
) as ymlfile:
    cfg = Box(yaml.safe_load(ymlfile))
    ge_root_directory = cfg.resources.ge_data_context.config.ge_root_dir
    cfg.resources.ge_data_context.config.ge_root_dir = (
        get_project_root().joinpath(f"dagster/{ge_root_directory}").as_posix()
    )

with open(
    get_project_root().joinpath(f"environments/config/local_resource.yaml"),
    "r",
) as ymlfile:
    local_cfg = Box(yaml.safe_load(ymlfile))
    ge_root_directory = local_cfg.resources.ge_data_context.config.ge_root_dir
    local_cfg.resources.ge_data_context.config.ge_root_dir = (
        get_project_root().joinpath(f"dagster/{ge_root_directory}").as_posix()
    )

with open(
    get_project_root().joinpath(f"environments/config/dev_resource.yaml"), "r"
) as ymlfile:
    dev_cfg = Box(yaml.safe_load(ymlfile))
    ge_root_directory = dev_cfg.resources.ge_data_context.config.ge_root_dir
    dev_cfg.resources.ge_data_context.config.ge_root_dir = (
        get_project_root().joinpath(f"dagster/{ge_root_directory}").as_posix()
    )

with open(
    get_project_root().joinpath(f"environments/config/prod_resource.yaml"),
    "r",
) as ymlfile:
    prod_cfg = Box(yaml.safe_load(ymlfile))
    ge_root_directory = prod_cfg.resources.ge_data_context.config.ge_root_dir
    prod_cfg.resources.ge_data_context.config.ge_root_dir = (
        get_project_root().joinpath(f"dagster/{ge_root_directory}").as_posix()
    )

with open(
    get_project_root().joinpath(f"environments/config/test_resource.yaml"),
    "r",
) as ymlfile:
    test_cfg = Box(yaml.safe_load(ymlfile))
    file_path = test_cfg.resources.snowflake.config.file_path
    test_cfg.resources.snowflake.config.file_path = (
        get_project_root().joinpath(f"dagster/tests/{file_path}").as_posix()
    )
    ge_root_directory = test_cfg.resources.ge_data_context.config.ge_root_dir
    test_cfg.resources.ge_data_context.config.ge_root_dir = (
        get_project_root().joinpath(f"dagster/{ge_root_directory}").as_posix()
    )