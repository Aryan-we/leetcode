class listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addnodes(self):
        l = [1, 2, 3, 4, 5]
        if not l:
            return None
        head = listnode(l[0])
        temp = head
        for i in l[1:]:
            temp.next = listnode(i)
            temp = temp.next
        return head

    def shownodes(self, head):
        temp = head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()

    def reverselist(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def deletenode(self, head, value):
        dummy = listnode(0)
        dummy.next = head
        temp = dummy
        found = False
        while temp.next:
            if temp.next.val == value:
                temp.next = temp.next.next
                found = True
                break
            temp = temp.next
        return dummy.next, found


# Running the code
obj = listnode()
a = obj.addnodes()

print("Original List:")
obj.shownodes(a)

#b = obj.reverselist(a)
#print("Reversed List:")
#obj.shownodes(b)

# Fix here: delete from reversed list
c, d = obj.deletenode(a, 1)
a=c

if d:
    print(f"List After Deletion :")
    obj.shownodes(a)
else:
    print("Element not found")
