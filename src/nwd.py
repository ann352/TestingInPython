def nwd(a, b):
   while a != b:
       a, b = max(a, b), min(a, b)
       a = a - b
   return a

if __name__ == "__main__":
    r = nwd (30,50)
    print (r)