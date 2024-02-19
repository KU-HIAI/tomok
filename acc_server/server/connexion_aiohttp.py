# python
import os

# 3rd-party
import connexion
from aiohttp import web
import aiohttp_cors
from hydra.utils import to_absolute_path
from setproctitle import setproctitle


class ConnexionAioHttpApp():
    def __init__(self, *args, **kwargs):
        # init aio http server
        app = connexion.AioHttpApp(__name__, specification_dir=to_absolute_path(kwargs['specification_dir']))
        app.app._client_max_size = kwargs['client_max_size']
        # add api files
        for api_file in kwargs['api_files']:
            app.add_api(os.path.join(app.specification_dir, api_file))
        # cors
        cors = aiohttp_cors.setup(app.app, defaults={
            "*": aiohttp_cors.ResourceOptions(allow_credentials=True,
                                            expose_headers="*",
                                            allow_headers="*", allow_methods=["GET", "POST", "PUT"]
                                            )
        })
        for route in list(app.app.router.routes()):
            cors.add(route)
        # cuda
        if('cuda_visible_devices' in kwargs.keys()):
            os.environ["CUDA_VISIBLE_DEVICES"] = str(kwargs['cuda_visible_devices'])
        # process title
        if('process_title' in kwargs.keys()):
            setproctitle(kwargs['process_title'])
        # ready
        self.app = app
