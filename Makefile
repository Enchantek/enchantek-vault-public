.DEFAULT_GOAL := all

help: ## Show all Makefile targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

publish: ## Copy notes from private vault to public vault
	python utils/publish_notes.py

sync: ## Sync local public vault to GitHub repository
	npx quartz sync

preview: publish ## Build and serve a local preview of the website
	npx quartz build --serve

build: ## Build the website without serving
	npx quartz build

deploy: publish sync ## Publish notes and sync to GitHub
	@echo "Deployment complete. Remember to push changes to GitHub if needed."

all: publish sync ## Publishes notes from private vault to public vault and syncs