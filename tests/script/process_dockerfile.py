import sys
import os
import cmind as cm
import check as checks
import json
import yaml

files=sys.argv[1:]

for file in files:
  if not file.endswith("_cm.json") or not file.endswith("_cm.yaml"):
    continue
  if not file.startswith(os.path.join("cm-mlops", "script")):
    continue
  script_path = os.path.dirname(file)
  f = open(file)
  if f.endswith(".json")
    data = json.load(f)
  elif f.endswith(".yaml")
    data = yaml.safe_load(f)
  uid = data['uid']

  r = cm.access({'action':'dockerfile', 'automation':'script', 'artifact': uid, 'quiet': 'yes'})
  checks.check_return(r)
