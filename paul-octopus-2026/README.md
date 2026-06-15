# Paul Octopus 2026 input files

Arquivos iniciais para rodar previsoes da Copa de 2026.

- `results.csv`: historico atualizado usado pelo preprocessamento. Partidas sem placar sao ignoradas para treino/teste.
- `historical-results.csv`: copia do historico anterior do repositorio, mantida como referencia.
- `matches-schedule.csv`: agenda base da fase de grupos em formato compativel com o projeto de 2022. As datas estao como `TBD` ate o calendario oficial detalhado ser carregado.
- `sample_predictions_submission.csv`: confrontos da fase de grupos no formato esperado pelo preditor.

O preprocessamento esta configurado para treinar com as Copas de 2002 a 2018, testar em 2022 e gerar features para 2026.

Para validar os arquivos, datasets e previsoes geradas:

```bash
PYTHONPATH=paul_octopus_pre_processing_2:paul-octopus-python_submited paul_octopus_training/.venv/bin/python paul-octopus-2026/validate_2026.py
```

Os arquivos das fases eliminatorias devem ser gerados quando os classificados forem conhecidos.
