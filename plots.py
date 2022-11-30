import os
import matplotlib.pyplot as plt
import json

files = os.listdir("./comments")

fig, ax = plt.subplots(nrows=2, ncols=len(files))
plt.tight_layout()
print(ax.shape)

for i,file in enumerate(files):
    c = []
    with open(f"./comments/{file}", "r") as f:
        c = json.loads(f.read())
    current_sub = file.split(" ")[-1][:-5]

    ax[0,i].plot(
        # [e['post_id'] for e in c],
        [len(e['comments']) for e in c]
    )

    ax[0,i].set_title(f"Number of comments for r/{ current_sub }")

    ax[1,i].plot(
        # [e['post_id'] for e in c],
        [e['post_score'] for e in c]
    )

    ax[1,i].set_title(f"Scores for r/{ current_sub }")

plt.show()
