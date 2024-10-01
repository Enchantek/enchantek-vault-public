---
tags:
  - devlog
  - quartz
  - obsidian
  - publish
created: 2024-09-28T06:09
modified: 2024-10-01T15:44
---
# dev log quartz

### Brainstorming

The first thing on my mind is how I want to distinguish the line between my personal vault and my public vault. One option would be to keep everything, both my personal and public files, under one folder. But I don’t really feel comfortable with that. Another option would be to have two different folders, public and private vaults, and have some script copy the selected files I want to upload from private to public. A third option would be something that I saw online; have everything under one folder, but have the private and public vaults at different layers of the folder hierarchy, preventing public access to private files. I haven’t put too much thought into how I would do that so I’ll think about it.

### Original vault

Created a [[Vault title structure|naming convention]] for my personal vault first. Did this so that I would have a solid understanding of how specifically I want to structure my vault. Next I need to figure out what to do with the areas folder. I already decided I’m going to keep my permanent notes in the notes folder, so thinking of what I should put in areas other than east bay stuff would help.

### Taking inspiration

One of the biggest reasons for wanting to make a public Quartz vault was because of Simon Späti and his vault. I was looking at his `find-publish-notes.py` script and found a few good ideas from it I could use.

```python
git = os.getenv("git")
secondbrain = os.getenv("secondbrain")
secondbrain_public = os.getenv("public_secondbrain")


# define paths
second_brain_path = str(secondbrain)  # "/tmp/second-brain-tmp"
public_folder_path_copy = str(secondbrain_public)
public_brain_image_path = os.path.join(public_folder_path_copy, "images")
```

He uses environment variables when getting the directories of the public/private vaults. This allows the script to work across multiple devices, which would be in my case because I always use my desktop computer and laptop. I thought this would be better than the alternatives; manually inputting the directories whenever I run the script or hardcoding them. 

### Search function implemented

```python
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
```

### Success

```python
import os
import yaml
import shutil
import re

# recursively loop through the private directory
# copies .md files with "#publish" tag into public
# WARNING: I have not implemented error checking

private_vault = os.getenv('private_vault')
public_vault = os.getenv('public_vault')
regex = r'!\[\[(.*?)\]\](.*)\s'

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
        # Find attachments
        with open(target_path, "r", encoding='utf-8') as file:
            content = file.read()
            attachments = re.findall("!\[\[(.*?)\]\](.*)\s", content)
            print(f"Attachments found: {[att[0] for att in attachments]}")
            for attachment_tuple in attachments:
                attachment = attachment_tuple[0]
                for root, dir, files in os.walk(private_vault):
                    if attachment in files:
                        attachment_destination_path = os.path.join(os.path.dirname(destination_path), "attachments", attachment)
                        attachment_target_path = os.path.join(root, attachment)
                        os.makedirs(os.path.dirname(attachment_destination_path), exist_ok=True)
                        shutil.copy(attachment_target_path, attachment_destination_path)
                        print(f"Copied attachment to: {destination_path}")

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
```

I got everything to work. It took a bit longer than I expected but I was learning as I went along. While learning I tried to take notes of whatever I could that I found interesting or important.

### Makefile

```makefile
.DEFAULT_GOAL := all

help: ## Show all Makefile targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

publish: ## Copy notes from private vault to public vault
	python utils/publish_notes.py

sync: ## Sync local public vault to GitHub repository
	npx quartz sync

preview: ## Build and serve a local preview of the website
	npx quartz build --serve

build: ## Build the website without serving
	npx quartz build

deploy: publish sync ## Publish notes and sync to GitHub
	@echo "Deployment complete. Remember to push changes to GitHub if needed."

all: ## Publishs notes from private vault to public vault and syncs
	@echo "Starting publish process..."
	@make publish
	@echo "Publishing complete. Starting sync process..."
	@make sync
```

Created a Makefile so that I could run the publish and syncing commands easily.

I might need to modify the code so that it would render any Excalidraw drawings that I embed into my documents, if that’s even possible. I’ll have to look into that because I’m not sure if somebody came up with a solution for it already.

- [ ] TODO: add Excalidraw compatibility
- [ ] TODO: HTML conversion? So you’d be able to click on the pure HTML files to open them separately from the website
- [ ] TODO: custom domain

Thankfully Quartz has plenty of documentation on how it works. I could look through [this](https://quartz.jzhao.xyz/advanced/architecture) to read a walkthrough of its components.

### Organization ideas

I was thinking of some modifications I could make to my obsidian vault. Maybe changing the way I [[Vault title structure|categorize]] my notes. On a slightly off topic note, I find myself swinging between something technical or something romanticized when it comes to how I look at my notes. Do I want to look at is as purely knowledge based? Or maybe I want to give it a philosophical flare. But then how would that affect my foundational notes? Perhaps there’s a way to bring these two ideas together.