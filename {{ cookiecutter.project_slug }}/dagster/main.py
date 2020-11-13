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

from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.dagster.custom_types import (
    {{cookiecutter.project_slug}}DF,
    {{cookiecutter.project_slug}}TransformedDF,
)

@solid(required_resource_keys={"snowflake"})
def get_{{cookiecutter.project_slug}}_df(context, query: String) -> {{cookiecutter.project_slug}}DF:
    """Load Snowflake Dataframe"""
    {{cookiecutter.project_slug}}_df = context.resources.snowflake.get_pandas_dataframe(query)
    return {{cookiecutter.project_slug}}_df

@solid
def transform_{{cookiecutter.project_slug}}_df(context, df: {{cookiecutter.project_slug}}DF) -> {{cookiecutter.project_slug}}TransformedDF:
    """Transform Snowflake Dataframe"""
    df = context.resources.snowflake.get_pandas_dataframe(query)
    transformed_df = df.drop(['recency_rk', 'recommendation_rk'], axis=1)
    return transformed_df

@solid
def {{cookiecutter.project_slug}}_df_to_list(context, df: {{cookiecutter.project_slug}}TransformedDF) -> List:
    """Load Snowflake Data as List and log some information"""
    {{cookiecutter.project_slug}}_list = df.tolist()
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
    df = get_{{cookiecutter.project_slug}}_df()
    transformed_df = transform_{{cookiecutter.project_slug}}_df(df)
    {{cookiecutter.project_slug}}_list = {{cookiecutter.project_slug}}_df_to_list(transformed_df)
    write_{{cookiecutter.project_slug}}_to_redis({{cookiecutter.project_slug}}_list)


def test_{{cookiecutter.project_slug}}_to_redis_pipeline():
    res = execute_pipeline({{cookiecutter.project_slug}}_to_redis_pipeline)
    assert res.success
    assert len(res.solid_result_list) == 4
    for solid_res in res.solid_result_list:
        assert solid_res.success
