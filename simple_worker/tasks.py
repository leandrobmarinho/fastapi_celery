import time
from celery import Celery
from celery.utils.log import get_task_logger
import os

logger = get_task_logger(__name__)

# Obter a URL do Redis das variáveis de ambiente, com um valor padrão
redis_url = os.getenv('REDIS_URL', 'redis://redis:6379/0')

# Configurar o Celery para usar o Redis como broker e backend
app = Celery('tasks', broker=redis_url, backend=redis_url)
# app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


@app.task()
def longtime_add(x, y):    
    logger.info('[Celery] Got Request - Starting work ')
    # time.sleep(10)
    logger.info('[Celery] Work Finished ')


    # Abrir o arquivo em modo de leitura
    with open('/simple_worker/teste.txt', 'r') as arquivo:
        conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo

    logger.info('[Celery] Conteúdo do arquivo: ' + conteudo)

    return x + y
