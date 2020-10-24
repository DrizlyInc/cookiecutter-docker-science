from integrations.snowflake import SnowflakeConn

if __name__ == '__main__':
    SnowflakeConn.from_secret("snowflake/analytics_api").execute_query("SELECT 'Hello World';")