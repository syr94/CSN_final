
class Factory(object):
        __instance = None

        def __init__(self):
            if not Factory.__instance:     
                print(" __init__ method called..")
            else:
                print("Instance already created:", self.get_instance())
                
        @classmethod
        def get_instance(cls):
            if not cls.__instance:
                cls.__instance = Factory()
            return cls.__instance


      #  def build(class_name : str, options : dict = {}) -> object:
        def build(self,class_name_s, options):
            try:
                options = {
                    'voice' : "meow"
                }
                print(globals()[class_name_s])
                return globals()[class_name_s](options)
            except Exception as e:
                print("Can't find class {}".format(class_name_s))
                print(e)
