import logging

# static
class Log:
    """
    Log é uma classe para gerenciar logs na aplicação.

    Esta classe fornece métodos para configurar loggers de debug, info e erro,
    e registrar mensagens em um arquivo de log especificado.

    Métodos
    -------
    debug(message: str) -> None
        Registra uma mensagem de debug usando o logger de debug.
    info(message: str) -> None
        Registra uma mensagem informativa usando o logger de info.
    error(message: str) -> None
        Registra uma mensagem de erro usando o logger de erro.
    """

    _debug_logger: logging.Logger | None
    _info_logger: logging.Logger | None
    _error_logger: logging.Logger | None

    @classmethod
    def _create_handler(cls) -> logging.FileHandler:
        """
        Cria e retorna um manipulador de arquivo com um formatador específico.

        O manipulador escreve mensagens de log no arquivo 'storage/logs/primate.log'.

        Retorna
        -------
        logging.FileHandler
            O manipulador de arquivo com o formatador especificado.
        """
        formatter: logging.Formatter = logging.Formatter('%(asctime)s %(name)s "%(message)s"')
        handler: logging.FileHandler = logging.FileHandler("storage/logs/primate.log")
        handler.setFormatter(formatter)

        return handler

    @classmethod
    def _load_debug(cls) -> None:
        """
        Configura o logger de debug se ainda não foi configurado.

        Este método configura o logger com um manipulador de arquivo e um formatador.
        As mensagens de log são armazenadas no arquivo 'storage/logs/primate.log'.
        """
        if not hasattr(cls, "_debug_logger"):
            debug_logger = logging.getLogger("DEBUG")
            debug_logger.setLevel(logging.DEBUG)
            debug_logger.addHandler(cls._create_handler())

            cls._debug_logger = debug_logger

    @classmethod
    def _load_info(cls) -> None:
        """
        Configura o logger de info se ainda não foi configurado.

        Este método configura o logger com um manipulador de arquivo e um formatador.
        As mensagens de log são armazenadas no arquivo 'storage/logs/primate.log'.
        """
        if not hasattr(cls, "_info_logger"):
            info_logger = logging.getLogger("INFO")
            info_logger.setLevel(logging.INFO)
            info_logger.addHandler(cls._create_handler())

            cls._info_logger = info_logger

    @classmethod
    def _load_error(cls) -> None:
        """
        Configura o logger de erro se ainda não foi configurado.

        Este método configura o logger com um manipulador de arquivo e um formatador.
        As mensagens de log são armazenadas no arquivo 'storage/logs/primate.log'.
        """
        if not hasattr(cls, "_error_logger"):
            error_logger = logging.getLogger("ERROR")
            error_logger.setLevel(logging.ERROR)
            error_logger.addHandler(cls._create_handler())

            cls._error_logger = error_logger

    @classmethod
    def debug(cls, message: str) -> None:
        """
        Registra uma mensagem de debug usando o logger de debug.

        Este método garante que o logger de debug esteja configurado antes de registrar a mensagem.

        Parâmetros
        ----------
        message : str
            A mensagem de debug a ser registrada.
        """
        cls._load_debug()
        cls._debug_logger.debug(message)

    @classmethod
    def info(cls, message: str) -> None:
        """
        Registra uma mensagem informativa usando o logger de info.

        Este método garante que o logger de info esteja configurado antes de registrar a mensagem.

        Parâmetros
        ----------
        message : str
            A mensagem informativa a ser registrada.
        """
        cls._load_info()
        cls._info_logger.info(message)

    @classmethod
    def error(cls, message: str) -> None:
        """
        Registra uma mensagem de erro usando o logger de erro.

        Este método garante que o logger de erro esteja configurado antes de registrar a mensagem.

        Parâmetros
        ----------
        message : str
            A mensagem de erro a ser registrada.
        """
        cls._load_error()
        cls._error_logger.error(message)

    def track(func: callable) -> callable:
        """
        Decorador que faz o tracking (rastreamento) de chamadas de métodos, registrando a entrada
        e a saída do método no log.

        Retorna
        -------
        callable
            Função decorada.
        """
        def wrapper(*args: any, **kwargs: any):
            Log.debug(f"Chamado {func.__name__}")

            result: any = func(*args, **kwargs)

            Log.debug(f"Finalizado {func.__name__}")
            return result
        return wrapper
