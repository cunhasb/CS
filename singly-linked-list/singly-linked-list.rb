# Class representing a singly list element
class Element
  def initialize(*value)
    @value = value
    @next = None
  end
end

# New class representing singly linked lists, it takes an element as the head,
# if it does not contain one it will be set to None
class LinkedList
  @head = None
  def initialize(_new_element)
    current = head
  end

  def append(new_element)
    if head
      current = current.next while current.next
      current.next = new_element
    else
      current.nex = new_element
    end
  end
end
