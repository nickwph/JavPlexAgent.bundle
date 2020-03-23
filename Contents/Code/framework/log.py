# noinspection PyPep8Naming,PyClassHasNoInit
class Log:

    @classmethod
    def Debug(cls, message):
        """
        :type message: str
        """
        print "[DEBUG] {}".format(message)

    @classmethod
    def Info(cls, message):
        """
        :type message: str
        """
        pass

    @classmethod
    def Warn(cls, message):
        """
        :type message: str
        """
        pass

    @classmethod
    def Error(cls, message):
        """
        :type message: str
        """
        print "[ERROR] {}".format(message)

    @classmethod
    def Critical(cls, message):
        """
        :type message: str
        """
        pass

    @classmethod
    def Exception(cls, message):
        """
        :type message: str
        """
        pass
