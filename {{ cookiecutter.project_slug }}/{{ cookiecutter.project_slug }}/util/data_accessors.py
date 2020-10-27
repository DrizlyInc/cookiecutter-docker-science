from integrations.snowflake import SnowflakeConn, MySQLConn, s3
import pandas as pd
from config import resource_config

def snowflake_execute_query(sql):
    secret_name = resource_config.resources.snowflake.config.secret_name
    region_name = resource_config.resources.snowflake.config.region_name
    connection = SnowflakeConn.from_secret(f"{secret_name}", f"{region_name}")
    return connection.execute_query(sql)

def snowflake_dataframe_from_sql(sql):
    result = snowflake_execute_query(sql)
    return pd.DataFrame(result)

def mysql_execute_query(sql):
    secret_name = resource_config.resources.mysql.config.secret_name
    region_name = resource_config.resources.mysql.config.region_name
    connection = MySQLConn.from_secret(f"{secret_name}", f"{region_name}")
    return connection.execute_query(sql)

def mysql_dataframe_from_sql(sql):
    result = snowflake_execute_query(sql)
    return pd.DataFrame(result)
