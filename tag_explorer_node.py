import os
import random
import json
import folder_paths

class TagExplorerNode:
    def __init__(self):
        self.last_tags = ""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "tags": ("STRING", {"default": "", "multiline": True}),
                "random_mode": ("BOOLEAN", {"default": False}),
                "random_target": (["none", "group", "category"], {"default": "none"}),
                "random_group": ("STRING", {"default": ""}),
                "random_category": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("tags",)
    FUNCTION = "process_tags"
    CATEGORY = "utils"
    OUTPUT_NODE = True

    def process_tags(self, tags, random_mode, random_target, random_group, random_category):
        output_tags = tags

        if random_mode and random_target != "none":
            wildcards_path = os.path.join(folder_paths.base_path, "wildcards")

            if random_target == "group" and random_group:
                group_path = os.path.join(wildcards_path, random_group)
                if os.path.exists(group_path):
                    all_tags = []
                    for txt_file in os.listdir(group_path):
                        if txt_file.endswith('.txt'):
                            file_path = os.path.join(group_path, txt_file)
                            with open(file_path, 'r', encoding='utf-8') as f:
                                file_tags = [line.strip() for line in f if line.strip()]
                                all_tags.extend(file_tags)
                    if all_tags:
                        random_tag = random.choice(all_tags)
                        output_tags = random_tag if not tags else f"{tags}, {random_tag}"

            elif random_target == "category" and random_category:
                parts = random_category.split('/')
                if len(parts) == 2:
                    group_name, category_name = parts
                    file_path = os.path.join(wildcards_path, group_name, category_name)
                    if os.path.exists(file_path):
                        with open(file_path, 'r', encoding='utf-8') as f:
                            category_tags = [line.strip() for line in f if line.strip()]
                            if category_tags:
                                random_tag = random.choice(category_tags)
                                output_tags = random_tag if not tags else f"{tags}, {random_tag}"

        self.last_tags = output_tags
        return (output_tags,)

NODE_CLASS_MAPPINGS = {
    "TagExplorerNode": TagExplorerNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TagExplorerNode": "Tag Explorer"
}
