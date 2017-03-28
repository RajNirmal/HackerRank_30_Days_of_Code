    def insert(self,head,data): 
    #Complete this method
        if( head == None ):
            head = Node(data)
            head.next = None
            return head;
        else:
            current = head
            while (current.next != None):
                current = current.next
            nodes = Node(data)
            current.next = nodes
            return head
  