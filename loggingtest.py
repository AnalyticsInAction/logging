import datetime
import logging
import requests
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    logging.info('Logging:Python timer trigger function started running at %s', utc_timestamp)  

    def return_json(url):
        try:
            response = requests.get(url)
            if response.status_code // 100 == 2:                
                return [logging.info(f"Logging :Status code returned: {response.status_code} for this url {url}"), response.json()]
            else:
                return [logging.info(f"Logging :Status code returned: {response.status_code}, for this url {url}")]
        except:
            return [logging.info(f"Logging : Status code wasn't returned, an error must of occured, for this url {url}") ]

    test_urls = ["https://api.agify.io?name=bella", "https://api.agify.io?name=steve",  "http://httpbin.org/status/404", "http://httpbin.org/status/500",  "http://invalid/url"]

    for each_url in test_urls:
        print(return_json(each_url))
