import os
import sys
import docker
import shutil
import unittest
import argparse
from pathlib import Path


DEFAULT_TAG = 'testme/submission:0.01'


class TestMe(unittest.TestCase):

    ARGS: argparse.Namespace = None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def run_submission(cls, submission: Path = None, data: Path = None, output: Path = None, tag: str = DEFAULT_TAG, command: str = 'bash run.sh /input /output'):
        # run submission program
        submission = submission or cls.ARGS.submission
        data = data or cls.ARGS.data
        output = output or cls.ARGS.output
        tag = tag or cls.ARGS.tag
        assert submission.exists()
        assert data.exists()

        if not os.path.isdir(output):
            os.makedirs(output)

        mounts = [
            docker.types.Mount(target='/src', source=submission.absolute().as_posix(), type='bind', read_only=False),
            docker.types.Mount(target='/input', source=data.absolute().as_posix(), type='bind', read_only=True),
            docker.types.Mount(target='/output', source=output.absolute().as_posix(), type='bind', read_only=False),
        ]

        client = docker.from_env()
        assert tag is not None
        container_name = 'testme-job'
        try:
            container = client.containers.get(container_name)
        except docker.errors.NotFound:
            pass
        else:
            container.remove(force=True)

        client.images.build(path=submission.absolute().as_posix(), tag=tag, forcerm=True)
        out = client.containers.run(tag, mounts=mounts, command=command, remove=True, name=container_name)
        client.close()
        return out

    @classmethod
    def get_parser(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument('--submission', default='submission', help='submission directory', type=Path)
        parser.add_argument('--tag', default=DEFAULT_TAG, help='docker image tag')
        parser.add_argument('--data', default='sample/data', help='data directory', type=Path)
        parser.add_argument('--gold', default='sample/gold', help='data directory', type=Path)
        parser.add_argument('--private', default='', help='private directory', type=Path)
        parser.add_argument('--output', default='output', help='output directory', type=Path)
        return parser

    @classmethod
    def autorun(cls):
        cls.ARGS, leftover = cls.get_parser().parse_known_args()
        sys.argv = sys.argv[:1] + leftover
        unittest.main()
