
path = '/home/berg/Desktop/dummy.json'
text = str('{"itemValidity":"","erpReferenceKey":"040060106","productERPReferenceKey":"040060106 ","discountValue":0,"minimunSalePrice":72.6,"discountFactor":0,"isActive":"true","removed":"false"}')

r = open(path, 'w')

for x in range(10):
    r.write(text + ',')    

r.close()