"""Modes"""
from dagster import ModeDefinition
from drizly_dagster_utils.utils.resources import (
    mock_redis,
    mock_snowflake,
    redis,
    snowflake,
)
from drizly_dagster_utils.utils.slack_logger import json_console_logger

# TODO: Write up a howto for this portion.
# Modes are largely used to define things external to the pipeline that are referenced
# resource_defs points to external resources that may vary by environment.
# e.g. The common use case here is in prod mode we might reference Snowflake but in
# local mode that may be inconvenient or impossible.
# e.g. The more common case where you truly cannot use something locally is one of our
# AWS instances of redis, which don't permit local connection, and in order to use
# a redis connection locally, you would need to stand up your own redis cluster.

local_mode = ModeDefinition(
    name="local",
    resource_defs={"snowflake": snowflake, "redis": redis},
    description="Local mode of pipelines (No AWS, Dev/Local Resources)",
    logger_defs={"custom_logger": json_console_logger},
)

dev_mode = ModeDefinition(
    name="dev",
    description="Dev mode of pipelines (Dev AWS, Dev Resources)",
    resource_defs={"snowflake": snowflake, "redis": redis},
    logger_defs={"custom_logger": json_console_logger},
)

prod_mode = ModeDefinition(
    name="prod",
    description="Production mode of pipelines (Prod AWS, Prod Resources)",
    resource_defs={"snowflake": snowflake, "redis": redis},
    logger_defs={"custom_logger": json_console_logger},
)

test_mode = ModeDefinition(
    name="test",
    resource_defs={"snowflake": mock_snowflake, "redis": mock_redis},
    description="Test mode of pipelines (No AWS, Dev/Local Resources)",
    logger_defs={"custom_logger": json_console_logger},
)
