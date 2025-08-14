# Gerador de Loterias (UK) — EuroMillions, Lotto, Set For Life

Aplicação em Streamlit para gerar combinações aleatórias de três jogos do Reino Unido.

- **EuroMillions**: 5 números (1–50) + 2 Lucky Stars (1–12)
- **Lotto (UK)**: 6 números (1–59)
- **Set For Life**: 5 números (1–47) + 1 Life Ball (1–10)

## Como rodar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy no Streamlit Cloud

1. Crie um repositório no GitHub e suba os arquivos: `app.py`, `gerador_loterias.py`, `requirements.txt`.
2. No Streamlit Cloud, crie um novo app apontando para o repositório.
3. Em **Main file path**, selecione `app.py`.
4. Salve e execute o app.

## Observações

- A opção de *semente* permite reproduzir os mesmos resultados (útil para testes).
- A opção *Evitar linhas duplicadas* impede que duas linhas idênticas apareçam no mesmo lote.
- Uso educacional e recreativo. Jogue com responsabilidade.