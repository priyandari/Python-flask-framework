class ArtikelModel:
    def __init__(self, title=None, date=None, content=None):
        self.title = title
        self.date = date
        self.content = content
   
    def setTitle(self, title):
        self.title = title
    def setDate(self, date):
        self.date = date
    def setContent(self,content):
        self.content = content
    
    def getTitle(self):
        return self.title
    def getDate(self):
        return self.date
    def getContent(self):
        return self.content