import pytest
import os
import json

from lib.framework.file_handler import FileHandler


@pytest.mark.unit
def test_raise_FileNotFoundError_import_json():
    with pytest.raises(FileNotFoundError):
        FileHandler().import_json("fake_path")


@pytest.mark.unit
def test_raise_JSONDecodeError_import_json():
    with pytest.raises(json.JSONDecodeError):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_dir, "crash.json")
        FileHandler().import_json(json_path)
