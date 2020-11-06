from {{cookiecutter.project_slug}}.ds_util import model_util

if __name__ == "__main__":
    trained_model = None
    model_util.save_model(model=trained_model)