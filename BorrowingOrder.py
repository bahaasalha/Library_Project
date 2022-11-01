class BorrowingOrder:
    id =None
    start_date =None
    end_date =None
    book_id =None
    client_id =None
    status =None

    def __init__(self,id,start_date,end_date,book_id,client_id,status):
        self.id=id
        self.start_date=start_date
        self.end_date=end_date
        self.book_id=book_id
        self.client_id=client_id
        self.status=status


