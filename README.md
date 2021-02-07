# ![SteamCheckerAPI](https://github.com/jekahk/portfolio/blob/master/src/Assets/SteamCheckAPI.png?raw=true)

API service to scrape data from Steam profiles. It is made using python with [flask](https://flask.palletsprojects.com/en/1.1.x/) and [BeatifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) libraries. The API scrapes the profiles HTML, which ID or URL is given by frontend, and finds the specific data from there. It finds profile name, picture, level, number of padges, experience points and how much XP needed for level up. It sends them back to the frontend by an object. The API also checks if the given ID/URL is invalid or the profile is private. 

## Deployment

I have deployd this API on a Virtual private server using [NGINX](https://www.nginx.com/) and [Gunicorn3](https://gunicorn.org/). The server has a HTTPS sertificate that is made with [Certbot](https://certbot.eff.org/). 

URL for the API is https://www.steam-check-api.xyz/
