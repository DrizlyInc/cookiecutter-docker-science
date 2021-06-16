from dagster.utils import file_relative_path

dev_run_config = {
    "resources": {
        "snowflake": {
            "config": {
                "secret_name": "snowflake/dagster",
                "region": "us-east-1",
            }
        },
        "ge_data_context": {
            "config": {
                "ge_root_dir": file_relative_path(
                    __file__, "../../../great_expectations"
                )
            }
        },
        "s3": {"config": {"bucket": "drizly-ml"}},
    },
    "solids": {
        "get_{{cookiecutter.project_slug}}_df": {
            "inputs": {
                "query": {
                    "value": """SELECT user_id,
      store_id,
      is_gift,
      store_state,
      CEIL(eta_high_actual / 5.0) *5 eta,
      avg(delivery_minutes) delivery_minutes,
      sum(store_order_total) store_order_total
      FROM PROD.REPORTING.STORE_ORDERS_COMPLETED_CORE
      GROUP BY 1,2,3,4,5
      ORDER BY RANDOM()
      LIMIT 1000"""
                }
            }
        },
    }
}
