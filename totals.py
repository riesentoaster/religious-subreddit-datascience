import os
import json

for sub in os.listdir("freqs"):
    if not os.path.isdir(f"freqs/{sub}"):
        continue
    for file in os.listdir(f"freqs/{sub}"):
        if not file.endswith("freq.json"):
            continue
        with open(f"freqs/{sub}/{file}", "r") as f:
            file_string = file.split("_")[0]
            print(f"total weight in {sub} – {file_string}:", sum(json.loads(f.read()).values()))