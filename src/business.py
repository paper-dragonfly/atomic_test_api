# Business Logic - declutter api.py by writing supporting functions here

import yaml

def get_conn_str(env:str = 'dev_local', config_file:str = 'config/config.yaml') -> str:
    """
    Get database connection string from config file
    """
    with open(config_file, 'r') as file:
        config_dict = yaml.safe_load(file)
    conn_str = config_dict[env]["conn_str"]
    return conn_str