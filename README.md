
pandoc-tpp 0.1
==============

*pandoc-tpp* is a [pandoc] template preprocessor.

Pandoc templates lack an `$include(path)$` statement.  This script provides one.

A demonstration can be found in the [`demo/`] directory.  Run `make` to generate `out/demo.html` from `demo.md` using the nested templates in `templates/`.

I am pleased to receive bug reports and feature requests on the project's [Issues tracker].

[pandoc]: http://pandoc.org/
[`demo/`]: demo/
[Issues tracker]: https://github.com/tomduck/pandoc-tpp/issues


Syntax
------

The `$include(path)$` statement is used in a pandoc template to read the contents at `path` into the template.  The contents of `path` are also scanned for `$include(...)$` statements.


Usage
-----

Suppose we have a template `templates.default.html` that includes other templates.

Standard application of pandoc-tpp to the template results in output to stdout; e.g.,

    pandoc-tpp templates/default.html

The output can be redirected to a file.

Alternatively, we can make the preprocessed template available directly to pandoc (via a tempfile) as follows:

    pandoc demo.md -o demo.html --template $(pandoc-tpp -t templates/default.html5)

In a Makefile, use this instead:

    pandoc demo.md -o demo.html --template $(shell pandoc-tpp -t templates/default.html5)


Installation
------------

Pandoc-tpp requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed on Windows.  Either python 2.7 or 3.x will do.

[python]: https://www.python.org/


#### Standard installation ####

Install pandoc-tpp as root using the shell command

    pip install pandoc-tpp

To upgrade to the most recent release, use

    pip install --upgrade pandoc-tpp

Pip is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution.

[PyPI]: https://pypi.python.org/pypi


#### Installing on linux ####

If you are running linux, pip may be packaged separately from python.  On Debian-based systems (including Ubuntu), you can install pip as root using

    apt-get update
    apt-get install python-pip

During the install you may be asked to run

    easy_install -U setuptools

owing to the ancient version of setuptools that Debian provides.  The command should be executed as root.  You may now follow the [standard installation] procedure given above.

[standard installation]: #standard-installation


#### Installing on Windows ####

It is easy to install python on Windows.  First, [download] the latest release.  Run the installer and complete the following steps:

 1. Install Python pane: Check "Add Python 3.5 to path" then
    click "Customize installation".

 2. Optional Features pane: Click "Next".

 3. Advanced Options pane: Optionally check "Install for all
    users" and customize the install location, then click "Install".

Once python is installed, start the "Command Prompt" program.  Depending on where you installed python, you may need to elevate your privileges by right-clicking the "Command Prompt" program and selecting "Run as administrator".  You may now follow the [standard installation] procedure given above.  Be sure to close the Command Prompt program when you have finished.

[download]: https://www.python.org/downloads/windows/
