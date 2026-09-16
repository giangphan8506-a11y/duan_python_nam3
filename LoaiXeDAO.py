from Database import Database
class LoaiXeDAO:
    def __init__(self):
        db = Database()
        self.conn = db.get_connection()

    def get_all(self):
        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT * 
            FROM LoaiXe
            """
        )

        result = cursor.fetchall()

        cursor.close()
        return result

    def tim_loai_xe_theo_ma(self, maloai):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM LoaiXe
            WHERE MaLoai = ?
            """, (maloai,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result

    def them_loai_xe(self, maloai, tenloai):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO LoaiXe (MaLoai, TenLoai)
                VALUES (?, ?)
                """, maloai, tenloai
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.conn.rollback()
            cursor.close()
            return False
    def sua_loai_xe(self, maloai, tenloai):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                UPDATE LoaiXe
                SET TenLoai = ?
                WHERE MaLoai = ?
                """, tenloai, maloai
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.conn.rollback()
            cursor.close()
            return False
    def xoa_loai_xe(self, maloai):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                DELETE FROM LoaiXe
                WHERE MaLoai = ?
                """,maloai
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.conn.rollback()
            cursor.close()
            return False

