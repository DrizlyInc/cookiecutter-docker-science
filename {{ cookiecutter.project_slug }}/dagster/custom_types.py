"""{{cookiecutter.project_slug}} Custom Types"""
from dagster_pandas import PandasColumn, create_dagster_pandas_dataframe_type

{{cookiecutter.project_slug}}DF = create_dagster_pandas_dataframe_type(
    name="{{cookiecutter.project_slug}}DF",
    columns=[
        PandasColumn("user_id"),
        PandasColumn("catalog_item_id"),
        PandasColumn("recommendations"),
        PandasColumn("score"),
        PandasColumn("volume_rk"),
        PandasColumn("recency_rk"),
        PandasColumn("recommendation_rk"),
    ],
)

{{cookiecutter.project_slug}}TransformedDF = create_dagster_pandas_dataframe_type(
    name="{{cookiecutter.project_slug}}TransformedDF",
    columns=[
        PandasColumn("user_id"),
        PandasColumn("catalog_item_id"),
        PandasColumn("recommendations"),
        PandasColumn("score"),
        PandasColumn("volume_rk"),
    ],
)
