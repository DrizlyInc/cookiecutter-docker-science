"""Modes"""
from dagster import ModeDefinition
from dagster_ge.factory import ge_data_context
from drizly_dagster_utils.utils.resources import (
    mock_s3,
    mock_snowflake,
    s3,
    snowflake,
)
from drizly_dagster_utils.utils.slack_logger import json_console_logger
#TODO: If you are using a resource outside of s3 and snowflake, you need to specify it here
local_mode = ModeDefinition(
    name="local",
    resource_defs={
        "s3": mock_s3,
        "snowflake": mock_snowflake,
        "ge_data_context": ge_data_context,
    },
    description="Local mode of pipelines (No AWS, Dev/Local Resources)",
)

dev_mode = ModeDefinition(
    name="dev",
    description="Dev mode of pipelines (Dev AWS, Dev Resources)",
    resource_defs={
        "s3": s3,
        "snowflake": mock_snowflake,
        "ge_data_context": ge_data_context,
    },
)

prod_mode = ModeDefinition(
    name="prod",
    description="Production mode of pipelines (Prod AWS, Prod Resources)",
    resource_defs={
        "s3": s3,
        "snowflake": snowflake,
        "ge_data_context": ge_data_context,
    },
    logger_defs={"custom_logger": json_console_logger},
)
