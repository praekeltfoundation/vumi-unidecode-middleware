from vumi.middleware import BaseMiddleware


class UnidecodeMiddlewareConfig(BaseMiddleware.CONFIG_CLASS):
    """
    Configuration parameters for UnidecodeMiddleware.
    """
    pass


class UnidecodeMiddleware(BaseMiddleware):
    """
    Middleware that passes message content through unidecode.
    """
    CONFIG_CLASS = UnidecodeMiddlewareConfig

    def setup_middleware(self):
        pass

    def teardown_middleware(self):
        pass

    def handle_inbound(self, message, connector_name):
        pass

    def handle_outbound(self, message, connector_name):
        pass

    def handle_event(self, event, connector_name):
        pass

    def handle_failure(self, failure, connector_name):
        pass
