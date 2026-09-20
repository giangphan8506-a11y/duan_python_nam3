USE QuanLyXeLaiXe;
GO

-- ==========================================
-- XÓA CÁC BẢNG CŨ
-- ==========================================

DROP TABLE IF EXISTS PhanCong;
DROP TABLE IF EXISTS Xe;
DROP TABLE IF EXISTS LaiXe;
DROP TABLE IF EXISTS LoaiXe;
GO


-- ==========================================
-- TẠO BẢNG LAIXE
-- ==========================================

CREATE TABLE LaiXe
(
    MaLaiXe VARCHAR(10) PRIMARY KEY,

    HoTen NVARCHAR(100) NOT NULL,

    SoDienThoai VARCHAR(15),

    SoGPLX VARCHAR(20) NOT NULL UNIQUE,

    LoaiBang VARCHAR(10) NOT NULL,

    TrangThai NVARCHAR(30) NOT NULL
);
GO


-- ==========================================
-- TẠO BẢNG XE
-- ==========================================

CREATE TABLE Xe
(
    MaXe VARCHAR(10) PRIMARY KEY,

    BienSo VARCHAR(15) NOT NULL UNIQUE,

    TenXe NVARCHAR(100) NOT NULL,

    MaLoai VARCHAR(10) NOT NULL,

    TrangThai NVARCHAR(30) NOT NULL
);
GO


-- ==========================================
-- TẠO BẢNG PHANCONG
-- ==========================================

CREATE TABLE PhanCong
(
    MaPhanCong INT IDENTITY(1,1) PRIMARY KEY,

    MaLaiXe VARCHAR(10) NOT NULL,

    MaXe VARCHAR(10) NOT NULL,

    NgayPhanCong DATE NOT NULL,

    NgayKetThuc DATE NULL,

    TrangThai NVARCHAR(30) NOT NULL,


    -- KHÓA NGOẠI TỚI LAIXE
    CONSTRAINT FK_PhanCong_LaiXe
        FOREIGN KEY (MaLaiXe)
        REFERENCES LaiXe(MaLaiXe),


    -- KHÓA NGOẠI TỚI XE
    CONSTRAINT FK_PhanCong_Xe
        FOREIGN KEY (MaXe)
        REFERENCES Xe(MaXe),


    -- NGÀY KẾT THÚC KHÔNG ĐƯỢC NHỎ HƠN NGÀY PHÂN CÔNG
    CONSTRAINT CK_PhanCong_Ngay
        CHECK
        (
            NgayKetThuc IS NULL
            OR NgayKetThuc >= NgayPhanCong
        )
);

CREATE TABLE LoaiXe
(
    MaLoai VARCHAR(10) PRIMARY KEY,
    TenLoai NVARCHAR(50) NOT NULL
);
GO
ALTER TABLE Xe
ADD CONSTRAINT FK_Xe_LoaiXe
FOREIGN KEY (MaLoai)
REFERENCES LoaiXe(MaLoai);


INSERT INTO LoaiXe (MaLoai, TenLoai)
VALUES
('L01', N'Xe 4 chỗ'),
('L02', N'Xe 5 chỗ'),
('L03', N'Xe 7 chỗ'),
('L04', N'Xe bán tải'),
('L05', N'Xe SUV'),
('L06', N'Xe sedan'),
('L07', N'Xe MPV'),
('L08', N'Xe địa hình'),
('L09', N'Xe sang'),
('L10', N'Xe đa dụng');
GO

INSERT INTO Xe
(MaXe, BienSo, TenXe, MaLoai, TrangThai)
VALUES
('X01', '67A-10001', N'Toyota Vios', 'L02', N'Đang hoạt động'),
('X02', '67A-10002', N'Toyota Camry', 'L06', N'Đang hoạt động'),
('X03', '67A-10003', N'Toyota Innova', 'L03', N'Đang hoạt động'),
('X04', '67A-10004', N'Toyota Fortuner', 'L05', N'Bảo trì'),
('X05', '67A-10005', N'Toyota Hilux', 'L04', N'Đang hoạt động'),
('X06', '67A-10006', N'Toyota Corolla Cross', 'L05', N'Đang hoạt động'),
('X07', '67A-10007', N'Toyota Yaris', 'L02', N'Ngừng hoạt động'),
('X08', '67A-10008', N'Toyota Raize', 'L05', N'Đang hoạt động'),
('X09', '67A-10009', N'Toyota Corolla Altis', 'L06', N'Đang hoạt động'),
('X10', '67A-10010', N'Toyota Land Cruiser', 'L09', N'Bảo trì'),

