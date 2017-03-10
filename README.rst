python-project-template
=======================

Template for Python projects.
The sample project **nyan** is assumed to be released as a CLI tool as well as a library.

Requirements
------------

* Python 2.7+ or 3.6+

Installation
------------

.. code-block:: bash

    git clone git@github.com:mynlp/nyan.git
    cd nyan
    pip install -e .

Coding Style
------------

Follow `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_.
Use some extension of your editor to validate the code automatically.

Document
--------

Write docstring for public functions.
Follow the format of `Sphinx <http://www.sphinx-doc.org/en/stable/>`_.
There are several major styles in writing docstring for Sphinx.
You can see an example `here (Google Style Python Docstrings) <http://www.sphinx-doc.org/en/stable/ext/example_google.html>`_.

To convert docstrings into HTML pages, edit author, project, and version variable in :code:`Makefile` and run :code:`make doc`.
It automatically configures Sphinx and creates some files under directory :code:`docs`.

Edit :code:`*.rst` file to document your source code in an organized format.
Then :code:`make doc; make preview` to view the pages on the browser.

.. code-block:: rst

    An Example of API Document
    --------------------------
    .. automodule:: nyan.cat
        :members:
        :undoc-members:
        :show-inheritance:
