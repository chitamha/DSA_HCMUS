#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int INSERTION_THRESHOLD = 16;

// Hàm hoán vị có điều kiện in
void printSwap(vector<int>& A, int i, int j, bool print) {
    if (print && i != j) {
        cout << min(i, j) << " " << max(i, j) << "\n";
    }
    swap(A[i], A[j]);
}

// 1. Insertion Sort cho mảng con nhỏ
void insertion_sort(vector<int>& A, int low, int high) {
    for (int i = low + 1; i <= high; ++i) {
        int j = i;
        while (j > low && A[j] < A[j - 1]) {
            printSwap(A, j - 1, j, true);
            j--;
        }
    }
}

// 2. Các hàm hỗ trợ Heap Sort
void heapify(vector<int>& A, int n, int i, int offset) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && A[offset + left] > A[offset + largest])
        largest = left;

    if (right < n && A[offset + right] > A[offset + largest])
        largest = right;

    if (largest != i) {
        printSwap(A, offset + i, offset + largest, true);
        heapify(A, n, largest, offset);
    }
}

void heap_sort(vector<int>& A, int low, int high) {
    int n = high - low + 1;
    // Build heap
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(A, n, i, low);
    }
    // Extract elements
    for (int i = n - 1; i > 0; i--) {
        printSwap(A, low, low + i, true);
        heapify(A, i, 0, low);
    }
}

// 3. Phân hoạch Quick Sort (Lomuto Partition) với Median-of-Three
int partition(vector<int>& A, int low, int high) {
    int mid = low + (high - low) / 2;
    
    // Tìm Median-of-Three và đưa về cuối mảng
    if (A[mid] < A[low]) printSwap(A, low, mid, false);
    if (A[high] < A[low]) printSwap(A, low, high, false);
    if (A[high] < A[mid]) printSwap(A, mid, high, false);
    
    printSwap(A, mid, high - 1, false);
    int pivot = A[high - 1];

    int i = low;
    for (int j = low + 1; j < high - 1; j++) {
        if (A[j] < pivot) {
            i++;
            printSwap(A, i, j, false);
        }
    }
    i++;
    printSwap(A, i, high - 1, false);
    return i;
}

// 4. Thuật toán lai Introsort
void introsort(vector<int>& A, int low, int high, int depth_limit) {
    if (low >= high) return;

    int size = high - low + 1;
    
    // Rơi vào ngưỡng thì dùng Insertion Sort
    if (size <= INSERTION_THRESHOLD) {
        insertion_sort(A, low, high);
        return;
    }
    
    // Quá giới hạn đệ quy thì fallback về Heap Sort
    if (depth_limit == 0) {
        heap_sort(A, low, high);
        return;
    }

    // Bước chia của Quick Sort
    int pivot_idx = partition(A, low, high);
    cout << pivot_idx << "\n"; // In ra vị trí pivot theo yêu cầu đề bài

    introsort(A, low, pivot_idx - 1, depth_limit - 1);
    introsort(A, pivot_idx + 1, high, depth_limit - 1);
}

int main() {
    // Tối ưu I/O cho C++
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        int depth_limit = 2 * floor(log2(n));
        introsort(a, 0, n - 1, depth_limit);
    }
    return 0;
}