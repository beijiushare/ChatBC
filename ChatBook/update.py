import sys
import json
import os

def update_json(library, chapter, section, file_path):
    # 检查参数数量
    if len(sys.argv) != 5:
        print("用法: python update.py <库名> <章名> <节名> <文件路径>")
        sys.exit(1)

    # 初始化数据结构
    data = {}

    # 如果 content.json 文件存在，则读取它
    if os.path.exists('content.json'):
        try:
            with open('content.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            print("警告: content.json 文件内容无效，将创建一个新的文件。")

    # 确保库存在
    if library not in data:
        data[library] = {}

    # 确保章存在
    if chapter not in data[library]:
        data[library][chapter] = {}

    # 添加节和文件路径
    data[library][chapter][section] = file_path

    # 写回 JSON 文件
    with open('content.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"已成功将 {file_path} 添加到 {library}/{chapter}/{section}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("用法: python update.py <库名> <章名> <节名> <文件路径>")
        sys.exit(1)

    library = sys.argv[1]
    chapter = sys.argv[2]
    section = sys.argv[3]
    file_path = sys.argv[4]

    update_json(library, chapter, section, file_path)