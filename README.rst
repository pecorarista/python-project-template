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

   git clone https://github.com/pecorarista/python-project-template
   cd nyan
   pip install -e .

Usage
-----

1. Use this as a CLI tool.

   .. code-block:: bash

      nyan --name Chomusuke \
          --breed "Russian Blue" \
          --sex male

   The command shows the following message.

   .. code-block::

      This is my cat, Chomusuke.
      He is a Russian Blue.

2. Import the project as a library.

   .. code-block:: bash

      from nyan import Cat

      cat = Cat(name="Artemis",
                breed="Russian Blue",
                sex=Sexes.FEMALE)
      print(cat.praise())

Coding Style
------------

Follow `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_.
Use some extension of your editor to validate the code automatically.

Test
----

Test the source code by :code:`make test`.

Document
--------

Write docstring for public functions.
Follow the format of `Sphinx <http://www.sphinx-doc.org/en/stable/>`_.
There are several major styles in writing docstring for Sphinx.
You can see an example `here (Google Style Python Docstrings) <http://www.sphinx-doc.org/en/stable/ext/example_google.html>`_.

To convert docstrings into HTML pages, first edit author, project, and version in :code:`Makefile`. Then run :code:`make doc`.
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
