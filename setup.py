from setuptools import setup,find_packages
from typing import List, Optional

HYPHEN_E_DOT = '-e.'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        #remove extra line
        requirements = [req.replace('\n',"") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements



setup(
    name = 'DiamondPricePrediction' ,
    author= 'Sagar Aggarwal' ,
    author_email= 'aggarwal311@hotmail.com' ,
    install_requires = get_requirements('requirements.txt') , 
    packages= find_packages()

)