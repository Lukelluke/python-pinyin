#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from itertools import chain

import pytest

from pypinyin import (
    lazy_pinyin, pinyin, NORMAL, TONE, TONE2, TONE3, INITIALS,
    FIRST_LETTER, FINALS, FINALS_TONE, FINALS_TONE2, FINALS_TONE3
)

# test data from http://www.moe.edu.cn/s78/A19/yxs_left/moe_810/s230/195802/t19580201_186000.html  # noqa
# 声母表
data_for_initials = [
    ['玻', dict(style=INITIALS), ['b']],
    ['坡', dict(style=INITIALS), ['p']],
    ['摸', dict(style=INITIALS), ['m']],
    ['佛', dict(style=INITIALS), ['f']],
    ['得', dict(style=INITIALS), ['d']],
    ['特', dict(style=INITIALS), ['t']],
    ['讷', dict(style=INITIALS), ['n']],
    ['勒', dict(style=INITIALS), ['l']],
    ['哥', dict(style=INITIALS), ['g']],
    ['科', dict(style=INITIALS), ['k']],
    ['喝', dict(style=INITIALS), ['h']],
    ['基', dict(style=INITIALS), ['j']],
    ['欺', dict(style=INITIALS), ['q']],
    ['希', dict(style=INITIALS), ['x']],
    ['知', dict(style=INITIALS), ['zh']],
    ['蚩', dict(style=INITIALS), ['ch']],
    ['诗', dict(style=INITIALS), ['sh']],
    ['日', dict(style=INITIALS), ['r']],
    ['资', dict(style=INITIALS), ['z']],
    ['雌', dict(style=INITIALS), ['c']],
    ['思', dict(style=INITIALS), ['s']],
]


@pytest.mark.parametrize('hans, kwargs, result', data_for_initials)
def test_initials(hans, kwargs, result):
    assert lazy_pinyin(hans, **kwargs) == result
    assert list(chain(*pinyin(hans, **kwargs))) == result


# 韵母表
data_for_finals = [
    ['衣', dict(style=FINALS), ['i']],
    ['乌', dict(style=FINALS), ['u']],
    ['迂', dict(style=FINALS), ['v']],
    ['啊', dict(style=FINALS), ['a']],
    ['呀', dict(style=FINALS), ['ia']],
    ['蛙', dict(style=FINALS), ['ua']],
    ['喔', dict(style=FINALS), ['o']],
    ['窝', dict(style=FINALS), ['uo']],
    ['鹅', dict(style=FINALS), ['e']],
    ['耶', dict(style=FINALS), ['ie']],
    ['约', dict(style=FINALS), ['ve']],
    ['哀', dict(style=FINALS), ['ai']],
    ['歪', dict(style=FINALS), ['uai']],
    # ['欸', dict(style=FINALS), ['ei']],
    ['诶', dict(style=FINALS), ['ei']],
    ['威', dict(style=FINALS), ['uei']],
    ['熬', dict(style=FINALS), ['ao']],
    ['腰', dict(style=FINALS), ['iao']],
    ['欧', dict(style=FINALS), ['ou']],
    ['忧', dict(style=FINALS), ['iou']],
    ['安', dict(style=FINALS), ['an']],
    ['烟', dict(style=FINALS), ['ian']],
    ['弯', dict(style=FINALS), ['uan']],
    ['冤', dict(style=FINALS), ['van']],
    ['恩', dict(style=FINALS), ['en']],
    ['因', dict(style=FINALS), ['in']],
    ['温', dict(style=FINALS), ['uen']],
    ['晕', dict(style=FINALS), ['vn']],
    ['昂', dict(style=FINALS), ['ang']],
    ['央', dict(style=FINALS), ['iang']],
    ['汪', dict(style=FINALS), ['uang']],
    ['亨', dict(style=FINALS), ['eng']],
    ['英', dict(style=FINALS), ['ing']],
    ['翁', dict(style=FINALS), ['ueng']],
    ['轰', dict(style=FINALS), ['ong']],
    ['雍', dict(style=FINALS), ['iong']],
    ['儿', dict(style=FINALS), ['er']],
]


@pytest.mark.parametrize('hans, kwargs, result', data_for_finals)
def test_finals(hans, kwargs, result):
    assert lazy_pinyin(hans, **kwargs) == result
    assert pinyin(hans, **kwargs) == [result]


