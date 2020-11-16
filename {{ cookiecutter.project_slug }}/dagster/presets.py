"""Presets"""
from dagster import PresetDefinition
from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.ds_util.config import  local_cfg, cfg

# Just one config loaded by environment except for local which is universal
run_config = cfg.to_dict()

local = PresetDefinition(
    name="local",
    run_config=local_cfg.to_dict(),
    mode="local",
)

dev = PresetDefinition(
    name="dev",
    run_config=run_config,
    mode="dev",
)

prod = PresetDefinition(
    name="prod",
    run_config=run_config,
    mode="prod",
)

test = PresetDefinition(
    name="test",
    run_config=run_config,
    mode="test",
)

PRESETS = [local, dev, prod, test]