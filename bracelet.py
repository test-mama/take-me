#Name: Ajani Levere
#Date: 06/06/23
#Purpose: Bracelet class which creates linked list of all charm nodes; open and close functionality

from collectible_charm import CollectibleCharm
from your_charms import CharacterCharm
from friendship_charm import FriendshipCharm
from charm import Charm
from linked_list import LinkedList

# Define Bracelet Class Here
class Bracelet(LinkedList):
    
    def __init__(self, marketValue):
        super().__init__()
        self.__marketValue = marketValue
        
    #getter for market value
    def getMarketValue(self):
        return self.__marketValue
    
    #if given type is a charm, it adds the charm to the bracelet linkedlist
        #if it's closed, though, then it opens up the bracelet, append as normally, and closes again
    def append(self, data):
        if isinstance(data, Charm):
            if self.isClosed():
                self.open()
                super().append(data)
                self.close()
            else:
                super().append(data)
    
    #for every item in the bracelet linked list, get the market value and add it to total
    def appraise(self):
        totalValue = self.getMarketValue()
        for i in range(len(self)):
            totalValue += self[i].getMarketValue()
        return float(f"{totalValue:.2f}")
    
    #close: goes through the linked list as long as the next node is not the head
        #if it finds a none, it sets it to the head, violating the while condition and ending func
    def close(self):
        if len(self) > 0:
            current = self.getHead()
            while current.getNext() != self.getHead():
                if current.getNext() == None:
                    current.setNext(self.getHead())
                else:
                    current = current.getNext()
                    
    #isClosed: first, if the length is == 0, it's false, but other than that it iterates bracelet
        #if it finds a none, it's over, it's done, but if it goes all the way...
        #and finds no none, then that mean the bracelet is closed
    def isClosed(self):
        if len(self) > 0:
            current = self.getHead()
            while current.getNext() != self.getHead():
                if current.getNext() == None:
                    return False
                else:
                    current = current.getNext()
            return True
        else:
            return False
    
    #open: iterates thru bracelet (as long as len > 0) and keeps going as long as current's next
        #doesn't point to a head, if points to a head, end while loop and set current's next to None
    def open(self):
        if len(self) > 0:
            current = self.getHead()
            while current.getNext() != self.getHead():
                current = current.getNext()
            current.setNext(None)
    
    #isOpen: (same as isClosed for length)iterates thru Linked list as long as there isn't a none,
        #if there is then it returns true, in the list, though, it continues to check for a head
        #and if it sees a head, then it's false
    def isOpen(self):
        if len(self) > 0:
            current = self.getHead()
            while current.getNext() != None:
                if current.getNext() == self.getHead():
                    return False
                else:
                    current = current.getNext()
            return True
        else:
            return True
    
    #overriding length method to include condition: if the next is a head (closed), stop the count
        #and return the current num
    def __len__(self):
        if self.getHead() == None:  # if list is empty return 0
            return 0
        
        current = self.getHead()   #list is not empty and has at least 1 Node
        counter = 1
        
        while current.getNext() != None: # check if theres's another item after the current node
            if current.getNext() == self.getHead():
                return counter
            counter += 1
            current = current.getNext()
        return counter
    
    #overrides str method to include condition: if the current is a head or is None, then just print
        #what it's collected so far and stop moving forward
    def __str__(self):
        myStr = ''
        current = self.getHead()
            
        while current != None:
            myStr += str(current.getData()) + ' --> '
            current = current.getNext()
            if current == self.getHead() or current == None:
                return myStr
        return myStr
    
    #overrides remove method to open bracelet if closed (so it functions like a typical linked list),
        #because that is what the remove function is programmed to follow, but then closes once done
    def remove(self, item):
        if self.isClosed():
            self.open()
            super().remove(item)
            self.close()
        else:
            super().remove(item)
            
    #overrides search method to do the same thing as remove, but stores result in boolean
        #that's returned at the end of the function
    def search(self, item):
        result = None
        if self.isClosed():
            self.open()
            result = super().search(item)
            self.close()
        else:
            result = super().search(item)
        return result


    
    
    
    

