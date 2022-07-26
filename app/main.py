import hashlib
import os
import subprocess
import time
import pprint

from RiskInDroid import RiskInDroid
from model import db, Apk

ALLOWED_EXTENSIONS = {"apk", "zip"}
pp = pprint.PrettyPrinter(indent=4)
def check_if_valid_file_name(file_name):
    return (
        "." in file_name and file_name.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

file_path = "/home/anurag/dl/apktool/compass.apk"
filename = "compass.apk"
rid = RiskInDroid()
permissions = rid.get_permission_json(file_path)
risk = rid.calculate_risk(rid.get_feature_vector_from_json(permissions))
pp.pprint(permissions)
print("Risk Factor: ", risk)
