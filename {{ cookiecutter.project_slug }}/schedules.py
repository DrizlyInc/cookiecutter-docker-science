from dagster import ScheduleDefinition
from repos.{{cookiecutter.dagster_repo}}.pipelines.{{cookiecutter.project_slug}}.environments.prod_run_config import (
    prod_run_config,
)

{{cookiecutter.project_slug}}_schedule = ScheduleDefinition(
    name="{{cookiecutter.project_slug}}",
    cron_schedule="0 12 * * *",
    execution_timezone="UTC",
    pipeline_name="{{cookiecutter.project_slug}}_pipeline",
    run_config=prod_run_config,
    mode="prod",
)
