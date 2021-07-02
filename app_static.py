from flask_frozen import Freezer

from website import app

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()


# import pathlib
# import shutil
#
# from jinja2 import Environment, PackageLoader, select_autoescape
#
#
# if __name__ == "__main__":
#     src_path = pathlib.Path("website")
#     target_path = pathlib.Path("target")
#
#     if target_path.exists() and target_path.is_dir():
#         shutil.rmtree(target_path)
#
#     env = Environment(
#         loader=PackageLoader(str(src_path)),
#         autoescape=select_autoescape(),
#     )
#
#     shutil.copytree(src_path / "static", target_path / "static", dirs_exist_ok=True)
#     env.get_template("index.html").stream(template="layout.html").dump(
#         str(target_path / "index.html")
#     )
