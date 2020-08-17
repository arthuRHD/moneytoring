import sys
import os
import shutil


def setup_csv():
    path = sys.argv[1]
    try:
        with open(path, "r") as src:
            with open(os.path.join(os.path.dirname(__file__), "transactions.csv"), "w+") as dst:
                data = src.read()
                dst.write(data)
    except Exception:
        pass