('X11', '67A-10011', N'Toyota Avanza Premio', 'L07', N'Đang hoạt động'),
('X12', '67A-10012', N'Toyota Wigo', 'L02', N'Đang hoạt động'),
('X13', '67A-10013', N'Toyota Rush', 'L05', N'Đang hoạt động'),
('X14', '67A-10014', N'Toyota Hiace', 'L10', N'Bảo trì'),
('X15', '67A-10015', N'Toyota Alphard', 'L09', N'Đang hoạt động'),
('X16', '67A-10016', N'Toyota Prado', 'L08', N'Đang hoạt động'),
('X17', '67A-10017', N'Toyota Supra', 'L06', N'Đang hoạt động'),
('X18', '67A-10018', N'Toyota GR86', 'L06', N'Ngừng hoạt động'),
('X19', '67A-10019', N'Toyota Sienna', 'L07', N'Đang hoạt động'),
('X20', '67A-10020', N'Toyota Tacoma', 'L04', N'Đang hoạt động'),

('X21', '67A-10021', N'Toyota Tundra', 'L04', N'Bảo trì'),
('X22', '67A-10022', N'Toyota Sequoia', 'L05', N'Đang hoạt động'),
('X23', '67A-10023', N'Toyota Highlander', 'L05', N'Đang hoạt động'),
('X24', '67A-10024', N'Toyota RAV4', 'L05', N'Đang hoạt động'),
('X25', '67A-10025', N'Toyota Prius', 'L06', N'Đang hoạt động'),
('X26', '67A-10026', N'Toyota C-HR', 'L05', N'Bảo trì'),
('X27', '67A-10027', N'Toyota Mirai', 'L06', N'Đang hoạt động'),
('X28', '67A-10028', N'Toyota Venza', 'L05', N'Đang hoạt động'),
('X29', '67A-10029', N'Toyota Crown', 'L09', N'Ngừng hoạt động'),
('X30', '67A-10030', N'Toyota Century', 'L09', N'Đang hoạt động'),

('X31', '67A-10031', N'Toyota Sienta', 'L07', N'Đang hoạt động'),
('X32', '67A-10032', N'Toyota Estima', 'L07', N'Đang hoạt động'),
('X33', '67A-10033', N'Toyota FJ Cruiser', 'L08', N'Bảo trì'),
('X34', '67A-10034', N'Toyota 4Runner', 'L08', N'Đang hoạt động'),
('X35', '67A-10035', N'Toyota Sequoia', 'L05', N'Đang hoạt động'),
('X36', '67A-10036', N'Toyota Aygo', 'L02', N'Ngừng hoạt động'),
('X37', '67A-10037', N'Toyota Corolla', 'L06', N'Đang hoạt động'),
('X38', '67A-10038', N'Toyota Avalon', 'L06', N'Đang hoạt động'),
('X39', '67A-10039', N'Toyota Venza', 'L05', N'Bảo trì'),
('X40', '67A-10040', N'Toyota Matrix', 'L10', N'Đang hoạt động'),

('X41', '67A-10041', N'Toyota Proace', 'L10', N'Đang hoạt động'),
('X42', '67A-10042', N'Toyota Granvia', 'L10', N'Đang hoạt động'),
('X43', '67A-10043', N'Toyota Harrier', 'L05', N'Đang hoạt động'),
('X44', '67A-10044', N'Toyota Kluger', 'L05', N'Bảo trì'),
('X45', '67A-10045', N'Toyota Mark X', 'L06', N'Đang hoạt động'),
('X46', '67A-10046', N'Toyota Belta', 'L06', N'Đang hoạt động'),
('X47', '67A-10047', N'Toyota Caldina', 'L10', N'Ngừng hoạt động'),
('X48', '67A-10048', N'Toyota Voxy', 'L07', N'Đang hoạt động'),
('X49', '67A-10049', N'Toyota Noah', 'L07', N'Đang hoạt động'),
('X50', '67A-10050', N'Toyota Land Cruiser Prado', 'L08', N'Đang hoạt động');
GO

