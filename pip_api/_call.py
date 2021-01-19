import os
import subprocess
import sys


def call(*args, cwd=None):
    python_location = os.environ.get("PIPAPI_PYTHON_LOCATION", sys.executable)
    result = subprocess.check_output(
        [python_location, "-m", "pip"] + list(args), cwd=cwd, env={"PIP_YES": "true"}
    )
    return result.decode()
