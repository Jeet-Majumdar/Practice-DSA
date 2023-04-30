#include <iostream>
#include <vector>

using namespace std;

class MaxHeap {
private:
    vector<int> heap;

    void heapify(int i) {
        int left = 2*i + 1;
        int right = 2*i + 2;
        int largest = i;

        if (left < heap.size() && heap[left] > heap[largest]) {
            largest = left;
        }
        if (right < heap.size() && heap[right] > heap[largest]) {
            largest = right;
        }
        if (largest != i) {
            swap(heap[i], heap[largest]);
            heapify(largest);
        }
    }

public:
    void insert(int k) {
        heap.push_back(k);
        int i = heap.size() - 1;
        while (i > 0 && heap[i] > heap[(i-1)/2]) {
            swap(heap[i], heap[(i-1)/2]);
            i = (i-1)/2;
        }
    }

    int remove() {
        if (heap.empty()) {
            throw runtime_error("Heap is empty");
        }
        int max_val = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        heapify(0);
        return max_val;
    }
};


class MinHeap {
private:
    vector<int> heap;

    void heapify(int i) {
        int left = 2*i + 1;
        int right = 2*i + 2;
        int smallest = i;

        if (left < heap.size() && heap[left] < heap[smallest]) {
            smallest = left;
        }
        if (right < heap.size() && heap[right] < heap[smallest]) {
            smallest = right;
        }
        if (smallest != i) {
            swap(heap[i], heap[smallest]);
            heapify(smallest);
        }
    }

public:
    void insert(int k) {
        heap.push_back(k);
        int i = heap.size() - 1;
        while (i > 0 && heap[i] < heap[(i-1)/2]) {
            swap(heap[i], heap[(i-1)/2]);
            i = (i-1)/2;
        }
    }

    int remove() {
        if (heap.empty()) {
            throw runtime_error("Heap is empty");
        }
        int min_val = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        heapify(0);
        return min_val;
    }
};



int main() {
    cout << "Checking MaxHeap\n";
    MaxHeap heap;
    heap.insert(8);
    heap.insert(5);
    heap.insert(6);
    heap.insert(4);
    cout << heap.remove() << endl; 
    cout << heap.remove() << endl; 
    cout << heap.remove() << endl;

    cout << "Checking MinHeap\n";
    MinHeap heap;
    heap.insert(8);
    heap.insert(5);
    heap.insert(6);
    heap.insert(4);
    cout << heap.remove() << endl; 
    cout << heap.remove() << endl; 
    cout << heap.remove() << endl; 

    return 0;
}
