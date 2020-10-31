import yaml
from box import Box
import os
#TODO: Figure out how to pass envirorment variables and possibly still support sagemaker SLA
env = os.environ.get('ENV')
# dev, local, or prod
with open(f"../../config/{env}_resource.yaml", "r") as ymlfile:
  cfg = Box(yaml.safe_load(ymlfile))

