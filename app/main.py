from RiskInDroid import RiskInDroid
import os
import pprint
import argparse
import os
import sys
import datetime
import json
import argparse

ALLOWED_EXTENSIONS = {"apk", "zip"}

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--file", help="apk file name")
group.add_argument("-d", "--dir", help="apk directory path")
parser.add_argument("-c", "--cli", help="Show Result in Terminal", action='store_true')
parser.add_argument("-o", "--out", help="Path to result storeage path")
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=2)
rid = RiskInDroid()

if args.out:
    out_path = args.out
    if not os.path.exists(out_path):
        print("Not a valid path: " + out_path)
        exit()
    if(not os.path.exists("results")):
        os.mkdir("results")

    result_path = os.path.join("results", datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))
    os.mkdir(result_path)


def print_result(permissions_dict):
    print("\n\nAPK Name: " + permissions_dict['apk'])
    print("\nPermission Declared: ")
    for i in permissions_dict['declared']:
        print('\t' + i)

    print("\nPermission Not Required But Used: ")
    for i in permissions_dict['notRequiredButUsed']:
        print('\t' + i)

    print("\nPermission Required And Used: ")
    for i in permissions_dict['requiredAndUsed']:
        print('\t' + i)

    print("\nPermission Required But Not Used: ")
    for i in permissions_dict['requiredButNotUsed']:
        print('\t' + i)

    print("\nTotal Risk Score: " + str(permissions_dict['risk_factor']))


def result_store(permission_dict, file_name):
    out_path = args.out
    permission_json = json.dumps(permission_dict, indent=4)
    result_file = file_name.replace(" ", "_").removesuffix(".apk").removesuffix(".zip")+".json"
    with open(os.path.join(out_path, result_path, result_file), "w") as f:
        f.write(permission_json)
    print("Result Written for: " + file_name)


def check_if_valid_file_name(file_name):
    return (
        "." in file_name and file_name.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


def get_risk(file_path):
    permissions = rid.get_permission_json(file_path)
    risk = rid.calculate_risk(rid.get_feature_vector_from_json(permissions))
    permissions["risk_factor"] = risk
    return permissions


def run():
    if args.file:
        apk_file_path = args.file
        if not os.path.isfile(apk_file_path):
            print("File not found", apk_file_path)
            return
        
        if not check_if_valid_file_name(apk_file_path):
            print(apk_file_path, ": Not and apk")
            return

        print(apk_file_path)
        file_name = os.path.basename(apk_file_path)

        print("\nAnazying " + file_name)
        permission_dict = get_risk(apk_file_path)
        permission_dict = {**{"apk": file_name}, **permission_dict}
        if args.cli:
            print_result(permission_dict)
        if args.out:
            result_store(permission_dict, file_name)

    elif args.dir:
        apk_dir_path = args.dir
        if(not os.path.exists(apk_dir_path)):
            print("The Directory path does not exists..", file=sys.stderr)
            return
        file_list = [f for f in os.listdir(apk_dir_path)
                     if os.path.isfile(os.path.join(apk_dir_path, f))]

        for file_name in file_list:
            file_path = os.path.join(apk_dir_path ,file_name)
            if not check_if_valid_file_name(file_path):
                print(file_name, ": Not and apk, skipping...")
                continue

            print("\nAnazying " + file_name)
            permission_dict = get_risk(file_path)
            permission_dict = {**{"apk": file_name}, **permission_dict}
            if args.cli:
                print_result(permission_dict)
            if args.out:
                result_store(permission_dict, file_name)

run()
