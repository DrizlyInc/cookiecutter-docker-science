"""Modes"""
from dagster import ModeDefinition
from drizly_dagster_utils.utils.resources import (
    mock_redis,
    mock_snowflake,
    redis,
    snowflake,
)
from drizly_dagster_utils.utils.slack_logger import json_console_logger
from dagster_ge.factory import ge_data_context

# Modes are largely used to define things external to the pipeline that are referenced
# resource_defs points to external resources that may vary by environment.
# e.g. The common use case here is in prod mode we might reference Snowflake but in
# local mode that may be inconvenient or impossible.
# e.g. The more common case where you truly cannot use something locally is one of our
# AWS instances of redis, which don't permit local connection, and in order to use
# a redis connection locally, you would need to stand up your own redis cluster.

local = ModeDefinition(
    name="local",
    resource_defs={"snowflake": snowflake, "redis": mock_redis, "ge_data_context": ge_data_context},
    description="Local mode of pipelines (No AWS, Dev/Local Resources)",
    logger_defs={"custom_logger": json_console_logger},
)

dev = ModeDefinition(
    name="dev",
    description="Dev mode of pipelines (Dev AWS, Dev Resources)",
    resource_defs={"snowflake": snowflake, "redis": redis, "ge_data_context": ge_data_context},
    logger_defs={"custom_logger": json_console_logger},
)

prod = ModeDefinition(
    name="prod",
    description="Production mode of pipelines (Prod AWS, Prod Resources)",
    resource_defs={"snowflake": snowflake, "redis": redis, "ge_data_context": ge_data_context},
    logger_defs={"custom_logger": json_console_logger},
)

test = ModeDefinition(
    name="test",
    resource_defs={"snowflake": mock_snowflake, "redis": mock_redis, "ge_data_context": ge_data_context},
    description="Test mode of pipelines (No AWS, Dev/Local Resources)",
    logger_defs={"custom_logger": json_console_logger},
)

MODES = [local, dev, prod, test]