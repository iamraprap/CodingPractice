class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lcs = {}
        tlcs = ""
        maxlen = 0 
        start = 0
        finish = 0
        while start < len(s):
            finish = start+1
            while finish <= len(s):
                print("maxlen:%d start:%d finish:%d s:'%s'" % (maxlen, start, finish, s[start:finish]))
                if s[finish-1] in tlcs:
                    print("foundChar %s" % (s[finish-1]))
                    #start = finish-1
                    break
                else:
                    tlcs = s[start:finish]
                    maxlen = maxlen if maxlen>len(tlcs) else len(tlcs)
                    lcs[maxlen] = tlcs
                    print("maxlen:%d tlcs:%s l_tlcs:%d" % (maxlen, tlcs, len(tlcs)))
                finish+=1               
            start+=1
            tlcs = ""
        #print("maxlen:%d" % (maxlen))
        #for i in lcs.items():
        #    print("%d %s" % (len(i), i))
        return maxlen
        
def stringToString(input):
    return input[1:-1].decode('string_escape')

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToString(line)
            
            ret = Solution().lengthOfLongestSubstring("dvdf")

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()