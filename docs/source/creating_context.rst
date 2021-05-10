================
Creating context
================

Context, like a `tasks <creating_tasks.html>`_, is a text file in yaml format
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

If you want specify certain Saturday or Sunday as working day
you must specify it in ``workdays`` subsection.

.. code-block:: yaml

   workdays:
     - 2020-01-04
     - 2020-01-05


If one date would be in both sections then ``workdays`` section would be in priority.


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

Specify when period of view must begin.
Value is date in format ``<year>-<month>-<day>``.
If not indicated them Linum will consider it as today date.


``length``
==========

Specify when period of view must be over after ``start`` date.
Value must be integer.


``finish``
==========

Specify when period of view must be over.
Value is date in format ``<year>-<month>-<day>``.
If both ``length`` and ``finish`` are specifying then
``finish`` would be in priority.


``months_in_row``
=================

Specify how many months must be in one row.
Value must be integer.


************
Txt renderer
************

``txt_renderer`` section overrides period settings and specifies
styles for both console and txt renderers.

You may override period settings specially for xlsx renderer.
Use params from :ref:`render_period` section for it.


Cell size
=========

To determine cell size use ``cell_width`` keyword. Value must be integer.

.. code-block:: yaml

   txt_renderer:
     cell_width: 5


Borders
=======

There are some border settings for txt renderer.

.. code-block:: yaml

   txt_renderer:
     inner_borders: False
     month_inner_borders: True
     left_border: True
     right_border: True


``inner_borders``
-----------------

Determines borders presence between days.
Value must be ``True`` or ``False``.


``month_inner_borders``
-----------------------

Determines borders presence between months.
Value must be ``True`` or ``False``.


``left_border``
---------------

Determines left border for resulted render.
Value must be ``True`` or ``False``.


``right_border``
----------------

Determines right border for resulted render.
Value must be ``True`` or ``False``.


*************
Xlsx renderer
*************

``xlsx_renderer`` section overrides period settings and specifies
styles for excel render.

You may override period settings specially for xlsx renderer.
Use params from :ref:`render_period` section for it.

To determine excel styles you need to use ``styles`` sub section.

.. note::

   Using ``styles`` subsection will be drop all default style settings.

   You can see default theme in ``linum/styles/xlsx_default_context.yaml`` file.

.. code-block:: yaml

   xlsx_renderer:
     start: 2020-06-01
     finish: 2020-07-01
     styles:
       font: Roboto
       cell_width_px: 30

For this example new font and cell width would be apply to all cells.

In ``styles`` section and all of it sub sections you may use params
which be determine later.

If you want to determine cell style in certain hierarchy place
you must use correspond subsections.
There is 3 sub sections for ``styles`` sections:

- ``header`` to determine header style;

- ``layers`` to determine layers styles;

- ``days_off`` sub section which include another ``header`` and ``layers``
  subsections, and need to determine cells in days-off positions.

.. code-block:: yaml

   xlsx_renderer:
     styles:
       header:
         # some header styles
       layers:
         # some layers styles

       days_off:
         header:
           # some header styles for days-off
         layers:
           # some layers styles for days-off

The ``header`` sections contain 3 sub sections:

- ``months`` sub section to determine months cell style;

- ``days`` sub section to determine days cell style;

- ``weekdays`` sub section to determine weekdays cell style.

.. code-block:: yaml

   xlsx_renderer:
     styles:
       header:
         months:
           # some months styles
         days:
           # some days styles
         weekdays:
           # some weekdays styles

       days_off:
         header:
           months:
             # some months styles for days-off
           days:
             # some days styles for days-off
           weekdays:
             # some weekdays styles for days-off

The ``layers`` sections contain 3 sub sections:

- ``space_row`` sub section to determine cells style between layers;

- ``space`` sub section to determine cells style between tasks in one layer;

- ``tasks`` sub section to determine tasks cell style.

.. code-block:: yaml

   xlsx_renderer:
     styles:
       layers:
         space_row:
           # some space row styles
         space:
           # some space styles
         tasks:
           # some tasks styles

       days_off:
         layers:
           space_row:
             # some space row styles for days-off
           space:
             # some space styles for days-off
           tasks:
             # some tasks styles for days-off

.. note:: For ``days-off`` section all sub sections will be inherit correspond properties
   from ``styles`` section.

For example:

.. code-block:: yaml

   xlsx_renderer:
     styles:
       header:
         days:
           bg_color: 0x00FF00  # Green color

       days_off:
         header:
           days:
             font_size: 16