# 零声母
data_for_zero_consonant = [
    # i行的韵母，前面没有声母的时候，写成yi(衣)，ya(呀)，ye(耶)，yao(腰)，
    # you(忧)，yan(烟)，yin(因)，yang(央)，ying(英)，yong(雍)。

    ['衣', dict(style=NORMAL), ['yi']],
    ['衣', dict(style=FINALS), ['i']],
    ['衣', dict(style=FINALS, strict=False), ['i']],
    ['呀', dict(style=NORMAL), ['ya']],
    ['呀', dict(style=FINALS), ['ia']],
    ['呀', dict(style=FINALS, strict=False), ['a']],
    ['耶', dict(style=NORMAL), ['ye']],
    ['耶', dict(style=FINALS), ['ie']],
    ['耶', dict(style=FINALS, strict=False), ['e']],
    ['腰', dict(style=NORMAL), ['yao']],
    ['腰', dict(style=FINALS), ['iao']],
    ['腰', dict(style=FINALS, strict=False), ['ao']],
    ['忧', dict(style=NORMAL), ['you']],
    ['忧', dict(style=FINALS), ['iou']],
    ['忧', dict(style=FINALS, strict=False), ['ou']],
    ['烟', dict(style=NORMAL), ['yan']],
    ['烟', dict(style=FINALS), ['ian']],
    ['烟', dict(style=FINALS, strict=False), ['an']],
    ['因', dict(style=NORMAL), ['yin']],
    ['因', dict(style=FINALS), ['in']],
    ['因', dict(style=FINALS, strict=False), ['in']],
    ['央', dict(style=NORMAL), ['yang']],
    ['央', dict(style=FINALS), ['iang']],
    ['央', dict(style=FINALS, strict=False), ['ang']],
    ['英', dict(style=NORMAL), ['ying']],
    ['英', dict(style=FINALS), ['ing']],
    ['英', dict(style=FINALS, strict=False), ['ing']],
    ['雍', dict(style=NORMAL), ['yong']],
    ['雍', dict(style=FINALS), ['iong']],
    ['雍', dict(style=FINALS, strict=False), ['ong']],

    ['宜', dict(style=NORMAL), ['yi']],
    ['宜', dict(style=NORMAL, strict=False), ['yi']],
    ['宜', dict(style=TONE), ['yí']],
    ['宜', dict(style=TONE, strict=False), ['yí']],
    ['宜', dict(style=TONE2), ['yi2']],
    ['宜', dict(style=TONE2, strict=False), ['yi2']],
    ['宜', dict(style=TONE3), ['yi2']],
    ['宜', dict(style=TONE3, strict=False), ['yi2']],
    ['宜', dict(style=INITIALS), ['']],
    ['宜', dict(style=INITIALS, strict=False), ['y']],
    ['宜', dict(style=FIRST_LETTER), ['y']],
    ['宜', dict(style=FIRST_LETTER, strict=False), ['y']],
    ['宜', dict(style=FINALS), ['i']],
    ['宜', dict(style=FINALS, strict=False), ['i']],
    ['宜', dict(style=FINALS_TONE), ['í']],
    ['宜', dict(style=FINALS_TONE, strict=False), ['í']],
    ['宜', dict(style=FINALS_TONE2), ['i2']],
    ['宜', dict(style=FINALS_TONE2, strict=False), ['i2']],
    ['宜', dict(style=FINALS_TONE3), ['i2']],
    ['宜', dict(style=FINALS_TONE3, strict=False), ['i2']],

    ['盐', dict(style=NORMAL), ['yan']],
    ['盐', dict(style=NORMAL, strict=False), ['yan']],
    ['盐', dict(style=TONE), ['yán']],
    ['盐', dict(style=TONE, strict=False), ['yán']],
    ['盐', dict(style=TONE2), ['ya2n']],
    ['盐', dict(style=TONE2, strict=False), ['ya2n']],
    ['盐', dict(style=TONE3), ['yan2']],
    ['盐', dict(style=TONE3, strict=False), ['yan2']],
    ['盐', dict(style=INITIALS), ['']],
    ['盐', dict(style=INITIALS, strict=False), ['y']],
    ['盐', dict(style=FIRST_LETTER), ['y']],
    ['盐', dict(style=FIRST_LETTER, strict=False), ['y']],
    ['盐', dict(style=FINALS), ['ian']],
    ['盐', dict(style=FINALS, strict=False), ['an']],
    ['盐', dict(style=FINALS_TONE), ['ián']],
    ['盐', dict(style=FINALS_TONE, strict=False), ['án']],
    ['盐', dict(style=FINALS_TONE2), ['ia2n']],
    ['盐', dict(style=FINALS_TONE2, strict=False), ['a2n']],
    ['盐', dict(style=FINALS_TONE3), ['ian2']],
    ['盐', dict(style=FINALS_TONE3, strict=False), ['an2']],


    # u行的韵母，前面没有声母的时候，写成wu(乌)，wa(蛙)，wo(窝)，wai(歪)，
    # wei(威)，wan(弯)，wen(温)，wang(汪)，weng(翁)。
    ['乌', dict(style=NORMAL), ['wu']],
    ['乌', dict(style=FINALS), ['u']],
    ['乌', dict(style=FINALS, strict=False), ['u']],
    ['蛙', dict(style=NORMAL), ['wa']],
    ['蛙', dict(style=FINALS), ['ua']],
    ['蛙', dict(style=FINALS, strict=False), ['a']],
    ['窝', dict(style=NORMAL), ['wo']],
    ['窝', dict(style=FINALS), ['uo']],
    ['窝', dict(style=FINALS, strict=False), ['o']],
    ['歪', dict(style=NORMAL), ['wai']],
    ['歪', dict(style=FINALS), ['uai']],
    ['歪', dict(style=FINALS, strict=False), ['ai']],
    ['威', dict(style=NORMAL), ['wei']],
    ['威', dict(style=FINALS), ['uei']],
    ['威', dict(style=FINALS, strict=False), ['ei']],
    ['弯', dict(style=NORMAL), ['wan']],
    ['弯', dict(style=FINALS), ['uan']],
    ['弯', dict(style=FINALS, strict=False), ['an']],
    ['温', dict(style=NORMAL), ['wen']],
    ['温', dict(style=FINALS), ['uen']],
    ['温', dict(style=FINALS, strict=False), ['en']],
    ['汪', dict(style=NORMAL), ['wang']],
    ['汪', dict(style=FINALS), ['uang']],
    ['汪', dict(style=FINALS, strict=False), ['ang']],
    ['翁', dict(style=NORMAL), ['weng']],
    ['翁', dict(style=FINALS), ['ueng']],
    ['翁', dict(style=FINALS, strict=False), ['eng']],

    ['武', dict(style=NORMAL), ['wu']],
    ['武', dict(style=NORMAL, strict=False), ['wu']],
    ['武', dict(style=TONE), ['wǔ']],
    ['武', dict(style=TONE, strict=False), ['wǔ']],
    ['武', dict(style=TONE2), ['wu3']],
    ['武', dict(style=TONE2, strict=False), ['wu3']],
    ['武', dict(style=TONE3), ['wu3']],
    ['武', dict(style=TONE3, strict=False), ['wu3']],
    ['武', dict(style=INITIALS), ['']],
    ['武', dict(style=INITIALS, strict=False), ['w']],
    ['武', dict(style=FIRST_LETTER), ['w']],
    ['武', dict(style=FIRST_LETTER, strict=False), ['w']],
    ['武', dict(style=FINALS), ['u']],
    ['武', dict(style=FINALS, strict=False), ['u']],
    ['武', dict(style=FINALS_TONE), ['ǔ']],
    ['武', dict(style=FINALS_TONE, strict=False), ['ǔ']],
    ['武', dict(style=FINALS_TONE2), ['u3']],
    ['武', dict(style=FINALS_TONE2, strict=False), ['u3']],
    ['武', dict(style=FINALS_TONE3), ['u3']],
    ['武', dict(style=FINALS_TONE3, strict=False), ['u3']],

    ['旺', dict(style=NORMAL), ['wang']],
    ['旺', dict(style=NORMAL, strict=False), ['wang']],
    ['旺', dict(style=TONE), ['wàng']],
    ['旺', dict(style=TONE, strict=False), ['wàng']],
    ['旺', dict(style=TONE2), ['wa4ng']],
    ['旺', dict(style=TONE2, strict=False), ['wa4ng']],
    ['旺', dict(style=TONE3), ['wang4']],
    ['旺', dict(style=TONE3, strict=False), ['wang4']],
    ['旺', dict(style=INITIALS), ['']],
    ['旺', dict(style=INITIALS, strict=False), ['w']],
    ['旺', dict(style=FIRST_LETTER), ['w']],
    ['旺', dict(style=FIRST_LETTER, strict=False), ['w']],
    ['旺', dict(style=FINALS), ['uang']],
    ['旺', dict(style=FINALS, strict=False), ['ang']],
    ['旺', dict(style=FINALS_TONE), ['uàng']],
    ['旺', dict(style=FINALS_TONE, strict=False), ['àng']],
    ['旺', dict(style=FINALS_TONE2), ['ua4ng']],
    ['旺', dict(style=FINALS_TONE2, strict=False), ['a4ng']],
    ['旺', dict(style=FINALS_TONE3), ['uang4']],
    ['旺', dict(style=FINALS_TONE3, strict=False), ['ang4']],


    # ü行的韵母，前面没有声母的时候，写成yu(迂)，yue(约)，yuan(冤)，
    ['迂', dict(style=NORMAL), ['yu']],
    ['迂', dict(style=FINALS), ['v']],
    ['迂', dict(style=FINALS, strict=False), ['u']],
    ['约', dict(style=NORMAL), ['yue']],
    ['约', dict(style=FINALS), ['ve']],
    ['约', dict(style=FINALS, strict=False), ['ue']],
    ['冤', dict(style=NORMAL), ['yuan']],
    ['冤', dict(style=FINALS), ['van']],
    ['冤', dict(style=FINALS, strict=False), ['uan']],

    ['鱼', dict(style=NORMAL), ['yu']],
    ['鱼', dict(style=NORMAL, strict=False), ['yu']],
    ['鱼', dict(style=TONE), ['yú']],
    ['鱼', dict(style=TONE, strict=False), ['yú']],
    ['鱼', dict(style=TONE2), ['yu2']],
    ['鱼', dict(style=TONE2, strict=False), ['yu2']],
    ['鱼', dict(style=TONE3), ['yu2']],
    ['鱼', dict(style=TONE3, strict=False), ['yu2']],
    ['鱼', dict(style=INITIALS), ['']],
    ['鱼', dict(style=INITIALS, strict=False), ['y']],
    ['鱼', dict(style=FIRST_LETTER), ['y']],
    ['鱼', dict(style=FIRST_LETTER, strict=False), ['y']],
    ['鱼', dict(style=FINALS), ['v']],
    ['鱼', dict(style=FINALS, strict=False), ['u']],
    ['鱼', dict(style=FINALS_TONE), ['ǘ']],
    ['鱼', dict(style=FINALS_TONE, strict=False), ['ú']],
    ['鱼', dict(style=FINALS_TONE2), ['v2']],
    ['鱼', dict(style=FINALS_TONE2, strict=False), ['u2']],
    ['鱼', dict(style=FINALS_TONE3), ['v2']],
    ['鱼', dict(style=FINALS_TONE3, strict=False), ['u2']],

    ['约', dict(style=NORMAL), ['yue']],
    ['约', dict(style=NORMAL, strict=False), ['yue']],
    ['约', dict(style=TONE), ['yuē']],
    ['约', dict(style=TONE, strict=False), ['yuē']],
    ['约', dict(style=TONE2), ['yue1']],
    ['约', dict(style=TONE2, strict=False), ['yue1']],
    ['约', dict(style=TONE3), ['yue1']],
    ['约', dict(style=TONE3, strict=False), ['yue1']],
    ['约', dict(style=INITIALS), ['']],
    ['约', dict(style=INITIALS, strict=False), ['y']],
    ['约', dict(style=FIRST_LETTER), ['y']],
    ['约', dict(style=FIRST_LETTER, strict=False), ['y']],
    ['约', dict(style=FINALS), ['ve']],
    ['约', dict(style=FINALS, strict=False), ['ue']],
    ['约', dict(style=FINALS_TONE), ['üē']],
    ['约', dict(style=FINALS_TONE, strict=False), ['uē']],
    ['约', dict(style=FINALS_TONE2), ['ve1']],
    ['约', dict(style=FINALS_TONE2, strict=False), ['ue1']],
    ['约', dict(style=FINALS_TONE3), ['ve1']],
    ['约', dict(style=FINALS_TONE3, strict=False), ['ue1']],

    ['元', dict(style=NORMAL), ['yuan']],
    ['元', dict(style=NORMAL, strict=False), ['yuan']],
    ['元', dict(style=TONE), ['yuán']],
    ['元', dict(style=TONE, strict=False), ['yuán']],
    ['元', dict(style=TONE2), ['yua2n']],
    ['元', dict(style=TONE2, strict=False), ['yua2n']],
    ['元', dict(style=TONE3), ['yuan2']],
    ['元', dict(style=TONE3, strict=False), ['yuan2']],
    ['元', dict(style=INITIALS), ['']],
    ['元', dict(style=INITIALS, strict=False), ['y']],
    ['元', dict(style=FIRST_LETTER), ['y']],
    ['元', dict(style=FIRST_LETTER, strict=False), ['y']],
    ['元', dict(style=FINALS), ['van']],
    ['元', dict(style=FINALS, strict=False), ['uan']],
    ['元', dict(style=FINALS_TONE), ['üán']],
    ['元', dict(style=FINALS_TONE, strict=False), ['uán']],
    ['元', dict(style=FINALS_TONE2), ['va2n']],
    ['元', dict(style=FINALS_TONE2, strict=False), ['ua2n']],
    ['元', dict(style=FINALS_TONE3), ['van2']],
    ['元', dict(style=FINALS_TONE3, strict=False), ['uan2']],

    # yun 不应该受 un -> uen 规则的影响
    ['晕', dict(style=NORMAL), ['yun']],
    ['晕', dict(style=NORMAL, strict=False), ['yun']],
    ['晕', dict(style=TONE), ['yūn']],
    ['晕', dict(style=TONE, strict=False), ['yūn']],
    ['晕', dict(style=TONE2), ['yu1n']],
    ['晕', dict(style=TONE2, strict=False), ['yu1n']],
    ['晕', dict(style=TONE3), ['yun1']],
    ['晕', dict(style=TONE3, strict=False), ['yun1']],
    ['晕', dict(style=INITIALS), ['']],
    ['晕', dict(style=INITIALS, strict=False), ['y']],
    ['晕', dict(style=FIRST_LETTER), ['y']],
    ['晕', dict(style=FIRST_LETTER, strict=False), ['y']],
    ['晕', dict(style=FINALS), ['vn']],
    ['晕', dict(style=FINALS, strict=False), ['un']],
    ['晕', dict(style=FINALS_TONE), ['ǖn']],
    ['晕', dict(style=FINALS_TONE, strict=False), ['ūn']],
    ['晕', dict(style=FINALS_TONE2), ['v1n']],
    ['晕', dict(style=FINALS_TONE2, strict=False), ['u1n']],
    ['晕', dict(style=FINALS_TONE3), ['vn1']],
    ['晕', dict(style=FINALS_TONE3, strict=False), ['un1']],
]


