def partition(arr, l, r):
    pivot = arr[r]
    
    # Biến 'i' sẽ theo dõi ranh giới của các phần tử NHỎ HƠN chốt
    # Ban đầu chưa có phần tử nào, nên i nằm ngoài vùng xét (l - 1)
    i = l - 1 
    
    # Duyệt từ đầu đến phần tử kế cuối (trước chốt)
    for j in range(l, r):
        # Nếu tìm thấy phần tử nhỏ hơn chốt, đưa nó về bên trái (vùng của i)
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Kết thúc vòng lặp, mọi thứ từ l đến i đều nhỏ hơn chốt.
    # Vị trí i + 1 chính là nơi DÀNH RIÊNG cho chốt
    pivot_idx = i + 1
    
    # Đưa chốt từ vị trí r về đúng vị trí của nó
    arr[pivot_idx], arr[r] = arr[r], arr[pivot_idx]
    
    # TRẢ VỀ CHỈ SỐ (INDEX) CỦA CHỐT
    return pivot_idx

def quickSort(arr, l, r):
    if l < r:
        # Nhận lại index của chốt sau khi nó đã được đặt đúng chỗ
        p_idx = partition(arr, l, r)
        
        # Gọi đệ quy cho nửa trái (từ l đến trước p_idx)
        quickSort(arr, l, p_idx - 1)
        
        # Gọi đệ quy cho nửa phải (từ sau p_idx đến r)
        quickSort(arr, p_idx + 1, r)


if __name__ == "__main__":
    my_arr = [10, 80, 30, 90, 40, 50, 70]
    print("Mảng ban đầu:", my_arr)
    quickSort(my_arr, 0, len(my_arr) - 1)
    print("Mảng sau khi sắp xếp:", my_arr)