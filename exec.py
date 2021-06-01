from youtubetomp3 import Youtubetomp3


def main():
    print("Execution !!!")


def exec():
    exec = Youtubetomp3()
    # exec.makeTheSearch("worship song")
    # names = exec.getNames() 'Break Every Chain',
    names = ['Yes I Will', 'New Wine',
             'Worthy Is The Lamb', 'Lead Me to the Cross', 'No One But You', 'Good Grace', 'Here I Am to Worship/Call', 'God, You’re So Good', 'Behold (Then Sings My Soul)', 'Run To The Father']

    for i in names:
        results = exec.goToYoutubeAndSearch(i)
        exec.execute(results)

    print("Success")


if __name__ == '__main__':
    main()
    exec()
# [['Who You Say I Am by Hillsong Lyrics', ['5 minutes', '27 seconds'], 'https://www.youtube.com/watch?v=GgBB863p2vw'], ['Who You Say I Am (Acoustic) - Hillsong Worship',
# ['3 minutes', '12 seconds'], 'https://www.youtube.com/watch?v=k-rjczm7uCo'], ['Who You Say I Am | Corey Voss | Worship Moments - Madison Street Worship', ['5 minutes', '29 seconds'], 'https://www.youtube.com/watch?v=Wt5q4_XRCBs'], ['Who You Say I Am - Cross Worship feat. Jillian Ellis', ['5 minutes', '24 seconds'], 'https://www.youtube.com/watch?v=76OFLNtX1ak'], ['Who You Say I Am | Anthem Lights', ['3 minutes', '41 seconds'], 'https://www.youtube.com/watch?v=Sp7V1HyZJhw'], ['Who You Say I Am - The Recording Collective (MultiTracks.com Session)', ['5 minutes', '38 seconds'], 'https://www.youtube.com/watch?v=UOhRXYy_6UU']]
# stop at Lord I need you 212 files uploaded