@pytest.mark.parametrize('hans, kwargs, result', data_for_zero_consonant)
def test_zero_consonant(hans, kwargs, result):
    assert lazy_pinyin(hans, **kwargs) == result
    assert pinyin(hans, **kwargs) == [result]


data_for_uv = [
    # ü行的韵跟声母j，q，x拼的时候，写成ju(居)，qu(区)，xu(虚)，
    # ü上两点也省略；但是跟声母n，l拼的时候，仍然写成nü(女)，lü(吕)。
    ['居', dict(style=NORMAL), ['ju']],
    ['居', dict(style=FINALS), ['v']],
    ['居', dict(style=FINALS, strict=False), ['u']],
    ['区', dict(style=NORMAL), ['qu']],
    ['区', dict(style=FINALS), ['v']],
    ['区', dict(style=FINALS, strict=False), ['u']],
    ['虚', dict(style=NORMAL), ['xu']],
    ['虚', dict(style=FINALS), ['v']],
    ['虚', dict(style=FINALS, strict=False), ['u']],
    ['女', dict(style=NORMAL), ['nv']],
    ['女', dict(style=FINALS), ['v']],
    ['女', dict(style=FINALS, strict=False), ['v']],
    ['吕', dict(style=NORMAL), ['lv']],
    ['吕', dict(style=FINALS), ['v']],
    ['吕', dict(style=FINALS, strict=False), ['v']],

    ['具', dict(style=NORMAL), ['ju']],
    ['具', dict(style=NORMAL, strict=False), ['ju']],
    ['具', dict(style=TONE), ['jù']],
    ['具', dict(style=TONE, strict=False), ['jù']],
    ['具', dict(style=TONE2), ['ju4']],
    ['具', dict(style=TONE2, strict=False), ['ju4']],
    ['具', dict(style=TONE3), ['ju4']],
    ['具', dict(style=TONE3, strict=False), ['ju4']],
    ['具', dict(style=INITIALS), ['j']],
    ['具', dict(style=INITIALS, strict=False), ['j']],
    ['具', dict(style=FIRST_LETTER), ['j']],
    ['具', dict(style=FIRST_LETTER, strict=False), ['j']],
    ['具', dict(style=FINALS), ['v']],
    ['具', dict(style=FINALS, strict=False), ['u']],
    ['具', dict(style=FINALS_TONE), ['ǜ']],
    ['具', dict(style=FINALS_TONE, strict=False), ['ù']],
    ['具', dict(style=FINALS_TONE2), ['v4']],
    ['具', dict(style=FINALS_TONE2, strict=False), ['u4']],
    ['具', dict(style=FINALS_TONE3), ['v4']],
    ['具', dict(style=FINALS_TONE3, strict=False), ['u4']],

    ['取', dict(style=NORMAL), ['qu']],
    ['取', dict(style=NORMAL, strict=False), ['qu']],
    ['取', dict(style=TONE), ['qǔ']],
    ['取', dict(style=TONE, strict=False), ['qǔ']],
    ['取', dict(style=TONE2), ['qu3']],
    ['取', dict(style=TONE2, strict=False), ['qu3']],
    ['取', dict(style=TONE3), ['qu3']],
    ['取', dict(style=TONE3, strict=False), ['qu3']],
    ['取', dict(style=INITIALS), ['q']],
    ['取', dict(style=INITIALS, strict=False), ['q']],
    ['取', dict(style=FIRST_LETTER), ['q']],
    ['取', dict(style=FIRST_LETTER, strict=False), ['q']],
    ['取', dict(style=FINALS), ['v']],
    ['取', dict(style=FINALS, strict=False), ['u']],
    ['取', dict(style=FINALS_TONE), ['ǚ']],
    ['取', dict(style=FINALS_TONE, strict=False), ['ǔ']],
    ['取', dict(style=FINALS_TONE2), ['v3']],
    ['取', dict(style=FINALS_TONE2, strict=False), ['u3']],
    ['取', dict(style=FINALS_TONE3), ['v3']],
    ['取', dict(style=FINALS_TONE3, strict=False), ['u3']],

    ['徐', dict(style=NORMAL), ['xu']],
    ['徐', dict(style=NORMAL, strict=False), ['xu']],
    ['徐', dict(style=TONE), ['xú']],
    ['徐', dict(style=TONE, strict=False), ['xú']],
    ['徐', dict(style=TONE2), ['xu2']],
    ['徐', dict(style=TONE2, strict=False), ['xu2']],
    ['徐', dict(style=TONE3), ['xu2']],
    ['徐', dict(style=TONE3, strict=False), ['xu2']],
    ['徐', dict(style=INITIALS), ['x']],
    ['徐', dict(style=INITIALS, strict=False), ['x']],
    ['徐', dict(style=FIRST_LETTER), ['x']],
    ['徐', dict(style=FIRST_LETTER, strict=False), ['x']],
    ['徐', dict(style=FINALS), ['v']],
    ['徐', dict(style=FINALS, strict=False), ['u']],
    ['徐', dict(style=FINALS_TONE), ['ǘ']],
    ['徐', dict(style=FINALS_TONE, strict=False), ['ú']],
    ['徐', dict(style=FINALS_TONE2), ['v2']],
    ['徐', dict(style=FINALS_TONE2, strict=False), ['u2']],
    ['徐', dict(style=FINALS_TONE3), ['v2']],
    ['徐', dict(style=FINALS_TONE3, strict=False), ['u2']],

    ['女', dict(style=NORMAL), ['nv']],
    ['女', dict(style=NORMAL, strict=False), ['nv']],
    ['女', dict(style=TONE), ['nǚ']],
    ['女', dict(style=TONE, strict=False), ['nǚ']],
    ['女', dict(style=TONE2), ['nv3']],
    ['女', dict(style=TONE2, strict=False), ['nv3']],
    ['女', dict(style=TONE3), ['nv3']],
    ['女', dict(style=TONE3, strict=False), ['nv3']],
    ['女', dict(style=INITIALS), ['n']],
    ['女', dict(style=INITIALS, strict=False), ['n']],
    ['女', dict(style=FIRST_LETTER), ['n']],
    ['女', dict(style=FIRST_LETTER, strict=False), ['n']],
    ['女', dict(style=FINALS), ['v']],
    ['女', dict(style=FINALS, strict=False), ['v']],
    ['女', dict(style=FINALS_TONE), ['ǚ']],
    ['女', dict(style=FINALS_TONE, strict=False), ['ǚ']],
    ['女', dict(style=FINALS_TONE2), ['v3']],
    ['女', dict(style=FINALS_TONE2, strict=False), ['v3']],
    ['女', dict(style=FINALS_TONE3), ['v3']],
    ['女', dict(style=FINALS_TONE3, strict=False), ['v3']],

    ['吕', dict(style=NORMAL), ['lv']],
    ['吕', dict(style=NORMAL, strict=False), ['lv']],
    ['吕', dict(style=TONE), ['lǚ']],
    ['吕', dict(style=TONE, strict=False), ['lǚ']],
    ['吕', dict(style=TONE2), ['lv3']],
    ['吕', dict(style=TONE2, strict=False), ['lv3']],
    ['吕', dict(style=TONE3), ['lv3']],
    ['吕', dict(style=TONE3, strict=False), ['lv3']],
    ['吕', dict(style=INITIALS), ['l']],
    ['吕', dict(style=INITIALS, strict=False), ['l']],
    ['吕', dict(style=FIRST_LETTER), ['l']],
    ['吕', dict(style=FIRST_LETTER, strict=False), ['l']],
    ['吕', dict(style=FINALS), ['v']],
    ['吕', dict(style=FINALS, strict=False), ['v']],
    ['吕', dict(style=FINALS_TONE), ['ǚ']],
    ['吕', dict(style=FINALS_TONE, strict=False), ['ǚ']],
    ['吕', dict(style=FINALS_TONE2), ['v3']],
    ['吕', dict(style=FINALS_TONE2, strict=False), ['v3']],
    ['吕', dict(style=FINALS_TONE3), ['v3']],
    ['吕', dict(style=FINALS_TONE3, strict=False), ['v3']],
]


