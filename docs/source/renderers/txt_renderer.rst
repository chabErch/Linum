============
Txt renderer
============

``txt`` section overrides period settings and specifies
styles for console and txt renderers.

You may override period settings specially for txt renderer.
Use params from :ref:`render_period` section for it, for example:

.. code-block:: yaml

   start: 2020-01-01
   finish: 2020-02-01

   txt:
      finish: 2021-01-01

*********
Cell size
*********

To determine cell size use ``cell_width`` keyword. Value must be integer.

.. code-block:: yaml

   txt:
     cell_width: 5


*******
Borders
*******

There are some border settings for txt renderer.

.. code-block:: yaml

   txt:
     inner_borders: False
     month_inner_borders: True
     left_border: True
     right_border: True


``inner_borders``
=================

Determines border presence between days.
Value must be ``True`` or ``False``.


``month_inner_borders``
=======================

Determines border presence between months.
Value must be ``True`` or ``False``.


``left_border``
===============

Determines left border for resulted render.
Value must be ``True`` or ``False``.


``right_border``
================

Determines right border for resulted render.
Value must be ``True`` or ``False``.

