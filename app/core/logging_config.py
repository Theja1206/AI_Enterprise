import logging 

def setup_logging(level):
    logging.basicConfig(
        level= level,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    return logging.getLogger("Agentic AI")