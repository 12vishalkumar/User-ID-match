# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = int(input())
for i in range(T):
    st = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', st)
        assert re.search(r'\d\d\d', st)
        assert not re.search(r'[^a-zA-Z0-9]', st)
        assert not re.search(r'(.)\1', st)
        assert len(st) == 10
    except:
        print('Invalid')
    else:
        print('Valid')