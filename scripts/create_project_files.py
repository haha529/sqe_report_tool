import os

# Define the directory and file structure
structure = {
    "web-automation-system": {
        "backend": {
            "app": {
                "__init__.py": "",
                "main.py": "",
                "models.py": "",
                "routes.py": "",
                "services": {
                    "__init__.py": "",
                    "screenshot_service.py": "",
                    "email_service.py": ""
                },
                "utils": {
                    "__init__.py": "",
                    "image_utils.py": ""
                }
            },
            "tests": {
                "__init__.py": "",
                "test_main.py": "",
                "test_screenshot_service.py": "",
                "test_email_service.py": ""
            },
            "Dockerfile": "",
            "requirements.txt": "",
            ".env": ""
        },
        "frontend": {
            "app.py": "",
            "requirements.txt": "",
            "Dockerfile": ""
        },
        "templates": {
            "email_template.html": ""
        },
        "screenshots": {},
        "logs": {},
        ".gitignore": "",
        "README.md": ""
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

if __name__ == "__main__":
    # Create the directory and file structure
    create_structure(".", structure)