import os

# recursively loop through the private directory
# copies .md files with "#publish" tag into public

private_vault = os.getenv('private_vault')
public_vault = os.getenv('public_vault')

private_vault_path = str(private_vault)

def search_publish_hashtag(public_path, private_path):
    for root, dirs, files in os.walk(public_path):
        for file in files:
            if file.endswith('.md'):
                print(os.path.join(root, file))