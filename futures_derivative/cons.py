#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2021/8/20 16:13
Desc: 期货衍生指标配置文件
西本新干线-指数数据
"""
# xgx
symbol_dict = {
    '钢材指数': '65',
    '铁矿指数': '61',
    '焦炭指数': '64',
    '煤炭指数': '1002',
    '水泥指数': '1003',
    'FTZ指数': '1100',
    '钢铁行业PMI指数': '118',
    '生产指数': '119',
    '新订单指数': '120',
    '新出口订单指数': '121',
    '产成品库存指数': '122',
    '原材料库存指数': '123',
    '沪市终端线螺每周采购量监控': '74',
    '沪螺纹钢社会库存': '72',
    '国内螺纹钢社会库存量': '67',
    '国内线材社会库存量': '68',
    '国内主要城市热轧卷板库存': '69',
    '国内主要城市冷轧卷板库存': '70',
    '国内主要城市中厚板库存': '73',
    '全国主要钢材品种库存总量': '117',
    '热轧价格走势': '108',
    '冷轧价格走势': '109',
    '中板价格走势': '110',
    '型材价格走势': '111',
    '沪二级螺纹钢价格走势': '127',
    '螺纹钢主力合约收盘价格': '179',
    '铁矿石主力合约收盘价格': '180',
    '热轧板卷主力合约收盘价格': '181',
    '焦煤主力合约收盘价格': '182',
    '焦炭主力合约收盘价格': '183',
    '存款基准利率': '52',
    '贷款基准利率': '53',
    '存款准备金率': '105',
    '人民币新增贷款（亿元）': '174',
    '广义货币供应量增速（M2，%）': '175',
    '狭义货币供应量增速（M1，%)': '176',
    '上海大额银行承兑汇票(Ⅰ)': '129',
    '上海大额银行承兑汇票(Ⅱ)': '130',
    '上海大额银行承兑汇票(Ⅲ)': '131',
    '上海大额商业承兑汇票(Ⅰ)': '132',
    '上海大额商业承兑汇票(II)': '133',
    '上海大额商业承兑汇票(III)': '134',
    '重点企业粗钢日均产量（旬报）': '99',
    '重点企业钢材库存量（旬报）': '124',
    '国内月度粗钢日均产量': '159',
    '国内月度粗钢产量': '35',
    '国内月度钢材产量': '88',
    '国内月度螺纹钢产量': '40',
    '国内月度线材产量': '41',
    '国内月度热轧板卷产量': '114',
    '国内月度冷轧板卷产量': '115',
    '国内月度中厚板产量': '116',
    '国内月度生铁产量': '177',
    '国内月度焦炭产量': '37',
    '国内月度铁矿石原矿产量': '36',
    '国内月度铁矿石进口量': '42',
    '国内月度钢材出口量': '38',
    '国内月度钢材进口量': '39',
    '国内铁矿石港口存量': '43',
    '唐山地区钢坯库存量': '161',
    '印度矿港口库存': '100',
    '波罗的海干散货指数（BDI）': '77',
    '废钢价格走势': '78',
    '钢坯价格走势': '79',
    '钢材成本指数': '178',
    '铁矿石进口月度均价': '93',
    '巴西图巴朗-北仑铁矿海运价': '94',
    '西澳-北仑铁矿海运价': '95',
    '澳大利亚粉矿价格（56.5%，日照港）': '1006',
    '澳大利亚粉矿价格(61.5%青岛港，元/吨）': '106',
    '巴西粉矿价格（ 65% 日照港，元/吨）': '107',
    '62%铁矿石指数': '125',
    '63.5%印度粉矿外盘报价': '126',
    '国民生产总值季度增速（GDP）': '166',
    '居民消费物价指数（CPI）': '30',
    '工业生产者出厂价格指数（PPI）': '165',
    '制造业采购经理指数（PMI）': '104',
    '月度建筑安装工程投资额': '91',
    '月度固定资产投资额': '32',
    '月度房地产建设投资额': '34',
    '城填固定资产投资增速（累计值，%）': '171',
    '房地产开发投资增速（累计值，%）': '167',
    '土地购置面积同比增速（累计值，%）': '168',
    '房屋新开工面积同比增速（累计值，%）': '169',
    '商品房销售面积同比增速（累计值，%）': '170',
    '钢铁业固定资产投资增速（累计值，%）': '172',
    'CRU全球': '80',
    'CRU长材': '81',
    'CRU扁平材': '82',
    'CRU北美': '83',
    'CRU欧洲': '84',
    'CRU亚洲': '85',
    '全球粗钢月度产量（万吨）': '162',
    '全球粗钢日均产量（万吨）': '163',
    '全球粗钢产能利用率（%）': '164'}

xgx_code_url = "http://www.96369.net/Other/ValidateCode.aspx"
xgx_main_url = "http://www.96369.net/indices/{}"
xgx_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "57",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "www.96369.net",
    "Origin": "http://www.96369.net",
    "Pragma": "no-cache",
    "Referer": "http://www.96369.net/indices/67",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}
xgx_short_headers = {
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "www.96369.net",
    "Pragma": "no-cache",
    "Referer": "http://www.96369.net/indices/67",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}
# csa
csa_params_url = "https://www.jiaoyifamen.com/tools/nav/spread"
csa_url_spread = "https://www.jiaoyifamen.com/tools/future/spread/free"
csa_url_ratio = "https://www.jiaoyifamen.com/tools/future/valence/free"
csa_url_customize = "https://www.jiaoyifamen.com/tools/future/customize"

csa_payload = {
    "type1": "RB",
    "code1": "01",
    "type2": "RB",
    "code2": "05"
}