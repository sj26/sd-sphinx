import subprocess

class Sphinx:
    def __init__(self, agent_config, checks_logger, raw_config):
        self.agent_config = agent_config
        self.checks_logger = checks_logger
        self.raw_config = raw_config

        self.command = ['searchd']
        if 'Sphinx' in self.raw_config:
            config = self.raw_config['Sphinx']
            if 'config' in config:
                self.command.extend(('--config', config['config']))
        self.command.append('--status')

    def run(self):
        try:
            output = subprocess.check_output(self.command)
            lines = output.splitlines()
            stats = dict((key.strip(), value.strip()) for (key, value) in (line.split(':', 1) for line in lines[lines.index('--------------') + 1:]))
            stats['running'] = True
            return stats
        except subprocess.CalledProcessError:
            self.checks_logger.exception("Sphinx doesn't seem to be running, perhaps check your configuration?")
            return {'running': False}

if __name__ == '__main__':
    import logging
    print Sphinx({}, logging, {}).run()
