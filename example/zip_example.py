a = ("Chelsea", "Manchester", "Chester")
b = ("Rain", "Snow", "Winter")

x = zip(a, b)
#use the tuple() function to display a readable version of the result:
print(tuple(x)) 
# Output : (('Chelsea', 'Rain'), ('Manchester', 'Snow'), ('Chester', 'Winter'))

for i, j in zip(a, b):
    print("{}: {}".format(i, j))
# Output : 
# Chelsea: Rain
# Manchester: Snow
# Chester: Winter

