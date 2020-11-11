"""Test Supplier Forecast"""
import datetime
import unittest

import pandas as pd
import pytest
from dagster import execute_pipeline, execute_solid
from drizly_dagster_utils.utils.modes import local_mode
from repos.forecasts.supplier_forecast.environments.test_run_config import (
    test_run_config,
)
from repos.forecasts.supplier_forecast.main import (
    store_order_items,
    supplier_forecast,
    supplier_forecast_pipeline,
    upload_supplier_forecast,
)


class TestSupplierForecast(unittest.TestCase):
    """Test Supplier Forecast"""

    def test_store_order_items(self):
        """Store order items"""
        result = execute_solid(
            store_order_items,
            mode_def=local_mode,
            input_values={"query": "SELECT 1"},
            run_config=test_run_config,
        )
        self.assertTrue(result)

    @pytest.mark.datascience
    def test_supplier_forecast(self):
        """Test subcategory forecast"""
        records = [
            {
                "delivered_at": "2020-05-15",
                "top_subcategory": "Gin",
                "gmv": 69569.04,
            },
            {
                "delivered_at": "2020-05-14",
                "top_subcategory": "Gin",
                "gmv": 43214.04,
            },
        ]

        result = execute_solid(
            supplier_forecast,
            mode_def=local_mode,
            input_values={"store_order_df": pd.DataFrame(records)},
            run_config=test_run_config,
        )
        self.assertTrue(result)

    def test_upload_supplier_forecast(self):
        """Test upload supplier forecast"""
        records = [
            {
                "ds": datetime.datetime.strptime("2020-05-15", "%Y-%m-%d"),
                "yhat": 69569.04,
                "yhat_lower": 69569.04,
                "yhat_upper": 69569.04,
                "top_subcategory": "Gin",
            },
        ]

        result = execute_solid(
            upload_supplier_forecast,
            mode_def=local_mode,
            input_values={"forecast_df": pd.DataFrame(records)},
            run_config=test_run_config,
        )
        self.assertTrue(result)

    @pytest.mark.datascience
    def test_pipeline(self):
        """Test pipeline"""
        execute_pipeline(supplier_forecast_pipeline, preset="local")
