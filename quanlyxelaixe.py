import tkinter as tk
from LoaiXeDAO import LoaiXeDAO
from XeDAO import XeDAO
from LaiXeDAO import LaiXeDAO
from PhanCongDAO import PhanCongDAO
from tkinter import ttk, messagebox
from center import center_window
from AnHienFrame import hien_xe, hien_laixe, hien_phancong
xedao = XeDAO()
laixedao = LaiXeDAO()
phancongdao = PhanCongDAO()
loaixedao = LoaiXeDAO()
#========== WINDOW ==============
root = tk.Tk() #tao cua so chinh gan vao root
root.title("QUẢN LÝ XE VÀ LÁI XE")
center_window(root, 1100, 700)
frame_main = tk.Frame(root)
frame_main.pack(fill='both', expand=True)
root.resizable(False, False)

#========== KHOI TAO FRAME ==========
frame_status = tk.Frame(frame_main)
#========== FRAME HEADER ========
frame_header = tk.Frame(frame_main)
label_tieude = tk.Label(
    frame_header,
    text="QUẢN LÝ XE VÀ LÁI XE",
    fg="red",
    font=("Arial", 24, "bold")
)
label_tieude.pack()
frame_header.pack(
    fill = 'x'
)
# ========= FRAME MENU ===========
frame_menu = tk.Frame(frame_main)
frame_xe = tk.Frame(frame_main)
frame_laixe = tk.Frame(frame_main)
frame_phancong = tk.Frame(frame_main)

btn_xe = tk.Button(
    frame_menu,
    text="QUẢN LÝ XE",
    font=("Arial", 14, "bold"),
    height=2,
    bg="#3498DB",
    fg="white",
    relief="groove", #kiểu viền nút
    cursor="hand2",
    command = lambda: hien_xe(frame_xe, frame_laixe, frame_phancong)
)

btn_laixe = tk.Button(
    frame_menu,
    text=" QUẢN LÝ LÁI XE",
    font=("Arial", 14, "bold"),
    height=2,
    bg="#E67E22",
    fg="white",
    relief="groove",
    cursor="hand2",
    command =  lambda:hien_laixe(frame_xe, frame_laixe, frame_phancong)
)

btn_phancong = tk.Button(
    frame_menu,
    text="PHÂN CÔNG",
    font=("Arial", 14, "bold"),
    height=2,
    bg="#8E44AD",
    fg="white",
    relief="groove",
    cursor="hand2", #đua chuot hien hinh ban tay
    command=lambda: hien_phancong(frame_xe, frame_laixe, frame_phancong)
)
btn_xe.grid(row=0, column=0, sticky="ew", padx =(1,3))
btn_laixe.grid(row=0, column=1, sticky="ew")
btn_phancong.grid(row=0, column=2, sticky="ew", padx = (3,1))


frame_menu.grid_columnconfigure(0, weight=1)
frame_menu.grid_columnconfigure(1, weight=1)
frame_menu.grid_columnconfigure(2, weight=1)

frame_menu.pack(fill="x")

frame_xe.pack(fill="both", expand=True) # cho frame_xe lam giao dien mặt đinhk=j

# ========= GIAO DIEN QUAN LY XE =========

frame_thongtin_xe = tk.LabelFrame( #tạo khung thong tin
    frame_xe,
    text="THÔNG TIN XE",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)

frame_thongtin_xe.pack(
    fill="x",
    padx=10,
    pady=10
)

label_maxe = tk.Label(
    frame_thongtin_xe,
    text="Mã xe:",
    font = ("Arial", 10, "bold"),
)

entry_maxe = tk.Entry(
    frame_thongtin_xe,
    width=25
)
label_maxe.grid(row=0, column=0, padx=5, pady=8)
entry_maxe.grid(row=0, column=1, padx=5, pady=8)

label_bienso = tk.Label(
    frame_thongtin_xe,
    text="Biển số:",
    font = ("Arial", 10, "bold"),
)

entry_bienso = tk.Entry(
    frame_thongtin_xe,
    width=25
)

label_bienso.grid(row=0, column=2, padx=5, pady=8)
entry_bienso.grid(row=0, column=3, padx=5, pady=8)

label_tenxe = tk.Label(
    frame_thongtin_xe,
    text="Tên xe:",
    font = ("Arial", 10, "bold"),
)

