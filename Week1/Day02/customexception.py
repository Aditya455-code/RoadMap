try:
    x=100
    y=2
    z=x/y
    if z>10:
        raise ValueError(z)
except ValueError:
    print(z,"Value count out of bounded range")

else:
    print(z,"Value is within the range")
    