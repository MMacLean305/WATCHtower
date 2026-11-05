import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_session():
    retry_strategy = Retry(total=4, backoff_factor=1, backoff_max=30, backoff_jitter=0.5, status_forcelist=[429, 500, 502, 503, 504], allowed_methods=["GET"], respect_retry_after_header=True)

    adapter = HTTPAdapter(max_retries=retry_strategy)

    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    return session
