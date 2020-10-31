from sklearn.externals import joblib
from sklearn.base import BaseEstimator
from drizly_dagster_utils.integrations.s3 import S3
from {{cookiecutter.project_slug}}.util.config import cfg


def save_model(model: BaseEstimator,) -> None:
    joblib.dump(model, f"{cfg.model.train_output}{cfg.model.model_name}")

def push_model_to_s3() -> None:
    s3 = S3(cfg.resources.s3.config.bucket)
    s3.upload_file(
        key_path=f"{cfg.resources.s3.{{cookiecutter.project_slug}}.key_path}",
        local_path=f"{cfg.model.train_output}{cfg.model.model_name}",
    )
