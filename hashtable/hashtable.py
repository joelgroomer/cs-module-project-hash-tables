class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.nodes = 0

        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY

        self.table = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.nodes / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        FNV_PRIME = 1099511628211
        FNV_OFFSET = 14695981039346656037
        hash = FNV_OFFSET

        key_bytes = key.encode()
        for byte in key_bytes:
            hash *= FNV_PRIME
            hash = hash ^ byte

        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """

        hash = 5381
        key_bytes = key.encode()

        for byte in key_bytes:
            # shift the current hashed value, add the next byte
            hash = ((hash << 5)) + hash + byte

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        if self.table[index] is None:
            # if there were no entries at this index, add this one
            self.table[index] = HashTableEntry(key, value)
            self.nodes += 1
        else:
            searching = True
            found = False
            entry = self.table[index]

            while searching:
                if entry.key == key:
                    # if this entry has the same key, overwrite
                    entry.value = value
                    found = True
                    searching = False
                elif entry.next is None:
                    searching = False
                else:
                    entry = entry.next

            if not found:
                # add new entry to the end of the linked list
                entry.next = HashTableEntry(key, value)
                self.nodes += 1

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.table[index] is not None:
            searching = True
            prev_entry = None
            entry = self.table[index]

            while searching:
                if entry.key == key:
                    # this is the entry we want to delete
                    if prev_entry is not None:
                        # link the previous entry to the next entry,
                        # effectively dropping the current entry
                        prev_entry.next = entry.next
                    else:
                        # if there's no previous entry, make the entry
                        # after this one the first entry
                        self.table[index] = entry.next
                    return
                elif entry.next is not None:
                    # if this isn't the entry we're looking for, move on
                    entry = entry.next
                else:
                    searching = False

        # if we get here, the index was empty or the key wasn't found
        print(
            f"WARNING: Key '{key}'not found in hash table. Could not delete.")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.table[index] is None:
            return None

        searching = True
        entry = self.table[index]

        while searching:
            if entry.key == key:
                return entry.value
            elif entry.next is not None:
                entry = entry.next
            else:
                searching = False

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        self.capacity = new_capacity
        old_table = self.table
        self.table = [None] * new_capacity

        for node in old_table:
            # loop through all of the indexes
            if node is None:
                continue

            self.put(node.key, node.value)
            while node.next is not None:
                # loop through old linked list and add to new array
                node = node.next
                self.put(node.key, node.value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
