n,m,k,x,y,z,t,a = (int(input()) for _ in range(8))
b = m + n - t - x
c = m + k - t - y
d = n + k - t - z
ans1 = (n-b-d-t) + (m-b-t-c) + (k-d-c-t)
ans2 = b+c+d
ans3 = a - ((n-b-d-t)+(m-b-t-c)+(k-d-c-t))-(b+c+d+t)
print(ans1,ans2,ans3,sep='\n')


# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# mylist = [word.lower().strip(',.!?-:;()') for word in sentence.split() if len(word)<=4]
# print(*sorted(mylist))
# myset = {word.lower().strip(',.!?-:;()') for word in mylist if len(word)<4}
# print(*sorted(myset))


# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# myset = {word.lower().strip(',.!?-:;()') for word in sentence.split()}
# print(*sorted(myset))