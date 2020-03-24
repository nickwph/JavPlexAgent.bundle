# coding=utf-8


# noinspection PyPep8Naming,PyClassHasNoInit
class Log:
    """
    The Log API allows the developer to add their own messages to the plug-in’s log file. The different methods
    represent the different log levels available, in increasing levels of severity. The first argument to each method
    should be a format string, which is formatted using any additional arguments and keyword arguments provided.
    """

    @staticmethod
    def Debug(fmt, *args, **kwargs):
        """
        :type fmt: str
        """
        print "[DEBUG]     {}".format(fmt)

    @staticmethod
    def Info(fmt, *args, **kwargs):
        """
        :type fmt: str
        """
        print "[INFO]      {}".format(fmt)

    @staticmethod
    def Warn(fmt, *args, **kwargs):
        """
        :type fmt: str
        """
        print "[WARN]      {}".format(fmt)

    @staticmethod
    def Error(fmt, *args, **kwargs):
        """
        :type fmt: str
        """
        print "[ERROR]     {}".format(fmt)

    @staticmethod
    def Critical(fmt, *args, **kwargs):
        """
        :type fmt: str
        """
        print "[CRITICAL]  {}".format(fmt)

    @staticmethod
    def Exception(fmt, *args, **kwargs):
        """
        :type fmt: str
        """
        print "[EXCEPTION] {}".format(fmt)