entry_tenxe = tk.Entry(
    frame_thongtin_xe,
    width=25
)
label_tenxe.grid(row=1, column=0, padx=5, pady=8)
entry_tenxe.grid(row=1, column=1, padx=5, pady=8)

label_maloai = tk.Label(
    frame_thongtin_xe,
    text="Mã loại:",
    font = ("Arial", 10, "bold"),)

entry_maloai = tk.Entry(
    frame_thongtin_xe,
    width=25
)

label_maloai.grid(row=1, column=2, padx=5, pady=8)
entry_maloai.grid(row=1, column=3, padx=5, pady=8)

label_trangthai = tk.Label(
    frame_thongtin_xe,
    text="Trạng thái:",
    font = ("Arial", 10, "bold"),
)

label_trangthai.grid(
    row=0,
    column=4,
    padx=5,
    pady=8
)

combo_trangthai = ttk.Combobox( #la loai ô cho phép ng dùng chọn 1 gia tri tu danh sách
    frame_thongtin_xe,
    values=["Đang hoạt động", "Bảo trì", "Ngừng hoạt động"],
    width=22,
    state="readonly" #ko cho phép ng dung nhap vao
)

combo_trangthai.grid(
    row=0,
    column=5,
    padx=5,
    pady=8
)
#=========KHU VUC HAM ===========
def chon_xe(event):
    selected = tree_xe.selection()

    if selected:
        xe = tree_xe.item(selected[0], 'values')

        entry_maxe.delete(0, 'end')
        entry_maxe.insert(0, xe[0])

        entry_bienso.delete(0, 'end')
        entry_bienso.insert(0, xe[1])

        entry_tenxe.delete(0, 'end')
        entry_tenxe.insert(0, xe[2])

        entry_maloai.delete(0, 'end')
        entry_maloai.insert(0, xe[3])

        combo_trangthai.set(xe[4])
def hien_thi_danh_sach_xe():
    danh_sach = xedao.get_all()

    for item in tree_xe.get_children():
        tree_xe.delete(item)

    for ds in danh_sach:
        tree_xe.insert(
            '',
            tk.END,
            values=(ds[0], ds[1], ds[2], ds[3], ds[4])
        )
def them_xe():
    maxe = entry_maxe.get().strip()
    bienso = entry_bienso.get().strip()
    tenxe = entry_tenxe.get().strip()
    maloai = entry_maloai.get().strip()
    trangthai = combo_trangthai.get().strip()

    # ===== KIỂM TRA RỖNG =====
    if maxe == "":
        messagebox.showwarning("CẢNH BÁO", "Vui lòng nhập Mã xe!")
        entry_maxe.focus()
        return

    if bienso == "":
        messagebox.showwarning("CẢNH BÁO", "Vui lòng nhập Biển số!")
        entry_bienso.focus()
        return

    if tenxe == "":
        messagebox.showwarning("CẢNH BÁO", "Vui lòng nhập Tên xe!")
        entry_tenxe.focus()
        return

    if maloai == "":
        messagebox.showwarning("CẢNH BÁO", "Vui lòng nhập Mã loại!")
        entry_maloai.focus()
        return

    if trangthai == "":
        messagebox.showwarning("CẢNH BÁO", "Vui lòng chọn Trạng thái!")
        combo_trangthai.focus()
        return
    if len(bienso) < 5:
        messagebox.showwarning(
            "CẢNH BÁO",
            "Biển số xe không hợp lệ!"
        )
        entry_bienso.focus()
        return
    maxe = maxe.upper()
    bienso = bienso.upper()
    tenxe = tenxe.title()
    maloai = maloai.upper()

    kq = xedao.them_xe(maxe, bienso, tenxe, maloai, trangthai)
    if kq:
        messagebox.showinfo("THÔNG BÁO", "THÊM XE THÀNH CÔNG!")
        hien_thi_danh_sach_xe()
    else:
        messagebox.showerror("ERROR", "THÊM XE THẤT BẠI!!!")

def xoa_xe():
    selected = tree_xe.selection()
    if not selected:
        messagebox.showerror("ERROR", "Vui Lòng Chọn Xe Cần Xóa!")
        return
    xoaxe = tree_xe.item(selected[0], 'values')
    maxexoa = xoaxe[0]
    kq = xedao.xoa_xe(maxexoa)
    if kq:
        messagebox.showinfo("THÔNG BÁO", "Xóa Xe Thành Công!")
        hien_thi_danh_sach_xe()
    else:
        messagebox.showerror("ERROR", "Xóa Xe Thất Bại!!!")
