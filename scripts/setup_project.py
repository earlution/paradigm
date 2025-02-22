#!/usr/bin/env python3
"""
Project setup script.

This script replaces template placeholders with actual project values.
"""
import os
import re
import sys
from pathlib import Path


def replace_in_file(file_path, placeholder, replacement):
    """Replace placeholder with replacement in file."""
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    content = content.replace(placeholder, replacement)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Updated {file_path}")


def setup_project(project_name):
    """Set up project by replacing placeholders."""
    root_dir = Path(__file__).parent.parent
    
    # Files to update
    files_to_update = [
        root_dir / "README.md",
        root_dir / "pyproject.toml",
        root_dir / "src" / "{{project_name}}" / "__init__.py",
    ]
    
    # Replace placeholders in files
    for file_path in files_to_update:
        if file_path.exists():
            replace_in_file(file_path, "{{project_name}}", project_name)
    
    # Rename directories
    src_dir = root_dir / "src" / "{{project_name}}"
    tests_dir = root_dir / "tests" / "{{project_name}}"
    docs_dir = root_dir / "docs" / "{{project_name}}"
    
    if src_dir.exists():
        os.rename(src_dir, root_dir / "src" / project_name)
        print(f"Renamed directory: {src_dir} -> {root_dir / 'src' / project_name}")
    
    if tests_dir.exists():
        os.rename(tests_dir, root_dir / "tests" / project_name)
        print(f"Renamed directory: {tests_dir} -> {root_dir / 'tests' / project_name}")
    
    if docs_dir.exists():
        os.rename(docs_dir, root_dir / "docs" / project_name)
        print(f"Renamed directory: {docs_dir} -> {root_dir / 'docs' / project_name}")
    
    print(f"Project setup complete: {project_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python setup_project.py <project_name>")
        sys.exit(1)
        
    project_name = sys.argv[1]
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', project_name):
        print("Error: Project name must start with a letter and contain only letters, numbers, and underscores.")
        sys.exit(1)
        
    setup_project(project_name)