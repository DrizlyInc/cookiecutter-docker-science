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

from drizly_dagster_utils.utils.environment_parsing import (
    filter_modes,
    filter_presets,
)

from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.dagster.custom_types import (
    {{cookiecutter.project_slug}}DF,
    {{cookiecutter.project_slug}}TransformedDF,
)
import random
from dagster_ge import ge_validation_solid_factory
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

# GE solid
{{cookiecutter.project_slug}}_expectations = ge_validation_solid_factory(
    name="{{cookiecutter.project_slug}}_expectations",
    datasource_name="pandas",
    suite_name="{{cookiecutter.project_slug}}.basic.warning",
)

@solid
def transform_{{cookiecutter.project_slug}}_df(context, df: {{cookiecutter.project_slug}}DF) -> {{cookiecutter.project_slug}}TransformedDF:
    """Transform Snowflake Dataframe"""
    transformed_df = df.drop(['store_city', 'store_state', 'store_id'], axis=1)
    return transformed_df

@solid
def {{cookiecutter.project_slug}}_df_to_list(context, df: {{cookiecutter.project_slug}}TransformedDF) -> List:
    """Load Snowflake Data as List and log some information"""
    {{cookiecutter.project_slug}}_list = df.values.tolist()
    sample_size = min(len({{cookiecutter.project_slug}}_list), 10)
    context.log.info(str(random.sample({{cookiecutter.project_slug}}_list, sample_size)))
    return {{cookiecutter.project_slug}}_list

@solid(required_resource_keys={"redis"})
def write_{{cookiecutter.project_slug}}_to_redis(context, {{cookiecutter.project_slug}}_list: List) -> None:
    """Load Snowflake Data"""
    # Redis keys and values need to be strings
    list_to_str = [[str(x) for x in row] for row in {{cookiecutter.project_slug}}_list]
    context.resources.redis.write_iter_to_redis(list_to_str)


@pipeline(
    mode_defs=filter_modes([local_mode, dev_mode, prod_mode, test_mode]),
    preset_defs=filter_presets([local, dev, prod, test]),
    tags={"type": "{{cookiecutter.dagster_repo}}"},
)
def {{cookiecutter.project_slug}}_to_redis_pipeline():
    df = get_{{cookiecutter.project_slug}}_df()
    {{ cookiecutter.project_slug }}_expectations(df)
    transformed_df = transform_{{cookiecutter.project_slug}}_df(df)
    {{cookiecutter.project_slug}}_list = {{cookiecutter.project_slug}}_df_to_list(transformed_df)
    write_{{cookiecutter.project_slug}}_to_redis({{cookiecutter.project_slug}}_list)

