"""{{cookiecutter.project_slug}} Custom Types"""
from dagster_pandas import PandasColumn, create_dagster_pandas_dataframe_type

#TODO: Match this to what your input queries from Snowflake produces
{{cookiecutter.project_slug}}DF = create_dagster_pandas_dataframe_type(
    name="{{cookiecutter.project_slug}}DF",
    columns=[
        PandasColumn("user_id"),
        PandasColumn("store_id"),
        PandasColumn("is_gift"),
        PandasColumn("store_state"),
        PandasColumn("eta"),
        PandasColumn("delivery_minutes"),
        PandasColumn("store_order_total"),
    ],
)
{{cookiecutter.project_slug}}TransformedDF = create_dagster_pandas_dataframe_type(
    name="{{cookiecutter.project_slug}}TransformedDF",
    columns=[
        PandasColumn("user_id"),
        PandasColumn("store_order_total"),
    ],
)
