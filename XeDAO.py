from Database import Database
class XeDAO:
    def __init__(self):
        db = Database()
        self.conn = db.get_connection()

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM Xe
            ORDER BY CAST(SUBSTRING(MaXe, 2, LEN(MaXe)) AS INT) ASC
            """
        )
        results = cursor.fetchall()
        cursor.close()
        return results
    def tim_xe_theo_ma(self, maxe):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM Xe
            WHERE MaXe = ?
            """, maxe
        )
        results = cursor.fetchone()
        cursor.close()
        return results
    def tim_xe_theo_ten(self, tenxe):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM Xe
            WHERE TenXe LIKE ?
            """, '%' + tenxe + '%'
        )
        results = cursor.fetchall()
        cursor.close()
        return results
    def them_xe(self, maxe, bienso, tenxe, maloai, trangthai):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO Xe (MaXe, BienSo, TenXe, MaLoai, TrangThai)
                VALUES (?, ?, ?, ?, ?)
                """, maxe, bienso, tenxe, maloai, trangthai
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.conn.rollback()
            cursor.close()
            return False
    def sua_xe(self, maxe, bienso, tenxe, maloai, trangthai):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                UPDATE Xe
                SET BienSo = ?, TenXe = ?, MaLoai = ?, TrangThai = ?
                WHERE MaXe = ?
                """, bienso, tenxe, maloai, trangthai, maxe
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.conn.rollback()
            cursor.close()
            return False
    def xoa_xe(self, maxe):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                DELETE FROM Xe
                WHERE MaXe = ?
                """, maxe
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.conn.rollback()
            cursor.close()
            return False

    def thong_ke_xe(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT TrangThai, COUNT(*)
            FROM Xe
            GROUP BY TrangThai
        """)

        return cursor.fetchall()