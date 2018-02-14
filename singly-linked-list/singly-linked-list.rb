# Class representing a singly list element
class Element
  def initialize(*value)
    @value=value
    @next= None
  end
end


# New class representing singly linked lists, it takes an element as the head,
# if it does not contain one it will be set to None
class linkedList
  @head = None
  def initialize(new_element)
    current = self.head

    if self.head
      while current.next
        current = current.next
      end
      current.next = new_element
    else
      current.nex = new_element
    end
  end
end
