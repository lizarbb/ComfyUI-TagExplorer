# ComfyUI-TagExplorer  
**how come did no one else thought of this??** xddd

Brain dead simple custom node for ComfyUI that lets you explore and use organized tag lists as wildcards

## Features
- Super easy wildcard-style tag groups
- Drop your custom tag lists into folders
- Restart ComfyUI → new node appears → profit

## Installation
1. Clone this repo into your ComfyUI `custom_nodes` folder:
   ```bash
   cd path/to/ComfyUI/custom_nodes
   git clone https://github.com/lizarbb/ComfyUI-TagExplorer.git
2. Restart ComfyUI
3. Add the tagexplorer node

## Usage / How to Add Your Own Tags
1. Follow this exact structure inside your ComfyUI root directory (the same level as main.py, models/, etc.):
```text
ComfyUI/
├── custom_nodes/
│   └── ComfyUI-TagExplorer/
├── models/
├── wildcards/                ← create this folder
│   ├── group_1/
│   │   └── your_tags_list.txt          ← one tag per line
│   ├── group_2/
│   │   └── your_tags_list2.txt
│   ├── characters/
│   │   └── anime_girls.txt
│   ├── moods/
│   │   └── happy_emotions.txt
│   └── ...etc. (add as many groups/folders as you want)
└── ...other comfy stuff
```
2. Example content of wildcards/group_1/your_tags_list.txt:
```text
1girl
solo
long hair
blue eyes
smile
cat ears
maid outfit
```
Have fun
