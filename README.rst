Naver Shopping Parser
---------------------

Naver Shopping Parser is parser library for searching items on shopping.naver.com.
It use lxml for parsing HTML.

You can install the package following method.

PIP:

.. code-block:: console

    $ pip install git+https://github.com/jeyraof/naver-shopping-parser.git

or checkout `Github Repository`__:

.. code-block:: console

    $ git clone git://github.com/jeyraof/naver-shopping-parser.git
    $ cd naver-shopping-parser/
    $ python setup.py install

__ https://github.com/jeyraof/naver-shopping-parser

if you use OSX, following error could be attack you.

.. code-block:: console

    clang: error: unknown argument: '-mno-fused-madd' [-Wunused-command-line-argument-hard-error-in-future]

This error could be fixed by doing add flags forcely:

.. code-block:: console

    $ ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future python setup.py install

instead of,

.. code-block:: console

    $ python setup.py install

To solve this error nicely, first of all, you can install lxml clearly.