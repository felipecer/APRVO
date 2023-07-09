import json
import os
import serialization.objects as objects

def list_prebuilt_env():
    return ["deadlock","square","3-room"]

def make_env_from_json(path):
    with open(path) as file:
        data = json.load(file)
    environment = objects.Environment.from_json(data) 
    return environment

def make_prebuilt_env(name):
    prebuilt_envs = list_prebuilt_env()
    if name not in prebuilt_envs:
        return None
    name = name + ".json"
    root = os.path.abspath(".")
    file_dir = os.path.join(root,"serialization", "prebuilt_environments", name)
    print(file_dir)
    return make_env_from_json(file_dir)
    

