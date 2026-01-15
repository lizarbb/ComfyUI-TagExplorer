import os
import json
from aiohttp import web
import folder_paths
import server

@server.PromptServer.instance.routes.get("/tag_explorer/structure")
async def get_tag_structure(request):
    wildcards_path = os.path.join(folder_paths.base_path, "wildcards")
    
    if not os.path.exists(wildcards_path):
        os.makedirs(wildcards_path)
        return web.json_response({"groups": []})
    
    structure = {"groups": []}
    
    for group_name in os.listdir(wildcards_path):
        group_path = os.path.join(wildcards_path, group_name)
        if os.path.isdir(group_path):
            group_data = {
                "name": group_name,
                "categories": []
            }
            
            for txt_file in os.listdir(group_path):
                if txt_file.endswith('.txt'):
                    category_data = {
                        "name": txt_file,
                        "display_name": txt_file[:-4],
                        "tags": []
                    }
                    
                    file_path = os.path.join(group_path, txt_file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            tags = [line.strip() for line in f if line.strip()]
                            category_data["tags"] = tags
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
                    
                    group_data["categories"].append(category_data)
            
            structure["groups"].append(group_data)
    
    return web.json_response(structure)

web_directory = os.path.join(os.path.dirname(__file__), "web")
server.PromptServer.instance.app.router.add_static('/tag_explorer_web/', web_directory)
