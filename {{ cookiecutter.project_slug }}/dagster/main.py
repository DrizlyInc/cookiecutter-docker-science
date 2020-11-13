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

#TODO: There are many TODOs flagged throughout this project that you will need to
# configure before your project will run properly.
# You need to (if you plan on using some of the pandas solids below):
# 1) Edit the queries in the config directory to pull the data you want
# 2) Edit the custom types to match the columns from ^ these queries
# 3) Change test.csv to match the columns in the custom types/output of your queries
# If you search the project for TODO flags you should find this (except for config files)
# The project out of the box will pull from PROD.REPORTING.STORE_ORDERS_COMPLETED_CORE to demonstrate a functioning flow

@solid(required_resource_keys={"snowflake"})
def get_{{cookiecutter.project_slug}}_df(context, query: String) -> {{cookiecutter.project_slug}}DF:
    """Load Snowflake Dataframe"""
    {{cookiecutter.project_slug}}_df = context.resources.snowflake.get_pandas_dataframe(query)
    return {{cookiecutter.project_slug}}_df

@solid
def transform_{{cookiecutter.project_slug}}_df(context, df: {{cookiecutter.project_slug}}DF) -> {{cookiecutter.project_slug}}TransformedDF:
    """Transform Snowflake Dataframe"""
    df = context.resources.snowflake.get_pandas_dataframe(query)
    transformed_df = df.drop(['store_city', 'store_state'], axis=1)
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

