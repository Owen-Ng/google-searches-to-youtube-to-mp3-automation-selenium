from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from song_namescollection import namesCollections
import sys

# Where you access Youtube and collect the links and appropriate name for mp3 conversion


class Download(namesCollections):

    def goToYoutubeAndSearch(self, search):
        self.searchresult = search
        self.driver.get("https://youtube.com")
        time.sleep(1)
        self.Search(search)
        time.sleep(1)

        return self.SearchResult()

    def Search(self, search):

        s = self.driver.find_element_by_id("search")
        s.send_keys(search)
        s.send_keys(Keys.RETURN)

    def SearchResult(self):
        try:
            resultcontainer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "ytd-item-section-renderer"))
                # EC.presence_of_elements_located((By.CLASS_NAME, "KKHQ8c"))
            )

            # print(resultcontainer[3])
            results = resultcontainer[3].find_elements_by_tag_name(
                "ytd-video-renderer")

            tmp = []
            counter = 0
            for index, i in enumerate(results):

                ls = i.text.split("\n")
                href = i.find_element_by_id("thumbnail")
                authors = i.find_elements_by_class_name("yt-simple-endpoint")
                ls.append(href.get_attribute("href"))
                author = authors[3].text
                timetag = i.find_elements_by_class_name(
                    "ytd-thumbnail-overlay-time-status-renderer")

                try:

                    time = timetag[1]
                    if "hour" in time.get_attribute("aria-label"):
                        continue
                    ls.append(time.get_attribute("aria-label"))
                    title = ls[0]
                    timestamp = ls[-1].split(", ")
                    link = ls[-2]
                    # print(timestamp[1][0], title.lower(), self.search in title.lower(), len(
                    #     timestamp), timestamp, end="\n")
                    if counter > 30:
                        print(counter, 2)
                        break
                    if len(timestamp) <= 2 and self.searchresult.lower() in title.lower() and int(timestamp[0].split(" ")[0]) <= 6:
                        counter += 1

                        tmp.append(
                            {"title": title, "timestamp": timestamp, "link": link, "author": author, "searchresult": self.searchresult})
                except:
                    continue
            return tmp

        except:
            print(sys.exc_info())
            # self.driver.quit()


# test = Download()
# print(test.goToYoutubeAndSearch("who you say I am"))
