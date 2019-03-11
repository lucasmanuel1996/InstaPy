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
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=0.8,
                                    delimit_by_numbers=True,
                                    max_followers=6000,
                                    max_following=3000,
                                    min_followers=100,
                                    min_following=100)

    session.set_user_interact(amount=2, randomize=False, percentage=80, media='Photo')

    session.set_skip_users(skip_private=False,
                           skip_no_profile_pic=True,
                           skip_business=True,
                           dont_skip_business_categories=['Photographer'])

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_d"],
                                 sleepyhead=True, stochastic_flow=True, notify_me=True,
                                 peak_likes=(57, 585),
                                 peak_comments=(21, 182),
                                 peak_follows=(48, None),
                                 peak_unfollows=(35, 402))

    session.set_do_like(enabled=True, percentage=100)
    session.set_do_comment(enabled=True, percentage=50)
    session.set_comments(
        ['I love your profile! @{}', '@{} Love it!',
         '@{} :heart::heart:', '@{}:fire::fire::fire:', '@{}:ok_hand::ok_hand::ok_hand:',
         u'Unreal!! :ok_hand::ok_hand: Would be awesome if '
         u'you would checkout my photos as well!',
         u'Nice!! :ok_hand::ok_hand: I would be honored '
         u'if you would checkout my images and tell me '
         u'what you think. :wink:',
         u'@{} Unreal :ok_hand: If '
         u'you have time, check out my photos, too. I '
         u'bet youll like them. :ok_hand:'],
        media='Photo')

    # follow activity
    # amount_number = 100
    insta_usernames = ['shaunllwellyn_',
                      'calquinn',
                      'the.97',
                      'laurenkhalfayan',
                      'cjharvey2',
                      'gregnoire',
                      'ian.laidlaw'
                      ]
    shuffled_users = insta_usernames[:]
    random.shuffle(shuffled_users)
    randomSleepDelay = random.randrange(540,830) # Makes timeouts seems more human

    session.follow_likers(shuffled_users, photos_grab_amount=2, follow_likers_per_photo=50, randomize=True,
                          sleep_delay=600, interact=True)

    # unfollow activity
    session.set_dont_unfollow_active_users(enabled=True, posts=5)
    session.unfollow_users(amount=300, InstapyFollowed=(False, "nonfollowers"), style="FIFO", unfollow_after=1,
                           sleep_delay=600)

