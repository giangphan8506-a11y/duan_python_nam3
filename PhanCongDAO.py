from Database import Database

class PhanCongDAO(Database):
    def __init__(self):
        db = Database()
        self.conn = db.get_connection()

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM PhanCong
            """
        )
        results = cursor.fetchall()
        cursor.close()
        return results

    def tim_phancong_theo_ma(self, maphancong):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM PhanCong
            WHERE MaPhanCong = ?
            """, maphancong
        )
        results = cursor.fetchone()
        cursor.close()
        return results

    def them_phancong (self, malaixe, maxe, ngayphancong, trangthai):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO PhanCong (MaLaiXi, MaXe, NgayPhanCong, Trangthai)
                VALUES (?, ?, ?, ?)
                """,malaixe, maxe, ngayphancong, trangthai
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.cursor.rollback()
            cursor.close()
            return False
    def sua_phancong(self, maphancong, malaixe, maxe, ngayphancong, trangthai):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                UPDATE PhanCong
                SET MaLaiXe = ?, MaXe = ?, NgayPhanCong = ?, Trangthai = ?
                WHERE MaPhanCong = ?
                """, malaixe, maxe, ngayphancong, trangthai, maphancong
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.cursor.rollback()
            cursor.close()
            return False
    def Xoa_phancong(self, maphancong):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                DELETE FROM PhanCong
                WHERE MaPhanCong = ?
                """, maphancong
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.cursor.rollback()
            cursor.close()
            return False
    def xem_phan_cong_chi_tiet(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT PhanCong.MaPhanCong, LaiXe.MaLaiXe, LaiXe.HoTen, 
                    Xe.MaXe,Xe.BienSo, Xe.TenXe, PhanCong.NgayPhanCong, PhanCong.Trangthai
            FROM PhanCong
            INNER JOIN LaiXe
                ON PhanCong.MaLaiXe = LaiXe.MaLaiXe
            INNER JOIN Xe
                ON PhanCong.MaXe = Xe.MaXe         
            """
        )
        results = cursor.fetchall()
        cursor.close()
        return results


