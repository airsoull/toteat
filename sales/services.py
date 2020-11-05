# standar libraries
import requests
import logging

logger = logging.getLogger(__name__)

URL = 'https://storage.googleapis.com/backupdatadev/ejercicio/ventas.json'


def get_sales_data():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError as e:
        logger.error(e)
        return {}
    except requests.exceptions.HTTPError as e:
        logger.error(e)
        return {}
