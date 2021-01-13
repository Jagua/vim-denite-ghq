from .base import Base
import subprocess


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'ghq'
        self.kind = 'directory'
        self.vars = {
            'command': []
        }

    def on_init(self, context):
        if not self.vars['command']:
            self.vars['command'] = ['ghq', 'list', '--full-path']

    def gather_candidates(self, context):
        return [{'word': path, 'action__path': path}
                for path
                in subprocess.run(self.vars['command'],
                                  check=True,
                                  universal_newlines=True,
                                  stdout=subprocess.PIPE
                                  ).stdout.split()]
