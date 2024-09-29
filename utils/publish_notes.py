import os
import yaml

# recursively loop through the private directory
# copies .md files with "#publish" tag into public

private_vault = os.getenv('private_vault')
public_vault = os.getenv('public_vault')

private_vault_path = str(private_vault)

def search_files(public_path, private_path):
    for root, dirs, files in os.walk(public_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if has_publish_hashtag(file_path):
                    print(file_path)

def has_publish_hashtag(path):
    with open(path, 'r', encoding='iso-8859-1') as file:
            content = file.read()
            parts = content.split('---', 2)
            if len(parts) >= 3:
                    frontmatter = parts[1].strip()
                    metadata = yaml.safe_load(frontmatter)
                    if 'tags' in metadata and isinstance(metadata['tags'], list):
                        return any(str(tag).startswith('publish') for tag in metadata['tags'])

search_files(private_vault, public_vault)