INSERT INTO LaiXe
(MaLaiXe, HoTen, SoDienThoai, SoGPLX, LoaiBang, TrangThai)
VALUES
('LX01', N'Nguyễn Văn An', '0901000001', '790100000001', 'B2', N'Đang làm việc'),
('LX02', N'Trần Văn Bình', '0901000002', '790100000002', 'B2', N'Đang làm việc'),
('LX03', N'Lê Minh Cường', '0901000003', '790100000003', 'C', N'Đang làm việc'),
('LX04', N'Phạm Văn Dũng', '0901000004', '790100000004', 'B2', N'Đang làm việc'),
('LX05', N'Võ Hoàng Nam', '0901000005', '790100000005', 'C', N'Tạm nghỉ'),
('LX06', N'Đặng Minh Tuấn', '0901000006', '790100000006', 'B2', N'Đang làm việc'),
('LX07', N'Nguyễn Hoàng Long', '0901000007', '790100000007', 'C', N'Đang làm việc'),
('LX08', N'Trần Minh Đức', '0901000008', '790100000008', 'B2', N'Đang làm việc'),
('LX09', N'Lê Quốc Huy', '0901000009', '790100000009', 'B2', N'Đang làm việc'),
('LX10', N'Phan Thanh Tùng', '0901000010', '790100000010', 'C', N'Tạm nghỉ'),

('LX11', N'Nguyễn Minh Khang', '0901000011', '790100000011', 'B2', N'Đang làm việc'),
('LX12', N'Đỗ Văn Thành', '0901000012', '790100000012', 'C', N'Đang làm việc'),
('LX13', N'Bùi Anh Tuấn', '0901000013', '790100000013', 'B2', N'Đang làm việc'),
('LX14', N'Huỳnh Minh Hoàng', '0901000014', '790100000014', 'B2', N'Tạm nghỉ'),
('LX15', N'Vũ Đức Anh', '0901000015', '790100000015', 'C', N'Đang làm việc'),
('LX16', N'Nguyễn Thành Đạt', '0901000016', '790100000016', 'B2', N'Đang làm việc'),
('LX17', N'Trần Quốc Việt', '0901000017', '790100000017', 'C', N'Đang làm việc'),
('LX18', N'Lê Hoàng Phúc', '0901000018', '790100000018', 'B2', N'Đang làm việc'),
('LX19', N'Phạm Minh Khôi', '0901000019', '790100000019', 'B2', N'Đang làm việc'),
('LX20', N'Võ Văn Hùng', '0901000020', '790100000020', 'C', N'Tạm nghỉ'),

('LX21', N'Nguyễn Đức Thịnh', '0901000021', '790100000021', 'B2', N'Đang làm việc'),
('LX22', N'Trần Anh Khoa', '0901000022', '790100000022', 'B2', N'Đang làm việc'),
('LX23', N'Lê Văn Sơn', '0901000023', '790100000023', 'C', N'Đang làm việc'),
('LX24', N'Phạm Minh Tâm', '0901000024', '790100000024', 'B2', N'Đang làm việc'),
('LX25', N'Đặng Quốc Bảo', '0901000025', '790100000025', 'C', N'Tạm nghỉ'),
('LX26', N'Nguyễn Hoàng Nam', '0901000026', '790100000026', 'B2', N'Đang làm việc'),
('LX27', N'Trần Minh Quân', '0901000027', '790100000027', 'C', N'Đang làm việc'),
('LX28', N'Bùi Văn Phong', '0901000028', '790100000028', 'B2', N'Đang làm việc'),
('LX29', N'Võ Minh Trí', '0901000029', '790100000029', 'B2', N'Đang làm việc'),
('LX30', N'Phạm Hoàng Sơn', '0901000030', '790100000030', 'C', N'Đang làm việc'),

