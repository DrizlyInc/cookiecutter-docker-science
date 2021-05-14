"""Test {{cookiecutter.project_slug}}"""
import pytest
import unittest
from dagster import execute_pipeline, execute_solid

#TODO: If you remove or add solids, you'll need to add tests in here accordingly
from repos.{{cookiecutter.dagster_repo}}.pipelines.{{cookiecutter.project_slug}}.main import (
    get_{{cookiecutter.project_slug}}_df,
    transform_{{cookiecutter.project_slug}}_df,
    {{cookiecutter.project_slug}}_to_redis_pipeline,
)

from repos.{{cookiecutter.dagster_repo}}.pipelines.{{cookiecutter.project_slug}}.modes import test as test_mode
from drizly_dagster_utils.utils.test_utils import add_solid_to_config
import pandas as pd

#TODO: If you remove or add solids, you'll need to add tests in here accordingly
class Test{{cookiecutter.project_slug}}(unittest.TestCase):
    """Test {{cookiecutter.project_slug}}"""

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_{{cookiecutter.project_slug}}_df(self):
        """{{cookiecutter.project_slug}}"""
        input_values_dict = {"query": "SELECT 1"}
        result = execute_solid(
            get_{{cookiecutter.project_slug}}_df,
            mode_def=test_mode,
            run_config=run_config,
            input_values=input_values_dict,
        )
        self.assertTrue(result)

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_transform_{{cookiecutter.project_slug}}_df(self):
        """Transform Snowflake Dataframe"""
        input_values_dict = {"df": pd.DataFrame([[1,2,3,4,5,6,7]],
                                               columns = ["user_id",
                                                          "store_id",
                                                          "is_gift",
                                                          "store_state",
                                                          "eta",
                                                          "delivery_minutes",
                                                          "store_order_total",])}
        result = execute_solid(
            transform_{{cookiecutter.project_slug}}_df,
            mode_def = test_mode,
            run_config=run_config,
            input_values=input_values_dict,
        )
        self.assertTrue(result)

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_{{cookiecutter.project_slug}}_to_snowflake_pipeline(self):
        first_solid_name = "get_{{cookiecutter.project_slug}}_df"
        first_input_values_dict = {"query": "SELECT 1"}
        pipeline_run_config = add_solid_to_config(run_config, first_solid_name, first_input_values_dict)
        res = execute_pipeline({{cookiecutter.project_slug}}_to_snowflake_pipeline,
                                mode="test",
                                run_config=pipeline_run_config,
        )
        print(res)
        assert res.success
        # This should be the number of solids
        assert len(res.solid_result_list) == 5
        for solid_res in res.solid_result_list:
            assert solid_res.success
