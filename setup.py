from setuptools import setup, find_packages

setup(
    name='jinjastatic',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyYAML',
        'Jinja2',
        'jinja_markdown',
        'htmlmin',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'jinjastatic = jinjastatic.jinjastatic_tool:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool for rendering Jinja templates with static files and HTML minification.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/jinjastatic',  # Update this with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
