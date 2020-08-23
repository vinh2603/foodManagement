#1 quán bán đồ ăn nhanh bán A món ăn. Mỗi món ăn có công thức làm riêng biệt sử dụng một số lượng các nguyên liệu nấu ăn khác nhau.


Viết chương trình quản lý bán đồ ăn nhanh như sau:
-	Người bán hàng có một file json “foodStorage” lưu trữ các nguyên liệu đồ ăn trong kho nhà hàng và số lượng tương ứng. Danh sách các nguyên liệu là không thay đổi và được cho trước.
-	Người bán hàng có thể nhập thêm số lượng cho các nguyên liệu (trong danh sách cố định trên) bất kì lúc nào và lưu vào trong file “foodStorage”.
-	Người bán có thể nhập công thức các món ăn từ bàn phím bất kì lúc nào (VD: bấm “N” để nhập công thức các món ăn từ bàn phím). Với các món có sẵn, sau khi nhập công thức mới thì sẽ thay đổi công thức cũ chứ không thêm món mới vào danh sách các món.
-	Công thức làm 1 món ăn là một file định dạng bất kì chứa danh sách các nguyên liệu và số lượng cần dùng cho 1 suất ăn. Các nguyên liệu phải nằm trong danh sách nguyên liệu ở foodStorage.
-	Khi có yêu cầu của khách hàng về món ăn (một hoặc nhiều món), hệ thống kiểm tra kho nguyên liệu và cho biết liệu có thể hoàn thành được yêu cầu của khách hàng. 
-	Nếu thực hiện được, nhà hàng tiến hành làm món ăn và cập nhật lại dữ liệu vào file foodStorage. 
-	Nếu không đủ nguyên liệu để tiến hành làm món ăn, hệ thống in ra số lượng nguyên liệu còn thiếu. 
-	Mỗi món ăn đem lại lợi nhuận khác nhau. Giả sử khi khách hàng yêu cầu món ăn mà kho nguyên liệu không đáp ứng được nhu cầu, in ra danh sách các món ăn có thể làm được với tổng lợi nhuận trên đơn hàng cao nhất.
-	Chương trình chính sẽ gồm hàm main, các hàm khác sẽ viết theo dạng module để import vào chương trình chính.

#Ví dụ: 
Kho của nhà hàng có: 5 gio, 3 pate, 3 rau, 4 my, 4 banhmy (lưu trong file foodStorage, được cho trước)
Nhà hàng bán 2 món ăn là banhmy và mytom. (các công thức nhập từ bàn phím).
Công thức làm banhmy bao gồm: 1 gio, 1 pate, 1 banhmy, 2 rau.
Công thức làm mytom bao gồm: 1 gio, 3 rau, 1 my. 
Yêu cầu của khách hàng: 1 banhmy, 1 mytom 
Kết quả: banhmy sẽ được làm trong khi mytom bị thiếu 2 rau, sau đó kho sẽ cập nhật lại còn 4 gio, 2 pate, 1 rau, 4 my, 4 banhmy