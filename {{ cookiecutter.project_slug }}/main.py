"""{{cookiecutter.project_slug}}"""
import pandas as pd
from dagster import String, pipeline, solid
from dagster_ge.factory import ge_validation_solid_factory
#TODO: Replace NameThisDataframe with what is in custom_types.py if you are using pandas
from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.custom_types import (
    NameThisDataframe,
    NameThisDataframeTransformed,
)
from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.modes import (
    dev_mode,
    local_mode,
    prod_mode,
)
from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.presets import dev, local, prod


@solid(required_resource_keys={"snowflake"})
def get_config_query_from_snowflake(context, query: String) -> NameThisDataframe:
    """Load Snowflake Data"""
    df = context.resources.snowflake.get_pandas_dataframe(query)
    return df

@solid(required_resource_keys={"snowflake"})
def transform_df(context, query: String) -> NameThisDataframeTransformed:
    """Load Snowflake Data"""
    result = context.resources.snowflake.execute_query(query)
    return pd.DataFrame(result)

#Example push dataframe to s3
@solid(required_resource_keys={"s3"})
def upload_{{cookiecutter.project_slug}}(
    context, forecast_df: NameThisDataframe
) -> None:
    """Upload data to S3"""
    context.resources.s3.upload_dataframe(
        dataframe=forecast_df, key_path="data/{{cookiecutter.project_slug}}/data.gz"
    )


# GE solid
{{cookiecutter.project_slug}}_expectations = ge_validation_solid_factory(
    name="{{cookiecutter.project_slug}}_expectations",
    datasource_name="getest",
    suite_name="basic.warning",
)


@pipeline(
    mode_defs=[local_mode, dev_mode, prod_mode],
    preset_defs=[local, dev, prod],
    tags={"type": "forecast"},
)
def {{cookiecutter.project_slug}}_pipeline():
    df = get_config_query_from_snowflake()
    transformed_df = transform_df(df)
    {{cookiecutter.project_slug}}_expectations(transformed_df)
    upload_{{cookiecutter.project_slug}}(transformed_df)
