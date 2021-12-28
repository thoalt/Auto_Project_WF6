from utilites import global_dir
import configparser
import os

""" Parses ini files """
config = configparser.RawConfigParser()
config.read(global_dir.INI_CONFIGS_PATH)

# returns ini file sections as dictionary
def config_section_dict(section):
    section_dict = {}
    section_keys = config.options(section)
    for key in section_keys:
        try:
            section_dict[key] = config.get(section, key)
        except:
            section_dict[key] = None
    #print(section_dict)
    return section_dict


class ConfigParserIni:
    @staticmethod
    def config_timeout():
        timeout_dict = config_section_dict('timeout info')
        return timeout_dict


    @staticmethod
    def config_url_info():
        return config_section_dict('url info')

    @staticmethod
    def config_data_info():
        return config_section_dict('data info')