@pytest.mark.parametrize('hans, kwargs, result', data_for_uv)
def test_uv(hans, kwargs, result):
    assert lazy_pinyin(hans, **kwargs) == result
    assert pinyin(hans, **kwargs) == [result]


data_for_iou = [
    # iou，uei，uen前面加声母的时候，写成iu，ui，un。
    # 例如niu(牛)，gui(归)，lun(论)。
    ['牛', dict(style=NORMAL), ['niu']],
    ['牛', dict(style=FINALS), ['iou']],
    ['牛', dict(style=FINALS, strict=False), ['iu']],
    ['归', dict(style=NORMAL), ['gui']],
    ['归', dict(style=FINALS), ['uei']],
    ['归', dict(style=FINALS, strict=False), ['ui']],
    ['论', dict(style=NORMAL), ['lun']],
    ['论', dict(style=FINALS), ['uen']],
    ['论', dict(style=FINALS, strict=False), ['un']],

    ['牛', dict(style=NORMAL), ['niu']],
    ['牛', dict(style=NORMAL, strict=False), ['niu']],
    ['牛', dict(style=TONE), ['niú']],
    ['牛', dict(style=TONE, strict=False), ['niú']],
    ['牛', dict(style=TONE2), ['niu2']],
    ['牛', dict(style=TONE2, strict=False), ['niu2']],
    ['牛', dict(style=TONE3), ['niu2']],
    ['牛', dict(style=TONE3, strict=False), ['niu2']],
    ['牛', dict(style=INITIALS), ['n']],
    ['牛', dict(style=INITIALS, strict=False), ['n']],
    ['牛', dict(style=FIRST_LETTER), ['n']],
    ['牛', dict(style=FIRST_LETTER, strict=False), ['n']],
    ['牛', dict(style=FINALS), ['iou']],
    ['牛', dict(style=FINALS, strict=False), ['iu']],
    ['牛', dict(style=FINALS_TONE), ['ioú']],
    ['牛', dict(style=FINALS_TONE, strict=False), ['iú']],
    ['牛', dict(style=FINALS_TONE2), ['iou2']],
    ['牛', dict(style=FINALS_TONE2, strict=False), ['iu2']],
    ['牛', dict(style=FINALS_TONE3), ['iou2']],
    ['牛', dict(style=FINALS_TONE3, strict=False), ['iu2']],
]


