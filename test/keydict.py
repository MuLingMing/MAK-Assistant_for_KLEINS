"""
filename:keydict.py
包含虚拟键码
"""

key_dict = {
    "LBUTTON": 1,  # 鼠标左键
    "RBUTTON": 2,  # 鼠标右键
    "CANCEL": 3,  # Cancel
    "MBUTTON": 4,  # 鼠标中键
    "XBUTTON1": 5,  # X1鼠标按钮
    "XBUTTON2": 6,  # X2鼠标按钮
    "BACK": 8,  # Backspace
    "TAB": 9,  # Tab
    "CLEAR": 12,  # Clear
    "RETURN": 13,  # Enter
    "SHIFT": 16,  # Shift
    "CONTROL": 17,  # Ctrl
    "MENU": 18,  # ALt
    "PAUSE": 19,  # Pause
    "CAPITAL": 20,  # Caps Lock
    "KANA": 21,  # IME Kana模式
    "HANGEUL": 21,  # IME Hanguel模式（全角）
    "HANGUL": 21,  # IME Hanguel模式（半角）
    "JUNJA": 23,  # IME Junja模式
    "FINAL": 24,  # IME final mode
    "HANJA": 25,  # IME Hanja模式
    "KANJI": 25,  # IME Kanji模式
    "ESCAPE": 27,  # Escape
    "CONVERT": 28,  # IME convert
    "NONCONVERT": 29,  # IME nonconvert
    "ACCEPT": 30,  # IME accept
    "MODECHANGE": 31,  # IME mode change request
    "SPACE": 32,  # Space
    "PRIOR": 33,  # Prior
    "NEXT": 34,  # Next
    "END": 35,  # End
    "HOME": 36,  # Home
    "LEFT": 37,  # Left
    "UP": 38,  # Up
    "RIGHT": 39,  # Right
    "DOWN": 40,  # Down
    "SELECT": 41,  # Select
    "PRINT": 42,  # Print
    "EXECUTE": 43,  # Execute
    "SNAPSHOT": 44,  # Snapshot
    "INSERT": 45,  # Insert
    "DELETE": 46,  # Delete
    "HELP": 47,  # Help
    "0": 48, "1": 49, "2": 50, "3": 51, "4": 52, "5": 53, "6": 54, "7": 55, "8": 56, "9": 57,
    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71,
    "H": 72, "I": 73, "J": 74, "K": 75, "L": 76, "M": 77, "N": 78,
    "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90,
    "LWIN": 91,  # 左Windows键（自然键盘）
    "RWIN": 92,  # 右Windows键（自然键盘）
    "APPS": 93,  # Applications键（自然键盘）
    "SLEEP": 95,  # 睡眠
    "NUMPAD0": 96, "NUMPAD1": 97, "NUMPAD2": 98, "NUMPAD3": 99, "NUMPAD4": 100,
    "NUMPAD5": 101, "NUMPAD6": 102, "NUMPAD7": 103, "NUMPAD8": 104, "NUMPAD9": 105,
    "MULTIPLY": 106,  # 小键盘 *
    "ADD": 107,  # 小键盘 +
    "SEPARATOR": 108,  # 小键盘 enter
    "DECIMAL": 110,  # 小键盘 .
    "DIVIDE": 111,  # 小键盘 /
    "F1": 112, "F2": 113, "F3": 114, "F4": 115, "F5": 116, "F6": 117,
    "F7": 118, "F8": 119, "F9": 120, "F10": 121, "F11": 122, "F12": 123,
    "F13": 124, "F14": 125, "F15": 126, "F16": 127, "F17": 128, "F18": 129,
    "F19": 130, "F20": 131, "F21": 132, "F22": 133, "F23": 134, "F24": 135,
    "NUMLOCK": 144,  # 小键盘 Num Lock
    "SCROLLLOCK": 145,  # 小键盘 Scroll Lock
    "LSHIFT": 160,  # 左SHIFT键
    "RSHIFT": 161,  # 右SHIFT键
    "LCTRL": 162,  # 左CTRL键
    "RCONTROL": 163,  # 右CTRL键
    "LMENU": 164,  # 左Menu键
    "RMENU": 165,  # 右Menu键
    "BROWSER_BACK": 166,  # 浏览器后退
    "BROWSER_FORWARD": 167,  # 浏览器前进
    "BROWSER_REFRESH": 168,  # 浏览器刷新
    "BROWSER_STOP": 169,  # 浏览器停止
    "BROWSER_SEARCH": 170,  # 浏览器搜索
    "BROWSER_FAVORITES": 171,  # 浏览器收藏
    "BROWSER_HOME": 172,  # 浏览器主页
    "VOLUME_MUTE": 173,  # 静音
    "VOLUME_DOWN": 174,  # 音量-
    "VOLUME_UP": 175,  # 音量+
    "MEDIA_NEXT_TRACK": 176,  # 播放下一首
    "MEDIA_PREV_TRACK": 177,  # 播放上一首
    "MEDIA_STOP": 178,  # 停止
    "MEDIA_PLAY_PAUSE": 179,  # 暂停/播放
    "LAUNCH_MAIL": 180,  # 启动邮件
    "LAUNCH_MEDIA_SELECT": 182,  # 启动媒体选择器
    "LAUNCH_APP1": 183,  # 启动App1
    "LAUNCH_APP2": 184,  # 启动App2
    "OEM_1": 186,  # ;: 半角
    "OEM_PLUS": 187,  # += 半角
    "OEM_COMMA": 188,  # ,< 半角
    "OEM_MINUS": 189,  # -_ 半角
    "OEM_PERIOD": 190,  # .> 半角
    "OEM_2": 191,  # /? 半角
    "OEM_3": 192,  # ~ 半角
    "OEM_4": 219,  # { [ 半角
    "OEM_5": 220,  # | \ 半角
    "OEM_6": 221,  # } ] 半角
    "OEM_7": 222,  # ' " 半角
    "OEM_8": 223,  # 非半角
    "OEM_102": 226,  # <> 半角
    "PROCESSKEY": 229,  # Process
    "PACKET": 231,  # Packet
    "ATTN": 246,  # Attn
    "CRSEL": 247,  # CrSel
    "EXSEL": 248,  # ExSel
    "EREOF": 249,  # Erase EOF
    "PLAY": 250,  # Play
    "ZOOM": 251,  # Zoom
    "NONAME": 252,  # Reserved
    "PA1": 253,  # PA1
    "OEM_CLEAR": 254,  # OemClear
}
"""winuser.h
#define VK_LBUTTON	1
#define VK_RBUTTON	2
#define VK_CANCEL	3
#define VK_MBUTTON	4
#if (_WIN32_WINNT >= 0x0500)
#define VK_XBUTTON1	5
#define VK_XBUTTON2	6
#endif
#define VK_BACK	8
#define VK_TAB	9
#define VK_CLEAR	12
#define VK_RETURN	13
#define VK_SHIFT	16
#define VK_CONTROL	17
#define VK_MENU	18
#define VK_PAUSE	19
#define VK_CAPITAL	20
#define VK_KANA	0x15
#define VK_HANGEUL	0x15
#define VK_HANGUL	0x15
#define VK_JUNJA	0x17
#define VK_FINAL	0x18
#define VK_HANJA	0x19
#define VK_KANJI	0x19
#define VK_ESCAPE	0x1B
#define VK_CONVERT	0x1C
#define VK_NONCONVERT	0x1D
#define VK_ACCEPT	0x1E
#define VK_MODECHANGE	0x1F
#define VK_SPACE	32
#define VK_PRIOR	33
#define VK_NEXT	34
#define VK_END	35
#define VK_HOME	36
#define VK_LEFT	37
#define VK_UP	38
#define VK_RIGHT	39
#define VK_DOWN	40
#define VK_SELECT	41
#define VK_PRINT	42
#define VK_EXECUTE	43
#define VK_SNAPSHOT	44
#define VK_INSERT	45
#define VK_DELETE	46
#define VK_HELP	47
#define VK_LWIN	0x5B
#define VK_RWIN	0x5C
#define VK_APPS	0x5D
#define VK_SLEEP	0x5F
#define VK_NUMPAD0	0x60
#define VK_NUMPAD1	0x61
#define VK_NUMPAD2	0x62
#define VK_NUMPAD3	0x63
#define VK_NUMPAD4	0x64
#define VK_NUMPAD5	0x65
#define VK_NUMPAD6	0x66
#define VK_NUMPAD7	0x67
#define VK_NUMPAD8	0x68
#define VK_NUMPAD9	0x69
#define VK_MULTIPLY	0x6A
#define VK_ADD	0x6B
#define VK_SEPARATOR	0x6C
#define VK_SUBTRACT	0x6D
#define VK_DECIMAL	0x6E
#define VK_DIVIDE	0x6F
#define VK_F1	0x70
#define VK_F2	0x71
#define VK_F3	0x72
#define VK_F4	0x73
#define VK_F5	0x74
#define VK_F6	0x75
#define VK_F7	0x76
#define VK_F8	0x77
#define VK_F9	0x78
#define VK_F10	0x79
#define VK_F11	0x7A
#define VK_F12	0x7B
#define VK_F13	0x7C
#define VK_F14	0x7D
#define VK_F15	0x7E
#define VK_F16	0x7F
#define VK_F17	0x80
#define VK_F18	0x81
#define VK_F19	0x82
#define VK_F20	0x83
#define VK_F21	0x84
#define VK_F22	0x85
#define VK_F23	0x86
#define VK_F24	0x87
#define VK_NUMLOCK	0x90
#define VK_SCROLL	0x91
#define VK_LSHIFT	0xA0
#define VK_RSHIFT	0xA1
#define VK_LCONTROL	0xA2
#define VK_RCONTROL	0xA3
#define VK_LMENU	0xA4
#define VK_RMENU	0xA5
#if (_WIN32_WINNT >= 0x0500)
#define VK_BROWSER_BACK	0xA6
#define VK_BROWSER_FORWARD	0xA7
#define VK_BROWSER_REFRESH	0xA8
#define VK_BROWSER_STOP	0xA9
#define VK_BROWSER_SEARCH	0xAA
#define VK_BROWSER_FAVORITES	0xAB
#define VK_BROWSER_HOME	0xAC
#define VK_VOLUME_MUTE	0xAD
#define VK_VOLUME_DOWN	0xAE
#define VK_VOLUME_UP	0xAF
#define VK_MEDIA_NEXT_TRACK	0xB0
#define VK_MEDIA_PREV_TRACK	0xB1
#define VK_MEDIA_STOP	0xB2
#define VK_MEDIA_PLAY_PAUSE	0xB3
#define VK_LAUNCH_MAIL	0xB4
#define VK_LAUNCH_MEDIA_SELECT	0xB5
#define VK_LAUNCH_APP1	0xB6
#define VK_LAUNCH_APP2	0xB7
#endif
#define VK_OEM_1	0xBA
#if (_WIN32_WINNT >= 0x0500)
#define VK_OEM_PLUS	0xBB
#define VK_OEM_COMMA	0xBC
#define VK_OEM_MINUS	0xBD
#define VK_OEM_PERIOD	0xBE
#endif
#define VK_OEM_2	0xBF
#define VK_OEM_3	0xC0
#define VK_OEM_4	0xDB
#define VK_OEM_5	0xDC
#define VK_OEM_6	0xDD
#define VK_OEM_7	0xDE
#define VK_OEM_8	0xDF
#if (_WIN32_WINNT >= 0x0500)
#define VK_OEM_102	0xE2
#endif
#define VK_PROCESSKEY	0xE5
#if (_WIN32_WINNT >= 0x0500)
#define VK_PACKET	0xE7
#endif
#define VK_ATTN	0xF6
#define VK_CRSEL	0xF7
#define VK_EXSEL	0xF8
#define VK_EREOF	0xF9
#define VK_PLAY	0xFA
#define VK_ZOOM	0xFB
#define VK_NONAME	0xFC
#define VK_PA1	0xFD
#define VK_OEM_CLEAR	0xFE
"""
