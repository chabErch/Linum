=============
Xlsx renderer
=============

``xlsx`` section overrides period settings and specifies
styles for excel render.

You may override period settings specially for xlsx renderer.
Use params from :ref:`render_period` section for it. For example:

.. code-block:: yaml

   xlsx:
     start: 2020-06-01
     finish: 2020-07-01

To determine excel styles you need to use ``styles`` sub section.

.. note::

   Using ``styles`` subsection drops all default style settings.

   You can see default theme in ``linum/styles/xlsx/xlsx_default_context.yaml`` file.

.. code-block:: yaml

   xlsx:
     styles:
       font: Roboto
       cell_width_px: 30

For this example new font and cell width would be applied to all cells.

In ``styles`` section and all of it sub sections you may use params.
Details of using this params will be provided :ref:`later <cell_size>`.

If you want to determine cell style in certain hierarchy place
you must use correspond sub sections.
There is 3 sub sections for ``styles`` section:

- ``header`` to determine header style;

- ``layers`` to determine layers styles;

- ``days_off`` sub section includes ``header`` and ``layers`` subsections,
  and need to determine cell styles in days-off positions.

.. code-block:: yaml

   xlsx:
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

   xlsx:
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

   xlsx:
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

.. note:: For ``days-off`` section all sub sections inherit matching properties
   from ``styles`` section.

For example:

.. code-block:: yaml

   xlsx:
     styles:
       header:
         days:
           bg_color: 0x00FF00  # Green color

       days_off:
         header:
           days:
             font_size: 16

all days-off will be green.


.. _cell_size:

*********
Cell size
*********

``cell_width_px``
=================

Sets cell width in pixels. Value must be integer.


``cell_height_px``
==================

Sets cell height in pixels. Value must be integer.


************
Setting font
************

Example:

.. code-block:: yaml

   xlsx:
     styles:
       font_name: Roboto
       font_size: 16
       font_color: auto
       bold: False
       italic: True
       underline: True


``font_name``
=============

Font to use. Value must be string with proper font name.


``font_size``
=============


Font size. Value must be integer.


``font_color``
==============

Font color. Value must be integer constant color
or ``auto`` for auto choosing between black and white color.
In second case color choose depends on background contrast.


``bold``
========

Sets font bold. Must be ``True`` or ``False``


``italic``
==========

Sets font italic. Must be ``True`` or ``False``


``underline``
=============

Sets font underline. Must be ``True`` or ``False``



*****
Align
*****

Example:

.. code-block:: yaml

   xlsx:
     styles:
       align: center
       valign: top


``align``
=========

Horizontal cell aligning. Must be one of ``left``, ``right``, or ``center``.


``valign``
==========

Vertical cell aligning. Must be one of ``top``, ``vcenter``, or ``bottom``.


************
``bg_color``
************

Background color. Must be integer for constant color or ``Null`` for setting off color.

.. code-block:: yaml

   xlsx:
     styles:
       bg_color: 0x000000  # Black color


********
Blackout
********

Blackout is changing color mixing it with solid black with
``blackout_value`` percents opacity.
Blackout changes background color and border colors.

Example:

.. code-block:: yaml

   xlsx:
     styles:
       use_blackout: True
       blackout_value: 0.12


``use_blackout``
================

Sets blackout for cell. Must be ``True`` or ``False``.


``blackout_value``
==================

Blackout value. Value must be in percents (float value between 0.0 and 1.0).


.. _cell_borders:

************
Cell borders
************

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

Use index integer value to set border, or ``Null`` to deactivate border style.

Example:

.. code-block:: yaml

   xlsx:
     styles:
       left: 0
       right: 1
       top: Null
       bottom: 10


``left``
========

Left border style. See style values here: :ref:`cell_borders`.


``right``
=========

Right border style. See style values here: :ref:`cell_borders`.


``top``
=======

Top border style. See style values here: :ref:`cell_borders`.


``bottom``
==========

Bottom border style. See style values here: :ref:`cell_borders`.


.. _border_colors:

*************
Border colors
*************

To set border color use hex rgb integer values or ``blackout`` keyword.
In second case border color is equal cell background color with blackout.

Example:

.. code-block:: yaml

   xlsx:
     styles:
       left_color: 0x000000  # Black color
       right_color: 0xFF0000  # Red color
       top_color: 0x0000FF  # Blue color
       bottom_color: blackout


``left_color``
==============

Color for left border. See possible values here: :ref:`border_colors`.


``right_color``
===============

Color for right border. See possible values here: :ref:`border_colors`.


``top_color``
=============

Color for top border. See possible values here: :ref:`border_colors`.


``bottom_color``
================

Color for bottom border. See possible values here: :ref:`border_colors`.
