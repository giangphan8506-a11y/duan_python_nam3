from Database import Database


class PhanCongDAO(Database):

    def __init__(self):
        db = Database()
        self.conn = db.get_connection()


    # ==========================================
    # LẤY TẤT CẢ PHÂN CÔNG
    # ==========================================
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


    # ==========================================
    # TÌM PHÂN CÔNG THEO MÃ
    # ==========================================
    def tim_phancong_theo_ma(self, maphancong):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM PhanCong
            WHERE MaPhanCong = ?
            """,
            maphancong
        )

        results = cursor.fetchone()

        cursor.close()

        return results


    # ==========================================
    # THÊM PHÂN CÔNG
    # ==========================================
    def them_phancong(
            self,
            malaixe,
            maxe,
            ngayphancong,
            ngayketthuc,
            trangthai
    ):

        cursor = self.conn.cursor()

        try:

            # ==================================
            # 1. KIỂM TRA XE CÓ TỒN TẠI KHÔNG
            # ==================================
            cursor.execute(
                """
                SELECT TrangThai
                FROM Xe
                WHERE MaXe = ?
                """,
                maxe
            )

            xe = cursor.fetchone()

            if xe is None:

                cursor.close()
                return False


            # ==================================
            # 2. XE PHẢI ĐANG HOẠT ĐỘNG
            #    KHI ĐANG PHÂN CÔNG
            # ==================================
            if trangthai == "Đang phân công":

                if xe[0] != "Đang hoạt động":

                    cursor.close()
                    return False


            # ==================================
            # 3. KIỂM TRA LÁI XE CÓ TỒN TẠI
            # ==================================
            cursor.execute(
                """
                SELECT TrangThai
                FROM LaiXe
                WHERE MaLaiXe = ?
                """,
                malaixe
            )

            laixe = cursor.fetchone()

            if laixe is None:

                cursor.close()
                return False


            # ==================================
            # 4. LÁI XE PHẢI ĐANG LÀM VIỆC
            #    KHI ĐANG PHÂN CÔNG
            # ==================================
            if trangthai == "Đang phân công":

                if laixe[0] != "Đang làm việc":

                    cursor.close()
                    return False


            # ==================================
            # 5. KIỂM TRA NGÀY KẾT THÚC
            # ==================================

            if trangthai == "Đang phân công":

                # Đang phân công thì chưa có ngày kết thúc
                ngayketthuc = None


            elif trangthai == "Đã kết thúc":

                # Đã kết thúc thì bắt buộc phải có ngày kết thúc
                if ngayketthuc is None or ngayketthuc == "":

                    cursor.close()
                    return False

                # Ngày kết thúc không được trước ngày phân công
                cursor.execute(
                    """
                    SELECT 1
                    WHERE CAST(? AS DATE) < CAST(? AS DATE)
                    """,
                    ngayketthuc,
                    ngayphancong
                )

                if cursor.fetchone() is not None:

                    cursor.close()
                    return False


            # ==================================
            # 6. KIỂM TRA XE ĐÃ ĐƯỢC PHÂN CÔNG
            # ==================================

            if trangthai == "Đang phân công":

                cursor.execute(
                    """
                    SELECT MaPhanCong
                    FROM PhanCong
                    WHERE MaXe = ?
                    AND TrangThai = N'Đang phân công'
                    """,
                    maxe
                )

                phancong_xe = cursor.fetchone()

                if phancong_xe is not None:

                    cursor.close()
                    return False


            # ==================================
            # 7. KIỂM TRA LÁI XE ĐÃ ĐƯỢC PHÂN CÔNG
            # ==================================

            if trangthai == "Đang phân công":

                cursor.execute(
                    """
                    SELECT MaPhanCong
                    FROM PhanCong
                    WHERE MaLaiXe = ?
                    AND TrangThai = N'Đang phân công'
                    """,
                    malaixe
                )

                phancong_laixe = cursor.fetchone()

                if phancong_laixe is not None:

                    cursor.close()
                    return False


            # ==================================
            # 8. THÊM PHÂN CÔNG
            # ==================================

            cursor.execute(
                """
                INSERT INTO PhanCong
                (
                    MaLaiXe,
                    MaXe,
                    NgayPhanCong,
                    NgayKetThuc,
                    TrangThai
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                malaixe,
                maxe,
                ngayphancong,
                ngayketthuc,
                trangthai
            )


            self.conn.commit()

            cursor.close()

            return True


        except Exception as e:

            self.conn.rollback()

            cursor.close()

            print("LỖI THÊM PHÂN CÔNG:", e)

            return False


    # ==========================================
    # SỬA PHÂN CÔNG
    # ==========================================
    def sua_phancong(
            self,
            maphancong,
            malaixe,
            maxe,
            ngayphancong,
            ngayketthuc,
            trangthai
    ):

        cursor = self.conn.cursor()

        try:

            # ==================================
            # 1. KIỂM TRA XE
            # ==================================
            cursor.execute(
                """
                SELECT TrangThai
                FROM Xe
                WHERE MaXe = ?
                """,
                maxe
            )

            xe = cursor.fetchone()

            if xe is None:

                cursor.close()
                return False


            # ==================================
            # 2. XE PHẢI ĐANG HOẠT ĐỘNG
            #    KHI ĐANG PHÂN CÔNG
            # ==================================
            if trangthai == "Đang phân công":

                if xe[0] != "Đang hoạt động":

                    cursor.close()
                    return False


            # ==================================
            # 3. KIỂM TRA LÁI XE
            # ==================================
            cursor.execute(
                """
                SELECT TrangThai
                FROM LaiXe
                WHERE MaLaiXe = ?
                """,
                malaixe
            )

            laixe = cursor.fetchone()

            if laixe is None:

                cursor.close()
                return False


            # ==================================
            # 4. LÁI XE PHẢI ĐANG LÀM VIỆC
            #    KHI ĐANG PHÂN CÔNG
            # ==================================
            if trangthai == "Đang phân công":

                if laixe[0] != "Đang làm việc":

                    cursor.close()
                    return False


            # ==================================
            # 5. KIỂM TRA NGÀY KẾT THÚC
            # ==================================

            if trangthai == "Đang phân công":

                ngayketthuc = None


            elif trangthai == "Đã kết thúc":

                if ngayketthuc is None or ngayketthuc == "":

                    cursor.close()
                    return False


                # Ngày kết thúc >= ngày phân công
                cursor.execute(
                    """
                    SELECT 1
                    WHERE CAST(? AS DATE) < CAST(? AS DATE)
                    """,
                    ngayketthuc,
                    ngayphancong
                )

                if cursor.fetchone() is not None:

                    cursor.close()
                    return False


            # ==================================
            # 6. KIỂM TRA XE ĐANG PHÂN CÔNG
            # ==================================

            if trangthai == "Đang phân công":

                cursor.execute(
                    """
                    SELECT MaPhanCong
                    FROM PhanCong
                    WHERE MaXe = ?
                    AND TrangThai = N'Đang phân công'
                    AND MaPhanCong <> ?
                    """,
                    maxe,
                    maphancong
                )

                phancong_xe = cursor.fetchone()

                if phancong_xe is not None:

                    cursor.close()
                    return False


            # ==================================
            # 7. KIỂM TRA LÁI XE ĐANG PHÂN CÔNG
            # ==================================

            if trangthai == "Đang phân công":

                cursor.execute(
                    """
                    SELECT MaPhanCong
                    FROM PhanCong
                    WHERE MaLaiXe = ?
                    AND TrangThai = N'Đang phân công'
                    AND MaPhanCong <> ?
                    """,
                    malaixe,
                    maphancong
                )

                phancong_laixe = cursor.fetchone()

                if phancong_laixe is not None:

                    cursor.close()
                    return False


            # ==================================
            # 8. CẬP NHẬT PHÂN CÔNG
            # ==================================

            cursor.execute(
                """
                UPDATE PhanCong
                SET
                    MaLaiXe = ?,
                    MaXe = ?,
                    NgayPhanCong = ?,
                    NgayKetThuc = ?,
                    TrangThai = ?
                WHERE MaPhanCong = ?
                """,
                malaixe,
                maxe,
                ngayphancong,
                ngayketthuc,
                trangthai,
                maphancong
            )


            self.conn.commit()

            cursor.close()

            return True


        except Exception as e:

            self.conn.rollback()

            cursor.close()

            print("LỖI SỬA PHÂN CÔNG:", e)

            return False


    # ==========================================
    # XÓA PHÂN CÔNG
    # ==========================================
    def Xoa_phancong(self, maphancong):

        cursor = self.conn.cursor()

        try:

            cursor.execute(
                """
                DELETE FROM PhanCong
                WHERE MaPhanCong = ?
                """,
                maphancong
            )

            self.conn.commit()

            cursor.close()

            return True


        except Exception as e:

            self.conn.rollback()

            cursor.close()

            print("LỖI XÓA PHÂN CÔNG:", e)

            return False


    # ==========================================
    # XEM PHÂN CÔNG CHI TIẾT
    # ==========================================
    def xem_phan_cong_chi_tiet(self):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                PhanCong.MaPhanCong,
                LaiXe.MaLaiXe,
                LaiXe.HoTen,
                Xe.MaXe,
                Xe.BienSo,
                Xe.TenXe,
                PhanCong.NgayPhanCong,
                PhanCong.NgayKetThuc,
                PhanCong.TrangThai

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
