import json
import sys

try:
    with open('pipeline/cache/topics.json', 'r', encoding='utf-8') as f:
        topics = json.load(f)
    
    pending = [t for t in topics if t.get('status') == 'pending']
    print(f"Total pending: {len(pending)}")
    
    # Check for KK topics
    kk_topics = [t for t in pending if t.get('topic_id', '').startswith('kk-platform')]
    other_topics = [t for t in pending if not t.get('topic_id', '').startswith('kk-platform')]
    
    print(f"\nKK Platform Topics ({len(kk_topics)}):")
    for t in kk_topics:
        print(f"- {t.get('title')}")
        
    print(f"\nOther Topics ({len(other_topics)}):")
    for t in other_topics:
        print(f"- {t.get('title')}")
        
except Exception as e:
    print(f"Error parsing JSON: {e}")