@pytest.mark.parametrize('hans, kwargs, result', data_for_iou)
def test_iou(hans, kwargs, result):
    assert lazy_pinyin(hans, **kwargs) == result
    assert pinyin(hans, **kwargs) == [result]


data_for_uei = [
    # iou，uei，uen前面加声母的时候，写成iu，ui，un。
    # 例如niu(牛)，gui(归)，lun(论)。
    ['鬼', dict(style=NORMAL), ['gui']],
    ['鬼', dict(style=NORMAL, strict=False), ['gui']],
    ['鬼', dict(style=TONE), ['guǐ']],
    ['鬼', dict(style=TONE, strict=False), ['guǐ']],
    ['鬼', dict(style=TONE2), ['gui3']],
    ['鬼', dict(style=TONE2, strict=False), ['gui3']],
    ['鬼', dict(style=TONE3), ['gui3']],
    ['鬼', dict(style=TONE3, strict=False), ['gui3']],
    ['鬼', dict(style=INITIALS), ['g']],
    ['鬼', dict(style=INITIALS, strict=False), ['g']],
    ['鬼', dict(style=FIRST_LETTER), ['g']],
    ['鬼', dict(style=FIRST_LETTER, strict=False), ['g']],
    ['鬼', dict(style=FINALS), ['uei']],
    ['鬼', dict(style=FINALS, strict=False), ['ui']],
    ['鬼', dict(style=FINALS_TONE), ['ueǐ']],
    ['鬼', dict(style=FINALS_TONE, strict=False), ['uǐ']],
    ['鬼', dict(style=FINALS_TONE2), ['uei3']],
    ['鬼', dict(style=FINALS_TONE2, strict=False), ['ui3']],
    ['鬼', dict(style=FINALS_TONE3), ['uei3']],
    ['鬼', dict(style=FINALS_TONE3, strict=False), ['ui3']],
]


