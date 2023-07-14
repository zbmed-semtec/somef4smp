import unittest
import os
from pathlib import Path

from ..extract_software_type import check_ontologies,check_notebooks,check_command_line,check_extras,check_static_websites,check_workflow

test_data_repositories = str(Path(__file__).parent / "test_data"/ "repositories") + os.path.sep

class TestEXTRAS(unittest.TestCase):

    def test_true_ontology(self):
        path = test_data_repositories + "auroral-core-ontology-master"
        result = check_ontologies(path,"auroral-core-ontology-master")
        assert result
     
    def test_false_ontology(self):
        path = test_data_repositories + "sprint-main"
        result = check_ontologies(path,"sprint-main")
        assert (result is False)
    
    def test_true_notebooks(self):
        path=test_data_repositories + "basis_functions_approach_to_GP-master"
        result=check_notebooks(path)
        assert result
    
    def test_false_notebooks(self):
        path=test_data_repositories + "ipynb-master"
        result=check_notebooks(path)
        assert (result is False)
    
    def test_true_commandline(self):
        path=test_data_repositories + "Fermi"
        result=check_command_line(path)
        assert result
    
    def test_false_commandline(self):
        path=test_data_repositories + "Clamp"
        result=check_command_line(path)
        assert (result is False)

    def test_true_extra(self):
        path = test_data_repositories + "OWL-To-OAS-Specification-master"
        result = check_extras(path)
        assert result

    def test_false_extra(self):
        path = test_data_repositories + "auroral-core-ontology-master"
        result = check_extras(path)
        assert result is False

    def test_true_website(self):
        path = test_data_repositories + "website-static-master"
        result = check_static_websites(path)
        assert result

    def test_false_website(self):
        path = test_data_repositories + "A-Dynamic-E-Commerce-Website-master"
        result = check_static_websites(path)
        assert result is False

    def test_true_workflows(self):
        path = test_data_repositories + "JAFFA-master"
        result = check_workflow(path,'JAFFA-master')
        assert result

    def test_false_workflows(self):
        path = test_data_repositories + "A-Dynamic-E-Commerce-Website-master"
        result = check_workflow(path,'DynamicPersonalWebsite-master')
        assert result is False
