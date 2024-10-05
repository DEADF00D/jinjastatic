import yaml
from jinja2 import Environment, FileSystemLoader
import os
import shutil
from htmlmin import minify
from rich.console import Console
import argparse
from jinja_markdown import MarkdownExtension

class ConfigParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pages = []
        self.templates = []
        self.env = Environment(loader=FileSystemLoader('_jinja/templates/'))
        self.env.add_extension(MarkdownExtension)
        self.console = Console()
        self.load_config()
        self.move_static_files()

    def load_config(self):
        with open(self.file_path, 'r') as file:
            config = yaml.safe_load(file)
            if 'pages' in config and isinstance(config['pages'], list):
                self.pages = config['pages']
                self.load_templates()
            else:
                raise ValueError("The 'pages' key is either missing or is not a list.")

    def load_templates(self):
        for page in self.pages:
            template = self.env.get_template(page)
            self.templates.append(template)
        self.render_templates()

    def render_templates(self):
        for template in self.templates:
            output_path = os.path.join('.', template.name)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            rendered_html = template.render()
            minified_html = minify(rendered_html, remove_comments=True, remove_empty_space=True)
            original_size = len(rendered_html.encode('utf-8'))
            minified_size = len(minified_html.encode('utf-8'))
            size_difference = original_size - minified_size

            with open(output_path, 'w') as output_file:
                output_file.write(minified_html)

            self.console.print(f"{template.name} -> [bold blue]{output_path}[/bold blue] ({size_difference} bytes reduced)")

    def move_static_files(self):
        src_static_dir = os.path.join('_jinja', 'static')
        dest_static_dir = 'static'
        if os.path.exists(dest_static_dir):
            shutil.rmtree(dest_static_dir)
        shutil.copytree(src_static_dir, dest_static_dir)
