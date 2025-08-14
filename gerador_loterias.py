from dataclasses import dataclass
import random
from typing import List, Tuple, Dict, Any

@dataclass(frozen=True)
class GameSpec:
    key: str
    name: str
    main_count: int
    main_max: int
    extra_count: int = 0     # quantidade de bolas extras (stars/life)
    extra_max: int = 0       # intervalo máximo da bola extra
    extra_label: str = ""    # nome da bola extra (ex.: "Star", "Life")

# Especificações dos jogos
GAMES = {
    "euromillions": GameSpec(
        key="euromillions", name="EuroMillions", main_count=5, main_max=50, extra_count=2, extra_max=12, extra_label="Star"
    ),
    "lotto": GameSpec(
        key="lotto", name="Lotto (UK)", main_count=6, main_max=59, extra_count=0, extra_max=0, extra_label=""
    ),
    "setforlife": GameSpec(
        key="setforlife", name="Set For Life", main_count=5, main_max=47, extra_count=1, extra_max=10, extra_label="Life"
    ),
}

def _sample_unique(rng: random.Random, k: int, max_n: int) -> List[int]:
    """Amostra k números únicos de 1..max_n (inclusive), em ordem crescente."""
    nums = rng.sample(range(1, max_n + 1), k)
    nums.sort()
    return nums

def generate_line(spec: GameSpec, rng: random.Random) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    main = tuple(_sample_unique(rng, spec.main_count, spec.main_max))
    extra = tuple(_sample_unique(rng, spec.extra_count, spec.extra_max)) if spec.extra_count > 0 else tuple()
    return main, extra

def generate_lines(game_key: str, n_lines: int = 5, unique_lines: bool = True, seed: str | None = None) -> List[Dict[str, Any]]:
    """Gera um conjunto de linhas (combinações) para o jogo escolhido.
    - unique_lines: evita repetir a mesma combinação dentro do lote.
    - seed: qualquer string/valor para tornar os resultados reprodutíveis.
    Retorna uma lista de dicionários com chaves dinâmicas conforme o jogo.
    """
    if game_key not in GAMES:
        raise ValueError(f"Jogo desconhecido: {game_key}")

    spec = GAMES[game_key]
    rng = random.Random(str(seed)) if seed is not None else random.Random()

    seen: set[tuple] = set()
    lines: List[Dict[str, Any]] = []

    while len(lines) < n_lines:
        main, extra = generate_line(spec, rng)
        key = (main, extra)
        if unique_lines and key in seen:
            continue
        seen.add(key)

        # Monta dict com chaves padrão: N1..Nn, e extras conforme label
        row: Dict[str, Any] = {}
        for i, val in enumerate(main, start=1):
            row[f"N{i}"] = val

        if spec.extra_count > 0:
            if spec.extra_count == 1:
                row[spec.extra_label] = extra[0]
            else:
                for i, val in enumerate(extra, start=1):
                    row[f"{spec.extra_label}{i}"] = val

        lines.append(row)

    return lines

def lines_to_dataframe(lines: List[Dict[str, Any]], spec: GameSpec):
    import pandas as pd
    # Ordena colunas: Ns primeiro, depois extras
    n_cols = [f"N{i}" for i in range(1, spec.main_count + 1)]
    extra_cols = []
    if spec.extra_count == 1:
        extra_cols = [spec.extra_label]
    elif spec.extra_count > 1:
        extra_cols = [f"{spec.extra_label}{i}" for i in range(1, spec.extra_count + 1)]
    cols = n_cols + extra_cols

    df = pd.DataFrame(lines)
    # Garante todas as colunas (em caso de pandas reordenar automaticamente)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    df = df[cols]
    return df