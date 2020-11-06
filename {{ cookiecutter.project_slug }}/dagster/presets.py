"""Presets"""
from dagster import PresetDefinition

from ds_util.config import local_cfg, dev_cfg, prod_cfg

local = PresetDefinition(
    name="local",
    run_config=local_cfg.to_dict(),
    mode="local",
)

dev = PresetDefinition(
    name="dev",
    run_config=dev_cfg.to_dict(),
    mode="dev",
)

prod = PresetDefinition(
    name="prod",
    run_config=prod_cfg.to_dict(),
    mode="prod",
)
