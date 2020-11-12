def load_command_table(self, _):

    with self.command_group("imds") as g:
        g.custom_command("start", "start_imds")

    with self.command_group("imds", is_experimental=True):
        pass
