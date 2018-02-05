from confmodel.errors import ConfigError
from vumi.tests.helpers import VumiTestCase

from vumi_unidecode_middleware import UnidecodeMiddleware


class UnidecodeMiddlewareTests(VumiTestCase):
    def make_unidecode_middleware(self, config):
        """
        Creates a fake UnidecodeMiddleware instance for testing.
        """
        worker = object()
        mw = UnidecodeMiddleware("test_unidecode", config, worker)
        mw.setup_middleware()
        self.addCleanup(mw.teardown_middleware)
        return mw

    def test_make_unidecode_middleware(self):
        """
        The make_unidecode_middleware helper function should return an instance
        of UnidecodeMiddleware
        """
        middleware = self.make_unidecode_middleware({})
        self.assertIsInstance(middleware, UnidecodeMiddleware)

    def test_invalid_message_direction(self):
        """
        If the config contains an invalid message direction, then a config
        error should be raised
        """
        with self.assertRaises(ConfigError) as e:
            self.make_unidecode_middleware({'message_direction': 'foo'})
        self.assertIn('foo', e.exception.message)
