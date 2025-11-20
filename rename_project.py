#!/usr/bin/env python3

import os
import sys
import argparse
import shutil

# ANSI Colors for CLI
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Files and directories to ignore to prevent corruption or huge processing times
IGNORE_DIRS = {'.git', '.idea', '.vscode', '__pycache__', 'node_modules', 'dist', 'build', 'bin', 
'obj', '.svn', '.hg'}
IGNORE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.exe', '.dll', '.so', '.dylib', '.zip', 
'.tar', '.gz', '.pdf', '.pyc'}

def is_text_file(filepath):
    """
    Check if a file is text or binary by reading a small chunk.
    """
    try:
        # Check extension first
        _, ext = os.path.splitext(filepath)
        if ext.lower() in IGNORE_EXTENSIONS:
            return False

        with open(filepath, 'rb') as f:
            chunk = f.read(1024)
            if not chunk:
                return True  # Empty file considered text
            # If null byte exists, likely binary
            if b'\0' in chunk:
                return False
            return True
    except Exception:
        return False

def generate_variations(old_term, new_term):
    """
    Generates mapping for:
    1. Exact Match
    2. Lowercase (project -> newproject)
    3. Uppercase (PROJECT -> NEWPROJECT)
    4. Capitalized (Project -> Newproject)
    """
    variations = {}
    
    # 1. Exact Input
    variations[old_term] = new_term
    
    # 2. Lowercase
    variations[old_term.lower()] = new_term.lower()
    
    # 3. Uppercase
    variations[old_term.upper()] = new_term.upper()
    
    # 4. Capitalized (Title case)
    variations[old_term.capitalize()] = new_term.capitalize()
    
    # Remove duplicates if input was already one of these cases
    return variations

def process_content(filepath, variations, dry_run):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        new_content = content
        changes_count = 0
        
        for old, new in variations.items():
            if old in new_content:
                count = new_content.count(old)
                changes_count += count
                new_content = new_content.replace(old, new)
        
        if changes_count > 0:
            print(f"{Colors.OKBLUE}[CONTENT]{Colors.ENDC} Found {changes_count} matches in: {filepath}")
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                    
    except Exception as e:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Could not process {filepath}: {e}")

def process_renames(root_dir, variations, dry_run):
    """
    Renames files and directories. 
    IMPORTANT: Must process depth-first (bottom-up) so we don't rename 
    a parent directory before its children are processed.
    """
    for root, dirs, files in os.walk(root_dir, topdown=False):
        
        # Skip ignored directories
        if any(ignored in root.split(os.sep) for ignored in IGNORE_DIRS):
            continue

        # 1. Rename Files
        for filename in files:
            name, ext = os.path.splitext(filename)
            
            new_filename = filename
            renamed = False
            
            # check all variations
            for old, new in variations.items():
                if old in new_filename:
                    new_filename = new_filename.replace(old, new)
                    renamed = True
            
            if renamed and new_filename != filename:
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                
                print(f"{Colors.WARNING}[RENAME FILE]{Colors.ENDC} {filename} -> {new_filename}")
                
                if not dry_run:
                    try:
                        os.rename(old_path, new_path)
                    except OSError as e:
                        print(f"{Colors.FAIL}Failed to rename file: {e}{Colors.ENDC}")

        # 2. Rename Directories
        for dirname in dirs:
            if dirname in IGNORE_DIRS:
                continue
                
            new_dirname = dirname
            renamed = False
            
            for old, new in variations.items():
                if old in new_dirname:
                    new_dirname = new_dirname.replace(old, new)
                    renamed = True
            
            if renamed and new_dirname != dirname:
                old_path = os.path.join(root, dirname)
                new_path = os.path.join(root, new_dirname)
                
                print(f"{Colors.WARNING}[RENAME DIR]{Colors.ENDC} {dirname} -> {new_dirname}")
                
                if not dry_run:
                    try:
                        os.rename(old_path, new_path)
                    except OSError as e:
                        print(f"{Colors.FAIL}Failed to rename dir: {e}{Colors.ENDC}")

def main():
    parser = argparse.ArgumentParser(description="CLI to rename any programming project recursively.")
    
    parser.add_argument("path", help="Path to the project directory")
    parser.add_argument("--old", required=True, help="The old project name (e.g., GPT-DB)")
    parser.add_argument("--new", required=True, help="The new project name (e.g., GPT-DB)")
    
    # Optional: Developer/Org rename
    parser.add_argument("--old-dev", help="Old Developer/Org name")
    parser.add_argument("--new-dev", help="New Developer/Org name")
    
    parser.add_argument("--run", action="store_true", help="Actually execute the changes. (Default is Dry Run)")

    args = parser.parse_args()

    target_path = os.path.abspath(args.path)
    
    if not os.path.exists(target_path):
        print(f"{Colors.FAIL}Error: Path '{target_path}' does not exist.{Colors.ENDC}")
        sys.exit(1)

    print(f"{Colors.HEADER}Target: {target_path}{Colors.ENDC}")
    if not args.run:
        print(f"{Colors.WARNING}*** DRY RUN MODE (No changes will be made) ***{Colors.ENDC}")
        print(f"Use {Colors.OKGREEN}--run{Colors.ENDC} to execute.")
    
    # 1. Build Map of replacements
    mappings = generate_variations(args.old, args.new)
    
    # Add developer/org mappings if provided
    if args.old_dev and args.new_dev:
        dev_mappings = generate_variations(args.old_dev, args.new_dev)
        mappings.update(dev_mappings)

    print(f"{Colors.OKBLUE}Replacements pattern:{Colors.ENDC}")
    for k, v in mappings.items():
        print(f"  '{k}' -> '{v}'")
    print("-" * 40)

    # 2. Process Content (Find and Replace inside text files)
    print(f"\n{Colors.HEADER}Phase 1: Updating File Contents...{Colors.ENDC}")
    for root, dirs, files in os.walk(target_path):
        # Skip ignored folders
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            file_path = os.path.join(root, file)
            if is_text_file(file_path):
                process_content(file_path, mappings, not args.run)

    # 3. Process Filesystem (Rename files and folders)
    print(f"\n{Colors.HEADER}Phase 2: Renaming Files and Folders...{Colors.ENDC}")
    process_renames(target_path, mappings, not args.run)

    if not args.run:
        print(f"\n{Colors.WARNING}Dry run complete. No changes made.{Colors.ENDC}")
    else:
        print(f"\n{Colors.OKGREEN}Refactoring Complete!{Colors.ENDC}")

if __name__ == "__main__":
    main()
