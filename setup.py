import os
from setuptools import setup


BIN_DIR = 'bin'


def is_shell_script(path):
    result = False
   
    try:
        with open(path) as file:
            lines = file.read().splitlines()
    
    except: # Sorry. Needed due to bad win10 os.listdir out:
        lines = []

    if len(lines) > 0:
        result = lines[0].startswith("#!/")
    
    return result


all_scripts = [
        BIN_DIR + "/" + script for 
        script in os.listdir(BIN_DIR) 
        if is_shell_script(os.path.join(BIN_DIR, script))
        ]

setup(
    name='autoscripts',
    version='0.1',
    description='auto install scripts in PATH',
    url='http://github.com/marcelotournier/autoscripts',
    author='Marcelo Tournier',
    author_email='marcelo@inova.life',
    license='MIT',
    packages=['autoscripts'],
    scripts=all_scripts,
    zip_safe=False)

