"""
Configuration for the matsuri data collection system
"""

# Major festival sources
TOURISM_SITES = {
    'kyoto': {
        'url': 'https://www.kyoto-kankou.or.jp',
        'encoding': 'utf-8',
        'patterns': [
            r'祭り',
            r'例大祭',
            r'神事'
        ]
    },
    'tokyo': {
        'url': 'https://www.gotokyo.org',
        'encoding': 'utf-8',
        'patterns': [
            r'祭り',
            r'例大祭',
            r'神事'
        ]
    }
}

# Keywords for identifying traditional festivals
TRADITIONAL_PATTERNS = [
    r'神社',
    r'寺院',
    r'例大祭',
    r'伝統',
    r'御祭'
]

# Keywords for filtering out commercial events
COMMERCIAL_PATTERNS = [
    r'セール',
    r'キャンペーン',
    r'生誕祭',
    r'物産展'
]

# Date patterns for Japanese text
DATE_PATTERNS = {
    'full': r'\d{4}年\d{1,2}月\d{1,2}日',
    'month_day': r'\d{1,2}月\d{1,2}日',
    'relative': r'(毎年|例年)',
    'period': r'(～|から)',
    'weekday': r'(月|火|水|木|金|土|日)曜日'
}

# Major festivals to use as seed data
SEED_FESTIVALS = [
    {
        'name': '祇園祭',
        'location': {'lat': 35.0035, 'lng': 135.7679},
        'dates': {'start': '2024-07-01', 'end': '2024-07-31'},
        'type': '神社祭り',
        'prefecture': '京都府',
        'city': '京都市',
        'tags': ['国重要無形民俗文化財', '山鉾巡行']
    },
    # Add more major festivals here
]