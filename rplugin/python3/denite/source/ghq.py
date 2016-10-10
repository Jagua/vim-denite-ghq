from .base import Base
import subprocess


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'ghq'
        self.kind = 'directory'

    def gather_candidates(self, context):
        cmd = ['ghq', 'list', '--full-path']
        return [{'word': path, 'action__path': path}
                for path
                in subprocess.run(cmd,
                                  check=True,
                                  universal_newlines=True,
                                  stdout=subprocess.PIPE
                                  ).stdout.split()]
