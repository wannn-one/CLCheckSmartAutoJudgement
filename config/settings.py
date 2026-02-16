# Perforce Settings
class P4:
    TIMEOUT = 15

# Excel Settings
class EXCEL:
    DEFAULT_SHEET_NAME = "CLCheck"
    MAX_HEADER_ROWS_TO_CHECK = 50

# Logic Evaluator Settings
class EVALUATOR:
    IGNORED_PREFIXES = (
        'MENU_TYPE', 'UIHarnessLocale', 'UIMENUITEM', 'UIMENUTYPE', 'UIHOME_MENUID'
    )

    IGNORED_KEYWORDS = {
        'IFDEF', 'IFNDEF', 'ENDIF', 'DEFINE', 'INCLUDE', 'PRAGMA', 'ELSE', 
        'STATIC', 'CONST', 'VOID', 'BOOL', 'INT', 'TRUE', 'FALSE', 'NULL',
        'PUBLIC', 'PRIVATE', 'CLASS', 'STRUCT', 'RETURN', 
        'UIMENUITEM_TBL', 'UIMENUTYPE2ITEMTBL_MAP', 'UIMENUID2ITEMTBL_MAP', 'UIUINT32'
    }

# GUI Settings
class GUI:
    APPEARANCE_MODE = "Dark"
    COLOR_THEME = "blue"
    WINDOW_TITLE = "CLCheck Smart Auto Judgement"
    WINDOW_GEOMETRY = "1280x720"

class FONT:
    GENERAL = "游ゴシック" 
    CODE = "Consolas"

class LOG:
    INFO = "#00BFFF"
    SUCCESS = "#4CAF50"
    WARNING = "#FFC107"
    ERROR = "#FF5555"