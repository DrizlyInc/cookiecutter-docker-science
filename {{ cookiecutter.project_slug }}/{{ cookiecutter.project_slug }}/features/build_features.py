from ds_util.data_accessors import snowflake_dataframe_from_sql

if __name__ == '__main__':
    df = snowflake_dataframe_from_sql("SELECT 1 as feature_1, 2 as feature_2;")