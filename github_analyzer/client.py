import json
import requests
from types import ModuleType
from .constants import HTTP_STATUS_CODE, ERROR_CODE, URL

from . import resources

from .errors import NotFoundError, ServerError


def capitalize_camel_case(string):
    return "".join(map(str.capitalize, string.split('_')))


# Create a dict of resource classes
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and \
            capitalize_camel_case(name) in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[capitalize_camel_case(name)]


class Client:
    """Github client class"""

    DEFAULTS = {
        'base_url': URL.BASE_URL
    }

    def __init__(self, session=None, auth=None, **options):
        self.session = session or requests.Session()
        self.auth = auth

        self.base_url = self._set_base_url(**options)

        self.app_details = []

        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

    def _set_base_url(self, **options):
        base_url = self.DEFAULTS['base_url']

        if 'base_url' in options:
            base_url = options['base_url']
            del(options['base_url'])

        return base_url

    def set_app_details(self, app_details):
        self.app_details.append(app_details)

    def get_app_details(self):
        return self.app_details

    def request(self, method, path, **options):
        url = "{}{}".format(self.base_url, path)

        response = getattr(self.session, method)(url, auth=self.auth,
                                                 **options)
        if ((response.status_code >= HTTP_STATUS_CODE.OK) and
                (response.status_code < HTTP_STATUS_CODE.REDIRECT)):
            return response.json()
        else:
            msg = ""
            code = response.status_code
            json_response = response.json()
            if 'message' in json_response:
                msg = json_response['message']

            if code == ERROR_CODE.NOT_FOUND_ERROR:
                raise NotFoundError(msg)
            else:
                raise ServerError(msg)

    def get(self, path, params, **options):
        """
        Parses GET request options and dispatches a request
        """
        return self.request('get', path, params=params, **options)

    def post(self, path, data, **options):
        """
        Parses POST request options and dispatches a request
        """
        data, options = self._update_request(data, options)
        return self.request('post', path, data=data, **options)

    def patch(self, path, data, **options):
        """
        Parses PATCH request options and dispatches a request
        """
        data, options = self._update_request(data, options)
        return self.request('patch', path, data=data, **options)

    def delete(self, path, data, **options):
        """
        Parses DELETE request options and dispatches a request
        """
        data, options = self._update_request(data, options)
        return self.request('delete', path, data=data, **options)

    def put(self, path, data, **options):
        """
        Parses PUT request options and dispatches a request
        """
        data, options = self._update_request(data, options)
        return self.request('put', path, data=data, **options)

    def _update_request(self, data, options):
        """
        Updates The resource data and header options
        """
        data = json.dumps(data)

        if 'headers' not in options:
            options['headers'] = {}

        options['headers'].update({'Content-type': 'application/json'})

        return data, options
