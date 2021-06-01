class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next=" + str(self.next) + ")"
class Solution:
    def list_to_ListNode(self,l):
        if type(l) is not list or  len(l) == 0:
            return None
        return ListNode(val = l[0],next= self.list_to_ListNode(self,l[1:]) if len(l)> 1 else None)


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def check_list(l):
            
            r = list()
            while True:
                if type(l.val) is not int or l.val< 0 or l.val> 9:
                    raise Exception(ValueError,'''Values must be integers between 0 and 9. 
                        Error on value {value} at index {index}'''.format(value= l.val, index= i))
                else:
                    r.append(str(l.val))
                if l.next is None:
                    break
                else:
                    l = l.next
            return int(''.join(reversed(r)))


        return self.list_to_ListNode(self,list(reversed([int(c) for c in str(check_list(l1) + check_list(l2))])))

    




l1 = Solution.list_to_ListNode(Solution,[2,4,3])
l2 = Solution.list_to_ListNode(Solution,[5,6,4])
n = Solution.addTwoNumbers(Solution,l1,l2)
print(n)