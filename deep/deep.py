
n = str( input("What is the Answer to the great Question of Life, the Universe, and Everything? "))

n = n.strip()
n = n.lower()


if n=="forty-two" or n=='forty two' or n=="42":
  print('yes')
else:
    print('no')