def sua_xe():
    selected = tree_xe.selection()
    if not selected:
        messagebox.showerror("ERROR", "Vui Lòng Chon Xe Cần Sửa")
        return
    xe = tree_xe.item(selected[0], 'values')
    maxe = xe[0]
    bienso = entry_bienso.get().strip()
    tenxe = entry_tenxe.get().strip()
    maloai = entry_maloai.get().strip()
    trangthai = combo_trangthai.get().strip()
    if bienso == "":
        messagebox.showwarning("CẢNH BÁO", "Vui lòng nhập Biển số!")
        entry_bienso.focus()
        return

    if tenxe == "":
        messagebox.showwarning("CẢNH BÁO", "Vui lòng nhập Tên xe!")
        entry_tenxe.focus()
        return

    if maloai == "":
        messagebox.showwarning("CẢNH BÁO", "Vui lòng nhập Mã loại!")
        entry_maloai.focus()
        return

    if trangthai == "":
        messagebox.showwarning("CẢNH BÁO", "Vui lòng chọn Trạng thái!")
        combo_trangthai.focus()
        return

    # ===== CHUẨN HÓA =====
    bienso = bienso.upper()
    tenxe = tenxe.title()
    maloai = maloai.upper()

    kq = xedao.sua_xe(maxe, bienso, tenxe, maloai, trangthai)

    if kq:
        messagebox.showinfo("THÔNG BÁO", "Cập Nhật Xe Thành Công")
        hien_thi_danh_sach_xe()
    else:
        messagebox.showerror("ERROR", "Cập Nhật Xe Thất Bại!")
def huy_xe():
    entry_maxe.delete(0, 'end')
    entry_bienso.delete(0, 'end')
    entry_tenxe.delete(0, 'end')
    entry_maloai.delete(0, 'end')
    combo_trangthai.set("")

    entry_maxe.focus()
def thong_ke_xe():
    ket_qua = xedao.thong_ke_xe()

    tong = 0
    dang_hoat_dong = 0
    bao_tri = 0
    ngung_hoat_dong = 0

    for xe in ket_qua:
        trangthai = xe[0]
        soluong = xe[1]

        tong += soluong

        if trangthai == "Đang hoạt động":
            dang_hoat_dong = soluong

        elif trangthai == "Bảo trì":
            bao_tri = soluong

        elif trangthai == "Ngừng hoạt động":
            ngung_hoat_dong = soluong

    messagebox.showinfo(
        "THỐNG KÊ XE",
        f"Tổng số xe: {tong}\n"
        f"Đang hoạt động: {dang_hoat_dong}\n"
        f"Đang bảo trì: {bao_tri}\n"
        f"Ngừng hoạt động: {ngung_hoat_dong}"
    )
def tim_kiem_theo_ten_xe():
    ten_xe = entry_timkiem.get().strip()
    if ten_xe == "":
        messagebox.showwarning(
            "CẢNH BÁO",
            "Vui lòng nhập tên xe cần tìm!"
        )
        entry_timkiem.focus()
        return
    danh_sach = xedao.tim_xe_theo_ten(ten_xe)
    for item in tree_xe.get_children():
        tree_xe.delete(item)
    for xe in danh_sach:
        tree_xe.insert('', tk.END, values=(xe[0], xe[1], xe[2], xe[3], xe[4]))
#============== FRAME BTN =========
frame_button = tk.Frame( frame_xe)
frame_button.pack(fill ='x', padx=10, pady =5)
button_themxe = tk.Button(
    frame_button,
    text ='THÊM XE',
    bg="#2563EB",
    fg="white",
    command = them_xe
)
button_themxe.grid(
    row = 0,
    column = 0,
    padx = 5,
    pady = 5,
    sticky="ew"
)
button_suaxe = tk.Button(
    frame_button,
    text='SỬA XE',
    bg="#2563EB",
    fg="white",
    command = sua_xe
)
button_suaxe.grid(
    row = 0,
    column = 1,
    padx = 5,
    pady = 5,
    sticky="ew"
)
button_xoaxe = tk.Button(
    frame_button,
    text='XÓA XE',
    bg='#DC2626',
    fg='white',
    command = xoa_xe
)
button_xoaxe.grid(
    row = 0,
    column = 2,
    padx = 5,
    pady = 5,
    sticky="ew"
)
button_huyxe = tk.Button(
    frame_button,
    text='HỦY',
    bg='#374151',
    fg='white',
    command = huy_xe
)
button_huyxe.grid(
    row = 0,
    column = 3,
    padx = 5,
    pady = 5,
    sticky="ew"
)
button_thongkexe = tk.Button(
    frame_button,
    text='THỐNG KÊ XE',
    bg ="#16A34A",
    fg ="white",
    command = thong_ke_xe
)
button_thongkexe.grid(
    row = 0,
    column = 4,
    padx = 5,
    pady = 5,
    sticky="ew"
)
button_danhsachxe = tk.Button(
    frame_button,
    text='DANH SÁCH XE',
    bg = '#7C3AED',
    fg = 'white',
    command = hien_thi_danh_sach_xe,
)
button_danhsachxe.grid(
    row = 0,
    column = 5,
    padx = 5,
    pady = 5,
    sticky="ew"
)
#========== FRAME TIM KIEM ==========

