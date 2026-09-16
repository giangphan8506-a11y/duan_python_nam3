def hien_xe(frame_xe, frame_laixe, frame_phancong):
    frame_xe.pack(fill="both", expand=True)
    frame_laixe.pack_forget()
    frame_phancong.pack_forget()


def hien_laixe(frame_xe, frame_laixe, frame_phancong):
    frame_xe.pack_forget()
    frame_laixe.pack(fill="both", expand=True)
    frame_phancong.pack_forget()


def hien_phancong(frame_xe, frame_laixe, frame_phancong):
    frame_xe.pack_forget()
    frame_laixe.pack_forget()
    frame_phancong.pack(fill="both", expand=True)

