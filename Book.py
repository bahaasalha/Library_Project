class Book:
    id = None
    title:str = None
    description = None
    author = None
    status:str = None


    def __init__(self,id,title,description,author,status):
        self.id=id
        self.title=title
        self.description=description
        self.author=author
        self.status=status