import subprocess, sys, signal

from app import app


processos = []

def encerrar(sig=None, frame=None):
    for processo in processos:
        if processo.poll() is None:
            processo.terminate()
            try:
                processo.wait(timeout=5)
            except subprocess.TimeoutExpired:
                processo.kill()
    sys.exit(0)


if __name__ == '__main__':
    # executa os comandos do guaraná ao rodar o sistema que:
    # permite visualizar a documentação na porta :5000 (rodar)
    # atualiza o arquivo estilo-min.css quando há mudança na pasta /css

    for comando in [['min'], ['rodar']]:
        processos.append(subprocess.Popen(
            [sys.executable, '-m', 'guarana'] + comando,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        ))

    signal.signal(signal.SIGINT, encerrar)
    signal.signal(signal.SIGTERM, encerrar)

    try:
        app.run(debug=True, host='0.0.0.0', port=3000)
    finally:
        encerrar()
