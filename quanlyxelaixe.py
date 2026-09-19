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
style = ttk.Style(root)
style.theme_use("clam")
style.configure(
    "Treeview.Heading",
    background="#18181B",
    foreground="white",
    font=("Arial", 10, "bold")
)
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
    fg ='#111111',
    font=("Segoe UI", 28, "bold")
)
label_tieude.pack()
frame_header.pack(
    fill = 'x',
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
    bg="#18181B",
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
    bg="#18181B",
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
    bg="#18181B",
    fg="white",
    relief="groove",
    cursor="hand2", #đua chuot hien hinh ban tay
    command=lambda: hien_phancong(frame_xe, frame_laixe, frame_phancong)
)
btn_xe.grid(row=0, column=0, sticky="ew",  pady = 5, padx =(0,5))
btn_laixe.grid(row=0, column=1, sticky="ew")
btn_phancong.grid(row=0, column=2, sticky="ew", padx = (5,0))


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
    bg="#18181B",
    fg="white",
    height = 2,
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
    bg="#18181B",
    fg="white",
    height=2,
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
    bg='#B91C1C',
    fg='white',
    height=2,
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
    bg='#CC0000',
    fg='white',
    height=2,
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
    bg ="#18181B",
    fg ="white",
    height=2,
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
    bg = '#18181B',
    fg = 'white',
    height=2,
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
    text ='Tên Xe: ',
    font = ("Arial", 10, 'bold'),
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
    bg="#1E293B",
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
#=============== CÁC HÀM TRONG BUTTON LÁI XE ===========
def chon_lai_xe(event):
    selected = tree_laixe.selection()
    if selected:
        laixe = tree_laixe.item(selected[0], 'values')

        entry_malaixe.delete(0, tk.END)
        entry_malaixe.insert(0, laixe[0])

        entry_hoten.delete(0, tk.END)
        entry_hoten.insert(0, laixe[1])

        entry_sdt.delete(0, tk.END)
        entry_sdt.insert(0, laixe[2])

        entry_sogplx.delete(0, tk.END)
        entry_sogplx.insert(0, laixe[3])

        entry_loaibang.delete(0, tk.END)
        entry_loaibang.insert(0, laixe[4])

        combo_trangthailaixe.set(laixe[5])

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
        hien_thi_danh_sach_lai_Xe()
    else:
        messagebox.showerror("ERROR", "Thêm Lái Xe Thất Bại !!!")

def hien_thi_danh_sach_lai_Xe():
    danh_sach = laixedao.get_all()
    for item in tree_laixe.get_children():
        tree_laixe.delete(item)
    for ds in danh_sach:
        tree_laixe.insert("", tk.END, values=(ds[0], ds[1], ds[2], ds[3], ds[4], ds[5]))
def sua_lai_xe():
    selected = tree_laixe.selection()
    if not selected:
        messagebox.showerror("ERROR", "Vui Lòng Chọn Xe Cần Xóa!")
        return
    laixe = tree_laixe.item(selected[0], 'values')
    malaixe = laixe[0]
    hoten = entry_hoten.get().strip()
    sodienthoai = entry_sdt.get().strip()
    sogplx = entry_sogplx.get().strip()
    loaibang = entry_loaibang.get().strip()
    trangthailaixe = combo_trangthailaixe.get()
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
    malaixe = malaixe.upper()
    hoten = hoten.title()
    sodienthoai = sodienthoai.upper()
    sogplx = sogplx.upper()
    loaibang = loaibang.upper()
    kq = laixedao.sua_lai_xe(malaixe, hoten, sodienthoai, sogplx, loaibang, trangthailaixe)
    if kq:
        messagebox.showinfo("THÔNG BÁO", "Cập Nhật Lái Xe Thành Công!")
        hien_thi_danh_sach_lai_Xe()
    else:
        messagebox.showerror("EROR", "Cập Nhật Lái Xe Thất Bại !")
def xoa_lai_xe():
    selected = tree_laixe.selection()
    if not selected:
        messagebox.showerror("ERROR", "Vui Lòng Chọn Lái Xe Cần Xóa !")
        return
    laixe = tree_laixe.item(selected[0], 'values')
    malaixe = laixe[0]
    kq = laixedao.xoa_lai_xe(malaixe)
    if kq:
        messagebox.showinfo("THÔNG BÁO", "Xóa Lái Xe Thành Công !")
        hien_thi_danh_sach_lai_Xe()
    else:
        messagebox.showerror("ERROR", "Xóa Lái Xe Thất Bại !")

