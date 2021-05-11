.. Linum documentation master file, created by
   sphinx-quickstart on Sun May  9 21:18:51 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================================
Welcome to Linum's documentation!
=================================

.. toctree::
   :maxdepth: 3
   :hidden:

   usage
   creating_tasks
   creating_context

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

Full documentation `available here <https://chaberch-linum.readthedocs-hosted.com/>`_.

Linum GitHub `project page <https://github.com/chabErch/Linum>`_.

- :doc:`usage`
- :doc:`creating_tasks`
- :doc:`creating_context`


***********
Description
***********

If you need to visualize your schedule or
working plan you are welcome to use Linum.
Actually, you are able to use Gantt charts,
but they are overloaded with extra information
if you have many simple tasks.
Gantt charts are better when tasks are sequential
and connected between themselves.

Linum allows you to visualize your information on chosen time interval
(week, month, year) like a timetable briefly and convenient.

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


Render examples
===============


TXT renderer
------------

.. image:: https://i.postimg.cc/zB3QnTbL/image-2021-05-10-00-29-15.png
   :align: center
   :alt: TXT renderer


XLSX renderer
-------------

.. image:: https://i.postimg.cc/NM7SbdJ0/image-2021-05-10-00-15-25.png
   :align: center
   :alt: XLSX renderer

All the date titles correspond your language version of Excel.
In this case all titles are shown in Russian locales.


************
Contributing
************

For now Linum is ready to go for rendering your tasks in several formats
on a chosen time interval.
Feel free to improve the project and develop any new output formats.


******
Author
******

- `Chaberch <https://github.com/chabErch>`_

