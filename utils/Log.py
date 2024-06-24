import logging

# static
class Log:
    """
    Log is a class for managing logging in the application.

    This class provides methods to set up debug, info, and error loggers
    and log messages to a specified log file.

    Methods
    -------
    debug(message: str) -> None
        Logs a debug message using the debug logger.
    info(message: str) -> None
        Logs an informational message using the info logger.
    error(message: str) -> None
        Logs an error message using the error logger.
    """

    _debug_logger: logging.Logger | None
    _info_logger: logging.Logger | None
    _error_logger: logging.Logger | None

    @classmethod
    def _create_handler(cls) -> logging.FileHandler:
        """
        Creates and returns a file handler with a specific formatter.

        The handler writes log messages to the 'storage/logs/primate.log' file.

        Returns
        -------
        logging.FileHandler
            The file handler with the specified formatter.
        """
        formatter: logging.Formatter = logging.Formatter('%(asctime)s %(name)s "%(message)s"')
        handler: logging.FileHandler = logging.FileHandler("storage/logs/primate.log")
        handler.setFormatter(formatter)

        return handler

    @classmethod
    def _load_debug(cls) -> None:
        """
        Sets up the debug logger if it hasn't been set up already.

        This method configures the logger with a file handler and a formatter.
        The log messages are stored in the 'storage/logs/primate.log' file.
        """
        if not hasattr(cls, "_debug_logger"):
            debug_logger = logging.getLogger("DEBUG")
            debug_logger.setLevel(logging.DEBUG)
            debug_logger.addHandler(cls._create_handler())

            cls._debug_logger = debug_logger

    @classmethod
    def _load_info(cls) -> None:
        """
        Sets up the info logger if it hasn't been set up already.

        This method configures the logger with a file handler and a formatter.
        The log messages are stored in the 'storage/logs/primate.log' file.
        """
        if not hasattr(cls, "_info_logger"):
            info_logger = logging.getLogger("INFO")
            info_logger.setLevel(logging.INFO)
            info_logger.addHandler(cls._create_handler())

            cls._info_logger = info_logger

    @classmethod
    def _load_error(cls) -> None:
        """
        Sets up the error logger if it hasn't been set up already.

        This method configures the logger with a file handler and a formatter.
        The log messages are stored in the 'storage/logs/primate.log' file.
        """
        if not hasattr(cls, "_error_logger"):
            error_logger = logging.getLogger("ERROR")
            error_logger.setLevel(logging.ERROR)
            error_logger.addHandler(cls._create_handler())

            cls._error_logger = error_logger

    @classmethod
    def debug(cls, message: str) -> None:
        """
        Logs a debug message using the debug logger.

        This method ensures that the debug logger is set up before logging the message.

        Parameters
        ----------
        message : str
            The debug message to be logged.
        """
        cls._load_debug()
        cls._debug_logger.debug(message)

    @classmethod
    def info(cls, message: str) -> None:
        """
        Logs an informational message using the info logger.

        This method ensures that the info logger is set up before logging the message.

        Parameters
        ----------
        message : str
            The informational message to be logged.
        """
        cls._load_info()
        cls._info_logger.info(message)

    @classmethod
    def error(cls, message: str) -> None:
        """
        Logs an error message using the error logger.

        This method ensures that the error logger is set up before logging the message.

        Parameters
        ----------
        message : str
            The error message to be logged.
        """
        cls._load_error()
        cls._error_logger.error(message)