def thong_ke_lai_xe():
    ket_qua = laixedao.thong_ke_lai_xe()

    tong = 0
    dang_lam_viec = 0
    tam_nghi = 0

    for laixe in ket_qua:
        trangthai = laixe[0]
        soluong = laixe[1]

        tong += soluong

        if trangthai == "Đang làm việc":
            dang_lam_viec = soluong
        elif trangthai == "Tạm nghỉ":
            tam_nghi = soluong

    messagebox.showinfo(
        "THỐNG KÊ XE",
        f"Tổng số lai xe: {tong}\n"
        f"Đang hoạt động: {dang_lam_viec}\n"
        f"Tạm Nghỉ: {tam_nghi}"
    )
def huy_lai_xe():
    entry_malaixe.delete(0, tk.END)
    entry_hoten.delete(0, tk.END)
    entry_sdt.delete(0, tk.END)
    entry_sogplx.delete(0, tk.END)
    entry_loaibang.delete(0, tk.END)
    combo_trangthailaixe.set("")

def tim_kiem_lai_xe_theo_ma():
    malaixe = entry_timkiemlaixe.get().strip()
    if malaixe == "":
        messagebox.showerror("ERROR", "Vui Lòng Nhập Mã Lái Xe Cần Tìm!")
        entry_timkiemlaixe.focus()
        return
    lx = laixedao.tim_lai_xe_theo_ma(malaixe)
    for item in tree_laixe.get_children():
        tree_laixe.delete(item)
    if lx:
        tree_laixe.insert("", tk.END, values=(lx[0], lx[1], lx[2], lx[3], lx[4], lx[5]))
    else:
        messagebox.showerror("ERROR", "Không Tìm Thấy Lái Xe !")

frame_buttonlaixe = tk.Frame(frame_laixe)
frame_buttonlaixe.pack(fill='x', padx=10, pady =10)

