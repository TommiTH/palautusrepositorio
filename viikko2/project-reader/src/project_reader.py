from urllib import request
from project import Project
import toml

def get_string_from_dictionary(dictionary : dict):
    return get_string_from_list(dictionary.keys())
    
def get_string_from_list(list : list):
    returnList = ""
    for item in list:
        returnList += "\n- " + item
    return returnList

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)
        name = parsed_toml["tool"]["poetry"]["name"]
        description = parsed_toml["tool"]["poetry"]["description"]
        license = parsed_toml["tool"]["poetry"]["license"] + "\n"
        authors = get_string_from_list(parsed_toml["tool"]["poetry"]["authors"])
        dependencies = get_string_from_dictionary(parsed_toml["tool"]["poetry"]["dependencies"])
        dev_dependencies = get_string_from_dictionary(parsed_toml["tool"]["poetry"]["group"]["dev"]["dependencies"])
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
