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
from drizly_dagster_utils.utils.test_utils import add_solid_to_config
from repos.{{cookiecutter.dagster_repo}}.{{cookiecutter.project_slug}}.ds_util.config import cfg, get_project_root
run_config = cfg.to_dict()
import pandas as pd

#TODO: If you remove or add solids, you'll need to add tests in here accordingly
class Test{{cookiecutter.project_slug}}(unittest.TestCase):
    """Test {{cookiecutter.project_slug}}"""

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_{{cookiecutter.project_slug}}_df(self):
        """{{cookiecutter.project_slug}}"""
        solid_name = "get_{{cookiecutter.project_slug}}_df"
        input_values_dict = {"query": "SELECT 1"}
        result = execute_solid(
            get_{{cookiecutter.project_slug}}_df,
            mode_def=test_mode,
            run_config=add_solid_to_config(run_config, solid_name, input_values_dict)),
        self.assertTrue(result)

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_transform_{{cookiecutter.project_slug}}_df(self):
        """Transform Snowflake Dataframe"""
        solid_name = "transform_{{cookiecutter.project_slug}}_df"
        input_values_dict = {"df": pd.DataFrame([1,2,3,4,5],
                                               columns = ["store_order_id",
                                                          "order_id",
                                                          "store_id",
                                                          "store_city",
                                                          "store_state"])}
        result = execute_solid(
            transform_{{cookiecutter.project_slug}}_df,
            mode_def = test_mode,
            run_config=add_solid_to_config(run_config, solid_name, input_values_dict)),
        )
        self.assertTrue(result)


    @pytest.mark.{{cookiecutter.dagster_repo}}
    def {{cookiecutter.project_slug}}_df_to_list(self):
        """Load Snowflake Data as List and log some information"""
        solid_name = "{{cookiecutter.project_slug}}_df_to_list"
        input_values_dict = {"df": pd.DataFrame(['1', '2'], columns = ['store_order_id', 'order_id'])}
        result = execute_solid(
            {{cookiecutter.project_slug}}_df_to_list,
            mode_def = test_mode,
            run_config=add_solid_to_config(run_config, solid_name, input_values_dict)),
        )
        self.assertTrue(result)

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_write_{{cookiecutter.project_slug}}_to_redis(self):
        """Test subcategory forecast"""
        solid_name = write_{{cookiecutter.project_slug}}_to_redis
        {"{{cookiecutter.project_slug}}_list":  [
            ("k", "v"),
            ("k2", "v2"),
        ]
        }
        result = execute_solid(
            write_{{cookiecutter.project_slug}}_to_redis,
            mode_def=test_mode,
            run_config=add_solid_to_config(run_config, solid_name, input_values_dict)),
        )
        self.assertTrue(result)

    @pytest.mark.{{cookiecutter.dagster_repo}}
    def test_{{cookiecutter.project_slug}}_to_redis_pipeline(self):
        res = execute_pipeline({{cookiecutter.project_slug}}_to_redis_pipeline,
                                preset="test",)
        assert res.success
        assert len(res.solid_result_list) == 4
        for solid_res in res.solid_result_list:
            assert solid_res.success