button_themlaixe = tk.Button(
    frame_buttonlaixe,
    text='THÊM LÁI XE',
    bg='#18181B',
    fg='white',
    height=2,
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
    bg='#18181B',
    fg='white',
    height=2,
    command = sua_lai_xe
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
    bg='#B91C1C',
    fg='white',
    height=2,
    command = xoa_lai_xe
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
    bg='#CC0000',
    fg='white',
    height=2,
    command = huy_lai_xe
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
    bg = '#18181B',
    fg = 'white',
    height=2,
    command = thong_ke_lai_xe
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
    bg='#18181B',
    fg='white',
    height=2,
    command = hien_thi_danh_sach_lai_Xe
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
    text='TÌM KIẾM',
    bg="#1E293B",
    fg ='#FFFFFF',
    command = tim_kiem_lai_xe_theo_ma
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
tree_laixe.bind('<<TreeviewSelect>>', chon_lai_xe)
hien_thi_danh_sach_lai_Xe()
#========== FRAME PHAN CONG ==========
frame_thongtin_phancong = tk.LabelFrame(
    frame_phancong,
    text="THÔNG TIN PHÂN CÔNG",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)

frame_thongtin_phancong.pack(
    fill="x",
    padx=10,
    pady=10
)


label_malaixe_pc = tk.Label(
    frame_thongtin_phancong,
    text="Mã lái xe:"
)

label_malaixe_pc.grid(
    row=0,
    column=0,
    padx=5,
    pady=8
)

entry_malaixe_pc = tk.Entry(
    frame_thongtin_phancong,
    width=25
)

entry_malaixe_pc.grid(
    row=0,
    column=1,
    padx=5,
    pady=8
)


label_maxe_pc = tk.Label(
    frame_thongtin_phancong,
    text="Mã xe:"
)

label_maxe_pc.grid(
    row=0,
    column=2,
    padx=5,
    pady=8
)

entry_maxe_pc = tk.Entry(
    frame_thongtin_phancong,
    width=25
)

entry_maxe_pc.grid(
    row=0,
    column=3,
    padx=5,
    pady=8
)




label_ngayphancong = tk.Label(
    frame_thongtin_phancong,
    text="Ngày phân công:"
)

label_ngayphancong.grid(
    row=1,
    column=0,
    padx=5,
    pady=8
)

entry_ngayphancong = tk.Entry(
    frame_thongtin_phancong,
    width=25
)

entry_ngayphancong.grid(
    row=1,
    column=1,
    padx=5,
    pady=8
)




label_trangthai_pc = tk.Label(
    frame_thongtin_phancong,
    text="Trạng thái:"
)

label_trangthai_pc.grid(
    row=1,
    column=2,
    padx=5,
    pady=8
)

combo_trangthai_pc = ttk.Combobox(
    frame_thongtin_phancong,
    values=[
        "Đang phân công",
        "Đã kết thúc"
    ],
    width=22,
    state="readonly"
)

combo_trangthai_pc.grid(
    row=1,
    column=3,
    padx=5,
    pady=8
)

def chon_phan_cong(event):

    selected = tree_phancong.selection()

    if selected:

        pc = tree_phancong.item(
            selected[0],
            "values"
        )

        entry_malaixe_pc.delete(0, tk.END)
        entry_malaixe_pc.insert(0, pc[1])

        entry_maxe_pc.delete(0, tk.END)
        entry_maxe_pc.insert(0, pc[2])

        entry_ngayphancong.delete(0, tk.END)
        entry_ngayphancong.insert(0, pc[3])

        combo_trangthai_pc.set(pc[4])



def hien_thi_danh_sach_phancong():

    danh_sach = phancongdao.get_all()

    for item in tree_phancong.get_children():
        tree_phancong.delete(item)

    for pc in danh_sach:

        tree_phancong.insert(
            "",
            tk.END,
            values=(
                pc[0],
                pc[1],
                pc[2],
                pc[3],
                pc[4]
            )
        )

def them_phan_cong():

    malaixe = entry_malaixe_pc.get().strip()
    maxe = entry_maxe_pc.get().strip()
    ngayphancong = entry_ngayphancong.get().strip()
    trangthai = combo_trangthai_pc.get().strip()

    if malaixe == "":
        messagebox.showwarning(
            "CẢNH BÁO",
            "Vui lòng nhập mã lái xe!"
        )

        entry_malaixe_pc.focus()
        return

    if maxe == "":
        messagebox.showwarning(
            "CẢNH BÁO",
            "Vui lòng nhập mã xe!"
        )
        entry_maxe_pc.focus()
        return

    if ngayphancong == "":
        messagebox.showwarning(
            "CẢNH BÁO",
            "Vui lòng nhập ngày phân công!"
        )
        entry_ngayphancong.focus()
        return

    if trangthai == "":
        messagebox.showwarning(
            "CẢNH BÁO",
            "Vui lòng chọn trạng thái!"
        )
        combo_trangthai_pc.focus()
        return

    malaixe = malaixe.upper()
    maxe = maxe.upper()

    kq = phancongdao.them_phancong(
        malaixe,
        maxe,
        ngayphancong,
        trangthai
    )

    if kq:

        messagebox.showinfo(
            "THÔNG BÁO",
            "THÊM PHÂN CÔNG THÀNH CÔNG!"
        )

        hien_thi_danh_sach_phancong()

    else:

        messagebox.showerror(
            "ERROR",
            "THÊM PHÂN CÔNG THẤT BẠI!"
        )

def sua_phan_cong():

    selected = tree_phancong.selection()

    if not selected:

        messagebox.showwarning(
            "CẢNH BÁO",
            "Vui lòng chọn phân công cần sửa!"
        )
        return

    pc = tree_phancong.item(
        selected[0],
        "values"
    )

    maphancong = pc[0]

    malaixe = entry_malaixe_pc.get().strip()
    maxe = entry_maxe_pc.get().strip()
    ngayphancong = entry_ngayphancong.get().strip()
    trangthai = combo_trangthai_pc.get().strip()

    if malaixe == "" or maxe == "" or ngayphancong == "" or trangthai == "":
        messagebox.showwarning(
            "CẢNH BÁO",
            "Vui lòng nhập đầy đủ thông tin!"
        )
        return

    kq = phancongdao.sua_phancong(
        maphancong,
        malaixe.upper(),
        maxe.upper(),
        ngayphancong,
        trangthai
    )

    if kq:

        messagebox.showinfo(
            "THÔNG BÁO",
            "SỬA PHÂN CÔNG THÀNH CÔNG!"
        )

        hien_thi_danh_sach_phancong()

    else:

        messagebox.showerror(
            "ERROR",
            "SỬA PHÂN CÔNG THẤT BẠI!"
        )



def xoa_phan_cong():

    selected = tree_phancong.selection()

    if not selected:

        messagebox.showwarning(
            "CẢNH BÁO",
            "Vui lòng chọn phân công cần xóa!"
        )
        return

    pc = tree_phancong.item(
        selected[0],
        "values"
    )

    maphancong = pc[0]

    xacnhan = messagebox.askyesno(
        "XÁC NHẬN",
        f"Bạn có chắc muốn xóa phân công {maphancong}?"
    )

    if not xacnhan:
        return

    kq = phancongdao.Xoa_phancong(
        maphancong
    )

    if kq:

        messagebox.showinfo(
            "THÔNG BÁO",
            "XÓA PHÂN CÔNG THÀNH CÔNG!"
        )

        hien_thi_danh_sach_phancong()

    else:

        messagebox.showerror(
            "ERROR",
            "XÓA PHÂN CÔNG THẤT BẠI!"
        )




def huy_phan_cong():

    entry_malaixe_pc.delete(
        0,
        tk.END
    )

    entry_maxe_pc.delete(
        0,
        tk.END
    )

    entry_ngayphancong.delete(
        0,
        tk.END
    )

    combo_trangthai_pc.set("")



frame_button_phancong = tk.Frame(
    frame_phancong
)

frame_button_phancong.pack(
    fill="x",
    padx=10,
    pady=5
)


button_themphancong = tk.Button(
    frame_button_phancong,
    text="THÊM PHÂN CÔNG",
    bg="#18181B",
    fg="white",
    height=2,
    font=("Arial", 10, "bold"),
    command=them_phan_cong
)

button_themphancong.grid(
    row=0,
    column=0,
    padx=5,
    pady=5,
    sticky="ew"
)


button_suaphancong = tk.Button(
    frame_button_phancong,
    text="SỬA PHÂN CÔNG",
    bg="#18181B",
    fg="white",
    height=2,
    font=("Arial", 10, "bold"),
    command=sua_phan_cong
)

button_suaphancong.grid(
    row=0,
    column=1,
    padx=5,
    pady=5,
    sticky="ew"
)


button_xoaphancong = tk.Button(
    frame_button_phancong,
    text="XÓA PHÂN CÔNG",
    bg="#B91C1C",
    fg="white",
    height=2,
    font=("Arial", 10, "bold"),
    command=xoa_phan_cong
)

button_xoaphancong.grid(
    row=0,
    column=2,
    padx=5,
    pady=5,
    sticky="ew"
)


button_huyphancong = tk.Button(
    frame_button_phancong,
    text="HỦY",
    bg="#CC0000",
    fg="white",
    height=2,
    font=("Arial", 10, "bold"),
    command=huy_phan_cong
)

button_huyphancong.grid(
    row=0,
    column=3,
    padx=5,
    pady=5,
    sticky="ew"
)


for i in range(4):

    frame_button_phancong.grid_columnconfigure(
        i,
        weight=1
    )


# ======== TREE PHAN CÔNG =============

frame_danhsachphancong = tk.LabelFrame(
    frame_phancong,
    text="DANH SÁCH PHÂN CÔNG",
    font=("Arial", 12, "bold"),
    padx=5,
    pady=5
)

frame_danhsachphancong.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=5
)


