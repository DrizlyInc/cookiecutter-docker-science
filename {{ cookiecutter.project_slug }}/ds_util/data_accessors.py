import pandas as pd
from drizly_dagster_utils.integrations.mysql import MySQLConn
from drizly_dagster_utils.integrations.snowflake import SnowflakeConn
from ds_util.config import cfg


def snowflake_execute_query(sql):
    secret_name = cfg.resources.snowflake.config.secret_name
    region = cfg.resources.snowflake.config.region
    connection = SnowflakeConn.from_secret(f"{secret_name}", f"{region}")
    return connection.execute_query_no_fetch(sql)


def snowflake_dataframe_from_sql(sql):
    result = snowflake_execute_query(sql)
    df = pd.DataFrame(result)
    df.columns = result.keys()
    return dfimport pandas as pd
from drizly_dagster_utils.integrations.mysql import MySQLConn
from drizly_dagster_utils.integrations.snowflake import SnowflakeConn
from ds_util.config import cfg


def snowflake_execute_query(sql):
    secret_name = cfg.resources.snowflake.config.secret_name
    region = cfg.resources.snowflake.config.region
    connection = SnowflakeConn.from_secret(f"{secret_name}", f"{region}")
    return connection.execute_query_no_fetch(sql)


def snowflake_dataframe_from_sql(sql):
    result = snowflake_execute_query(sql)
    df = pd.DataFrame(result)
    df.columns = result.keys()
    return df


def mysql_execute_query(sql):
    secret_name = cfg.resources.mysql.config.secret_name
    region = cfg.resources.mysql.config.region
    connection = MySQLConn.from_secret(f"{secret_name}", f"{region}")
    return connection.execute_query(sql)


def mysql_dataframe_from_sql(sql):
    result = mysql_execute_query(sql)
    df = pd.DataFrame(result)
    df.columns = result.keys()
    return df



def mysql_execute_query(sql):
    secret_name = cfg.resources.mysql.config.secret_name
    region = cfg.resources.mysql.config.region
    connection = MySQLConn.from_secret(f"{secret_name}", f"{region}")
    return connection.execute_query(sql)


def mysql_dataframe_from_sql(sql):
    result = mysql_execute_query(sql)
    df = pd.DataFrame(result)
    df.columns = result.keys()
    return df
