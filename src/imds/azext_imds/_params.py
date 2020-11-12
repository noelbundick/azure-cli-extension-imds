from knack.arguments import CLIArgumentType

from azure.cli.core.commands.parameters import get_enum_type


def load_arguments(self, _):
    with self.argument_context("imds start") as c:
        c.argument("port", type=int)
        c.argument(
            "imds_type",
            options_list=["--type"],
            arg_type=get_enum_type(["AppService2017", "AppService2019"]),
        )
