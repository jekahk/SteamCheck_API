from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

# asks the ID of the Steam profile the user wants to see


def scrape(url):

    # checks if the given ID is: full profile link / automated profile code / self set id
    if url.startswith("https://"):
        profile_url = url
        badge_url = f'{url}/badges/'

    elif url.isdecimal():
        profile_url = f'https://steamcommunity.com/profiles/{url}'
        badge_url = f'https://steamcommunity.com/profiles/{url}/badges/'

    else:
        profile_url = f'https://steamcommunity.com/id/{url}'
        badge_url = f'https://steamcommunity.com/id/{url}/badges/'

    try:

        # scrapes the website
        uClient = uReq(profile_url)
        page_profile = uClient.read()
        uClient.close()

        page_badge = requests.get(badge_url)

        profile_soup = soup(page_profile, "html.parser")
        badge_soup = soup(page_badge.content, "html.parser")

    # find the profile name
        name = ""
        container_name = profile_soup("div", {"class": "persona_name"})
        cont_name = container_name[0]
        name = cont_name.span.text

    # find the profile picture
        container_picture = profile_soup(
            "div", {"class": "playerAvatarAutoSizeInner"})
        cont_picture = container_picture[0]
        picture_images = cont_picture.findAll("img")
        if len(picture_images) == 2:
            picture_raw = picture_images[1]
            picture = picture_raw.get('src')
        else:
            picture_raw = picture_images[0]
            picture = picture_raw.get('src')

    # finds the profile level
        container_level = profile_soup(
            "div", {"class": "persona_name persona_level"})
        cont_lev = container_level[0]
        level = cont_lev.span.text

    # finds the profile level XP
        container_xp = badge_soup("div", {"class": "profile_xp_block"})
        cont_xp = container_xp[0]

        # finds the current amount of XP
        find_current_xp = cont_xp.findAll(
            "span", {"class": "profile_xp_block_xp"})
        xp_current = find_current_xp[0]
        xp = xp_current.text

        # finds the amount of XP needed for next level
        find_needed_xp = cont_xp.findAll(
            "div", {"class": "profile_xp_block_remaining"})
        xp_needed = find_needed_xp[0]
        nxp = xp_needed.text

    # finds the amount of badges
        container_badge = profile_soup.findAll(
            "span", {"class": "profile_count_link_total"})
        cont_bad = container_badge[0]
        badge_raw = cont_bad.text
        badge = badge_raw.strip()

        return name, picture, level, badge, xp, nxp, ""

    except Exception as e:
        if name != "":
            private = 'This profile is private.'
            return name, picture, "", "", "", "", private
        else:
            invalid = 'Invalid ID or Link.'
            return "", "", "", "", "", "", invalid
