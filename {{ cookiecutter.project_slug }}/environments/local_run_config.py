from dagster.utils import file_relative_path

local_run_config = {
    "resources": {
        "snowflake": {
            "config": {
                "file_path": file_relative_path(__file__, "../data"),
            }
        },
        "ge_data_context": {
            "config": {
                "ge_root_dir": file_relative_path(
                    __file__, "../../../great_expectations"
                )
            }
        },
    },
    "solids": {
        "get_{{cookiecutter.project_slug}}_df": {
            "inputs": {"query": {"value": "test.csv"}}
        },
    "write_dataframe_to_snowflake": {
            "inputs": {"table_name": {"value": "schema.table"}}
        },
    },
}
