from Database import Database

class LaiXeDAO:
    def __init__(self):
        db = Database()
        self.conn = db.conn

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT *            
            FROM LaiXe
            """
        )
        result = cursor.fetchall()
        cursor.close()
        return result

    def them_lai_xe(self, malaixe, hoten, sodienthoai, sogplx, loaibang):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO LaiXe (MaLaiXe, HoTen, SoDienThoai, SoGPLX, LoaiBang)
                VALUES (?, ?, ?, ?, ?)
                """, malaixe, hoten, sodienthoai, sogplx, loaibang
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.conn.rollback()
            cursor.close()
            return False

    def tim_lai_xe_theo_ma(self, malaixe):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT *            
            FROM LaiXe 
            WHERE MaLaiXe = ?
            """, malaixe
        )
        result = cursor.fetchone()
        cursor.close()
        return result

    def tim_lai_xe_theo_ten (self, hoten):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT *            
            FROM LaiXe 
            WHERE HoTen LIKE ?
            """, '%' + hoten + '%'
        )
        result = cursor.fetchone()
        cursor.close()
        return result

    def sua_lai_xe(self, malaixe, hoten, sodienthoai, sogplx, loaibang):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                UPDATE LaiXe 
                SET HoTen = ?, SoDienThoai = ?, SoGPLX = ?, LoaiBang = ?
                WHERE MaLaiXe = ?
                """, hoten, sodienthoai, sogplx, loaibang,malaixe
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.conn.rollback()
            cursor.close()
            return False

    def xoa_lai_xe(self, malaixe):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                DELETE FROM LaiXe 
                WHERE MaLaiXe = ?
                """,malaixe
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.conn.rollback()
            cursor.close()
            return False

