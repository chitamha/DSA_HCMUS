import sys

# Tăng giới hạn đệ quy để không bị lỗi Runtime trên cây sâu
sys.setrecursionlimit(300000)

class AVLNode:
    # __slots__ giới hạn các thuộc tính được phép tạo, giúp tiết kiệm RAM và truy xuất nhanh
    __slots__ = ['data', 'height', 'size', 'left', 'right']
    
    def __init__(self, data):
        self.data = data
        self.height = 1      # Chiều cao mặc định của node lá là 1
        self.size = 1        # Số lượng node trong cây con (bao gồm chính nó)
        self.left = None
        self.right = None

# ---------------------------------------------------------
# CÁC HÀM TRỢ GIÚP (HELPER FUNCTIONS)
# ---------------------------------------------------------

def update(node):
    """Cập nhật lại chiều cao (height) và kích thước (size) của node dựa vào 2 con"""
    lh = node.left.height if node.left else 0
    rh = node.right.height if node.right else 0
    node.height = 1 + (lh if lh > rh else rh)
    
    ls = node.left.size if node.left else 0
    rs = node.right.size if node.right else 0
    node.size = 1 + ls + rs

def get_bal(node):
    """Tính độ lệch = Chiều cao Phải - Chiều cao Trái. 
       - Âm: Lệch trái
       - Dương: Lệch phải"""
    lh = node.left.height if node.left else 0
    rh = node.right.height if node.right else 0
    return rh - lh

# ---------------------------------------------------------
# CÁC HÀM CÂN BẰNG (ROTATIONS & REBALANCE)
# ---------------------------------------------------------

def right_rotate(y):
    """Xoay phải: Kéo node con trái (x) lên làm gốc mới, đẩy y xuống làm con phải của x"""
    x = y.left
    y.left = x.right
    x.right = y
    update(y) # Cập nhật node bị đẩy xuống trước
    update(x) # Cập nhật node gốc mới sau
    return x

def left_rotate(y):
    """Xoay trái: Kéo node con phải (x) lên làm gốc mới, đẩy y xuống làm con trái của x"""
    x = y.right
    y.right = x.left
    x.left = y
    update(y)
    update(x)
    return x

def rebalance(node):
    """Kiểm tra và tự động xoay để cân bằng lại cây tại node hiện tại"""
    update(node)
    bal = get_bal(node)

    if bal < -1: # Nhánh trái đang cao hơn nhánh phải quá 1 bậc (Lệch Trái)
        if get_bal(node.left) <= 0:
            return right_rotate(node) # Lệch Trái-Trái -> Xoay phải 1 lần
        else:
            node.left = left_rotate(node.left) # Lệch Trái-Phải -> Xoay trái con trái, rồi xoay phải chính nó
            return right_rotate(node)
            
    if bal > 1: # Nhánh phải đang cao hơn nhánh trái quá 1 bậc (Lệch Phải)
        if get_bal(node.right) >= 0:
            return left_rotate(node) # Lệch Phải-Phải -> Xoay trái 1 lần
        else:
            node.right = right_rotate(node.right) # Lệch Phải-Trái -> Xoay phải con phải, rồi xoay trái chính nó
            return left_rotate(node)
    
    return node # Cây đang cân bằng, không cần xoay

# ---------------------------------------------------------
# CÁC HÀM THAO TÁC CHÍNH (INSERT, DELETE, QUERY)
# ---------------------------------------------------------

def insert(node, data):
    """Chèn đệ quy: Đi tìm vị trí chèn như BST thông thường, sau đó cân bằng trên đường quay lui"""
    if not node:
        return AVLNode(data)
    
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    else:
        return node # Bỏ qua nếu giá trị đã tồn tại

    return rebalance(node)

def get_min_value(node):
    """Tìm node có giá trị nhỏ nhất (nằm ở tận cùng bên trái)"""
    curr = node
    while curr.left:
        curr = curr.left
    return curr
    
def delete(node, data):
    """Xóa đệ quy: Tìm node cần xóa, thay thế hợp lý, sau đó cân bằng trên đường quay lui"""
    if not node:
        return node
    
    # Bước 1: Đi tìm node cần xóa
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # Bước 2: Đã tìm thấy. Xử lý các trường hợp xóa
        if not node.left or not node.right:
            # TH 1 & 2: Node có 0 hoặc 1 con -> Lấy con duy nhất thay thế chính nó
            temp = node.left if node.left else node.right
            if not temp:
                return None
            else:
                return temp # Bỏ qua rebalance vì nhánh này đã ngắn đi một cách tự nhiên
        else:            
            # TH 3: Node có 2 con -> Lấy phần tử nhỏ nhất bên nhánh phải để thế mạng
            temp = get_min_value(node.right)
            node.data = temp.data # Copy giá trị thế mạng lên node hiện tại
            node.right = delete(node.right, temp.data) # Xóa phần tử thế mạng ở dưới đi
    
    # Bước 3: Cân bằng lại cây sau khi xóa
    return rebalance(node)

def query_range(root, x, y):
    """Tìm node đầu tiên nằm trong khoảng [x, y], sau đó đếm số node nhỏ hơn nó"""
    if x > y:
        x, y = y, x 
        
    count = 0
    curr = root
    while curr:
        if curr.data > y:
            curr = curr.left # Giá trị quá lớn, phải đi sang trái để tìm node nhỏ hơn
        elif curr.data < x:
            count += (curr.left.size if curr.left else 0) + 1 # Cả nhánh trái và node hiện tại đều nhỏ hơn mức cần tìm
            curr = curr.right # Đi sang phải để tìm node lớn hơn
        else:
            # Đã lọt vào khoảng [x, y]. Số node nhỏ hơn nó chính là size của nhánh trái cộng dồn với count từ nãy giờ.
            return count + (curr.left.size if curr.left else 0)
    return -1

def pre_order_non_recursive(root):
    """Duyệt Tiền tố (Node - Left - Right) bằng Stack thay vì Đệ quy"""
    if not root:
        return ""
    
    stack = [root]
    result = []
    while stack:
        curr = stack.pop()
        result.append(str(curr.data))
        # Đẩy con phải vào Stack TRƯỚC, con trái vào SAU 
        # => Con trái nằm trên đỉnh Stack => Sẽ được pop ra và xử lý TRƯỚC
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
            
    return " ".join(result)

# ---------------------------------------------------------
# HÀM MAIN & I/O TỐI ƯU
# ---------------------------------------------------------

def main():
    """Đọc toàn bộ input một lần, gom kết quả xuất ra một lần để tránh nghẽn I/O"""
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    root = None
    
    out = [] 
    
    for cmd in iterator:
        t = int(cmd)
        if t == 1:
            root = insert(root, int(next(iterator)))
        elif t == 2:
            root = delete(root, int(next(iterator)))
        elif t == 3:
            x, y = int(next(iterator)), int(next(iterator))
            out.append(str(query_range(root, x, y)))
        elif t == 4:
            out.append(pre_order_non_recursive(root))

    if out:
        sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()