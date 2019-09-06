# Write your win_percentage function here:
def win_percentage(wins,losses):
  percnt=(wins/(wins+losses))*100
  return percnt
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100