('LX31', N'Nguyễn Văn Khánh', '0901000031', '790100000031', 'B2', N'Đang làm việc'),
('LX32', N'Trần Văn Phúc', '0901000032', '790100000032', 'C', N'Đang làm việc'),
('LX33', N'Lê Minh Tân', '0901000033', '790100000033', 'B2', N'Tạm nghỉ'),
('LX34', N'Phạm Quốc Trung', '0901000034', '790100000034', 'C', N'Đang làm việc'),
('LX35', N'Võ Thành Công', '0901000035', '790100000035', 'B2', N'Đang làm việc'),
('LX36', N'Đặng Hoàng Nam', '0901000036', '790100000036', 'C', N'Đang làm việc'),
('LX37', N'Nguyễn Đức Huy', '0901000037', '790100000037', 'B2', N'Đang làm việc'),
('LX38', N'Trần Minh Hoàng', '0901000038', '790100000038', 'C', N'Đang làm việc'),
('LX39', N'Lê Quốc Thắng', '0901000039', '790100000039', 'B2', N'Đang làm việc'),
('LX40', N'Phạm Văn Hậu', '0901000040', '790100000040', 'C', N'Tạm nghỉ'),

('LX41', N'Nguyễn Thành Long', '0901000041', '790100000041', 'B2', N'Đang làm việc'),
('LX42', N'Đỗ Minh Nhật', '0901000042', '790100000042', 'C', N'Đang làm việc'),
('LX43', N'Bùi Quốc Khánh', '0901000043', '790100000043', 'B2', N'Đang làm việc'),
('LX44', N'Huỳnh Văn Nam', '0901000044', '790100000044', 'C', N'Đang làm việc'),
('LX45', N'Võ Minh Tâm', '0901000045', '790100000045', 'B2', N'Đang làm việc'),
('LX46', N'Nguyễn Hoàng Phúc', '0901000046', '790100000046', 'C', N'Đang làm việc'),
('LX47', N'Trần Quốc Hưng', '0901000047', '790100000047', 'B2', N'Tạm nghỉ'),
('LX48', N'Lê Văn Phú', '0901000048', '790100000048', 'C', N'Đang làm việc'),
('LX49', N'Phạm Minh Quân', '0901000049', '790100000049', 'B2', N'Đang làm việc'),
('LX50', N'Đặng Văn Thành', '0901000050', '790100000050', 'C', N'Đang làm việc');
GO

INSERT INTO PhanCong
(MaLaiXe, MaXe, NgayPhanCong, NgayKetThuc, TrangThai)
VALUES

('LX01', 'X01', '2026-09-01', NULL, N'Đang phân công'),
('LX02', 'X02', '2026-09-01', NULL, N'Đang phân công'),
('LX03', 'X03', '2026-09-02', NULL, N'Đang phân công'),
('LX04', 'X05', '2026-09-02', NULL, N'Đang phân công'),
('LX06', 'X06', '2026-09-03', NULL, N'Đang phân công'),
('LX07', 'X08', '2026-09-03', NULL, N'Đang phân công'),
('LX08', 'X09', '2026-09-04', NULL, N'Đang phân công'),
('LX09', 'X11', '2026-09-04', NULL, N'Đang phân công'),
('LX11', 'X12', '2026-09-05', NULL, N'Đang phân công'),
('LX12', 'X13', '2026-09-05', NULL, N'Đang phân công'),

('LX13', 'X15', '2026-09-06', NULL, N'Đang phân công'),
('LX15', 'X16', '2026-09-06', NULL, N'Đang phân công'),
('LX16', 'X17', '2026-09-07', NULL, N'Đang phân công'),
('LX17', 'X19', '2026-09-07', NULL, N'Đang phân công'),
('LX18', 'X20', '2026-09-08', NULL, N'Đang phân công'),
('LX19', 'X22', '2026-09-08', NULL, N'Đang phân công'),
('LX21', 'X23', '2026-09-09', NULL, N'Đang phân công'),
('LX22', 'X24', '2026-09-09', NULL, N'Đang phân công'),
('LX23', 'X25', '2026-09-10', NULL, N'Đang phân công'),
('LX24', 'X27', '2026-09-10', NULL, N'Đang phân công'),

