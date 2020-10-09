f = open('/Users/mizumuratomoya/Desktop/pythontomo2/pdf.txt', 'r')

data = f.read()

ans = data.count('しょうが玄米')
print('しょうが玄米' + str(ans) + '個')

f.close()
