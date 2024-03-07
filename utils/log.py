import logging
import os


def setup_logging(logdir):

    try:
        #add log level COMMAND
        COMMAND_LEVEL = 25
        logging.addLevelName(COMMAND_LEVEL, "COMMAND")
        def command(self, message, *args, **kws):
            if self.isEnabledFor(COMMAND_LEVEL):
                self._log(COMMAND_LEVEL, message, args, **kws)
        logging.logger.command=command

        logger = logging.getLogger("logger")
        logger.setLevel("DEBUG")

        #config handler for log file
        DEBUG_handler=logging.FileHandler(os.path.join(logdir,"DEBUG"))
        INFO_handler=logging.FileHandler(os)
        
    except Exception :
        print(f"Logging setup failed: {Exception}")
        raise
    return logger