('LX26', 'X28', '2026-09-11', NULL, N'Đang phân công'),
('LX27', 'X30', '2026-09-11', NULL, N'Đang phân công'),
('LX28', 'X31', '2026-09-12', NULL, N'Đang phân công'),
('LX29', 'X32', '2026-09-12', NULL, N'Đang phân công'),
('LX30', 'X34', '2026-09-13', NULL, N'Đang phân công'),
('LX31', 'X35', '2026-09-13', NULL, N'Đang phân công'),
('LX32', 'X37', '2026-09-14', NULL, N'Đang phân công'),
('LX34', 'X38', '2026-09-14', NULL, N'Đang phân công'),
('LX35', 'X40', '2026-09-15', NULL, N'Đang phân công'),
('LX36', 'X41', '2026-09-15', NULL, N'Đang phân công');
GO

INSERT INTO PhanCong
(MaLaiXe, MaXe, NgayPhanCong, NgayKetThuc, TrangThai)
VALUES

('LX01', 'X03', '2026-08-01', '2026-08-05', N'Đã kết thúc'),
('LX02', 'X05', '2026-08-02', '2026-08-07', N'Đã kết thúc'),
('LX03', 'X06', '2026-08-03', '2026-08-08', N'Đã kết thúc'),
('LX04', 'X08', '2026-08-04', '2026-08-09', N'Đã kết thúc'),
('LX06', 'X09', '2026-08-05', '2026-08-10', N'Đã kết thúc'),
('LX07', 'X11', '2026-08-06', '2026-08-11', N'Đã kết thúc'),
('LX08', 'X12', '2026-08-07', '2026-08-12', N'Đã kết thúc'),
('LX09', 'X13', '2026-08-08', '2026-08-13', N'Đã kết thúc'),
('LX11', 'X15', '2026-08-09', '2026-08-14', N'Đã kết thúc'),
('LX12', 'X16', '2026-08-10', '2026-08-15', N'Đã kết thúc'),

('LX13', 'X17', '2026-08-11', '2026-08-16', N'Đã kết thúc'),
('LX15', 'X19', '2026-08-12', '2026-08-17', N'Đã kết thúc'),
('LX16', 'X20', '2026-08-13', '2026-08-18', N'Đã kết thúc'),
('LX17', 'X22', '2026-08-14', '2026-08-19', N'Đã kết thúc'),
('LX18', 'X23', '2026-08-15', '2026-08-20', N'Đã kết thúc'),
('LX19', 'X24', '2026-08-16', '2026-08-21', N'Đã kết thúc'),
('LX21', 'X25', '2026-08-17', '2026-08-22', N'Đã kết thúc'),
('LX22', 'X27', '2026-08-18', '2026-08-23', N'Đã kết thúc'),
('LX23', 'X28', '2026-08-19', '2026-08-24', N'Đã kết thúc'),
('LX24', 'X30', '2026-08-20', '2026-08-25', N'Đã kết thúc'),

('LX26', 'X31', '2026-08-21', '2026-08-26', N'Đã kết thúc'),
('LX27', 'X32', '2026-08-22', '2026-08-27', N'Đã kết thúc'),
('LX28', 'X34', '2026-08-23', '2026-08-28', N'Đã kết thúc'),
('LX29', 'X35', '2026-08-24', '2026-08-29', N'Đã kết thúc'),
('LX30', 'X37', '2026-08-25', '2026-08-30', N'Đã kết thúc'),
('LX31', 'X38', '2026-08-26', '2026-08-31', N'Đã kết thúc'),
('LX32', 'X40', '2026-08-27', '2026-09-01', N'Đã kết thúc'),
('LX34', 'X41', '2026-08-28', '2026-09-02', N'Đã kết thúc'),
('LX35', 'X42', '2026-08-29', '2026-09-03', N'Đã kết thúc'),
('LX36', 'X43', '2026-08-30', '2026-09-04', N'Đã kết thúc'),

