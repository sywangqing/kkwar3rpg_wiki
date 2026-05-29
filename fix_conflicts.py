import os
import re

def resolve_conflicts_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<<<<<<< HEAD' not in content:
        return False

    # For changelog.md, we want to keep both contents
    if 'changelog.md' in filepath:
        # remove the markers but keep both A and B
        content = re.sub(r'<<<<<<< HEAD\n(.*?)\n=======\n(.*?)\n>>>>>>> [a-f0-9]+.*?\n', r'\1\n\2\n', content, flags=re.DOTALL)
    else:
        # for other files, keep HEAD (Content A)
        content = re.sub(r'<<<<<<< HEAD\n(.*?)\n=======\n.*?\n>>>>>>> [a-f0-9]+.*?\n', r'\1\n', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

changed = 0
for root, dirs, files in os.walk('docs'):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            if resolve_conflicts_in_file(filepath):
                print(f"Fixed {filepath}")
                changed += 1

print(f"Total fixed: {changed}")