@pytest.mark.parametrize('hans, kwargs, result', data_for_uei)
def test_uei(hans, kwargs, result):
    assert lazy_pinyin(hans, **kwargs) == result
    assert pinyin(hans, **kwargs) == [result]


data_for_uen = [
    # iou，uei，uen前面加声母的时候，写成iu，ui，un。
    # 例如niu(牛)，gui(归)，lun(论)。
    ['论', dict(style=NORMAL), ['lun']],
    ['论', dict(style=TONE), ['lùn']],
    ['论', dict(style=TONE, strict=False), ['lùn']],
    ['论', dict(style=TONE2), ['lu4n']],
    ['论', dict(style=TONE2, strict=False), ['lu4n']],
    ['论', dict(style=TONE3), ['lun4']],
    ['论', dict(style=TONE3, strict=False), ['lun4']],
    ['论', dict(style=INITIALS), ['l']],
    ['论', dict(style=INITIALS, strict=False), ['l']],
    ['论', dict(style=FIRST_LETTER), ['l']],
    ['论', dict(style=FIRST_LETTER, strict=False), ['l']],
    ['论', dict(style=FINALS), ['uen']],
    ['论', dict(style=FINALS, strict=False), ['un']],
    ['论', dict(style=FINALS_TONE), ['ùen']],
    ['论', dict(style=FINALS_TONE, strict=False), ['ùn']],
    ['论', dict(style=FINALS_TONE2), ['u4en']],
    ['论', dict(style=FINALS_TONE2, strict=False), ['u4n']],
    ['论', dict(style=FINALS_TONE3), ['uen4']],
    ['论', dict(style=FINALS_TONE3, strict=False), ['un4']],
]


@pytest.mark.parametrize('hans, kwargs, result', data_for_uen)
def test_uen(hans, kwargs, result):
    assert lazy_pinyin(hans, **kwargs) == result
    assert pinyin(hans, **kwargs) == [result]


if __name__ == '__main__':
    import pytest
    pytest.cmdline.main()
