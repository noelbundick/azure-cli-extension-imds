import json
from uuid import uuid4
from enum import Enum

from knack.util import CLIError
from http.server import HTTPServer
from azext_imds.imds import AppService2017IMDS, AppService2019IMDS

handler_map = {
    "AppService2017": AppService2017IMDS,
    "AppService2019": AppService2019IMDS,
}


def start_imds(cmd, secret="", host="", port=0, imds_type="AppService2017"):
    if not secret:
        secret = str(uuid4())

    def handler(*args):
        handler_map[imds_type](secret, cmd, *args)

    server = HTTPServer((host, port), handler)

    endpoint_format = "http://{}:{}/MSI/token"
    info = {
        "localIdentityEndpoint": endpoint_format.format(
            "127.0.0.1", server.server_address[1]
        ),
        "dockerIdentityEndpoint": endpoint_format.format(
            "host.docker.internal", server.server_address[1]
        ),
        "identityHeader": str(secret),
    }
    print(json.dumps(info, indent=2))

    server.serve_forever()
