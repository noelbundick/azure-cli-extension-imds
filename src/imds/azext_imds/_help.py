from knack.help_files import helps  # pylint: disable=unused-import


helps[
    "imds"
] = """
    type: group
    short-summary: Commands to manage the local token endpoint emulator.
"""

helps[
    "imds start"
] = """
    type: command
    short-summary: Start the local token endpoint.
    parameters:
      - name: --host
        type: string
        short-summary: The host IP to start the endpoint on. Defaults to 0.0.0.0
      - name: --port
        type: string
        short-summary: The port to start the endpoint on. Defaults to a random available port
      - name: --secret
        type: string
        short-summary: The secret to be used to authenticate with the endpoint. Defaults to a random GUID
        default: foo
      - name: --host
        type: string
        short-summary: The type of endpoint to start. Defaults to Azure App Service api-version 2017-09-01
"""
