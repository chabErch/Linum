.. Linum documentation master file, created by
   sphinx-quickstart on Sun May  9 21:18:51 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================================
Welcome to Linum's documentation!
=================================

.. image:: https://i.postimg.cc/rFWHwqwq/Artboard-1-0-5x.png
   :alt: Linum logo
   :align: center

.. image:: https://readthedocs.org/projects/linum/badge/?version=latest
   :target: https://linum.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/l/ansicolortags.svg
   :target: https://pypi.python.org/pypi/ansicolortags/

.. image:: https://travis-ci.com/chabErch/Linum.svg?branch=master
   :target: https://travis-ci.com/chabErch/Linum


Linum is a tool for tasks visualization — like Gantt chart, but more compact.

Linum GitHub `project page <https://github.com/chabErch/Linum>`_.


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
- SVG (.svg)


Coming soon output formats
==========================

- HTML (.html)
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

SVG renderer
------------

.. image:: https://i.postimg.cc/6psCNTzn/svg-renderer.png
   :align: center
   :alt: SVG renderer


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


****************
Table of content
****************

.. toctree::
   :maxdepth: 1
   :caption: Usage

   usage

.. toctree::
   :maxdepth: 1
   :caption: Tasks

   creating_tasks

.. toctree::
   :maxdepth: 1
   :caption: Context

   creating_context
   renderers/txt_renderer
   renderers/xlsx_renderer
   renderers/svg_renderer

