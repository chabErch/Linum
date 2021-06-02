================
Creating context
================

Context, like `tasks <creating_tasks.html>`_, is a text file in YAML format
(``.yaml`` extension).
In context file you determine render period, style settings,
list of workdays and list of days-off.


**************
Base structure
**************

Context consists of several optional sections:

- ``period`` section for specifying base period settings;

- ``workdays`` section with list of dates which Linum must
  consider as working days;

- ``days_off`` section with list of dates which Linum must
  consider as days-off;

- ``txt_renderer`` section for overriding period settings and specifying
  styles for console and txt render;

- ``xlsx_renderer`` section for overriding period settings and specifying
  styles for excel render.

- ``svg_renderer`` section for overriding period settings and specifying
  styles for svg render.

All this sections may be in no particular order or be absent.


*************************
Days-off and working days
*************************

By default Linum considers all Saturdays and Sundays as days-off
and other weekdays as working days.
If you want specify day as day-off you must indicate it in ``days_off`` subsection.

.. code-block:: yaml

   days_off:
     - 2020-01-01
     - 2020-01-02
     - 2020-01-03

If you want to indicate certain Saturday or Sunday as working day
you must specify it in ``workdays`` subsection.

.. code-block:: yaml

   workdays:
     - 2020-01-04
     - 2020-01-05


If one date is in both sections then ``workdays`` section will be in priority.


.. _render_period:

*************
Render period
*************

``period`` section specify base period settings.

.. code-block:: yaml

  period:
    start: 2020-01-01
    finish: 2021-01-01
    months_in_row: 2


``start``
=========

Specifies date when period of view begins.
Value is date in format ``<year>-<month>-<day>``.
If not stated, then Linum will consider it as today date.


``length``
==========

Specify when period of view is over after ``start`` date.
Value must be integer.


``finish``
==========

Specify when period of view is over.
Value is date in format ``<year>-<month>-<day>``.
If both of ``length`` and ``finish`` are stated then
``finish`` will be in priority.


``months_in_row``
=================

Specify how many months must be in one row.
Value must be integer.


***************
Renderer custom
***************

There are 3 main renderers in Linum.
Each renderer has custom view settings that may be determine:

- `txt_renderer <renderers/txt_renderer.html>`_;

- `xlsx_renderer <renderers/xlsx_renderer.html>`_;

- `svg_renderer <renderers/svg_renderer.html>`_.
