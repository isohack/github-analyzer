from .base import Resource
from ..constants.url import URL


class Repository(Resource):
    def __init__(self, client=None):
        super(Repository, self).__init__(client)
        self.base_url = URL.REPOSITORY_GET_URL

    def fetch(self, username, repository_name, data={}, **kwargs):
        return super(Repository, self).get_url(self.base_url.format(user=username, repo=repository_name), data,
                                               **kwargs)
