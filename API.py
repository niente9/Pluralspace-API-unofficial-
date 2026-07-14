from gettext import find
import requests
import json
import time
from bs4 import BeautifulSoup
from lxml import etree
import pprint


payload = {
    "email": input("Enter your email: "),
    "password": input("Enter your password: ")
}

stime = time.time()

headers = {
    'Host': 'pluralspace.app',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Origin': 'https://pluralspace.app',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://pluralspace.app/login',
    'Cookie': 'XSRF-TOKEN=eyJpdiI6IkcxZkcyS3loV080dGhUa1NNMWJXbGc9PSIsInZhbHVlIjoieDVlUERXWkVTTW1DU2VGRVppajJ0NUhFbUpzTHBFeWVwdWthYm10dEpzWHFwTEJVaEtBY2tuWWt3TitvSEhXOU11RmVGNU4vZW9BeXpBWkFNU2tqcGxPZlptQTNab2F3ZURJU2pVdWZwalVhcDFmSnVzOFVta21QOTlGcUYzZi8iLCJtYWMiOiIwZDZiNzA1ZWE1MDQ5YjczMmUyODExMzUwNDAxNTRkZmRiOWMzZWMwOTkyOTRjNjYyYjIzZGM0N2U5ZWUwNTg0IiwidGFnIjoiIn0%3D; pluralspace-session=eyJpdiI6ImlhM3RRMU9LaDdUbEM1V2x2UU9teUE9PSIsInZhbHVlIjoiLytqUEVDRkFJbjd4dktKK0F6R1JHMytTSmlpRUhpUTVlWm1WSmxZTzJQQU85cmg2NktyMDNvWHhnSHRiWHJUTFc4c2tOcllJVkQxazNqQkZQK3ZwOXFiSVBIem5rYU5LZmsrM2s4TjBQVWJmMEJuSkgxcXZjRzlsUWpMODJtVksiLCJtYWMiOiI2NGIwYWMzZTc4ZWJmY2IxYjkxNjZiMTNhY2I1MjIyZTU0YjI1ZWJiYjk5NzU1ZjcyNDM3YTRiZWIwYmFhN2ZhIiwidGFnIjoiIn0%3D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'DNT': '1',
    'TE': 'trailers',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0',
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'X-XSRF-TOKEN': 'eyJpdiI6IkcxZkcyS3loV080dGhUa1NNMWJXbGc9PSIsInZhbHVlIjoieDVlUERXWkVTTW1DU2VGRVppajJ0NUhFbUpzTHBFeWVwdWthYm10dEpzWHFwTEJVaEtBY2tuWWt3TitvSEhXOU11RmVGNU4vZW9BeXpBWkFNU2tqcGxPZlptQTNab2F3ZURJU2pVdWZwalVhcDFmSnVzOFVta21QOTlGcUYzZi8iLCJtYWMiOiIwZDZiNzA1ZWE1MDQ5YjczMmUyODExMzUwNDAxNTRkZmRiOWMzZWMwOTkyOTRjNjYyYjIzZGM0N2U5ZWUwNTg0IiwidGFnIjoiIn0=',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'X-inertia': 'true',
    'X-inertia-version': 'b28a77258362a34e888b85b92b6b39f9',
    'Priority': 'u=0'
}

