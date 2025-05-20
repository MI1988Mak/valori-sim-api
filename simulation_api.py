from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="VALORI Simulations-API")

# -----------------------------
# Datenmodelle
# -----------------------------
class SimulationParameter(BaseModel):
    kapital: float
    rendite_etf: float
    rendite_immobilie: float
    kostenquote_etf: float
    kostenquote_immobilie: float
    steuersatz: float
    laufzeit_jahre: int

class SimulationPayload(BaseModel):
    sim_id: str
    parameter: SimulationParameter

# -----------------------------
# Simulations-Endpunkt
# -----------------------------
@app.post("/v1/run-simulation")
def run_simulation(payload: SimulationPayload):
    p = payload.parameter

    # Berechnung: ETF und Immobilie brutto
    etf_brutto = p.kapital * ((1 + p.rendite_etf - p.kostenquote_etf) ** p.laufzeit_jahre)
    immo_brutto = p.kapital * ((1 + p.rendite_immobilie - p.kostenquote_immobilie) ** p.laufzeit_jahre)

    # Steuerabzug
    etf_nachsteuer = etf_brutto * (1 - p.steuersatz)
    immo_nachsteuer = immo_brutto * (1 - p.steuersatz)

    # Entscheidungstext
    entscheidung = (
        "ETF bringt mehr – bei höherem Risiko"
        if etf_nachsteuer > immo_nachsteuer
        else "Immobilie bringt mehr – bei mehr Stabilität"
    )

    # Antwortdaten
    response_data = {
        "entscheidung": entscheidung,
        "kennzahlen": {
            "nachsteuer_etf": round(etf_nachsteuer, 2),
            "nachsteuer_immo": round(immo_nachsteuer, 2)
        },
        "eingabe": payload.dict()
    }

    # Rückgabe mit UTF-8-Header
    return JSONResponse(
        content=response_data,
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )
