import subprocess

class Sphinx:
    config_args = ("host", "port")

    def __init__(self, agent_config, checks_logger, raw_config):
        self.agent_config = agent_config
        self.checks_logger = checks_logger
        self.raw_config = raw_config

        self.command = ["mysql"]
        if "Sphinx" in self.raw_config:
            config = self.raw_config["Sphinx"]
            for arg in self.config_args:
                if arg in config:
                    self.command.extend(("--" + arg, config[arg]))
        self.command.extend(("--batch", "--skip-column-names", "--execute", "SHOW STATUS"))

    def run(self):
        try:
            output = subprocess.check_output(self.command)
            stats = output.splitlines()
            stats = (line.split("\t", 1) for line in stats)
            stats = dict((key.strip(), value.strip()) for (key, value) in stats)
            stats["running"] = True
            return stats
        except subprocess.CalledProcessError:
            self.checks_logger.exception("Sphinx doesn't seem to be running, perhaps check your configuration?")
            return {"running": False}

if __name__ == "__main__":
    import logging
    print Sphinx({}, logging, {"Sphinx": {"host": "127.0.0.1", "port": "10100"}}).run()
