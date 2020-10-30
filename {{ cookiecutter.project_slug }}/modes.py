"""Modes"""
from dagster import ModeDefinition

from drizly_dagster_utils.utils.resources import mock_s3, s3
from drizly_dagster_utils.utils.slack_logger import json_console_logger

#TODO: Write up a howto for this portion.
#TODO: Make a decision about the logger

local_mode = ModeDefinition(
    name="local",
    resource_defs={},
    description="Local mode of pipelines (No AWS, Dev/Local Resources)",
)

dev_mode = ModeDefinition(
    name="dev",
    description="Dev mode of pipelines (Dev AWS, Dev Resources)",
    resource_defs={},
    logger_defs={"custom_logger": json_console_logger},
)

prod_mode = ModeDefinition(
    name="prod",
    description="Production mode of pipelines (Prod AWS, Prod Resources)",
    resource_defs={},
    logger_defs={"custom_logger": json_console_logger},
)
