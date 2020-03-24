class Language(object):
    Chinese = 'zh'
    English = 'en'
    Japanese = 'ja'
    Korean = 'ko'
    NoLanguage = 'xn'
    French = 'fr'
    Swedish = 'sv'
    Italian = 'it'


# noinspection PyPep8Naming
class Locale(object):
    Language = Language

    def Match(self):
        pass
