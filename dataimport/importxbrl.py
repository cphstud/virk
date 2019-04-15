import sys
import re
import xml.dom.minidom

from xbrl import XBRLParser, GAAP, GAAPSerializer

#filename = sys.argv[1]
filename = "/Users/thw/test.xml"

#xbrl_import = xml.dom.minidom.parse( filename)

#for record in xbrl_import.getElementsByTagName('ko'):

#	name = record.getAttribute('unitRef')
#	print(record)

#print(str(xbrl_import))

from xbrl import XBRLParser, GAAP, GAAPSerializer

xbrl_parser = XBRLParser()

xbrl = xbrl_parser.parse(filename)

#Revenue = xbrl.find_all(name=re.compile("(fsa:GrossProfitLoss$)", re.IGNORECASE | re.MULTILINE))

Gross_Profit = xbrl.find_all(name=re.compile("(fsa:GrossProfitLoss$)", re.IGNORECASE | re.MULTILINE))

'''
Selling_and_General_Expenses = xbrl.find_all(name=re.compile("(us-gaap:SellingGeneralAndAdministrativeExpense$)", re.IGNORECASE | re.MULTILINE))

Depreciation = xbrl.find_all(name=re.compile("(us-gaap:DepreciationDepletionAndAmortization$)", re.IGNORECASE | re.MULTILINE))

Operating_Income = xbrl.find_all(name=re.compile("(us-gaap:OperatingIncomeLoss$)", re.IGNORECASE | re.MULTILINE))

Interest_Expense = xbrl.find_all(name=re.compile("(us-gaap:InterestExpense$)", re.IGNORECASE | re.MULTILINE))

Dividend = xbrl.find_all(name=re.compile("(us-gaap:CommonStockDividendsPerShareCashPaid$)", re.IGNORECASE | re.MULTILINE))

valuesy = '"usd">'

valuesz = '</us-gaap:grossprofit>'

valuesy_pos = str.find(str(Gross_Profit), valuesy)

valuesz_pos = str.find(str(Gross_Profit), valuesz)

valuex = valuesz_pos - valuesy_pos

gp = "".join(str(x) for x in Gross_Profit)

gross_profiteer = gp[valuesy_pos+5:valuesz_pos-1]

valuesrvz = '</us-gaap:salesrevenuegoodsnet>'

valuesrvy_pos = str.find(str(Revenue), valuesy)

valuesrvz_pos = str.find(str(Revenue), valuesrvz)

valuervx = valuesrvz_pos - valuesrvy_pos

rv = "".join(str(r) for r in Revenue)

revenue_amt = rv[valuesrvy_pos+5:valuesrvz_pos-1]

sga = "".join(str(y) for y in Selling_and_General_Expenses)    

valuesgax = '"usd">'

valuesgay = '</us-gaap:sellinggeneralandadministrativeexpense>'                                                                                               

valuesgax_pos = str.find(str(Selling_and_General_Expenses), valuesy)

valuesgay_pos = str.find(str(Selling_and_General_Expenses), valuesgay)

sga_exp = sga[valuesgax_pos+5:valuesgay_pos-1]

valuedpx = '"usd">'

valuedpy = '</us-gaap:depreciationdepletionandamortization>'

dpa = "".join(str(y) for y in Depreciation) 

valuesdpx_pos = str.find(str(Depreciation), valuedpx)

valuesdpy_pos = str.find(str(Depreciation), valuedpy)

depreciation_exp = dpa[valuesdpx_pos+5:valuesdpy_pos-1]

valuesy = '"usd">'

valuesz = '</us-gaap:commonstockdividendspersharecashpaid>'

valuesy_div_pos = str.find(str(Dividend), valuesy)

valuesz_div_pos = str.find(str(Dividend), valuesz)

diva = "".join(str(div) for div in Dividend)

dividends = diva[valuesy_div_pos+5:valuesz_div_pos-1]

valueoix = '"usd">'

valueoiy = '</us-gaap:operatingincomeloss>'

oia = "".join(str(o) for o in Operating_Income)

operatingincomex_pos = str.find(str(Operating_Income), valueoix)

operatingincomey_pos = str.find(str(Operating_Income), valueoiy)

operating_inc = oia[operatingincomex_pos+5:operatingincomey_pos-1]

interestexpx = '"usd">'

interestexpy = '</us-gaap:interestexpense>'

iexa = "".join(str(i) for i in Interest_Expense)

interestexpensex_pos = str.find(str(Interest_Expense), interestexpx)

interestexpensey_pos = str.find(str(Interest_Expense), interestexpy)

interest_exp = iexa[interestexpensex_pos+5:interestexpensey_pos-1]

Profit_Margin = int(gross_profiteer)/int(revenue_amt)


print("Coca Cola's Revenue for 2013 was $" + revenue_amt)
print("Coca Cola's Gross profit for 2013 was $" + gross_profiteer )
print("Coca Cola's Operating Income for 2013 was $" + operating_inc )
print("Coca Cola's Profit Margin's for 2013 is {0:%}".format(Profit_Margin))

print("Coca Cola's Selling and General Expenses for 2013 was $" + sga_exp )
print("Coca Cola's Depreciation Expenses for 2013 was $" + depreciation_exp )
print("Coca Cola's Interest Expenses for 2013 was $" + interest_exp)


sga_gp_ratio = int(sga_exp)/int(gross_profiteer)
dpa_gp_ratio = int(depreciation_exp)/int(gross_profiteer)
iex_oi_ratio = int(interest_exp)/int(operating_inc)

print("Selling and General Expenses is {0:%}".format(sga_gp_ratio) + " of Gross Profits which is acceptable for investment consideration")
print("Depreciation Expenses is {0:%}".format(dpa_gp_ratio) + " of Gross Profits which is below 10% and acceptable for investment consideration")
print("Interest Expenses is {0:%}".format(iex_oi_ratio) + " of Operating Income which is below 10%, not including interest income thus acceptable for investment consideration")
'''
print("Coca Cola's Gross profit for 2013 was $" + str(Gross_Profit))