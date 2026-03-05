import os
import re

def limpar_recursivo_total(pasta_raiz):
    # Regex para capturar o sufixo exato do Syncthing
    # Exemplo: .sync-conflict-20260126-132536-5T6WGWM
    padrao = re.compile(r'\.sync-conflict-\d{8}-\d{6}-[A-Z0-9]+')
    
    concluidos = 0
    pulados = 0

    print(f"🔍 Vasculhando TUDO a partir de: {os.path.abspath(pasta_raiz)}")

    # os.walk é recursivo por natureza e entra em todos os níveis
    for raiz, subpastas, arquivos in os.walk(pasta_raiz):
        for nome in arquivos:
            if ".sync-conflict-" in nome:
                caminho_antigo = os.path.join(raiz, nome)
                
                # Remove o sufixo mantendo a extensão original
                novo_nome = padrao.sub('', nome)
                caminho_novo = os.path.join(raiz, novo_nome)

                # Regra de segurança: não sobrescrever se o original existir
                if os.path.exists(caminho_novo):
                    print(f"⚠️  [PULADO] Já existe original em: {raiz}")
                    print(f"   Arquivo: {novo_nome}")
                    pulados += 1
                else:
                    try:
                        os.rename(caminho_antigo, caminho_novo)
                        print(f"✅ [REPARADO] {novo_nome}")
                        concluidos += 1
                    except Exception as e:
                        print(f"❌ [ERRO] Falha ao mover {nome}: {e}")

    print(f"\n--- Relatório Final ---")
    print(f"Arquivos restaurados: {concluidos}")
    print(f"Conflitos mantidos (originais já existiam): {pulados}")

if __name__ == "__main__":
    # Inicia a partir da pasta onde o script está
    limpar_recursivo_total('.')
