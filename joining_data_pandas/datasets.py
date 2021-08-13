import utils


social_fin_str = """             financial   company  year     value
0        total_revenue   twitter  2019   3459329
1      cost_of_revenue   twitter  2019   1137041
2         gross_profit   twitter  2019   2322288
3   operating_expenses   twitter  2019   1955915
4           net_income   twitter  2019   1465659
5        total_revenue  facebook  2019  70697000
6      cost_of_revenue  facebook  2019  12770000
7         gross_profit  facebook  2019  57927000
8   operating_expenses  facebook  2019  33941000
9           net_income  facebook  2019  18485000
10       total_revenue      snap  2019   1715534
11     cost_of_revenue      snap  2019    895838
12        gross_profit      snap  2019    819696
13  operating_expenses      snap  2019   1923024
14          net_income      snap  2019  -1033660
15       total_revenue   twitter  2018   3042359
16     cost_of_revenue   twitter  2018    964997
17        gross_profit   twitter  2018   2077362
18  operating_expenses   twitter  2018   1624037
19          net_income   twitter  2018   1205596
20       total_revenue  facebook  2018  55838000
21     cost_of_revenue  facebook  2018   9355000
22        gross_profit  facebook  2018  46483000
23  operating_expenses  facebook  2018  21570000
24          net_income  facebook  2018  22112000
25       total_revenue      snap  2018   1180446
26     cost_of_revenue      snap  2018    798865
27        gross_profit      snap  2018    381581
28  operating_expenses      snap  2018   1650031
29          net_income      snap  2018  -1255911
30       total_revenue   twitter  2017   2443299
31     cost_of_revenue   twitter  2017    861242
32        gross_profit   twitter  2017   1582057
33  operating_expenses   twitter  2017   1543317
34          net_income   twitter  2017   -108063
35       total_revenue  facebook  2017  40653000
36     cost_of_revenue  facebook  2017   5454000
37        gross_profit  facebook  2017  35199000
38  operating_expenses  facebook  2017  14996000
39          net_income  facebook  2017  15934000
40       total_revenue      snap  2017    824949
41     cost_of_revenue      snap  2017    717462
42        gross_profit      snap  2017    107487
43  operating_expenses      snap  2017   3593063
44          net_income      snap  2017  -3445066
45       total_revenue   twitter  2016   2529619
46     cost_of_revenue   twitter  2016    932240
47        gross_profit   twitter  2016   1597379
48  operating_expenses   twitter  2016   1964587
49          net_income   twitter  2016   -456873
50       total_revenue  facebook  2016  27638000
51     cost_of_revenue  facebook  2016   3789000
52        gross_profit  facebook  2016  23849000
53  operating_expenses  facebook  2016  11422000
54          net_income  facebook  2soc016  10217000
55       total_revenue      snap  2016    404482
56     cost_of_revenue      snap  2016    451660
57        gross_profit      snap  2016    -47178
58  operating_expenses      snap  2016    473207
59          net_income      snap  2016   -514643"""

social_fin = utils.social_fin_extractor(social_fin_str)


inflation_str = """  country    indicator  2017  2018  2019
0  Brazil  Inflation %  3.45  3.66  3.73
1  Canada  Inflation %  1.60  2.27  1.95
2  France  Inflation %  1.03  1.85  1.11
3   India  Inflation %  2.49  4.86  7.66"""

inflation = utils.inflation_extractor(inflation_str)

gov_data_str = """    year  jan  feb  mar  apr  may  jun  jul  aug  sep  oct  nov  dec
0   2010  9.8  9.8  9.9  9.9  9.6  9.4  9.4  9.5  9.5  9.4  9.8  9.3
1   2011  9.1  9.0  9.0  9.1  9.0  9.1  9.0  9.0  9.0  8.8  8.6  8.5
2   2012  8.3  8.3  8.2  8.2  8.2  8.2  8.2  8.1  7.8  7.8  7.7  7.9
3   2013  8.0  7.7  7.5  7.6  7.5  7.5  7.3  7.2  7.2  7.2  6.9  6.7
4   2014  6.6  6.7  6.7  6.2  6.3  6.1  6.2  6.1  5.9  5.7  5.8  5.6
5   2015  5.7  5.5  5.4  5.4  5.6  5.3  5.2  5.1  5.0  5.0  5.1  5.0
6   2016  4.9  4.9  5.0  5.0  4.8  4.9  4.8  4.9  5.0  4.9  4.7  4.7
7   2017  4.7  4.6  4.4  4.4  4.4  4.3  4.3  4.4  4.2  4.1  4.2  4.1
8   2018  4.1  4.1  4.0  4.0  3.8  4.0  3.8  3.8  3.7  3.8  3.7  3.9
9   2019  4.0  3.8  3.8  3.6  3.6  3.7  3.7  3.7  3.5  3.6  3.5  3.5
10  2020  3.6  3.5  4.4  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN"""

gov_data = utils.gov_data_extractor(gov_data_str)

