import json
import os

filterlist = []
with open("filterlist.txt", "r") as f:
    filterlist = f.readlines()
    filterlist = [e[:-1] for e in filterlist if len(e) > 1]
    filterlist = [e.lower() for e in filterlist]


for folder in os.listdir("freqs"):
    if os.path.isdir(f"freqs/{folder}"):
        for file in os.listdir(f"freqs/{folder}"):
            if file[-5:] == ".json" and "filtered" not in file:
                c = {}
                with open(f"freqs/{folder}/{file}", "r") as f:
                    c = json.loads(f.read())

                c = {k:v for k,v in c.items() if k in filterlist}
                
                with open(f"freqs/{folder}/{file[:-5]}_filtered.json", "w") as f:
                    f.write(json.dumps(c))