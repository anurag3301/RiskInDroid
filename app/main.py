import hashlib
import os
import subprocess
import time
import pprint
import argparse

from RiskInDroid import RiskInDroid
from model import db, Apk
import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--file", help="apk file name")
group.add_argument("-d", "--dir", help="apk directory path")
args = parser.parse_args()
ALLOWED_EXTENSIONS = {"apk", "zip"}

pp = pprint.PrettyPrinter(indent=2)

def check_if_valid_file_name(file_name):
    return (
        "." in file_name and file_name.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

def get_risk(file_path):
    file_path = "/home/anurag/dl/apktool/compass.apk"
    rid = RiskInDroid()
    permissions = rid.get_permission_json(file_path)
    risk = rid.calculate_risk(rid.get_feature_vector_from_json(permissions))
    permissions["risk_factor"] = risk
    pp.pprint(permissions)
