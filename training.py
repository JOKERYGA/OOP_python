from typing import Any


class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func

# здесь объявляйте декоратор Callback
class Callback:
    def __init__(self, path, router_cls) -> None:
        self.path = path
        self.router_cls = router_cls
    
    def __call__(self, func) -> Any:
        self.router_cls.add_callback(self.path, func)
        return func