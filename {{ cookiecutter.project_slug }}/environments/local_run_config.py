from dagster.utils import file_relative_path
#TODO: Any solid that takes an argument from outside of main.py needs to have those arguments defined here
#TODO: The local configuration requires a csv (no headers) be placed in the "data" directory
# that contains the data you want to work with
local_run_config = {
    "resources": {
        "snowflake": {
            "config": {
                "file_path": file_relative_path(
                    __file__, "data/{{cookiecutter.project_slug}}.csv"
                )
            }
        },
        "ge_data_context": {
            "config": {
                "ge_root_dir": file_relative_path(
                    __file__, "great_expectations"
                )
            }
        },
    },
    "solids": {
        "store_order_items": {"inputs": {"query": {"value": "SELECT 1"}}}
    },
}
