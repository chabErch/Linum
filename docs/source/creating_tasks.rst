==============
Creating tasks
==============

To produce tasks you need to create text file in `YAML <https://yaml.org/>`_
format (``.yaml`` extension).
It isn`t necessary for you to know all yaml syntax.
All you need is be careful with number of spaces per indent
(There is no requirement in YAML to indent any concrete number of spaces,
but you need to use the same number of spaces in all your YAML file)
and read this article.


*****
Basic
*****

Let`s create the first task. Here is the simple example:

.. code-block:: yaml
   :linenos:

   My first task:
     start: 2020-01-01
     length: 5

In the first line you specify task name. It may be any string you want.
After task name must be symbol ``:``

To specify properties for task you need to write indent and key-value pair.
Key and value separated by symbol ``:`` and one space symbol after it.

In the second line after ``date`` keyword you specify date when task starts.
All dates must be in format ``<year>-<month>-<day>``.
If you don`t specify start date Linum will consider it as a current day.

And in the third line after ``length`` keyword you specify length of a task.
If you don`t specify length it will consider as one day length.

All lines with keywords are optional, but you must specify at least one of them.


Length or finish
================

You may use ``finish`` keyword instead of ``length`` to specify date when task is over.
If both of keyword were used then ``finish`` would be in priority.

.. code-block:: yaml
   :linenos:

   My second task:
     start: 2020-01-10
     finish: 2020-02-10


Color
=====

You may specify color to render for certain task.
To do it use ``color`` keyword and hex rgb integer as value.

.. code-block:: yaml
   :linenos:

   Red task:
     start: 2020-02-10
     color: 0xFF0000

If you don`t set color property then random color from
`material design palette <https://material.io/design/color/the-color-system.html#tools-for-picking-colors>`_
will be applied.

*********
Sub tasks
*********

It is possible to specify sub tasks for certain task
using ``sub`` keyword. There are two ways to do it.

- If you want to create several tasks with one name use **list sub tasks**.

- If you want to create tasks with different names use **dictionary sub tasks**.

In both cases parent properties will be inherited for a child.

It is possible to specify sub tasks for sub tasks.


List sub tasks
==============

In YAML list elements start by minus symbol and one space after it.

.. code-block:: yaml
   :linenos:

    List Task:
      length: 3
      sub:
        - date: 2020-01-01
        - date: 2020-01-20
          length: 4
        - date: 2020-02-10
          color: 0x000000  # Black color

For this example Linum will create 3 tasks.
First starts at 2020-01-01,
second starts at 2020-01-20 and has length 4 days,
and third starts at 2020-02-10 and has black color.


Dictionary sub tasks
====================

For every **dictionary sub task** title would be computed as
parent name plus sub task name.

.. code-block:: yaml
   :linenos:

   Task 1.:
     color: 0x00FF00
     length: 3
     sub:
       1:
         start: 2020-03-01
       2:
         start: 2020-03-05
         finish: 2020-03-08

For this example Linum will create 2 tasks: "Task 1.1" and "Task 1.2".
