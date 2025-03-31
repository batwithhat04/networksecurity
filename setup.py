



from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """This function will return a list of requirements"""
    requirement_list:List[str]=[]
    try:
        with open("requirements.txt", "r") as file:
            #read lines from the file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e.
                if requirement and requirement !='-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("No requirements.txt file found")

    return requirement_list

setup(
    name= 'Network Security',
    version= '0.0.0.1',
    author='Avinash Singh',
    author_email= 'singhavinash04@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)