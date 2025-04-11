AUTHOR = 'Moo-fasa og Nu-sasha'
SITENAME = 'Koen på den glatte is.'
SITEURL = "https://glatis-dk.github.io/koen-p--den-glatte-is"

DEFAULT_LANG = 'EN'

PATH = "content"

THEME = 'themes/Peli-Kiera'
STATIC_PATHS = ['images', 'static']
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']

TIMEZONE = 'Europe/Copenhagen'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (

)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
