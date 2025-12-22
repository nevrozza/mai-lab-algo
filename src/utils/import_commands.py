import importlib
import pkgutil


def import_packages() -> None:
    packages = [
        "src.formulas",
        "src.sorts",
    ]

    for package_name in packages:
        try:
            package = importlib.import_module(package_name)
        except ImportError:
            continue

        for _, module_name, y in pkgutil.iter_modules(package.__path__, package.__name__ + "."):
            try:
                importlib.import_module(module_name)
            except ImportError as e:
                print(e)
