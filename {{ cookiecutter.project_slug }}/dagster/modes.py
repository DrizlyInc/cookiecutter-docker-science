"""Modes"""
from dagster import ModeDefinition

from drizly_dagster_utils.utils.resources import mock_snowflake, snowflake, redis
from drizly_dagster_utils.utils.slack_logger import json_console_logger
#TODO: Write up a howto for this portion.
#TODO: Make a decision about the logger
#TODO: Change snowflake to a mock, right now dev is fast enough tho
local_mode = ModeDefinition(
    name="local",
    resource_defs={
       "snowflake": mock_snowflake,
        "redis": mock_redis
    },
    description="Local mode of pipelines (No AWS, Dev/Local Resources)",
    logger_defs={"custom_logger": json_console_logger},
)

dev_mode = ModeDefinition(
    name="dev",
    description="Dev mode of pipelines (Dev AWS, Dev Resources)",
    resource_defs={
        "snowflake": snowflake,
        "redis": redis
    },
    logger_defs={"custom_logger": json_console_logger},
)

#TODO: You have to write this if you want it to go live
prod_mode = ModeDefinition(
    name="prod",
    description="Production mode of pipelines (Prod AWS, Prod Resources)",
    resource_defs={
    },
    logger_defs={"custom_logger": json_console_logger},
)

