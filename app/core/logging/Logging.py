import importlib


class Logging:
    logger_class_object = None

    def __init__(self, filename="request_log", logger_name="Loguru"):
        class_ = getattr(importlib.import_module("app.core.logging." + logger_name), logger_name)
        self.logger_class_object = class_()
        self.logger_class_object.init_log(filename)
