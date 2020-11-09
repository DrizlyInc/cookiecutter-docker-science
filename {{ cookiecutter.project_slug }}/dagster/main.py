import random

from dagster import List, String, execute_pipeline, pipeline, solid
from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.dagster.modes import (
    dev_mode,
    local_mode,
    prod_mode,
    test_mode,
)
from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.dagster.presets import (
    dev,
    local,
    prod,
    test,
)


@solid(required_resource_keys={"snowflake"})
def get_{{cookiecutter.project_slug}}_list(context, query: String) -> List:
    """Load Snowflake Data"""
    {{cookiecutter.project_slug}}_list = context.resources.snowflake.execute_query(query)
    sample_size = min(len({{cookiecutter.project_slug}}_list), 10)
    context.log.info(str(random.sample({{cookiecutter.project_slug}}_list, sample_size)))
    return {{cookiecutter.project_slug}}_list


@solid(required_resource_keys={"redis"})
def write_{{cookiecutter.project_slug}}_to_redis(context, {{cookiecutter.project_slug}}_list: List) -> None:
    """Load Snowflake Data"""
    context.resources.redis.write_iter_to_redis({{cookiecutter.project_slug}}_list)


@pipeline(
    mode_defs=[local_mode, dev_mode, prod_mode, test_mode],
    preset_defs=[local, dev, prod, test],
    tags={"type": "{{cookiecutter.dagster_repo}}"},
)
def {{cookiecutter.project_slug}}_to_redis_pipeline():
    {{cookiecutter.project_slug}}_list = get_{{cookiecutter.project_slug}}_list()
    write_{{cookiecutter.project_slug}}_to_redis({{cookiecutter.project_slug}}_list)


def test_{{cookiecutter.project_slug}}_to_redis_pipeline():
    res = execute_pipeline({{cookiecutter.project_slug}}_to_redis_pipeline)
    assert res.success
    assert len(res.solid_result_list) == 4
    for solid_res in res.solid_result_list:
        assert solid_res.success
