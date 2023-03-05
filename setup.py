from setuptools import find_packages,setup
from typing import List



HED='-e .'
def get_requirements(file_path:str)->List[str]:
    
    ''' 
    returns the list of requirenmts
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    
        if HED in requirements:
            requirements.remove(HED)

    return requirements

setup(
name='ML-PROJECT',
version='0.0.1',
author='Benedict',
author_email='benedicttirkey05@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),



)