-- Các phân công cũ

('LX37', 'X01', '2026-07-01', '2026-07-05', N'Đã kết thúc'),
('LX38', 'X02', '2026-07-02', '2026-07-06', N'Đã kết thúc'),
('LX39', 'X03', '2026-07-03', '2026-07-07', N'Đã kết thúc'),
('LX41', 'X05', '2026-07-04', '2026-07-08', N'Đã kết thúc'),
('LX42', 'X06', '2026-07-05', '2026-07-09', N'Đã kết thúc'),
('LX43', 'X08', '2026-07-06', '2026-07-10', N'Đã kết thúc'),
('LX44', 'X09', '2026-07-07', '2026-07-11', N'Đã kết thúc'),
('LX45', 'X11', '2026-07-08', '2026-07-12', N'Đã kết thúc'),
('LX46', 'X12', '2026-07-09', '2026-07-13', N'Đã kết thúc'),
('LX48', 'X13', '2026-07-10', '2026-07-14', N'Đã kết thúc'),

('LX49', 'X15', '2026-07-11', '2026-07-15', N'Đã kết thúc'),
('LX50', 'X16', '2026-07-12', '2026-07-16', N'Đã kết thúc'),
('LX01', 'X17', '2026-07-13', '2026-07-17', N'Đã kết thúc'),
('LX02', 'X19', '2026-07-14', '2026-07-18', N'Đã kết thúc'),
('LX03', 'X20', '2026-07-15', '2026-07-19', N'Đã kết thúc'),
('LX04', 'X22', '2026-07-16', '2026-07-20', N'Đã kết thúc'),
('LX06', 'X23', '2026-07-17', '2026-07-21', N'Đã kết thúc'),
('LX07', 'X24', '2026-07-18', '2026-07-22', N'Đã kết thúc'),
('LX08', 'X25', '2026-07-19', '2026-07-23', N'Đã kết thúc'),
('LX09', 'X27', '2026-07-20', '2026-07-24', N'Đã kết thúc'),

-- Lịch sử với lái xe hiện đang tạm nghỉ

('LX05', 'X04', '2026-06-01', '2026-06-10', N'Đã kết thúc'),
('LX10', 'X10', '2026-06-02', '2026-06-11', N'Đã kết thúc'),
('LX14', 'X14', '2026-06-03', '2026-06-12', N'Đã kết thúc'),
('LX20', 'X18', '2026-06-04', '2026-06-13', N'Đã kết thúc'),
('LX25', 'X21', '2026-06-05', '2026-06-14', N'Đã kết thúc'),
('LX33', 'X26', '2026-06-06', '2026-06-15', N'Đã kết thúc'),
('LX40', 'X29', '2026-06-07', '2026-06-16', N'Đã kết thúc'),
('LX47', 'X33', '2026-06-08', '2026-06-17', N'Đã kết thúc'),

-- Lịch sử với xe hiện bảo trì/ngừng hoạt động

('LX11', 'X04', '2026-05-01', '2026-05-08', N'Đã kết thúc'),
('LX12', 'X10', '2026-05-02', '2026-05-09', N'Đã kết thúc'),
('LX13', 'X14', '2026-05-03', '2026-05-10', N'Đã kết thúc'),
('LX15', 'X18', '2026-05-04', '2026-05-11', N'Đã kết thúc'),
('LX16', 'X21', '2026-05-05', '2026-05-12', N'Đã kết thúc'),
('LX17', 'X26', '2026-05-06', '2026-05-13', N'Đã kết thúc'),
('LX18', 'X29', '2026-05-07', '2026-05-14', N'Đã kết thúc'),
('LX19', 'X33', '2026-05-08', '2026-05-15', N'Đã kết thúc'),
('LX21', 'X36', '2026-05-09', '2026-05-16', N'Đã kết thúc'),
('LX22', 'X39', '2026-05-10', '2026-05-17', N'Đã kết thúc'),

('LX23', 'X44', '2026-05-11', '2026-05-18', N'Đã kết thúc'),
('LX24', 'X47', '2026-05-12', '2026-05-19', N'Đã kết thúc');

GO