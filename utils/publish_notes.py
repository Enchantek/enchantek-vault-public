import os
import yaml
import shutil

# recursively loop through the private directory
# copies .md files with "#publish" tag into public

private_vault = os.getenv('private_vault')
public_vault = os.getenv('public_vault')

private_vault_path = str(private_vault)

def search_files(private_path, public_path):
    for root, dirs, files in os.walk(private_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if has_publish_hashtag(file_path):
                    end_path = os.path.join(public_path, r"content", os.path.relpath(file_path, private_path))
                    print("Found: " + file_path)
                    copy_file(file_path, end_path)
            # TODO: check for image/attachment at this line, while it's still in the for loop

def copy_file(target_path, destination_path):
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.copy2(target_path, destination_path)
        print("Copied to: " + destination_path)

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