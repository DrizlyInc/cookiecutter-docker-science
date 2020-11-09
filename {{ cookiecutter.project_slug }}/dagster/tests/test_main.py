"""Test Supplier Forecast"""
import unittest

import pytest
from dagster import execute_pipeline, execute_solid
from repos.datascience.{{cookiecutter.project_slug}}.dagster.main import (
    get_{{cookiecutter.project_slug}}_list,
    write_{{cookiecutter.project_slug}}_to_redis,
)
from repos.datascience.{{cookiecutter.project_slug}}.dagster.modes import (
    dev_mode,
    local_mode,
    test_mode,
)
from repos.datascience.{{cookiecutter.project_slug}}.ds_util.config import test_cfg


class Test{{cookiecutter.project_slug}}(unittest.TestCase):
    """Test Supplier Forecast"""

    @pytest.mark.datascience
    def test_get_because_you_bought_list(self):
        """Store order items"""
        result = execute_solid(
            get_{{cookiecutter.project_slug}}_list,
            mode_def=test_mode,
            run_config=test_cfg.to_dict(),
            input_values={"query": "SELECT 1"},
        )
        self.assertTrue(result)

    @pytest.mark.datascience
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
