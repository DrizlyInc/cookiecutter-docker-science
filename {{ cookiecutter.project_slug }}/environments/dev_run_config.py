from dagster.utils import file_relative_path
#TODO: Any solid that takes an argument from outside of main.py needs to have those arguments defined here
#TODO: Write your snowflake queries here
QUERY = """
WITH cte AS(
    SELECT 
        1 AS a
)
SELECT
    a
FROM cte
LIMIT 10
"""


dev_run_config = {
    "resources": {
        "snowflake": {
            "config": {
                "file_path": file_relative_path(
                    __file__, "data/{{cookiecutter.project_slug}}.csv"
                )
            }
        },
        "s3": {"config": {"bucket": "drizly-dev-dagster"}},
        "ge_data_context": {
            "config": {
                "ge_root_dir": file_relative_path(
                    __file__, "great_expectations"
                )
            }
        },
    },
    "solids": {"store_order_items": {"inputs": {"query": {"value": QUERY}}}},
}
