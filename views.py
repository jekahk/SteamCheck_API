from flask import Blueprint, jsonify, request
from App import scrape
import sqlite3
from datetime import datetime

main = Blueprint('main', __name__)
@main.route('/give_id', methods=['POST'])

def give_id():
    
    id_data = request.get_json()

    name, picture, level, badge, xp, nxp, private  = scrape(id_data['SteamId'])

    con = sqlite3.connect("steamcheckerDB.db")
    cur = con.cursor()

    obj = {
        "name" : name,
        "picture" : picture,
        "level" : level,
        "badge" : badge,
        "xp" : xp,
        "nxp" : nxp,
        "private" : private
    }

    if private == "":
        xp = xp.replace("XP ", "")
        dt = datetime.now()
        cur.execute("INSERT INTO history VALUES ('{}',{},{},'{}','{}')".format(name,level,badge,xp,dt))
        con.commit()

    return obj, 201

@main.route('/get_history', methods=['GET'])
def get_history():
    con = sqlite3.connect("steamcheckerDB.db")
    cur = con.cursor()
    result = cur.execute("SELECT * FROM(SELECT name, level, badge, xp, row_number() OVER (ORDER BY timestamp DESC) row_num FROM (SELECT * FROM history)) WHERE row_num <= 10")
    result = result.fetchall();
    return result
