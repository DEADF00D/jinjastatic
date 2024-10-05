# Jinja Static

Jinja Static is an exceptionally lightweight static website generator that utilizes the powerful Jinja2 templating engine.

This tool allows for the creation of sophisticated static websites with a syntax reminiscent of Twig and all the features of python.

## Why?

I've built numerous Flask-based websites, and I always found the process cumbersome: setting up a minimal Flask backend, designing everything, packaging it in a Docker container, configuring Gunicorn and workers, managing dependencies, and deploying to production.

Each time I needed to make changes, I had to rebuild the containers, even for sites that were mostly static but not necessarily simple. Many had a lot of pages, and managing complex HTML through copy-pasting was inefficient.

I experimented with Hugo for a while, but I kept encountering frustrating build issues. The customization options, while powerful, came with a steep learning curve for me.

To solve these problems, I created this tool as a prebuilder, designed to keep the footprint on the repo minimal. The root directory contains production-ready files that are built before committing, making the workflow simpler and compatible with all static hosting platforms without needing to configure complex routing rules.

## Dead simple code

The entire codebase is 50 lines Python, it's basically a very simple Jinja2 configurator.

You can modify it, extend it, and implement whatever you need in about 30min.

## Getting Started
To install Jinja Static, run:

```bash
pip install jinjastatic
```

To initialize a new Jinja Static project, use the following command within your project directory:

```bash
mkdir myproject; cd myproject
jinjastatic --create-project
```

This will create the `_jinja` directory, where you can add your template files and define your pages in `_jinja/config.yaml`.

### Configuration Example

```yaml
pages:
  - index.html
```

A typical page can be defined as follows:

`index.html`
```html
{% extends "main.html" %}

{% block Body %}
<h1>Hello, world!</h1>
<ul>
{% for p in range(10) %}
  <li>{{ p }}</li>
{% endfor %}
</ul>
{% endblock %}
```

`main.html`
```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Hello, world!</title>
        <link href="/static/style.css" rel="stylesheet">
    </head>
    <body>
        {% block Body %}{% endblock %}
    </body>
</html>
```

Once your templates are ready, simply execute the following command to generate and minify your HTML:

```bash
$ jinjastatic
```

You can now test your website with a simple:
```
python -m http.server 8000
```

Or send it to any static hosting platform.

# Cool examples

## Build a blog

You can build an extensible and easy to maintain blog like so:

`blog.html`
```html
{% set articles = [
  { "title": "My first post!", "path": "/blog/my-first-post.html" }
  { "title": "My second post!", "path": "/blog/my-second-post.html" }
]%}

{% for article in articles %}
<a href="{{article.path}}">{{article.title}}</a>
{% endfor %}
```
`/blog/my-first-post.html`
```html
<h1>My first blog post!</h1>
```
`/blog/my-second-post.html`
```html
<h1>My second blog post!</h1>
```
`config.yaml`
```yaml
pages:
  - blog.html
  - blog/my-first-post.html
  - blog/my-second-post.html
```

In the future you can just create more page extending the same main template, and add elements to your `article` array.

## Use markdown

You can use markdown built-it like that:
```
{% markdown %}
# Hello, world!
Now this is a **really cool** static website generator.
{% markdown %}
```
