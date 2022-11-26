from jproperties import Properties

from helper.utils import path_from_project_root


class ConfigurationManager:
    __configs = Properties()
    with open(path_from_project_root('resources/config.properties'), 'rb') as __config_file:
        __configs.load(__config_file)

    @staticmethod
    def __fetch(property_key: str) -> str:
        return ConfigurationManager.__configs.get(property_key)[0]

    @staticmethod
    def browser() -> str:
        return ConfigurationManager.__fetch('browser')

    @staticmethod
    def headless() -> bool:
        return ConfigurationManager.__fetch('headless') == 'True'

    @staticmethod
    def slow_motion() -> int:
        return int(ConfigurationManager.__fetch('slow.motion'))

    @staticmethod
    def base_url() -> str:
        return ConfigurationManager.__fetch('base.url')