headers2 = {
    'Host': 'pluralspace.app',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:152.0) Gecko/20100101 Firefox/152.0',
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://pluralspace.app/',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Cookie': 'cf_clearance=XmpkniDrveB_CaWFocs9S7OLqy_fSFWB28f3eKmagUM-1776134969-1.2.1.1-HVXTWr48eFcQyAFeUCXkbiLKWiTSPqWxLEUj5_Ix.W6tSPy3GfnDYW0WHShOf9Cw2XZRds_9mpeDr0bLM2iIFyNgW.jdSiBkj2T7DnFH8g6Pjbhd2fsL72vKjiVSB9ycVxr48ssZWLcWbYiYCqtLhmUN6HjnYyHmh2.DSU2uiavYw3AOfR6dFZeU4f4TC5zrFSS6sKOs.0BxQMz1Rw24pwbF4DnG8ciaw60uL3FzY1BeQaTqpYOFFmuRhGbVEosx8KaO1OEaUwDExMYZiFW9Iu1gNi9pOfH3LARiC6lQ3sn91PtXdfAkr.NKha6yahgxB9iPtVFo4tIEff1FNSxPrg; eloquent_viewable=eyJpdiI6IkthbVd3VEFUaW5kRzVkMDM2dlBRWWc9PSIsInZhbHVlIjoiY0NEdU5uM1luZWVNbDNiZ0V5Z2lYa2F6ZU1QRkxUYXU3Nk1nRTZSdjFOSDlYbTFMTHI4THZXaTZ0N0d1dHQzSVVWdUo1aFdwV213d0JMZDFZTTB0dXRlTHdKK3hMWmkvYjBZQXBKZ01NZ0Y1R2F4bThrazM3TFFmK2tQd0xpU0p3d1JpLzhSYlFxUjYwL2FlN1FTOE9vV09mMW54cUIvQks1UTdGWUQ5NGIwPSIsIm1hYyI6ImI3OGY1YjkwYzYwZmZhMDkyNjg2ZjU5NWEzNDdiYzc1NGYwNDk1MzRlYjlmYzdiZTgwMzRiNDY2YjgyOWY1NzUiLCJ0YWciOiIifQ%3D%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6Inh2R292TDExbDAwQVVVVEk3K05IZ0E9PSIsInZhbHVlIjoiUE9zeHg1TjdET2lBWnd0TjNPM0R3UHFGaFVjRWIyeXo1K0ZaaVR3NHZ2ejcveVM4dXU5bUVTajQ3OXlJSVhTYmthTzk2NHU0ckJjSUtVL05YbE9TRFpZR3pMUGRmakRKU1FGbHR4M25VNlFPbFdpTDJNdlZnSXpyaTFXQUdVaVpkOGxDbHQ4UWg5N1l0YndpLzQ1Y2VUYVBFNkRyUmRkSzlxL05JMlRSRjRyOHBxNzBKWFdtRU9xYXgzbjVodWI4NDM5YTEzN2tWSVYzcXl2ZTlFYmUrQXAxUEhOYk85bnl0dGtBRGFHS0p2ND0iLCJtYWMiOiJkN2VmOGMxODVmNTg2OWNjYTYyODdhZTU4ODU5ZTA1NDZlMTFlODgyNjdiZTJlODZkYzEwZTM1YmI3ZTk3ZjUzIiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6IkVJNUlKUHNFaFdsRDBWMEJTNGl5dnc9PSIsInZhbHVlIjoiMm5yYmZsd1BWYzVyTkY0bnI4YVFpOUk0MDZMUEhRakF0MFZDeDAreFNyTTMwQnhORDB4WVJvUEpFRFlqbTJsajJCSVZSeXRmV3ZOSEFGWXB4VmFGcWlqeGZjMnRENncwRGNVbXlHTlRUQXUrQzJxZWN4SVlSVDJYc0hTVDUyRnQiLCJtYWMiOiI5YTc5MGU3MTAzYWQ5MGUzYmVmZDgxMzBiM2I2Zjg1MDBjNWZiMTM2NmEyNzk5NzgzMWU0YjU3MWY3ZWU1MTg4IiwidGFnIjoiIn0%3D; pluralspace-session=eyJpdiI6IllaRDZFdFBhQXFNaU5sN20wdFFaaEE9PSIsInZhbHVlIjoiSU9QajlaUzhkM3JZSXY2UHBXUTRBdjB3bkhseFJ2MEZKd3kxN0tqVTFlNHh5OXZ2Z2hlV1ZBNXFWbm4xSWg5NkxnRVBtK0lCNVRGeTZQdkRlREFXK2E3MlBtTFNNdk9QaGhoZU5YNUR2c2JvME5SRU5kRW1lQWE1OThMNE5JRVgiLCJtYWMiOiJiNDBjNTg1YzhjMDU1YTUzNzRlYTZhNjdiM2VmNWJhYzEwZDk0YTBmNWUzMWY2MzI3MzUyZTk3YzY4MDY5MTUzIiwidGFnIjoiIn0%3D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'DNT': '1',
    'TE': 'trailers',
    'X-XSRF-TOKEN': 'eyJpdiI6IkVJNUlKUHNFaFdsRDBWMEJTNGl5dnc9PSIsInZhbHVlIjoiMm5yYmZsd1BWYzVyTkY0bnI4YVFpOUk0MDZMUEhRakF0MFZDeDAreFNyTTMwQnhORDB4WVJvUEpFRFlqbTJsajJCSVZSeXRmV3ZOSEFGWXB4VmFGcWlqeGZjMnRENncwRGNVbXlHTlRUQXUrQzJxZWN4SVlSVDJYc0hTVDUyRnQiLCJtYWMiOiI5YTc5MGU3MTAzYWQ5MGUzYmVmZDgxMzBiM2I2Zjg1MDBjNWZiMTM2NmEyNzk5NzgzMWU0YjU3MWY3ZWU1MTg4IiwidGFnIjoiIn0=',
    'Cache-Control': 'no-cache',
    'X-Inertia-Partial-Component': 'App/Dashboard',
    'X-Inertia-Partial-Data': 'currentFronts,currentMember',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Inertia': 'true',
    'X-Inertia-Version': '5369c460e0b8c26fbefcc14d99a70f0a',
    'Pragma': 'no-cache'
}

