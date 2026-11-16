#!/usr/bin/env python3
import sys
import json
import re
import urllib.request
import urllib.parse

# Trello Credentials
KEY = '9cee8d11e30b9274ace1e9493bd94cc0'
TOKEN = 'ATTA8bb84adec857689e16ca5329d75519b374a7d85a1e14399c14079332796523d3A7A72267'
BOARD_ID = '678c1f7368436c700cf48e5f'

# Mapping project tags to Jira board URLs
PROJECT_MAPPING = {
    'HALO': {
        'name': 'Halo',
        'board_url': 'https://amap.atlassian.net/jira/software/c/projects/CHQ/boards/82',
        'board_id': '82'
    },
    'EVAL': {
        'name': 'Eval',
        'board_url': 'https://amap.atlassian.net/jira/software/c/projects/CHQ/boards/115/',
        'board_id': '115'
    }
}

def fetch_board_metadata():
    url_lists = f'https://api.trello.com/1/boards/{BOARD_ID}/lists?key={KEY}&token={TOKEN}'
    lists = json.loads(urllib.request.urlopen(url_lists).read().decode('utf-8'))
    list_map = {l['name']: l['id'] for l in lists}

    url_labels = f'https://api.trello.com/1/boards/{BOARD_ID}/labels?key={KEY}&token={TOKEN}'
    labels = json.loads(urllib.request.urlopen(url_labels).read().decode('utf-8'))
    label_map = {l['color']: l['id'] for l in labels}

    return list_map, label_map

def parse_line(line):
    line = line.strip()
    if not line:
        return None

    # Pattern: [Action] TICKET(ProjectTag)
    match = re.search(r'^(.*?)\s*([A-Z0-9]+-\d+)\s*[\(\[]([^\)\]]+)[\)\]]$', line, re.IGNORECASE)
    if match:
        action = match.group(1).strip()
        ticket = match.group(2).strip().upper()
        project_tag = match.group(3).strip()
    else:
        match_ticket = re.search(r'([A-Z0-9]+-\d+)', line)
        if not match_ticket:
            return None
        ticket = match_ticket.group(1).upper()
        action = line.replace(ticket, '').strip()
        project_tag = 'Halo'

    if not action:
        action = 'Implement'

    return {
        'raw': line,
        'action': action,
        'ticket': ticket,
        'project_tag': project_tag
    }

def create_trello_card(item, list_id, label_id):
    tag_upper = item['project_tag'].upper()
    proj_info = PROJECT_MAPPING.get(tag_upper, {
        'name': item['project_tag'],
        'board_url': f'https://amap.atlassian.net/browse/{item["ticket"]}'
    })

    if 'board_id' in proj_info:
        jira_url = f"{proj_info['board_url']}?selectedIssue={item['ticket']}"
    else:
        jira_url = proj_info['board_url']

    card_name = f"[{item['ticket']}] {item['action']} ({proj_info['name']})"
    if item['action'].lower() == 'implement':
        card_name = f"[{item['ticket']}] Implement feature ({proj_info['name']})"

    desc = f"""📌 **Mã Ticket**: [{item['ticket']}]({jira_url})
📂 **Dự án**: {proj_info['name']}
🔗 **Link Jira**: {jira_url}

📋 **Quy trình thực hiện**:
- [ ] Kiểm tra nội dung ticket & thiết kế giải pháp
- [ ] Thực hiện code & viết unit test
- [ ] Push code & tạo/cập nhật PR
- [ ] Thả icon 🚀 khi phản hồi review comment
"""

    data = urllib.parse.urlencode({
        'name': card_name,
        'desc': desc,
        'idList': list_id,
        'idLabels': label_id,
        'key': KEY,
        'token': TOKEN
    }).encode('utf-8')

    req = urllib.request.Request('https://api.trello.com/1/cards', data=data, method='POST')
    res = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    return res

def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        lines = text.split('\n')
    else:
        lines = sys.stdin.read().split('\n')

    list_map, label_map = fetch_board_metadata()
    target_list_id = list_map.get('Weekly Backlog') or list(list_map.values())[0]

    created_cards = []

    for line in lines:
        parsed = parse_line(line)
        if not parsed:
            continue

        act_lower = parsed['action'].lower()
        if 'review' in act_lower:
            label_id = label_map.get('yellow') # Collaboration/Review
        else:
            label_id = label_map.get('red') # Jira Project

        card = create_trello_card(parsed, target_list_id, label_id)
        created_cards.append({
            'name': card['name'],
            'url': card['shortUrl'],
            'ticket': parsed['ticket'],
            'action': parsed['action'],
            'project': parsed['project_tag']
        })

    print(json.dumps(created_cards, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
