## 1.)linked list and its implementation
# class Basic:
#     def __init__(self, data=None, next=None):
#      self.data=data
#      self.next=next
#
#         #head and next are the pointers
#
#
# class Linked:
#     def __init__(self, head=None):
#         self.head=head
#
#     def Insert_in_start(self,data):
#         nod=Basic(data,self.head)
#         self.head=nodllll
#
#     def Print(self):
#         if self.head is None:
#             print("empty")
#             return
#
#         ll=""
#         i=self.head
#         while i:
#             ll+=str(i.data)+" "
#             i=i.next
#         print(ll)
#
#     def get_len(self):
#
#        i=self.head
#        count=0
#        while i!=None:
#             i=i.next
#             count+=1
#        return count
#
#
#     def insert_in_end(self,data):
#         if self.head is None:
#             nod=Basic(data,None)
#             self.head=nod
#             return
#
#         i=self.head
#         while i.next is not None:
#
#             i=i.next
#         i.next=Basic(data,None)
#         return
#
#     def insert_values(self,data_list):
#         self.head =None
#         for i in data_list:
#              self.insert_in_end(i)
#
#
#
# #remove at
#     def remove_at(self,index):
#
#          if index<0 or index>=self.get_len():
#              print("invalid")
#              return
#          if index==0:
#              self.head=self.head.next
#              return
#
#          itr=self.head
#          count=0
#          while itr:
#              if count==index-1:
#                itr=itr.next.next
#                return
#              count=count+1
#              itr=itr.next
#
#
#
#     def insert_at(self,data,index):
#
#          if index<0 or index>=self.get_len():
#              print("invalid")
#              return
#          if index==0:
#              self.Insert_in_start(data)
#              return
#
#          itr=self.head
#          count=0
#          while itr.next:
#              if count==index-1:
#                  #itr.next at current pos or itr will be in our insert elemnt next then after that the itr.next of current itr shoul be updated with inserted data too.
#                nod=Basic(data,itr.next)
#                itr.next=nod
#                return
#              count=count+1
#              itr=itr.next
#     #insert after value
#     def insert_after(self,before,after):
#         if self.get_len()==0 or self.get_len()== 1:
#             self.insert_in_end(after)
#         itr=self.head
#         while itr.next:
#             if itr.data==before:
#                 nod = Basic(after, itr.next)
#                 itr.next = nod
#                 return
#
#             itr=itr.next
# #remove by value
#     def remove_val(self,value):
#          if self.head is None:
#              raise Exception("invalid")
# # here the index of element to be removed is found
#          itr=self.head
#          count=0
#          while itr:
#              if itr.data==value:
#                   break
#
#
#              itr=itr.next
#              count=count+1
# # here the found element is removed
#          itr = self.head
#          index=0
#          while itr:
#              if index==count-1:
#                itr.next=itr.next.next
#                return
#
#
#              index=index+1
#              itr=itr.next
#
#
#
#
#
#
#
#
# ak=Linked()
#
# ak.insert_values(["banana", "mango", "grapes", "orange"])
#
#
#
#
#
#
#
# ak.remove_val("orange") # remove orange from linked list
# ak.Print()
#
# ak.remove_val("banana")
# ak.remove_val("mango")
#
# ak.remove_val("grapes")
# ak.Print()


#2.)doubly linked list



# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print_forward(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data) + ' --> '
#             itr = itr.next
#         print(llstr)
#
#
#
#
#
#     def insert_at_begining(self, data):
#
#             node = Node(data, self.head, None)
#             self.head = node
#
#
#     def insert_at_end(self,data):
#         if self.head==None:
#             self. insert_at_begining(data)
#
#         itr=self.head
#         while itr.next:
#             itr = itr.next
#
#         itr.next = Node(data, None, itr)
#
#     def print_back(self):
#         if self.head==None:
#             print("list is empty")
#         itr=self.head
#
#         while itr.next:
#             itr=itr.next
#
#         ll = ""
#         while itr:
#             ll+=str(itr.data)+" "
#
#             itr=itr.prev
#         print(ll)
#
#
#
# ak=DoublyLinkedList()
# ak.insert_at_begining(5)
# ak.insert_at_begining(6)
# ak.insert_at_end(7)
# ak.print_forward()
# ak.print_back()

#3.) Hash function
#
# list comprehesnion
# name=["ak","nk","sk"]
# pk=[None for x in name if x]
# print(pk)

#


class Hashmap:
   def __init__(self):
     self.max=100
     self.arr=[[] for i in range(self.max)]

   def hashf(self,key):
        i=0
        for itr in key:
          i+=ord(itr)

        return i%self.max
   def add(self,key,value):
         h=self.hashf(key)
         found=False
          index, tuple in enumerate( self.arr[h]):
             if index==0 and tuple[0]==key:
                 self.arr[h][index]=(key,value)
                 found=True

         if found==False :
             self.arr[h].append(self)


   def get(self,key):
       h=self.hashf(key)
       return self.arr[h]
   def dell(self,key):
       h=self.hashf(key)
       self.arr[h]=None




ak=Hashmap()
ak.add('ak',9)
ak.add('ak',10)
print(ak.arr)