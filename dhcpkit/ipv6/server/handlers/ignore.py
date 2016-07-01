"""
A simple handler that tells the server to ignore the request.
"""
import logging

from typing import Type, Iterable

from dhcpkit.ipv6.messages import Message
from dhcpkit.ipv6.server.handlers import Handler, CannotRespondError, HandlerFactory
from dhcpkit.ipv6.server.transaction_bundle import TransactionBundle

logger = logging.getLogger(__name__)


class IgnoreRequestHandler(Handler):
    """
    A simple handler that tells the server to stop processing the request and ignore it
    """
    def __init__(self, message_types: Iterable[Type[Message]]):
        super().__init__()
        self.message_types = tuple(set(message_types))

    def pre(self, bundle: TransactionBundle):
        """
        Stop processing

        :param bundle: The transaction bundle
        """
        if isinstance(bundle.request, self.message_types):
            logging.info("Configured to ignore {}".format(bundle))
            raise CannotRespondError("Ignoring request")


class IgnoreRequestHandlerFactory(HandlerFactory):
    """
    Create an IgnoreRequestHandler
    """

    def create(self) -> Handler:
        """
        Create an IgnoreRequestHandler
        """
        return IgnoreRequestHandler(self.message_types)
