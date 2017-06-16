
import json
import requests

URL =  "http://musicbrainz.org/ws/2/artist/"


query_type = {  "simple": {}, "atr": {"inc": "aliases+tags+ratings"}, "aliases": {"inc": "aliases"}, "releases": {"inc": "releases"} }


def query_site(url, params, uid="", fmt="json"):
    
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data

def test():
    data  = query_by_name( URL, query_type["simple"], "First Aid Kit")
    names = 0
    for r in data['artists']:
        if r['name'] == 'First Aid Kit':
            names += 1
        
    print names
  
    
def main():
    results = query_by_name( URL, query_type["simple"], "Nirvana")
    pretty_print(results)

    print "\nARTIST:"
    pretty_print(results["artists"][3])

    artist_id = results["artists"][3]["id"]
    artist_data = query_site(URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]

    #print "\nONE RELEASE:"
    pretty_print(releases, indent=2)

    release_titles = [r["title"] for r in releases]
    print "\nALL TITLES:"
    for t in release_titles:
        print t


if __name__ == '__main__':
    test()
main()