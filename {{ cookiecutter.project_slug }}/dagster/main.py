
from dagster import pipeline, execute_pipeline
from repos.datascience.{{cookiecutter.project_slug}}.dagster.custom_types import {{cookiecutter.project_slug}}DataframeType
import pandas as pd
from dagster import (
    pipeline,
    solid,
    String,
)

from repos.datascience.{{cookiecutter.project_slug}}.dagster.modes import local_mode, dev_mode, prod_mode
from repos.datascience.{{cookiecutter.project_slug}}.dagster.presets import local, dev, prod


@solid(required_resource_keys={"snowflake"})
def get_{{cookiecutter.project_slug}}_df(context, query: String) -> {{cookiecutter.project_slug}}DataframeType:
    """Load Snowflake Data"""
    result = context.resources.snowflake.execute_query(query)
    context.log.info(type(result))
    df = pd.DataFrame(result)
    df.columns = result.keys()
    context.log.info(df.sample(n=10).to_string())
    return df


@pipeline(
    mode_defs=[local_mode, dev_mode, prod_mode],
    preset_defs=[local, dev, prod],
    tags={"type": "datascience"},
)

def {{cookiecutter.project_slug}}_pipeline():
    {{cookiecutter.project_slug}}_df = get_{{cookiecutter.project_slug}}_df()


def test_{{cookiecutter.project_slug}}_pipeline():
    res = execute_pipeline({{cookiecutter.project_slug}}_pipeline)
    assert res.success
    assert len(res.solid_result_list) == 4
    for solid_res in res.solid_result_list:
        assert solid_res.success