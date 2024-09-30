import os
import yaml
import shutil

# recursively loop through the private directory
# copies .md files with "#publish" tag into public
# WARNING: I have not implemented error checking

private_vault = os.getenv('private_vault')
public_vault = os.getenv('public_vault')

private_vault_path = str(private_vault)

def search_files(private_path, public_path):
    clear_dir(os.path.join(public_path, r"content"))
    for root, dirs, files in os.walk(private_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if has_publish_hashtag(file_path):
                    end_path = os.path.join(public_path, r"content", os.path.relpath(file_path, private_path))
                    print(f"Found: {file_path}")
                    copy_file(file_path, end_path)
            # TODO: check for image/attachment at this line, while it's still in the for loop

def clear_dir(directory):
    if not os.path.exists(directory):
        print(f"The folder {directory} does not exist.")
        return False
    print(f"Clearing: {directory}")
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            print(f"Cleared: {file_path}")
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            print(f"Cleared: {file_path}")
            shutil.rmtree(file_path)

def copy_file(target_path, destination_path):
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.copy2(target_path, destination_path)
        print(f"Copied to: {destination_path}")

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