frame_timkiem = tk.Frame( frame_button)
frame_timkiem.grid(
    row=0,
    column=6,
    padx=5,
    pady=5,
    sticky="e"
)
label_timkiem = tk.Label(
    frame_timkiem,
    text ='Tên Xe: '
)
label_timkiem.grid(
    row=0,
    column=0,
    padx=3,
    pady=5,
)
entry_timkiem = tk.Entry(
    frame_timkiem,
    width=25
)
entry_timkiem.grid(
    row=0,
    column=1,
    padx=3,
    pady=5
)

button_timkiem = tk.Button(
    frame_timkiem,
    text="TÌM KIẾM",
    bg="#0891B2",
    fg="white",
    command = tim_kiem_theo_ten_xe
)

button_timkiem.grid(
    row=0,
    column=2,
    padx=5,
    pady=5
)

frame_button.grid_columnconfigure(0, weight=1)
frame_button.grid_columnconfigure(1, weight=1)
frame_button.grid_columnconfigure(2, weight=1)
frame_button.grid_columnconfigure(3, weight=1)
frame_button.grid_columnconfigure(4, weight=1)
frame_button.grid_columnconfigure(5, weight=1)
frame_button.grid_columnconfigure(6, weight=1)
#========== TREEVIEW ===========

frame_danhsach = tk.Frame(frame_xe)
frame_danhsach.pack(
    fill='both',
    expand=True,
    padx=10,
    pady=5
)

tree_xe = ttk.Treeview(
    frame_danhsach,
    columns=("MaXe", "BienSo", "TenXe", "MaLoai", "TrangThai"),
    show="headings"
)
tree_xe.heading("MaXe", text="Mã xe")
tree_xe.heading("BienSo", text="Biển số")
tree_xe.heading("TenXe", text="Tên xe")
tree_xe.heading("MaLoai", text="Mã loại")
tree_xe.heading("TrangThai", text="Trạng thái")

tree_xe.column("MaXe", width=100)
tree_xe.column("BienSo", width=120)
tree_xe.column("TenXe", width=250)
tree_xe.column("MaLoai", width=100)
tree_xe.column("TrangThai", width=180)

tree_xe.pack(
    fill="both",
    expand=True
)
tree_xe.bind("<<TreeviewSelect>>", chon_xe)
hien_thi_danh_sach_xe()

#===========THONG TIN LAI XE ============
frame_thongtin_laixe = tk.LabelFrame( #tạo khung thong tin
    frame_laixe,
    text="THÔNG TIN LÁI XE",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)
frame_thongtin_laixe.pack(
    fill="x",
    padx=10,
    pady =10,
)

