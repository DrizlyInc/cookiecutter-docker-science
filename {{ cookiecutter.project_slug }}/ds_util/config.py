import yaml
from box import Box
import os
from pathlib import Path
#TODO: Figure out how to pass envirorment variables and possibly still support sagemaker SLA

env = os.environ.get('ENV')
# dev, local, or prod

# This gets you the path object for the root of the project and lets you load files from that
def get_project_root() -> Path:
    return Path(__file__).parent.parent

# You can import cfg from this module ala from config import cfg and access it anywhere
# in the project
with open(get_project_root().joinpath(f"environments/config/{env}_resource.yaml"), "r") as ymlfile:
    cfg = Box(yaml.safe_load(ymlfile))

with open(get_project_root().joinpath(f"environments/config/local_resource.yaml"), "r") as ymlfile:
    local_cfg = Box(yaml.safe_load(ymlfile))

with open(get_project_root().joinpath(f"environments/config/dev_resource.yaml"), "r") as ymlfile:
    dev_cfg = Box(yaml.safe_load(ymlfile))

with open(get_project_root().joinpath(f"environments/config/prod_resource.yaml"), "r") as ymlfile:
    prod_cfg = Box(yaml.safe_load(ymlfile))
