from .base import Resource
from ..constants.url import URL


class Repository(Resource):
    def __init__(self, client=None):
        super(Repository, self).__init__(client)
        self.fetch_repository = URL.FETCH_REPOSITORY_URL
        self.fetch_all_repository = URL.FETCH_ALL_REPOSITORY_URL

    def fetch(self, username, repository_name, data={}, **kwargs):
        return super(Repository, self).get_url(self.fetch_repository.format(username=username, repo=repository_name), data,
                                               **kwargs)

    def fetch_all(self, username, data={}, **kwargs):
        return super(Repository, self).get_url(self.fetch_all_repository.format(username=username), data,
                                               **kwargs)
