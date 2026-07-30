class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Key -> Node mapping
        
        # Dummy head and tail to simplify edge cases
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node):
        """Insert node right after head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        """Remove node from the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self,key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Move accessed node to head
        self._remove(node)
        self._add_to_head(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            # Update existing
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Add new
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            
            # Evict if over capacity
            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]