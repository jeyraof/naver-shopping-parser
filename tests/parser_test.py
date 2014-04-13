# -*- coding: utf-8 -*-
import os
import os.path

from shopping_parser import NaverShopping


def test_parse_html():
    import codecs
    html = codecs.open(os.path.join(os.path.dirname(__file__), 'assets', 'test_html.txt'), encoding='utf-8').read()

    r = NaverShopping.parse_html(html)
    data = r[0]
    assert data[0].name == '[스페리 탑사이더 초특가 SALE] 데저트 부츠 Boat Oxford Boot 다크탄 0297432 SPERRY 보트슈즈 로퍼'
    assert data[0].price == '96,260'
    assert data[0].thumb == 'http://shopping.phinf.naver.net/main_6725630/6725630529.jpg?type=f170'