from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT="-e"


def get_requirements(file_path: str) -> List[str]:
    '''
    returns list of requirements

    '''

    requirements=[]

    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.1',
    packages=find_packages(),
    author='Sushant',
    intall_requires=get_requirements('requirements.txt')
)