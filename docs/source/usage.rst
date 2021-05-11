=====
Usage
=====

There are two ways to use Linum.
First - via console, and second - via API.

For generating output file it requires to create input file with tasks.
You may read `here <creating_tasks.html>`_ how to do it.

Also to control render settings you need to create context file.
Read `Creating context <creating_context.html>`_ for more information.


************
Installation
************

Install Linum via ``pip``:

.. code-block:: bash

   $ pip install linum


*************
Console usage
*************

After installation ``linum`` command becomes available.
Here is the latest help info::

   $ linum --help
   Usage: linum [OPTIONS] TASKS_PATH

   Command line interface for linum.

   Options:
     -o, --out PATH                  Output file. If not specified then linum creates
                                     new file in current directory.
     -r, --renderer [CONSOLE|TXT|XLSX]
                                     Renderer to use. 'CONSOLE' - for console
                                     printing. 'TXT' - for rendering txt file.
                                     'XLSX' - for rendering xlsx file. Default
                                     is 'CONSOLE'.

     -c, --context PATH              Context for renderer. It is a YAML file
                                     with render settings.

     --help                          Show this message and exit. If not
                                     specified then default settings will be
                                     applied.


*************
Using via api
*************

Linum provides public render classes to generate schedule.
There is one renderer for every output format.

To use them in simple way you must specify path to yaml tasks file,
and call ``.render()`` method. That`s all!

.. code-block:: python

   from linum import ExcelRenderer, TxtRenderer, ConsoleRenderer

   TASKS_PATH = 'path/to/tasks.yaml'

   # Console output
   cr = ConsoleRenderer(TASKS_PATH)
   cr.render()

   # Txt output
   tr = TxtRenderer(TASKS_PATH)
   tr.render()

   # Xlsx output
   er = ExcelRenderer(TASKS_PATH)
   er.render()


If you have your yaml context file, provide valid path to it after task path.

.. code-block:: python

   from linum import ExcelRenderer, TxtRenderer, ConsoleRenderer

   TASKS_PATH = 'path/to/tasks.yaml'
   CONTEXT_PATH = 'path/to/context.yaml'

   # Xlsx output
   er = ExcelRenderer(TASKS_PATH, CONTEXT_PATH)
   er.render()


As an option you may specify output file name.

.. code-block:: python

   from linum import ExcelRenderer, TxtRenderer, ConsoleRenderer

   TASKS_PATH = 'path/to/tasks.yaml'
   CONTEXT_PATH = 'path/to/context.yaml'
   XLSX_OUT_PATH = 'path/to/new/xlsx/file.xlsx'

   # Xlsx output
   er = ExcelRenderer(TASKS_PATH, CONTEXT_PATH, XLSX_OUT_PATH)
   er.render()