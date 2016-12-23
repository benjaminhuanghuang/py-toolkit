# -*- coding: utf-8 -*-

# https://bible-api.com/
# https://github.com/gdagley/bible_gateway/blob/master/lib/bible_gateway.rb
# pip install --upgrade cffi


import re
import os.path
import requests

source_file = "365.txt"
output_file = "365_ouput.txt"
home_dir = os.path.expanduser('~')
source_file_path = os.path.join(home_dir, "Desktop", source_file)
output_file_path = os.path.join(home_dir, "Desktop", output_file)

book_dict = {"約珥書": "Joel", "歷代志下": "2 Chronicles", "以賽亞書": "Isaiah", "哈該書": "Haggai",
             "俄巴底亞書": "Obadiah", "雅歌": "Song of Songs", "腓利門書": "Philemon",
             "希伯來書": "Hebrews", "加拉太書": "Galatians", "彼得前書": "1 Peter",
             "羅馬書": "Romans", "彼得後書": "2 Peter", "但以理書": "Daniel",
             "約翰參書": "3 John", "以弗所書": "Ephesians", "雅各書": "James",
             "約翰壹書": "1 John", "箴言": "Proverbs", "提多書": "Titus",
             "瑪拉基書": "Malachi", "哈巴谷書": "Habakkuk", "歌羅西書": "Colossians",
             "帖撒羅尼迦後書": "2 Thessalonians", "耶利米哀歌": "Lamentations",
             "路加福音": "Luke", "阿摩司書": "Amos", "約伯記": "Job", "猶大書": "Jude",
             "以斯帖記": "Esther", "提摩太前書": "1 Timothy", "馬太福音": "Matthew",
             "帖撒羅尼迦前書": "1 Thessalonians", "詩篇": "Psalms", "創世記": "Genesis",
             "歷代志上": "1 Chronicles", "撒迦利亞書": "Zechariah", "提摩太後書": "2 Timothy",
             "約翰福音": "John", "以斯拉記": "Ezra", "耶利米書": "Jeremiah", "尼希米記": "Nehemiah",
             "那鴻書": "Nahum", "腓利比書": "Philippians", "何西阿書": "Hosea",
             "撒母耳記下": "2 Samuel", "路得記": "Ruth", "約書亞記": "Joshua", "以西結書": "Ezekiel",
             "馬可福音": "Mark", "士師記": "Judges", "約拿書": "Jonah", "傳道書": "Ecclesiastes",
             "利未記": "Leviticus", "約翰貳書": "2 John", "哥林多前書": "1 Corinthians",
             "列王紀上": "1Kings", "列王紀下": "2Kings", "啟示錄": "Revelation",
             "哥林多後書": "2 Corinthians", "使徒行傳": "Acts", "申命記": "Deuteronomy",
             "民數記": "Numbers", "出埃及記": "Exodus", "西番雅書": "Zephaniah",
             "彌迦書": "Micah", "撒母耳記上": "1 Samuel"}

def generate_titles():
    with open(source_file_path, 'r') as f:
        source_data = f.read()
    # 以賽亞書1:9-14*
    regex_title = r"\..*\d+:\d+.*\r\n"
    titles = re.findall(regex_title, source_data)
    print "find {} titles".format(len(titles))

    with open(output_file_path, 'w') as target:
        for num, title in enumerate(titles):
            line = "{}) {}".format(num, title)
            # target.write(line + os.linesep)
            target.write(line)


'''
"http://www.biblegateway.com/passage/?search=#{passage}&version=#{VERSIONS[version]}""
'''
def get_verse(book, chapter, verse):

    en_book = book_dict[book]
    if not en_book:
        print "cann't find book {}".format(book)
        return

    url = "https://www.biblegateway.com/passage/?search={}+{}&version=NKJV".format(en_book, chapter)
    response = requests.get(url)
    content = response.content

    print content

if __name__ == '__main__':
    # generate_titles()
    verse = get_verse("出埃及記", 19, 4)
    print verse



