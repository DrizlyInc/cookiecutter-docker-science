"""Test {{cookiecutter.project_slug}}"""
import pytest
from dagster import execute_pipeline, execute_solid
from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.dagster.main import (
    get_{{cookiecutter.project_slug}}_df,
    transform_{{cookiecutter.project_slug}}_df,
    {{cookiecutter.project_slug}}_df_to_list,
    write_{{cookiecutter.project_slug}}_to_redis,
)

from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.dagster.modes import (
    dev_mode,
    local_mode,
    test_mode,
)
from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.dagster.custom_types import (
    {{cookiecutter.project_slug}}TransformedDF,
    {{cookiecutter.project_slug}}DF,
)

from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.ds_util.config import test_cfg

import pandas as pd

class Test{{cookiecutter.project_slug}}(unittest.TestCase):
    """Test {{cookiecutter.project_slug}}"""

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_{{cookiecutter.project_slug}}_df(self):
        """{{cookiecutter.project_slug}}"""
        result = execute_solid(
            get_{{cookiecutter.project_slug}}_list,
            mode_def=test_mode,
            run_config=test_cfg.to_dict(),
            input_values={"query": "SELECT 1"},
        )
        self.assertTrue(result)

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_transform_{{cookiecutter.project_slug}}_df(context, df: {{cookiecutter.project_slug}}DF) -> {{cookiecutter.project_slug}}TransformedDF:
        """Transform Snowflake Dataframe"""
        result = execute_solid(
            transform_{{cookiecutter.project_slug}}_df,
            mode_def = test_mode,
            run_config = test_cfg.to_dict(),
            input_values = {"df": pd.read_csv("test.csv")},
        )
        self.assertTrue(result)

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def {{cookiecutter.project_slug}}_df_to_list(context, df: {{cookiecutter.project_slug}}TransformedDF) -> List:
        """Load Snowflake Data as List and log some information"""
        result = execute_solid(
            {{cookiecutter.project_slug}}_df_to_list,
            mode_def = test_mode,
            run_config = test_cfg.to_dict(),
            input_values = {"df": pd.DataFrame(['1', '2'])},
        )
        self.assertTrue(result)

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_write_{{cookiecutter.project_slug}}_to_redis(self):
        """Test subcategory forecast"""
        records = [
            ("k", "v"),
            ("k2", "v2"),
        ]
        result = execute_solid(
            write_{{cookiecutter.project_slug}}_to_redis,
            mode_def=test_mode,
            input_values={"{{cookiecutter.project_slug}}_list": records},
            run_config=test_cfg.to_dict(),
        )
        self.assertTrue(result)


# TODO: Write the pipeline test
