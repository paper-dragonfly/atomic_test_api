# Business Logic - declutter api.py by writing supporting functions here
import os
import yaml

def get_env(env='dev_local'):
    if os.getenv("ENV"):
        return os.getenv("ENV")
    return env
        

# def get_conn_str(env:str, config_file:str = 'config/config.yaml') -> str:
#     """
#     Get database connection string from config file or environment variable
#     """
#     print(f'ENV is: {env}')
#     if env == 'production':
#         return os.getenv("conn_str")
#     elif env == 'dev_local' or env=='dev_hybrid' or env=='dev_test':
#         with open(config_file, 'r') as file:
#             config_dict = yaml.safe_load(file)
#         conn_str = config_dict[env]["conn_str"]
#     else:
#         conn_str = 'no conn_str'
#     return conn_str

