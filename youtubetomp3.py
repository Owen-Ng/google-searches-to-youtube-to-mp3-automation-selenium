from downloads import Download
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# This accesses  https://youtubetomp3music.com/en17/ that convert youtube link to mp3


class Youtubetomp3(Download):
    def execute(self, data):
        self.gotowebsite()
        for d in data:
            self.search(d['link'])
            self.conversion()
            self.download(d['searchresult'], d['author'])

    def gotowebsite(self):
        self.driver.get("https://youtubetomp3music.com/en17/")

    def search(self, link):
        s = self.driver.find_element_by_id("url")
        s.send_keys(link)
        s.send_keys(Keys.RETURN)

    def conversion(self):
        # formatselect = self.driver.find_element_by_id("formatselect")
        # formatselect.click()
        try:
            convertbutton = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "cvt-btn"))
                # EC.presence_of_elements_located((By.CLASS_NAME, "KKHQ8c"))
            )
            convertbutton.click()
        except:
            print(sys.exc_info())
            self.driver.quit()

    def stop(self):
        self.driver.quit()

    def download(self, title, author):
        try:
            href = WebDriverWait(self.driver, 1000).until(
                EC.presence_of_element_located(
                    (By.ID, "mp3-dl-btn"))

            )
            href = href.get_attribute("href")
            ls = href.split("fn=")
            title = title.replace(" ", "")
            author = author.replace(" ", "")

            link = ls[0]

            if (len(title) > 20):
                title = title[:20]
            name = author + "_" + title
            self.driver.get(link + "fn=" + name + ".mp3")
            print(link + "fn=" + name)
        except:
            print(sys.exc_info())
            # self.driver.quit()

    # ['Who You Say I Am by Hillsong Lyrics', ['5 minutes', '27 seconds'], 'https://www.youtube.com/watch?v=GgBB863p2vw']
# test = Youtubetomp3()
# test.execute([{'title': 'Yancy - Who You Say I Am [OFFICIAL LYRIC VIDEO] Kids Worship', 'timestamp': ['3 minutes',
#              '43 seconds'], 'link': 'https://www.youtube.com/watch?v=YUfwoUPTg68', 'author': 'YancynotNancy'}])
# {'title': 'Yancy - Who You Say I Am [OFFICIAL LYRIC VIDEO] Kids Worship', 'timestamp': ['3 minutes', '43 seconds'], 'link': 'https://www.youtube.com/watch?v=YUfwoUPTg68', 'author': 'YancynotNancy'}
