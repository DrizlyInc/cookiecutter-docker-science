from sklearn.externals import joblib
from config import resource_config
config_output_directory = resource_config.job_configuration.output_directory

def save_model(model, target_directory=f"{config_output_directory}"):
    joblib.dump(model, target_directory)
