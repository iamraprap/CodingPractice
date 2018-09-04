class Solution(object):
       
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        out = []
        while len(nums1)>0 and len(nums2)>0:
            if nums1[0]<nums2[0]:
                out.append(nums1.pop(0))
            else:
                out.append(nums2.pop(0))
        out.extend(nums1+nums2)
        lout = len(out)
        mid = (lout-1)/2
        if lout%2:
            return out[mid]            
        else:
            return ( out[mid] + out[mid+1]  ) / 2.0
        
def stringToIntegerList(input):
    return json.loads(input)

def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums1 = stringToIntegerList(line)
            line = lines.next()
            nums2 = stringToIntegerList(line)
            
            ret = Solution().findMedianSortedArrays([1,2], [3,4])

            out = doubleToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()