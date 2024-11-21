class Heap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        if idx > 0 and self.heap[parent_idx] < self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            self._heapify_up(parent_idx)

    def delete(self):
        if not self.heap:
            return False
        del_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return del_item

    def _heapify_down(self, idx):
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        larger = idx
        if left_idx < len(self.heap) and self.heap[left_idx] > self.heap[larger]:
            larger = left_idx
        if right_idx < len(self.heap) and self.heap[right_idx] > self.heap[larger]:
            larger = right_idx
        if larger != idx:
            self.heap[larger], self.heap[idx] = self.heap[idx], self.heap[larger]
            self._heapify_down(larger)

    def display(self):
        print(self.heap)

    def peek(self):
        print(self.heap[0])


heap = Heap()
heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(50)
heap.insert(40)
heap.display()
heap.delete()
heap.display()
heap.insert(100)
heap.insert(0)
heap.display()
heap.peek()
