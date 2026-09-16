CREATE DATABASE QuanLyXeLaiXe;
GO

USE QuanLyXeLaiXe;
GO
-- 1. LOAI XE
CREATE TABLE LoaiXe
(
    MaLoai VARCHAR(10) PRIMARY KEY,
    TenLoai NVARCHAR(50) NOT NULL
);
GO


-- 2. XE
CREATE TABLE Xe
(
    MaXe VARCHAR(10) PRIMARY KEY,
    BienSo VARCHAR(15) NOT NULL UNIQUE,
    TenXe NVARCHAR(100) NOT NULL,
    MaLoai VARCHAR(10) NOT NULL,
    TrangThai NVARCHAR(30) NOT NULL,

    CONSTRAINT FK_Xe_LoaiXe
        FOREIGN KEY (MaLoai)
        REFERENCES LoaiXe(MaLoai)
);
GO


-- 3. LAI XE
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


-- 4. PHAN CONG
CREATE TABLE PhanCong
(
    MaPhanCong INT IDENTITY(1,1) PRIMARY KEY,
    MaLaiXe VARCHAR(10) NOT NULL,
    MaXe VARCHAR(10) NOT NULL,
    NgayPhanCong DATE NOT NULL,
    TrangThai NVARCHAR(30) NOT NULL,

    CONSTRAINT FK_PhanCong_LaiXe
        FOREIGN KEY (MaLaiXe)
        REFERENCES LaiXe(MaLaiXe),

    CONSTRAINT FK_PhanCong_Xe
        FOREIGN KEY (MaXe)
        REFERENCES Xe(MaXe)
);
GO
USE QuanLyXeLaiXe;
GO

INSERT INTO LoaiXe (MaLoai, TenLoai)
VALUES
('L01', N'Xe 4 chỗ'),
('L02', N'Xe 5 chỗ'),
('L03', N'Xe 7 chỗ'),
('L04', N'Xe bán tải'),
('L05', N'Xe SUV');
GO

INSERT INTO Xe (MaXe, BienSo, TenXe, MaLoai, TrangThai)
VALUES
('X01', '67A-12345', N'Toyota Vios', 'L02', N'Đang hoạt động'),
('X02', '67A-23456', N'Toyota Camry', 'L02', N'Đang hoạt động'),
('X03', '67A-34567', N'Toyota Innova', 'L03', N'Đang hoạt động'),
('X04', '67A-45678', N'Toyota Fortuner', 'L03', N'Bảo trì'),
('X05', '67A-56789', N'Toyota Hilux', 'L04', N'Đang hoạt động'),
('X06', '67A-67890', N'Toyota Corolla Cross', 'L05', N'Đang hoạt động'),
('X07', '67A-78901', N'Toyota Yaris', 'L02', N'Ngừng hoạt động'),
('X08', '67A-89012', N'Toyota Raize', 'L05', N'Đang hoạt động');
GO

INSERT INTO LaiXe
(MaLaiXe, HoTen, SoDienThoai, SoGPLX, LoaiBang, TrangThai)
VALUES
('LX01', N'Nguyễn Văn An', '0901234567', '790123456789', 'B2', N'Đang làm việc'),
('LX02', N'Trần Văn Bình', '0912345678', '790234567890', 'B2', N'Đang làm việc'),
('LX03', N'Lê Minh Cường', '0923456789', '790345678901', 'C', N'Đang làm việc'),
('LX04', N'Phạm Văn Dũng', '0934567890', '790456789012', 'B2', N'Đang làm việc'),
('LX05', N'Võ Hoàng Nam', '0945678901', '790567890123', 'C', N'Tạm nghỉ'),
('LX06', N'Đặng Minh Tuấn', '0956789012', '790678901234', 'B2', N'Đang làm việc');
GO

INSERT INTO PhanCong
(MaLaiXe, MaXe, NgayPhanCong, TrangThai)
VALUES
('LX01', 'X01', '2026-09-01', N'Đang phân công'),
('LX02', 'X02', '2026-09-02', N'Đang phân công'),
('LX03', 'X03', '2026-09-03', N'Đang phân công'),
('LX04', 'X05', '2026-09-05', N'Đang phân công'),
('LX06', 'X06', '2026-09-07', N'Đang phân công'),
('LX01', 'X03', '2026-08-15', N'Đã kết thúc'),
('LX02', 'X07', '2026-08-20', N'Đã kết thúc'),
('LX04', 'X08', '2026-08-25', N'Đã kết thúc');
GO

SELECT *
FROM LaiXe