headers3 = {
    'Host': 'pluralspace.app',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:152.0) Gecko/20100101 Firefox/152.0',
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://pluralspace.app/',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Cookie': 'cf_clearance=XmpkniDrveB_CaWFocs9S7OLqy_fSFWB28f3eKmagUM-1776134969-1.2.1.1-HVXTWr48eFcQyAFeUCXkbiLKWiTSPqWxLEUj5_Ix.W6tSPy3GfnDYW0WHShOf9Cw2XZRds_9mpeDr0bLM2iIFyNgW.jdSiBkj2T7DnFH8g6Pjbhd2fsL72vKjiVSB9ycVxr48ssZWLcWbYiYCqtLhmUN6HjnYyHmh2.DSU2uiavYw3AOfR6dFZeU4f4TC5zrFSS6sKOs.0BxQMz1Rw24pwbF4DnG8ciaw60uL3FzY1BeQaTqpYOFFmuRhGbVEosx8KaO1OEaUwDExMYZiFW9Iu1gNi9pOfH3LARiC6lQ3sn91PtXdfAkr.NKha6yahgxB9iPtVFo4tIEff1FNSxPrg; eloquent_viewable=eyJpdiI6IkthbVd3VEFUaW5kRzVkMDM2dlBRWWc9PSIsInZhbHVlIjoiY0NEdU5uM1luZWVNbDNiZ0V5Z2lYa2F6ZU1QRkxUYXU3Nk1nRTZSdjFOSDlYbTFMTHI4THZXaTZ0N0d1dHQzSVVWdUo1aFdwV213d0JMZDFZTTB0dXRlTHdKK3hMWmkvYjBZQXBKZ01NZ0Y1R2F4bThrazM3TFFmK2tQd0xpU0p3d1JpLzhSYlFxUjYwL2FlN1FTOE9vV09mMW54cUIvQks1UTdGWUQ5NGIwPSIsIm1hYyI6ImI3OGY1YjkwYzYwZmZhMDkyNjg2ZjU5NWEzNDdiYzc1NGYwNDk1MzRlYjlmYzdiZTgwMzRiNDY2YjgyOWY1NzUiLCJ0YWciOiIifQ%3D%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6Inh2R292TDExbDAwQVVVVEk3K05IZ0E9PSIsInZhbHVlIjoiUE9zeHg1TjdET2lBWnd0TjNPM0R3UHFGaFVjRWIyeXo1K0ZaaVR3NHZ2ejcveVM4dXU5bUVTajQ3OXlJSVhTYmthTzk2NHU0ckJjSUtVL05YbE9TRFpZR3pMUGRmakRKU1FGbHR4M25VNlFPbFdpTDJNdlZnSXpyaTFXQUdVaVpkOGxDbHQ4UWg5N1l0YndpLzQ1Y2VUYVBFNkRyUmRkSzlxL05JMlRSRjRyOHBxNzBKWFdtRU9xYXgzbjVodWI4NDM5YTEzN2tWSVYzcXl2ZTlFYmUrQXAxUEhOYk85bnl0dGtBRGFHS0p2ND0iLCJtYWMiOiJkN2VmOGMxODVmNTg2OWNjYTYyODdhZTU4ODU5ZTA1NDZlMTFlODgyNjdiZTJlODZkYzEwZTM1YmI3ZTk3ZjUzIiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6IkVJNUlKUHNFaFdsRDBWMEJTNGl5dnc9PSIsInZhbHVlIjoiMm5yYmZsd1BWYzVyTkY0bnI4YVFpOUk0MDZMUEhRakF0MFZDeDAreFNyTTMwQnhORDB4WVJvUEpFRFlqbTJsajJCSVZSeXRmV3ZOSEFGWXB4VmFGcWlqeGZjMnRENncwRGNVbXlHTlRUQXUrQzJxZWN4SVlSVDJYc0hTVDUyRnQiLCJtYWMiOiI5YTc5MGU3MTAzYWQ5MGUzYmVmZDgxMzBiM2I2Zjg1MDBjNWZiMTM2NmEyNzk5NzgzMWU0YjU3MWY3ZWU1MTg4IiwidGFnIjoiIn0%3D; pluralspace-session=eyJpdiI6IllaRDZFdFBhQXFNaU5sN20wdFFaaEE9PSIsInZhbHVlIjoiSU9QajlaUzhkM3JZSXY2UHBXUTRBdjB3bkhseFJ2MEZKd3kxN0tqVTFlNHh5OXZ2Z2hlV1ZBNXFWbm4xSWg5NkxnRVBtK0lCNVRGeTZQdkRlREFXK2E3MlBtTFNNdk9QaGhoZU5YNUR2c2JvME5SRU5kRW1lQWE1OThMNE5JRVgiLCJtYWMiOiJiNDBjNTg1YzhjMDU1YTUzNzRlYTZhNjdiM2VmNWJhYzEwZDk0YTBmNWUzMWY2MzI3MzUyZTk3YzY4MDY5MTUzIiwidGFnIjoiIn0%3D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'DNT': '1',
    'TE': 'trailers',
    'Cache-Control': 'no-cache',
    'X-Inertia-Partial-Component': 'App/Members/Show',
    'X-Inertia-Partial-Data': 'member,customFields',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Inertia': 'true',
    'X-Inertia-Version': '5369c460e0b8c26fbefcc14d99a70f0a'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as session:
    p = session.post('https://pluralspace.app/login', data=payload, headers=headers)
    # print(p.text)
    # An authorised request.
    frontResponse = session.get('https://pluralspace.app/space', headers=headers2)
    #print(frontResponse.headers)
    #print(frontResponse.text)      #for debugging purposes. prints entire HTML. or just go to view-source:https://pluralspace.app/space....

    if frontResponse.status_code == 200:
        try:
            frontJson = json.loads(frontResponse.text)
            frontJsonPretty = (json.dumps(frontJson, sort_keys=True, indent=4))  # Pretty print the JSON data
            # print(frontResponse.url)
            # print(frontJsonPretty)  # Print the pretty JSON data

            try:
                currentMemberName = frontJson['props']['currentMember']['name']
                currentMemberId = frontJson['props']['currentMember']['id']
                memberJson = json.loads(session.get(f'https://pluralspace.app/members/{currentMemberId}', headers=headers3).text)
                try:
                    description = BeautifulSoup(memberJson['props']['member']['description_html'], 'lxml').text[:-1]
                except TypeError:
                    description = ""
                    pass
                memberInfo = {
                    'memberName': currentMemberName,
                    'memberId': currentMemberId,
                    #'membersJson': membersJson['props'][],
                    'memberPrns': memberJson['props']['member']['pronouns'],
                    'memberColor': memberJson['props']['member']['color'],
                    'memberAvatar': memberJson['props']['member']['avatar_url'],
                    "Description": description,
                    "messagePrefix": memberJson['props']['member']['message_prefix'],
                    "customFields": {field['name']: field['value'] for field in memberJson['props']['customFields']}
                }
            except TypeError:
                pass

            frontLength = len(frontJson['props']['currentFronts'])
            fronterInfo = []

            for fronters in range(frontLength):
                fronterId = frontJson['props']['currentFronts'][fronters]['member']['id']
                time.sleep(1)     # delay to not overwhelm the pluralspace servers with repeated requests
                membersJson = json.loads(session.get(f'https://pluralspace.app/members/{fronterId}', headers=headers3).text)
                try:
                    description = BeautifulSoup(membersJson['props']['member']['description_html'], 'lxml').text[:-1]
                except TypeError:
                    description = ""
                    pass
                fronterInfo.append({
                    'fronterName': frontJson['props']['currentFronts'][fronters]['member']['display_label'],
                    'fronterId': fronterId,
                    #'membersJson': membersJson['props'][],
                    'fronterPrns': membersJson['props']['member']['pronouns'],
                    'fronterColor': membersJson['props']['member']['color'],
                    'fronterAvatar': membersJson['props']['member']['avatar_url'],
                    "Description": description,
                    "messagePrefix": membersJson['props']['member']['message_prefix'],
                    "customFields": {field['name']: field['value'] for field in membersJson['props']['customFields']}
                })

            #pprint.pprint(fronterInfo)
            output = {
                'currentMemberInfo': memberInfo,
                'fronterInfo': fronterInfo
            }
            pprint.pprint(output)
            
        except (requests.exceptions.HTTPError, NameError) as e:
            print(f"Error occurred: {e}")
    else:
        print(f"Request failed with status code: {frontResponse.status_code}")
    # print(frontResponse.url + "\n")


etime = time.time()
print("execution time: " + str(round(etime - stime, 4)) + " seconds")