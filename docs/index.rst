.. toctree::
   :maxdepth: 2
   :hidden:

   Creating tasks <creating_tasks.html#://>

=====
Linum
=====

.. image:: https://i.postimg.cc/rFWHwqwq/Artboard-1-0-5x.png
   :alt: Linum logo
   :align: center

.. image:: https://readthedocs.com/projects/chaberch-linum/badge/?version=latest&token=78b2cc17787db8f14e1038a6d8b054e9e6aaff80ea6706ac3990a9619969ee8c
   :target: https://chaberch-linum.readthedocs-hosted.com/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/l/ansicolortags.svg
   :target: https://pypi.python.org/pypi/ansicolortags/

.. image:: https://travis-ci.com/chabErch/Linum.svg?branch=master
   :target: https://travis-ci.com/chabErch/Linum


Linum is a tool for tasks visualization — like Gantt chart, but more compact.

Full documentation are `available here <https://chaberch-linum.readthedocs-hosted.com/>`_.
Also there is the `GitHub project page <https://github.com/chabErch/Linum>`_.

`Linum`_

- `Installation`_
- `Usage`_
    - `Supported output formats`_
    - `Coming soon output formats`_
- `Contributing`_
- `Author`_


************
Installation
************

Install Linum with `pip`:

.. code-block:: bash

   >>> pip install linum


*****
Usage
*****

If you need to visualize your schedule or working plan you are welcome to use Linum. Actually, you are able to use Gantt charts, but they are overloaded with extra information if you have many simple tasks. Gantt charts are better when tasks are sequential and connected between themselves.

Linum allows you to visualize your information on chosen time interval (week, month, year) like a timetable briefly and convenient.

To generate output file it require to create input file with tasks.
You may read here how to do it.

Supported output formats
========================

- Console
- Text (.txt)
- Excel (.xlsx)


Coming soon output formats
==========================

- HTML (.html)
- SVG (.svg)
- InDesign (.idml)


************
Contributing
************

For now Linum is ready to go for printing your tasks in console on a chosen time interval. Fell free to improve the project and develop any new output formats.


******
Author
******

- [Chaberch](https://github.com/chabErch)
