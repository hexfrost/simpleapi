from typing import List

from fastapi import APIRouter


def register_routers(app: object, routers: List[object]) -> None:
    pass


class BaseInterface:

    def __init__(self, router: APIRouter, route_name: str, tags: List[str] = None):
        self.router = self.r = router or APIRouter()
        self.route_name = self.rn = route_name
        self.tags = self.t = tags or []


class GetInterface(BaseInterface):

    def _get(self, *args, **kwargs):
        raise NotImplementedError

    def get(self, *args, **kwargs):
        return self.router.get(prefix, f"{self.rn}")(self._get)(*args, **kwargs)


class PostInterface(BaseInterface):
    def _post(self, *args, **kwargs):
        raise NotImplementedError

    def post(self, *args, **kwargs):
        return self.router.post(prefix, f"{self.rn}")(self._post)(*args, **kwargs)


class PatchInterface(BaseInterface):
    def _patch(self, *args, **kwargs):
        raise NotImplementedError

    def patch(self, *args, **kwargs):
        return self.router.patch(prefix, f"{self.rn}")(_patch)(*args, **kwargs)


class PutInterface(BaseInterface):
    def _put(self, *args, **kwargs):
        raise NotImplementedError

    def put(self, *args, **kwargs):
        return self.router.put(prefix, f"{self.rn}")(_put)(*args, **kwargs)


class DeleteInterface(BaseInterface):
    def _delete(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        return self.router.delete(prefix, f"{self.rn}")(_delete)(*args, **kwargs)


class OptionInterface(BaseInterface):
    def _option(self, *args, **kwargs):
        raise NotImplementedError

    def option(self, *args, **kwargs):
        return self.router.option(prefix, f"{self.rn}")(_option)(*args, **kwargs)


class HeadInterface(BaseInterface):
    def _head(self, *args, **kwargs):
        raise NotImplementedError

    def head(self, *args, **kwargs):
        return self.router.head(prefix, f"{self.rn}")(_head)(*args, **kwargs)


class TraceInterfaces(BaseInterface):
    def _trace(self, *args, **kwargs):
        raise NotImplementedError

    def trace(self):
        return self.router.get(prefix, f"{self.rn}")(_get)(*args, **kwargs)


class ConnectInterface(BaseInterface):
    def _connect(self, *args, **kwargs):
        raise NotImplementedError

    def connect(self):
        return self.router.get(prefix, f"{self.rn}")(_get)(*args, **kwargs)


class AbstractEndpoint(
    GetInterface, PostInterface, PutInterface, PatchInterface, DeleteInterface, HeadInterface, OptionInterface, ):
    pass


x
return self.router.get(prefix, f"{self.rn}")(_get)(*args, **kwargs)


class BaseWebhook(PostInterface, HeadInterface, OptionInterface):
    pass


class BaseEndpoint(AbstractEndpoint):
