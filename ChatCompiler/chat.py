import os
import re
from jinja2 import Environment, FileSystemLoader

def parse_chat_file(file_path):
    """解析 .chat 文件，返回标题、参与者和对话内容"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    title = None
    left_participants = {}  # 左边参与者
    right_participants = {}  # 右边参与者
    messages = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 解析标题
        if line.startswith('#'):
            title = line[1:].strip()
            continue

        # 解析参与者列表和头像
        if line.startswith('>') or line.startswith('<'):
            participant_str = line[1:].strip()
            # 修正正则表达式，使其能够处理没有空格的情况
            participant_data = re.findall(r'\["([^"]+)",\s*"([^"]+)"\]', participant_str)
            for name, avatar in participant_data:
                if line.startswith('>'):
                    left_participants[name] = avatar
                else:
                    right_participants[name] = avatar
            continue

        # 解析对话内容
        match = re.match(r'\[([^\]]+)\]\s+(.*)', line)
        if match:
            speaker, content = match.groups()
            # 确定消息位置
            position = 'left'
            avatar = None
            if speaker in left_participants:
                position = 'left'
                avatar = left_participants[speaker]
            elif speaker in right_participants:
                position = 'right'
                avatar = right_participants[speaker]
            messages.append({
                'speaker': speaker,
                'avatar': avatar,
                'content': content,
                'position': position
            })

    return {
        'title': title,
        'messages': messages
    }

def generate_chat_html(data, output_path):
    """使用模板生成 HTML 文件"""
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('chat_template.html')

    html = template.render(
        title=data['title'],
        messages=data['messages']
    )

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    input_chat_file = 'example.chat'
    output_html_file = 'output.html'

    chat_data = parse_chat_file(input_chat_file)
    generate_chat_html(chat_data, output_html_file)

    print(f"聊天记录已生成: {output_html_file}")
    os.system("pause")