label_malaixe = tk.Label(
    frame_thongtin_laixe,
    text ='Mã Lái Xe: ',
    font=("Arial", 10, "bold"),
)
label_malaixe.grid(
    row = 0,
    column =0,
    padx = 5,
    pady = 5,
)
entry_malaixe = tk.Entry(
    frame_thongtin_laixe,
    width=25
)
entry_malaixe.grid(
    row = 0,
    column=1,
    padx = 5,
    pady = 5,
)
label_hoten = tk.Label(
    frame_thongtin_laixe,
    text ='Họ Và Tên: ',
    font=("Arial", 10, 'bold'),
)
label_hoten.grid(
    row = 0,
    column=2,
    padx = 5,
    pady = 5,
)
entry_hoten = tk.Entry(
    frame_thongtin_laixe,
    width = 25,
)
entry_hoten.grid(
    row = 0,
    column=3,
    padx = 5,
    pady = 5,
)
label_sdt = tk.Label(
    frame_thongtin_laixe,
    text="Số Điện Thoại: ",
    font=("Arial", 10, 'bold'),
)
label_sdt.grid(
    row = 0,
    column=4,
    padx = 5,
    pady = 5,
)
entry_sdt = tk.Entry(
    frame_thongtin_laixe,
    width = 25,
)
entry_sdt.grid(
    row = 0,
    column=5,
    padx = 5,
    pady = 5,
)
label_sogplx = tk.Label(
    frame_thongtin_laixe,
    text = 'Số GPLX: ',
    font=("Arial", 10, 'bold'),
)
label_sogplx.grid(
    row = 1,
    column =0,
    padx = 5,
    pady = 5,
)
entry_sogplx = tk.Entry(
    frame_thongtin_laixe,
    width = 25,
)
entry_sogplx.grid(
    row = 1,
    column=1,
    padx = 5,
    pady = 5,
)
label_loaibang = tk.Label(
    frame_thongtin_laixe,
    text = 'Loại Bằng: ',
    font=("Arial", 10, 'bold'),
)
label_loaibang.grid(
    row =1,
    column=2,
    padx = 5,
    pady = 5,
)
entry_loaibang = tk.Entry(
    frame_thongtin_laixe,
    width = 25,
)
entry_loaibang.grid(
    row = 1,
    column=3,
    padx = 5,
    pady = 5,
)
label_trangthailaixe = tk.Label(
    frame_thongtin_laixe,
    text =' Trạng Thái: ',
    font=("Arial", 10, 'bold'),
)
label_trangthailaixe.grid(
    row =1,
    column=4,
    padx = 5,
    pady = 5,
)
combo_trangthailaixe = ttk.Combobox(
    frame_thongtin_laixe,
    values = ["Đang làm việc", "Tạm nghỉ"],
    width = 22,
    state="readonly"
)
combo_trangthailaixe.grid(
    row = 1,
    column=5,
    padx = 5,
    pady = 5,
)
#=============== CÁC HÀM TRONG BUTTON LÁI XA ===========
def them_lai_xe():
    malaixe = entry_malaixe.get().strip()
    hoten = entry_hoten.get().strip()
    sodienthoai = entry_sdt.get().strip()
    sogplx = entry_sogplx.get().strip()
    loaibang = entry_loaibang.get().strip()
    trangthailaixe = combo_trangthailaixe.get().strip()
    if malaixe == "":
        messagebox.showwarning("CẢNH BÁO", "Mã Lái Xe Không Được Để Trống!")
        entry_malaixe.focus()
        return
    if hoten == "":
        messagebox.showwarning("CẢNH BÁO", "Họ Và Tên Không Được Để Trống!")
        entry_hoten.focus()
        return

    if sodienthoai == "":
        messagebox.showwarning("CẢNH BÁO", "Số Điện Thoại Không Được Để Trống!")
        entry_sdt.focus()
        return

    if sogplx == "":
        messagebox.showwarning("CẢNH BÁO", "Số GPLX Không Được Để Trống!")
        entry_sogplx.focus()
        return

    if loaibang == "":
        messagebox.showwarning("CẢNH BÁO", "Loại Bằng Không Được Để Trống!")
        entry_loaibang.focus()
        return

    if trangthailaixe == "":
        messagebox.showwarning("CẢNH BÁO", "Trạng Thái Không Được Để Trống!")
        combo_trangthailaixe.focus()
        return

    #======== CHUẨN HÓA =========
    malaixe = malaixe.upper()
    hoten = hoten.title()
    sodienthoai = sodienthoai.upper()
    sogplx = sogplx.upper()
    loaibang = loaibang.upper()

    kq = laixedao.them_lai_xe(malaixe, hoten, sodienthoai, sogplx, loaibang, trangthailaixe)
    if kq:
        messagebox.showinfo("THÔNG BÁO", "Thêm Lái Xe Thành Công!")
    else:
        messagebox.showerror("ERROR", "Thêm Lái Xe Thất Bại !!!")

frame_buttonlaixe = tk.Frame(frame_laixe)
frame_buttonlaixe.pack(fill='x', padx=10, pady =10)

button_themlaixe = tk.Button(
    frame_buttonlaixe,
    text='THÊM LÁI XE',
    bg='#374151',
    fg='white',
    command = them_lai_xe
)
button_themlaixe.grid(
    row = 0,
    column = 0,
    sticky = 'ew',
    padx = (0,5),
    pady = 5,
)

