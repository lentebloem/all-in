import send_before_class


class Response:
    def __init__(self, phone, code, time):
        self.phone = phone
        self.code = code
        self.time = time
        self.attend = False
        self.next = None


class SeatChart:
    '''
    @params
    records:  a list of individual records
    date: class date
    start: class start time
    end: class end time
    '''
    def __init__(self, records, date, start, end, rows = 8):
        self.records = records
        self.date = date
        self.start = start
        self.end = end
        self.seatchart = dict()
        self.rows = rows


    # read records from SMS responses
    def read_records(self):
        # SMS functions to be implemented


    def map_seat_chart(self):
        seat_map = dict()
        for rec in self.records:
            if student_list[rec.phone].sid in seat_map:
                print("student already existed. Adding ")
            student_list[rec.phone].decryptCode(rec.code)
