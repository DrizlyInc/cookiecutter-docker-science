"""{{cookiecutter.dagster_repo}} Custom Types"""
from dagster_pandas import PandasColumn, create_dagster_pandas_dataframe_type

{{cookiecutter.project_slug}} = create_dagster_pandas_dataframe_type(
    name="{{cookiecutter.project_slug}}",
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
