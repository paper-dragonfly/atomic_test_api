# Business Logic - declutter api.py by writing supporting functions here
import os
import yaml

def get_env(env='dev_local'):
    pass

def get_conn_str(env:str, config_file:str = 'config/config.yaml') -> str:
    """
    Get database connection string from config file or environment variable
    """
    if env == 'production':
        return os.getenv(conn_str)
    with open(config_file, 'r') as file:
        config_dict = yaml.safe_load(file)
    conn_str = config_dict[env]["conn_str"]
    return conn_str

