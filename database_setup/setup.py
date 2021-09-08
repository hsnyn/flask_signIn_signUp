import platform


class setup_database():
    
    def get_arch(self):
        print("Accessing Architecture Information")
        try:
            temp = platform.architecture()
            self.architecture = temp[0]
            return True
        except Exception as e:
            self.message = "Error in Architecture Information [function: get_arch] " + str(e)
            return False
    
    def make_dir(self):
        path = r"C:\sqlite"
        print(path)
    
    def __init__(self):
        super(setup_database, self).__init__()
        self.architecture = None
        self.message = None
        if self.get_arch() == True:
            if self.architecture == '64bit':
                print("System Architecture is " +str(self.architecture))
                self.make_dir()
            elif self.architecture == '32bit':
                print("System Architecture is " +str(self.architecture))
                self.make_dir()
            else:
                print("Error in Architecture Information [function: get_arch] - Change the check parameters for self.architecture variable")
        else:
            print(self.message)
            
setup_database()