# =========================================================
#                     TREEVIEW
# =========================================================

tree_phancong = ttk.Treeview(
    frame_danhsachphancong,
    columns=(
        "MaPhanCong",
        "MaLaiXe",
        "MaXe",
        "NgayPhanCong",
        "TrangThai"
    ),
    show="headings"
)


tree_phancong.heading(
    "MaPhanCong",
    text="Mã phân công"
)

tree_phancong.heading(
    "MaLaiXe",
    text="Mã lái xe"
)

tree_phancong.heading(
    "MaXe",
    text="Mã xe"
)

tree_phancong.heading(
    "NgayPhanCong",
    text="Ngày phân công"
)

tree_phancong.heading(
    "TrangThai",
    text="Trạng thái"
)


tree_phancong.column(
    "MaPhanCong",
    width=150,
    anchor="center"
)

tree_phancong.column(
    "MaLaiXe",
    width=150,
    anchor="center"
)

tree_phancong.column(
    "MaXe",
    width=150,
    anchor="center"
)

tree_phancong.column(
    "NgayPhanCong",
    width=180,
    anchor="center"
)

tree_phancong.column(
    "TrangThai",
    width=200,
    anchor="center"
)


tree_phancong.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


tree_phancong.bind(
    "<<TreeviewSelect>>",
    chon_phan_cong
)


# Hiển thị danh sách khi chạy chương trình
hien_thi_danh_sach_phancong()
#=========== MAINLOOP ============
root.mainloop()