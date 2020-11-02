from drizly_dagster_utils.integrations.snowflake import SnowflakeConn
from drizly_dagster_utils.intergrations.mysql import MySQLConn
import pandas as pd
from {{cookiecutter.project_slug}}.util.config import cfg

def snowflake_execute_query(sql):
    secret_name = cfg.resources.snowflake.config.secret_name
    region_name = cfg.resources.snowflake.config.region_name
    connection = SnowflakeConn.from_secret(f"{secret_name}", f"{region_name}")
    return connection.execute_query(sql)

def snowflake_dataframe_from_sql(sql):
    result = snowflake_execute_query(sql)
    return pd.DataFrame(result)

def mysql_execute_query(sql):
    secret_name = cfg.resources.mysql.config.secret_name
    region_name = cfg.resources.mysql.config.region_name
    connection = MySQLConn.from_secret(f"{secret_name}", f"{region_name}")
    return connection.execute_query(sql)

def mysql_dataframe_from_sql(sql):
    result = snowflake_execute_query(sql)
    return pd.DataFrame(result)
