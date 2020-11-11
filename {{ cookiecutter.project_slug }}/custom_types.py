"""Supplier Custom Types"""
from dagster_pandas import PandasColumn, create_dagster_pandas_dataframe_type
#TODO: Name this dataframe and plug it in to main.py as a type hint for the get class
#TODO: Replace the columns with the correct columns for your query
NameThisDataframe = create_dagster_pandas_dataframe_type(
    name="NameThisDataframe",
    columns=[
        PandasColumn("delivered_at"),
        PandasColumn("top_subcategory"),
        PandasColumn("gmv"),
    ],
)


NameThisDataframeTransformed = create_dagster_pandas_dataframe_type(
    name="NameThisDataframeTransformed",
    columns=[
        PandasColumn.datetime_column("ds"),
        PandasColumn.float_column("yhat"),
        PandasColumn.float_column("yhat_lower"),
        PandasColumn.float_column("yhat_upper"),
        PandasColumn.string_column("top_subcategory"),
    ],
)
