"""Test {{cookiecutter.project_slug}}"""
import pytest
import unittest
from dagster import execute_pipeline, execute_solid

#TODO: If you remove or add solids, you'll need to add tests in here accordingly
from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.dagster.main import (
    get_{{cookiecutter.project_slug}}_df,
    transform_{{cookiecutter.project_slug}}_df,
    {{cookiecutter.project_slug}}_df_to_list,
    write_{{cookiecutter.project_slug}}_to_redis,
    {{cookiecutter.project_slug}}_to_redis_pipeline,
)

from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.dagster.modes import (
    test_mode,
)

from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.ds_util.config import test_cfg, get_project_root

import pandas as pd

#TODO: If you remove or add solids, you'll need to add tests in here accordingly
class Test{{cookiecutter.project_slug}}(unittest.TestCase):
    """Test {{cookiecutter.project_slug}}"""

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_{{cookiecutter.project_slug}}_df(self):
        """{{cookiecutter.project_slug}}"""
        result = execute_solid(
            get_{{cookiecutter.project_slug}}_df,
            mode_def=test_mode,
            run_config=test_cfg.to_dict(),
            input_values={"query": "SELECT 1"},
        )
        self.assertTrue(result)

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_transform_{{cookiecutter.project_slug}}_df(self):
        """Transform Snowflake Dataframe"""
        result = execute_solid(
            transform_{{cookiecutter.project_slug}}_df,
            mode_def = test_mode,
            run_config = test_cfg.to_dict(),
            input_values = {"df": pd.read_csv(get_project_root().joinpath("dagster/tests/test.csv")},
        )
        self.assertTrue(result)

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def {{cookiecutter.project_slug}}_df_to_list(self):
        """Load Snowflake Data as List and log some information"""
        result = execute_solid(
            {{cookiecutter.project_slug}}_df_to_list,
            mode_def = test_mode,
            run_config = test_cfg.to_dict(),
            input_values = {"df": pd.DataFrame(['1', '2'], columns = ['store_order_id', 'order_id'])},
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

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_{{cookiecutter.project_slug}}_to_redis_pipeline():
        res = execute_pipeline({{cookiecutter.project_slug}}_to_redis_pipeline)
        assert res.success
        assert len(res.solid_result_list) == 4
        for solid_res in res.solid_result_list:
            assert solid_res.success
