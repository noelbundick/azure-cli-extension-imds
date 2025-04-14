from enum import Enum
from base64 import b64decode
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from azure.cli.command_modules.profile.custom import get_access_token

import json
import time


class AppService2017IMDS(BaseHTTPRequestHandler):
    def __init__(self, secret, cmd, *args):
        self.secret = secret
        self.cmd = cmd
        super(AppService2017IMDS, self).__init__(*args)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path != "/MSI/token":
            print(f"{url.path} does not match /MSI/token")
            self.send_response(404)
            return

        identity_header = self.headers.get("secret")
        if identity_header != self.secret:
            print("Identity header missing or invalid")
            self.send_response(400)
            return

        query = parse_qs(url.query)
        resource = query.get("resource")[0]
        if not resource:
            print("No resource specified")
            self.send_response(400)
            return

        api_version = query.get("api-version")[0]
        if api_version != "2017-09-01":
            print("api-version missing or invalid")
            self.send_response(400)
            return

        cli_token = get_access_token(self.cmd, resource=resource)
        jwt = cli_token["accessToken"]
        payload = json.loads(b64decode(jwt.split(".")[1] + "==="))

        token = {
            "access_token": cli_token["accessToken"],
            "client_id": "",
            "expires_on": payload["exp"],
            "not_before": str(payload["nbf"]),
            "resource": resource,
            "token_type": "Bearer",
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(token).encode("utf-8"))


class AppService2019IMDS(BaseHTTPRequestHandler):
    def __init__(self, secret, cmd, *args):
        self.secret = secret
        self.cmd = cmd
        super(AppService2019IMDS, self).__init__(*args)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path != "/MSI/token":
            print(f"{url.path} does not match /MSI/token")
            self.send_response(404)
            return

        identity_header = self.headers.get("X-IDENTITY-HEADER")
        if identity_header != self.secret:
            print("Identity header missing or invalid")
            self.send_response(400)
            return

        query = parse_qs(url.query)
        resource = query.get("resource")[0]
        if not resource:
            print("No resource specified")
            self.send_response(400)
            return

        api_version = query.get("api-version")[0]
        if api_version != "2019-08-01":
            print("api-version missing or invalid")
            self.send_response(400)
            return

        cli_token = get_access_token(self.cmd, resource=resource)
        jwt = cli_token["accessToken"]
        payload = json.loads(b64decode(jwt.split(".")[1] + "==="))

        token = {
            "access_token": cli_token["accessToken"],
            "client_id": "",
            "expires_on": str(payload["exp"]),
            "not_before": str(payload["nbf"]),
            "resource": resource,
            "token_type": "Bearer",
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(token).encode("utf-8"))
