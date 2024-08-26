if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    k=list()
    i=0
while i<n:
  maxx=max(l)
  if l[i]!=maxx:
   k.append(l[i])
  i+=1
print(max(k))