all days-off would be green.


Cell size
=========

``cell_width_px``
-----------------

Sets cell width in pixels. Value must be integer.


``cell_height_px``
------------------

Sets cell height in pixels. Value must be integer.


Setting font
============

Example:

.. code-block:: yaml

   xlsx_renderer:
     styles:
       font_name: Roboto
       font_size: 16
       font_color: auto
       bold: False
       italic: True
       underline: True


``font_name``
-------------

Font to use. Value must be string with proper font name.


``font_size``
-------------

Font size. Value must be integer.


``font_color``
--------------

Font color. Value must be integer constant color
and ``auto`` for auto choosing between black and white color.


``bold``
--------

Bold for font. Must be ``True`` or ``False``


``italic``
----------

Italic for font. Must be ``True`` or ``False``


``underline``
-------------

Underline for font. Must be ``True`` or ``False``



Align
=====

Example:

.. code-block:: yaml

   xlsx_renderer:
     styles:
       align: center
       valign: top


``align``
---------

Horizontal cell aligning. Must be one of ``left``, ``right``, or ``center``.


``valign``
----------

Vertical cell aligning. Must be one of ``top``, ``vcenter``, or ``bottom``.


``bg_color``
============

Background color. Must be integer for constant color or ``Null`` for setting off color.

.. code-block:: yaml

   xlsx_renderer:
     styles:
       bg_color: 0x000000  # Black color


Blackout
========

Blackout is a changing color as mixing them with solid black with
``blackout_value`` percents opacity.
Blackout applies to background color and border colors.

Example:

.. code-block:: yaml

   xlsx_renderer:
     styles:
       use_blackout: True
       blackout_value: 0.12


``use_blackout``
----------------

Sets blackout for cell. Must be ``True`` or ``False``.


``blackout_value``
------------------

Blackout value in percents. Must be float value between 0.0 and 1.0.


.. _cell_borders:

Cell borders
============

A cell border is comprised of a border on the bottom, top, left and right.

The following shows the border styles:

+-------+---------------+--------+
| index | description   | weight |
+=======+===============+========+
|     0 | None          | 0      |
+-------+---------------+--------+
|     1 | Continuous    | 1      |
+-------+---------------+--------+
|     2 | Continuous    | 2      |
+-------+---------------+--------+
|     3 | Dash          | 1      |
+-------+---------------+--------+
|     4 | Dot           | 1      |
+-------+---------------+--------+
|     5 | Continuous    | 3      |
+-------+---------------+--------+
|     6 | Double        | 3      |
+-------+---------------+--------+
|     7 | Continuous    | 0      |
+-------+---------------+--------+
|     8 | Dash          | 2      |
+-------+---------------+--------+
|     9 | Dash Dot      | 1      |
+-------+---------------+--------+
|    10 | Dash Dot      | 2      |
+-------+---------------+--------+
|    11 | Dash Dot Dash | 1      |
+-------+---------------+--------+
|    12 | Dash Dot Dash | 2      |
+-------+---------------+--------+
|    13 | SlantDash Dot | 2      |
+-------+---------------+--------+

Use index integer value to set border, or ``Null`` to set off border style.

Example:

.. code-block:: yaml

   xlsx_renderer:
     styles:
       left: 0
       right: 1
       top: Null
       bottom: 10


``left``
--------

Left border style. See style values here: :ref:`cell_borders`.


``right``
---------
Right border style. See style values here: :ref:`cell_borders`.


``top``
-------
Top border style. See style values here: :ref:`cell_borders`.


``bottom``
----------
Bottom border style. See style values here: :ref:`cell_borders`.


.. _border_colors:

Border colors
=============

To set border color use integer values or ``blackout`` keyword.
In second case border color would be setted as cell background with blackout.

Example:

.. code-block:: yaml

   xlsx_renderer:
     styles:
       left_color: 0x000000  # Black color
       right_color: 0xFF0000  # Red color
       top_color: 0x0000FF  # Blue color
       bottom_color: blackout


``left_color``
--------------

Color for left border. See possible values here: :ref:`border_colors`.


``right_color``
---------------

Color for right border. See possible values here: :ref:`border_colors`.


``top_color``
-------------

Color for top border. See possible values here: :ref:`border_colors`.


``bottom_color``
----------------

Color for bottom border. See possible values here: :ref:`border_colors`.
