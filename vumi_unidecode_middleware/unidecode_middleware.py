from confmodel.fields import ConfigText
from confmodel.errors import ConfigError
from unidecode import unidecode
from vumi.middleware import BaseMiddleware


class UnidecodeMiddlewareConfig(BaseMiddleware.CONFIG_CLASS):
    """
    Configuration parameters for UnidecodeMiddleware.
    """
    message_direction = ConfigText(
        "The message direction to convert. Either 'inbound', 'outbound', or "
        "'both'. Defaults to 'both'", default="both", static=True)
    ignore_characters = ConfigText(
        "The characters, besides ASCII characters, that should not be "
        "converted. defaults to no characters", default="", static=True)


class UnidecodeMiddleware(BaseMiddleware):
    """
    Middleware that passes message content through unidecode.
    """
    CONFIG_CLASS = UnidecodeMiddlewareConfig
    INBOUND = 'inbound'
    OUTBOUND = 'outbound'
    BOTH = 'both'
    MESSAGE_DIRECTIONS = [INBOUND, OUTBOUND, BOTH]

    def setup_middleware(self):
        if self.config.message_direction not in self.MESSAGE_DIRECTIONS:
            raise ConfigError(
                "{} is not a valid direction. Must be one of {}".format(
                    self.config.message_direction, self.MESSAGE_DIRECTIONS))

    def handle_inbound(self, message, connector_name):
        pass

    def handle_outbound(self, message, connector_name):
        pass

    def handle_event(self, event, connector_name):
        pass

    def handle_failure(self, failure, connector_name):
        pass
