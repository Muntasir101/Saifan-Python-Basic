# currency conversion
def currency_converter(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount


usd_to_euro_rate = 0.95
usd_to_bdt_rate = 118.24
usd_to_rupee_rate = 88.55

usd_amount = 155.98

euro_amount = currency_converter(usd_amount, usd_to_euro_rate)
print("Euro Actual Amount: ", euro_amount)
print("Euro Rounded Amount: ", round(euro_amount))


bdt_amount = currency_converter(usd_amount, usd_to_bdt_rate)
print("BDT Actual Amount: ", bdt_amount)
print("BDT Rounded Amount: ", round(bdt_amount))

rupee_amount = currency_converter(usd_amount, usd_to_rupee_rate)
print("Rupee: ", rupee_amount)