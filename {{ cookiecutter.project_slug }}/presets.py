"""Presets"""
from dagster import PresetDefinition
from repos.forecasts.supplier_forecast.environments.dev_run_config import (
    dev_run_config,
)
from repos.forecasts.supplier_forecast.environments.local_run_config import (
    local_run_config,
)
from repos.forecasts.supplier_forecast.environments.prod_run_config import (
    prod_run_config,
)

local = PresetDefinition(
    name="local",
    run_config=local_run_config,
    mode="local",
)

dev = PresetDefinition(
    name="dev",
    run_config=dev_run_config,
    mode="dev",
)

prod = PresetDefinition(
    name="prod",
    run_config=prod_run_config,
    mode="prod",
)
