from pykwalify.core import Core
from pykwalify.errors import SchemaError
from pkg_resources import resource_filename
import logging

logging.basicConfig()
logging.getLogger("pykwalify").setLevel(logging.CRITICAL)

class Config(object):
    def __init__(self, config):
        self.config = config

    def validate(self):
        c = Core(source_data=self.config, schema_files=[resource_filename('pyregistrator', 'schemas/config.yaml')])
        try:
            c.validate(raise_exception=True)
        except SchemaError, e:
            raise RuntimeError("Configuration validation failed")

    def get_paths(self):
        return self.config.get("paths")
    
    def get_commands(self):
        return self.config.get("commands")
