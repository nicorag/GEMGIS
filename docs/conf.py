# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath("../"))

# import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'gemgis'
copyright = '2021, Alexander Juestel'
author = 'Alexander Juestel'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- GemGIS configuration ---------------------------------------------------
sys.path.append('../../gemgis')
# import gemgis
# import numpy as np

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx_rtd_theme',
    #'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'sphinx_markdown_tables',
    # 'notfound.extension',
    'sphinx_copybutton',
    #'sphinx_gallery.gen_gallery',
    'sphinx.ext.extlinks',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

nbsphinx_execute = 'never'

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]

copybutton_prompt_text = ">>> "

#sphinx_gallery_conf = {
#     'examples_dirs': ['../examples/models'],   # path to your example scripts
#     'gallery_dirs': ['getting_started/example_models'],  # path to where to save gallery generated output
#
#    'filename_pattern': r"\.py",
#
#    'remove_config_comments': True,
#    'notebook_images': True,
#    "image_scrapers": ('pyvista', 'matplotlib'),
#    'first_notebook_cell': ("%matplotlib inline\n"
#                            "from pyvista import set_plot_theme\n"
#                            "set_plot_theme('document')"),
#
#}
