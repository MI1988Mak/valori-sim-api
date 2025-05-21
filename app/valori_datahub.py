# valori_datahub.py – zentraler Datenhub für aktuelle Finanzdaten
import requests

# Beispielkonstanten als Fallback
DEFAULT_ETF_RETURN = 0.067
DEFAULT_ETF_COSTS = 0.0012
DEFAULT_IMMO_RETURN = 0.03
DEFAULT_INFLATION = 0.025
DEFAULT_INTEREST = 0.035

# --- ETF-Daten von RapidAPI / Yahoo Finance ---
def get_etf_data(symbol="URTH", fallback=True):
    url = f"https://yh-finance.p.rapidapi.com/stock/v3/get-summary?symbol={symbol}&region=US"
    headers = {
        "X-RapidAPI-Key": "DEIN_RAPIDAPI_KEY",
        "X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()
        return {
            "symbol": symbol,
            "return_10y": DEFAULT_ETF_RETURN,  # ggf. live ergänzen
            "ter": data.get("summaryDetail", {}).get("expenseRatio", {}).get("raw", DEFAULT_ETF_COSTS)
        }
    except:
        return {
            "symbol": symbol,
            "return_10y": DEFAULT_ETF_RETURN,
            "ter": DEFAULT_ETF_COSTS
        }

# --- Immobilien-Daten lokal (Benchmark) ---
def get_real_estate_data(city="Berlin"):
    benchmark = {
        "Berlin": {"price_per_sqm": 4820, "rendite_erwartet": 0.03},
        "München": {"price_per_sqm": 8100, "rendite_erwartet": 0.025},
        "Hamburg": {"price_per_sqm": 5400, "rendite_erwartet": 0.028}
    }
    return benchmark.get(city, {"price_per_sqm": 5000, "rendite_erwartet": DEFAULT_IMMO_RETURN})

# --- Inflationsdaten (Placeholder) ---
def get_inflation_data():
    # Optional: aus EZB / TradingEconomics abrufbar
    return {
        "source": "Fallback",
        "inflation": DEFAULT_INFLATION
    }

# --- Zinsdaten (Placeholder) ---
def get_interest_data():
    # Optional: aus ECB API oder FRED
    return {
        "source": "Fallback",
        "interest": DEFAULT_INTEREST
    }
