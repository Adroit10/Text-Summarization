import os
from box.exceptions import BoxValueError
import yaml
from TextSummarization.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object.
    param path_to_yaml: Path to the yaml file.
    Raises: Value error if yaml is empty"""

    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """
    Create directories if they do not exist.
    param path_to_directories: list of directories to create.
    param verbose: if True, print a message.
    """
    for path in path_to_directories:

        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"directory: {path} created successfully")

@ensure_annotations
def get_size(path:Path)-> str:
    """
    Return the size of a file in kilobytes.
    param path: Path to the file.
    """
    size_in_kb= round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
            