button_sualaixe = tk.Button(
    frame_buttonlaixe,
    text='SỬA LÁI XE',
    bg='#374151',
    fg='white',
)
button_sualaixe.grid(
    row = 0,
    column = 1,
    sticky = 'ew',
    padx = 5,
    pady = 5,
)

button_xoalaixe = tk.Button(
    frame_buttonlaixe,
    text ='XÓA LÁI XE',
    bg='#374151',
    fg='white',
)
button_xoalaixe.grid(
    row = 0,
    column = 2,
    sticky = 'ew',
    padx = 5,
    pady = 5,
)
button_huylaixe = tk.Button(
    frame_buttonlaixe,
    text = 'HỦY',
    bg='#374151',
    fg='white',
)
button_huylaixe.grid(
    row = 0,
    column = 3,
    sticky = 'ew',
    padx = 5,
    pady = 5,
)
button_thongkelaixe = tk.Button(
    frame_buttonlaixe,
    text = 'THỐNG KÊ LÁI XE',
    bg = '#374151',
    fg = 'white',
)
button_thongkelaixe.grid(
    row = 0,
    column = 4,
    sticky = 'ew',
    padx=5,
    pady=5,
)
button_danhsachlaixe = tk.Button(
    frame_buttonlaixe,
    text = 'DANH SÁCH LÁI XE',
    bg='#374151',
    fg='white',
)
button_danhsachlaixe.grid(
    row = 0,
    column = 5,
    sticky = 'ew',
    padx=5,
    pady=5,
)
frame_timkiemlaixe = tk.Frame(frame_buttonlaixe)
frame_timkiemlaixe.grid(
    row = 0,
    column = 6,
    sticky = 'w'
)
label_timkiemlaixe = tk.Label(
    frame_timkiemlaixe,
    text ='Tên Lái Xe: ',
    font = ("Arial", 10, 'bold'),
)
label_timkiemlaixe.grid(
    row = 0,
    column = 0,
    padx = 5,
    pady = 5,
)
entry_timkiemlaixe = tk.Entry(
    frame_timkiemlaixe,
    width = 25,
)
entry_timkiemlaixe.grid(
    row = 0,
    column=1,
    padx = 5,
    pady = 5,
)
button_timkiemlaixe = tk.Button(
    frame_timkiemlaixe,
    text='TÌM KIẾM'
)
button_timkiemlaixe.grid(
    row = 0,
    column = 2,
)
frame_buttonlaixe.grid_columnconfigure(0, weight=1)
frame_buttonlaixe.grid_columnconfigure(1, weight=1)
frame_buttonlaixe.grid_columnconfigure(2, weight=1)
frame_buttonlaixe.grid_columnconfigure(3, weight=1)
frame_buttonlaixe.grid_columnconfigure(4, weight=1)
frame_buttonlaixe.grid_columnconfigure(5, weight=1)
frame_buttonlaixe.grid_columnconfigure(6, weight=1)
#===========TREE LAI XE ============
frame_danhsachlaixe = tk.Frame(frame_laixe)
frame_danhsachlaixe.pack(
    fill = 'both',
    expand = True,
    padx= 5,
    pady =5
)
tree_laixe = ttk.Treeview(
    frame_danhsachlaixe,
    columns = ("MaLaiXe", "HoTen", "SoDienThoai", "SoGPLX", "LoaiBang", "TrangThai"),
    show = 'headings',
)

tree_laixe.heading("MaLaiXe", text="Mã Lái Xe")
tree_laixe.heading("HoTen", text= "Họ Và Tên")
tree_laixe.heading("SoDienThoai", text= "Số Điện Thoại")
tree_laixe.heading("SoGPLX", text= "Số GPLX")
tree_laixe.heading("LoaiBang", text= "Loại Bằng")
tree_laixe.heading("TrangThai", text= "Trạng Thái")

tree_laixe.column("MaLaiXe", width=100)
tree_laixe.column("HoTen", width=180)
tree_laixe.column("SoDienThoai", width=140)
tree_laixe.column("SoGPLX", width=140)
tree_laixe.column("LoaiBang", width=80)
tree_laixe.column("TrangThai", width=160)

tree_laixe.pack(
    fill ='both',
    expand = True,
    padx=10,
    pady=10,
)
#=========== MAINLOOP ============
root.mainloop()