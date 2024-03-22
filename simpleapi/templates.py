from typing import List

from fastapi import APIRouter, FastAPI


def register_routers(app: FastAPI, routers: List[APIRouter]) -> FastAPI:
    for router in routers:
        app.include_router(router)
    return app


class BaseInterface:

    def __init__(self, router: APIRouter, prefix: str, tags: List[str] = None):
        self.router = self.r = router or APIRouter()
        self.prefix = self.p = self._normalize_router_prefix(prefix)
        self.tags = self.t = tags or []

    @staticmethod
    def _normalize_router_prefix(string: str) -> str:
        string = string[:-1] if string[-1] == "/" else string
        string = string[1:] if string[0] == "/" else string
        return f"/{string}"


class GetInterface(BaseInterface):

    def _get(self, *args, **kwargs):
        raise NotImplementedError

    def get(self, *args, **kwargs):
        return self.router.get(prefix=f"{self.p}", tags=self.t)(self._get)(*args, **kwargs)


class PostInterface(BaseInterface):

    def _post(self, *args, **kwargs):
        raise NotImplementedError

    def post(self, *args, **kwargs):
        return self.router.post(prefix=f"{self.p}", tags=self.t)(self._post)(*args, **kwargs)


class PatchInterface(BaseInterface):

    def _patch(self, *args, **kwargs):
        raise NotImplementedError

    def patch(self, *args, **kwargs):
        return self.router.patch(prefix=f"{self.p}", tags=self.t)(self._patch)(*args, **kwargs)


class PutInterface(BaseInterface):

    def _put(self, *args, **kwargs):
        raise NotImplementedError

    def put(self, *args, **kwargs):
        return self.router.put(prefix=f"{self.p}", tags=self.t)(self._put)(*args, **kwargs)


class DeleteInterface(BaseInterface):

    def _delete(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        return self.router.delete(prefix=f"{self.p}", tags=self.t)(self._delete)(*args, **kwargs)


class OptionsInterface(BaseInterface):

    def _options(self, *args, **kwargs):
        raise NotImplementedError

    def options(self, *args, **kwargs):
        return self.router.options(prefix=f"{self.p}", tags=self.t)(self._options)(*args, **kwargs)


class HeadInterface(BaseInterface):

    def _head(self, *args, **kwargs):
        raise NotImplementedError

    def head(self, *args, **kwargs):
        return self.router.head(prefix=f"{self.p}", tags=self.t)(self._head)(*args, **kwargs)


class TraceInterfaces(BaseInterface):

    def _trace(self, *args, **kwargs):
        raise NotImplementedError

    def trace(self, *args, **kwargs):
        return self.router.trace(prefix=f"{self.p}", tags=self.t)(self._trace)(*args, **kwargs)


class ConnectInterface(BaseInterface):

    def _connect(self, *args, **kwargs):
        raise NotImplementedError

    def connect(self, *args, **kwargs):
        # return self.router.connect(prefix=f"{self.rn}", tags=self.t)(self._connect)(*args, **kwargs)
        pass


class AbstractEndpoint(
    GetInterface,
    PostInterface,
    PutInterface,
    PatchInterface,
    DeleteInterface,
    HeadInterface,
    OptionsInterface,
):
    pass


class BaseWebhook(PostInterface, HeadInterface, OptionsInterface):
    pass


class BaseEndpoint(AbstractEndpoint):
    pass
