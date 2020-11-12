from azure.cli.core import AzCommandsLoader

from azext_imds._help import helps  # pylint: disable=unused-import


class ImdsCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType

        imds_custom = CliCommandType(operations_tmpl="azext_imds.custom#{}")
        super(ImdsCommandsLoader, self).__init__(
            cli_ctx=cli_ctx, custom_command_type=imds_custom
        )

    def load_command_table(self, args):
        from azext_imds.commands import load_command_table

        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_imds._params import load_arguments

        load_arguments(self, command)


COMMAND_LOADER_CLS = ImdsCommandsLoader
