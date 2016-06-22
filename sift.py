from uniprot import uniprot_ensp
import requests
import json
import sys
import time


def sift(uid, position, ancestral, minor):
    print "SIFT score"

    ensp = uniprot_ensp(uid)

    # Test if ENSP found

    try:
        if ensp[0]:
            pass
    except:
        print "No ENSP Found"
        return False

    #print ensp  # TO DO ever get multiple ENSPs?

    def converter(aa_name):

        names = {   'A': 'ala',
                    'R': 'arg',
                    'N': 'asn',
                    'D': 'asp',
                    'C': 'cys',
                    'Q': 'gln',
                    'E': 'glu',
                    'G': 'gly',
                    'H': 'his',
                    'I': 'ile',
                    'L': 'leu',
                    'K': 'lys',
                    'M': 'met',
                    'F': 'phe',
                    'P': 'pro',
                    'S': 'ser',
                    'T': 'thr',
                    'W': 'trp',
                    'Y': 'tyr',
                    'V': 'val'
                }

        aa = names.keys()[names.values().index(aa_name.lower())]
        return aa


    def sift_score(ensp, position, ancestral, minor):

        ensp = ensp[0]
        # Capitalised single letter aa code
        ancestral = converter(ancestral)
        minor = converter(minor)

        server = "http://rest.ensembl.org"  # base API URL
        ext = "/vep/human/hgvs/{}:p.{}{}{}".format(ensp, ancestral, position, minor)
        
        tries = 5

        while tries >= 0:
            try:
                r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
                decoded = r.json()

                # print decoded

                if type(decoded) == dict:
                    if 'error' in decoded.keys():
                        print decoded["error"]
                        return False
                elif type(decoded) == list:
                    if len(decoded) == 0:
                        print "REST API query returned an empty list"
                        return False
                    elif len(decoded) == 1:
                        # print json.dumps(decoded[0], indent=4, separators=(',', ': '))
                        # sift = decoded[0]['transcript_consequences'][1]['sift_score']  # old code doesn't account for sift_score not being in index 1 dict
                        sift = decoded[0]['transcript_consequences']
                        for i in sift:
                            if 'sift_score' in i.keys():
                                sift = i['sift_score']
                                break
                        return sift
            except:
                if tries == 0:
                    raise
                else:
                    time.sleep(1)
                    tries -= 1
                    continue
        '''
        if not r.ok:  # exception handling
          r.raise_for_status()
          sys.exit()
        '''

    # Call sift_score within sift function

    sift = sift_score(ensp, position, ancestral, minor)
    return sift
