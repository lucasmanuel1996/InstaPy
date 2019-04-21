"""
This template is written by @zackvega

What does this quickstart script aim to do?
- This is my simple but effective script.
"""

from instapy import InstaPy
from instapy.util import smart_run
import random


# get a session!
session = InstaPy(headless_browser=True,
                  multi_logs=True)

# let's go! :>
with smart_run(session):

    val = 100000
    i = 0

    while (i < val):
        # general setting

        session.set_quota_supervisor(enabled=True,
                                     sleep_after=[
                                         "likes", "comments_d", "follows", "unfollows", "server_calls_d", "server_calls_h"],
                                     sleepyhead=True, stochastic_flow=True, notify_me=True,
                                     peak_likes=(57, 585),
                                     peak_comments=(21, 182),
                                     peak_follows=(160, None),
                                     peak_unfollows=(300, None),
                                     peak_server_calls=(500, None))

        # Makes timeouts seems more human
        randomSleepDelay = random.randrange(140, 330)

        # unfollow activity
        # session.set_dont_unfollow_active_users(enabled=True, posts=5)
        # session.unfollow_users(amount=3300, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=96*60*60,
        #                        sleep_delay=randomSleepDelay)
        session.unfollow_users(amount=4440, allFollowing=True,
                               style="LIFO", unfollow_after=3*60*60, sleep_delay=randomSleepDelay)
        i = i + 1
