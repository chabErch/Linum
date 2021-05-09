==============
Creating tasks
==============

Tasks creates in text file in `yaml <https://yaml.org/>`_ format.
It isn`t necessary you to know all yaml syntax.
All you need is be carefully with indent spaces
(use double space for one intend) and read this article.


*****
Basic
*****

Let`s create first task. Here is the simple example:

.. code-block:: yaml
   :linenos:

   My first task:
     start: 2020-01-01
     length: 5

In first line you specify task name. It may be any sting you want.
After task name must be symbol ':'

To specify properties for task you need to write indent and key-value pair.
Key and value separated by symbol ':' and one space symbol.

In second line after `date` keyword you specify when task starts.
All dates must be in format `<year>-<month>-<day>`.
If you don`t specify start date it will be considered as current day.

And in third line after `length` keyword  you specify length of task.
If you don`t specify length it will be considered as one day length.

All lines with keywords are optional, but you must specify at lest one of all of them.


Length or finish
================

You may use `finish` keyword instead `length` to specify when task is over.
If both keyword are using then `finish` will be in priority.

.. code-block:: yaml
   :linenos:

   My second task:
     start: 2020-01-10
     finish: 2020-02-10


Color
=====

You may specify color to render for certain task.
To do it use `color` keyword and hex rgb integer as value.

.. code-block:: yaml
   :linenos:

   Red task:
     start: 2020-02-10
     color: 0xFF0000

If color property does not setted then random color
from material design palette would be applied.

*********
Sub tasks
*********

It is also possible to specify sub tasks for certain task
using `sub` keyword. There are two ways how to do that.

If you want to create several tasks with one name
you need to use list sub tasks.
And if you want to create tasks with different names
you need to use dictionary sub tasks.

In both cases parent properties will be inherited for a child.

Also it is possible to specify sub tasks for sub tasks.


List sub tasks
==============

In yaml list elements start by minus symbol and one space after it.

.. code-block:: yaml
   :linenos:

    List Task:
      length: 3
      sub:
        - date: 2020-01-01
        - date: 2020-01-20
          length: 4
        - date: 2020-02-10
          color: 0x000000

For this example Linum would create 3 tasks.
First of them starts at 2020-01-01,
second starts at 2020-01-20 and has length 4,
and third starts at 2020-02-10 and has black color.


Dictionary sub tasks
====================

For every dictionary sub task title would be computed as
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
