from typing import List

from fastapi import APIRouter as FastAPIRouter
from fastapi.responses import JSONResponse


class APIErrors:

    @staticmethod
    def _405():
        return JSONResponse(
            status_code=405,
            content={"message": "Method Not Allowed"},
        )


class AbstractPathStyle:
    PATHS = {
        "OPTIONS": "/{id}",
        "HEAD": "/{id}",
        "DELETE": "/{id}",
        "PATCH": "/{id}",
        "PUT": "/{id}",
        "POST": "/{id}",
        "GET": "/{id}",
    }


class DjangoPathStyle:
    pass


class UserFrendlyPathStyle:
    PATHS = {
        "OPTIONS": "/{id}/options",
        "HEAD": "/{id}/head",
        "DELETE": "/{id}/delete",
        "PATCH": "/{id}/edit",
        "PUT": "/{id}/edit",
        "POST": "/{id}/create",
        "GET": "/list",
    }


class EndpointsRegister:

    def __init__(self, app, endpoints: List["BaseEndpoint"]):
        for endpoint in endpoints:
            prefix = endpoint.PREFIX
            tags = endpoint.TAGS
            methods = endpoint.methods
            print(methods)
            router = FastAPIRouter(prefix=prefix, tags=tags)
            for http_method in methods:
                path = endpoint.paths[http_method.lower()]
                method = getattr(endpoint, http_method.lower())
                router.add_api_route(methods=[http_method], path=path, endpoint=method)
            app.include_router(router)


class AbstractEndpoint:
    PREFIX: str = None
    TAGS: List[str] = None


class BaseEndpoint:

    def __init__(self, *args, **kwargs):
        self.methods = []
        self.paths = kwargs.get("paths", UserFrendlyPathStyle).PATHS

    def set_paths(self, paths_stype: "AbstractPathStyle"):
        self.paths = paths_stype.PATHS


class GetEndpoint(BaseEndpoint):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.methods.append("GET")

    def _get(self, *args, **kwargs):
        raise NotImplementedError

    def get(self, *args, **kwargs):
        return self._get(*args, **kwargs)


class PostEndpoint(BaseEndpoint):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.methods.append("POST")

    def _post(self, *args, **kwargs):
        raise NotImplementedError

    def post(self, *args, **kwargs):
        return self._post(*args, **kwargs)


class PatchEndpoint(BaseEndpoint):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.methods.append("PATCH")

    def _patch(self, *args, **kwargs):
        raise NotImplementedError

    def patch(self, *args, **kwargs):
        return self.patch(*args, **kwargs)


class PutEndpoint(BaseEndpoint):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.methods.append("PUT")

    def _put(self, *args, **kwargs):
        raise NotImplementedError

    def put(self, *args, **kwargs):
        return self._put(*args, **kwargs)


class DeleteEndpoint(BaseEndpoint):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.methods.append("DELETE")

    def _delete(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        return self._delete(*args, **kwargs)


class OptionsEndpoint(BaseEndpoint):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.methods.append("OPTIONS")

    def _options(self, *args, **kwargs):
        raise NotImplementedError

    def options(self, *args, **kwargs):
        return self._options(*args, **kwargs)


class HeadEndpoint(BaseEndpoint):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.methods.append("HEAD")

    def _head(self, *args, **kwargs):
        raise NotImplementedError

    def head(self, *args, **kwargs):
        return self._head(*args, **kwargs)


class TraceEndpoints(BaseEndpoint):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.methods.append("TRACE")

    def _trace(self, *args, **kwargs):
        raise NotImplementedError

    def trace(self, *args, **kwargs):
        return self._trace(*args, **kwargs)


class ConnectEndpoint(BaseEndpoint):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.methods.append("CONNECT")

    def _connect(self, *args, **kwargs):
        raise NotImplementedError

    def connect(self, *args, **kwargs):
        pass


class AbstractRouter(
    GetEndpoint,
    PostEndpoint,
    PutEndpoint,
    PatchEndpoint,
    DeleteEndpoint,
    HeadEndpoint,
    OptionsEndpoint,
):
    pass


class BaseWebhook(PostEndpoint, HeadEndpoint, OptionsEndpoint):
    pass


class BaseEndpoint(AbstractEndpoint):
    pass
