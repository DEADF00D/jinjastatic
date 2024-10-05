#!/usr/bin/env python

import argparse, os
from jinjastatic.config_parser import ConfigParser
from rich import print

# Command line entry point
def main():
    parser = argparse.ArgumentParser(description="Process the configuration file path.")
    parser.add_argument('-c', '--config', type=str, default="./_jinja/config.yaml", help="Path to the configuration YAML file")
    parser.add_argument('--new-project', action='store_true', help="Create a new project with default _jinja structure")
    args = parser.parse_args()

    # Determine the correct working directory
    current_dir = os.getcwd()
    if '_jinja' in current_dir:
        while current_dir.endswith('_jinja') or '_jinja' in os.path.basename(current_dir):
            current_dir = os.path.dirname(current_dir)
        os.chdir(current_dir)

    if args.new_project:
        os.makedirs('_jinja/templates', exist_ok=True)
        os.makedirs('_jinja/static', exist_ok=True)
        config_path = os.path.join('_jinja', 'config.yaml')
        if not os.path.exists(config_path):
            with open(config_path, 'w') as config_file:
                config_file.write("pages: []\n")
        print("[bold green]_jinja project structure created successfully.[/bold green]")
    else:
        config_path = args.config
        config_parser = ConfigParser(config_path)
        print("[bold green]Finished building.[/bold green]")

if __name__ == "__main__":
    main()
