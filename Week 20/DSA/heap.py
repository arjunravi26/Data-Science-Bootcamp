class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if not self.heap:
            return False
        if len(self.heap) == 1:
            return self.heap.pop()
        node_delete = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return node_delete

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        if idx > 0 and self.heap[parent_idx] < self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            self._heapify_up(parent_idx)

    def _heapify_down(self, idx):
        largest = idx
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        if left_idx < len(self.heap) and self.heap[largest] < self.heap[left_idx]:
            largest = left_idx
        if right_idx < len(self.heap) and self.heap[largest] < self.heap[right_idx]:
            largest = right_idx
        if largest != idx:
            self.heap[largest], self.heap[idx] = self.heap[idx], self.heap[largest]
            self._heapify_down(largest)

    def peek(self):
        if self.heap:
            print(self.heap[0])
            return self.heap[0]


heap = Heap()
heap.insert(10)
heap.insert(40)
heap.insert(20)
heap.insert(90)
heap.insert(50)
heap.peek()
print(heap.delete())
heap.peek()
