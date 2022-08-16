class store : 
    def __init__(self):
        self.types= [ 'S3','Glacier']
    
    def displays(self):
        for t in self.types : 
            print(t)
