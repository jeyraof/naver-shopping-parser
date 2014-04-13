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
    $ ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install git+https://github.com/jeyraof/naver-shopping-parser.git

instead of,

.. code-block:: console

    $ python setup.py install
    $ pip install git+https://github.com/jeyraof/naver-shopping-parser.git

To solve this error nicely, first of all, you can install lxml clearly.



Usage
-----

.. code-block:: python

    >>> from shopping_parser import NaverShopping, Condition
    >>>
    >>> c = Condition(sort='price_asc', ea=10)
    >>> n = NaverShopping(condition=c)
    >>>
    >>> data = n.search_by('sperry 0297432')
    >>> data
    [<shopping_parser.parser.Item object at 0x1041ca350>, <shopping_parser.parser.Item object at 0x1041ca0d0>, <shopping_parser.parser.Item object at 0x1041ca390>, <shopping_parser.parser.Item object at 0x1041ca190>, <shopping_parser.parser.Item object at 0x1041ca290>, <shopping_parser.parser.Item object at 0x1041ca2d0>, <shopping_parser.parser.Item object at 0x1041ca210>, <shopping_parser.parser.Item object at 0x1041ca150>, <shopping_parser.parser.Item object at 0x1041ca110>, <shopping_parser.parser.Item object at 0x1041ca3d0>]
    >>> data[0]
    <shopping_parser.parser.Item object at 0x1041ca350>
    >>> print data[0]
    <[스페리 탑사이더 초특가 SALE] 데저트 부츠 Boat Oxford Boot 다크탄 0297432 SPERRY 보트슈즈 로퍼 - 96,260>
    >>> print data[0].name
    [스페리 탑사이더 초특가 SALE] 데저트 부츠 Boat Oxford Boot 다크탄 0297432 SPERRY 보트슈즈 로퍼
    >>> print data[0].price
    96,260
    >>> print data[0].thumb
    http://shopping.phinf.naver.net/main_6725630/6725630529.jpg?type=f170
    >>>
    >>> data2 = n.next()
    >>> print data2[0]
    <[스페리 탑사이더 초특가 SALE] 데저트 부츠 Boat Oxford Boot 다크탄 0297432 SPERRY 보트슈즈 로퍼 - 109,500>