class Language(object):
    Chinese = 'zh'
    English = 'en'
    French = 'fr'
    Italian = 'it'
    Japanese = 'ja'
    Korean = 'ko'
    NoLanguage = 'xn'
    Swedish = 'sv'


# noinspection PyPep8Naming
class Locale(object):
    Language = Language

    def Match(self):
        pass
