from dagster import List, String, execute_pipeline, pipeline, solid
from repos.{{cookiecutter.dagster_repo}}.pipelines.{{cookiecutter.project_slug}}.modes import (
    local,
    dev,
    prod,
)
from repos.{{cookiecutter.dagster_repo}}.pipelines.{{cookiecutter.project_slug}}.presets import PRESETS
from repos.{{cookiecutter.dagster_repo}}.solids import write_dataframe_to_snowflake
from repos.{{cookiecutter.dagster_repo}}.pipelines.{{cookiecutter.project_slug}}.custom_types import (
    {{cookiecutter.project_slug}}DF,
    {{cookiecutter.project_slug}}TransformedDF,
)
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
    transformed_df = df.drop(['store_id',
                              'is_gift',
                              'store_state',
                              'eta',
                              'delivery_minutes'], axis=1)
    return transformed_df


@pipeline(
    mode_defs=[local, dev, prod],
    preset_defs=PRESETS,
    tags={"type": "{{cookiecutter.dagster_repo}}"},
)
def {{cookiecutter.project_slug}}_to_snowflake_pipeline():
    df = get_{{cookiecutter.project_slug}}_df()
    {{ cookiecutter.project_slug }}_expectations(df)
    transformed_df = transform_{{cookiecutter.project_slug}}_df(df)
    write_dataframe_to_snowflake(transformed_df)

